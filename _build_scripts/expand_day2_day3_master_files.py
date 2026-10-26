"""
expand_day2_day3_master_files.py
Part 2: Upgrades Day 2 and Day 3 files in HPC_Master_Curriculum
"""

import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# DAY 2 EXPANSIONS
# ==============================================================================

write_f("Day-02_Parallel_OpenMP_MPI_oneDAL/theory_notes/day02_openmp_mpi_onedal.md", """# Day 2 Master Theory: Parallel Computing, OpenMP, MPI & Intel oneDAL
**Program**: GLA University Block Teaching | High Performance Computing (Intel & NEC Edition)  
**Lead Trainer**: Shivam Gupta | Edulateral Foundation Master Curriculum  

---

## 1. Flynn's Classical Taxonomy & Parallel Models

```
┌────────────────────────────────────────────────────────────────────────┐
│                        FLYNN'S TAXONOMY MATRIX                         │
├───────────────────────────────────┬────────────────────────────────────┤
│   SISD (Single Instruction, Single Data)  │   SIMD (Single Instruction, Multiple Data) │
│   • Classical scalar uniprocessor │   • Vector units (AVX-512, SSE)    │
│   • Single instruction stream     │   • 1 instruction on N vector data │
├───────────────────────────────────┼────────────────────────────────────┤
│   MISD (Multiple Instruction, Single Data)│   MIMD (Multiple Instruction, Multiple Data)│
│   • Systolic arrays               │   • Modern Multi-Core & Clusters   │
│   • Fault-tolerant voting systems │   • OpenMP (Shared) & MPI (Distrib)│
└───────────────────────────────────┴────────────────────────────────────┘
```

Modern high-performance supercomputing architectures are **hybrid hierarchical MIMD systems**:
1. **Node Level (Distributed Memory)**: Independent compute nodes communicating across high-speed InfiniBand fabrics via the **Message Passing Interface (MPI)**.
2. **Socket/Core Level (Shared Memory)**: Multi-core CPUs sharing physical memory within a NUMA domain via **OpenMP multithreading**.
3. **Register Level (Vector Execution)**: Vector units (AVX-512, AMX, NEC VE) computing multiple data elements per cycle via **SIMD vectorization**.

---

## 2. Shared-Memory Parallelism with OpenMP

OpenMP (Open Multi-Processing) is an industry-standard API for shared-memory parallel programming in C, C++, and Fortran.

### 2.1 The Fork-Join Execution Model
- The program begins execution as a single thread (the **Master Thread**, Thread 0).
- Upon encountering an `#pragma omp parallel` construct, the master thread forks a **team of worker threads**.
- Iterations and statements inside the structured block are executed concurrently across threads.
- At the end of the parallel construct, an implicit barrier synchronizes the team, joining all threads back into the master thread.

```
Master Thread ───► [Fork: #pragma omp parallel] ───┬──► Worker Thread 0 (Master) ───┐
                                                    ├──► Worker Thread 1 ────────────┼──► [Join / Barrier] ───► Master Thread
                                                    ├──► Worker Thread 2 ────────────┤
                                                    └──► Worker Thread 3 ────────────┘
```

---

### 2.2 Worksharing Constructs & Scheduling Algorithms
The `#pragma omp for` directive distributes loop iterations across the thread team.

1. **`schedule(static, chunk)`**:
   - Loop iterations are partitioned into fixed chunks of size `chunk` and assigned round-robin at launch.
   - **Overhead**: Near zero runtime scheduling overhead.
   - **Optimal Use**: Uniform workloads where every loop iteration takes identical execution time.
2. **`schedule(dynamic, chunk)`**:
   - Iterations are partitioned into chunks. When a thread completes its assigned chunk, it dynamically requests the next chunk from a synchronized work queue.
   - **Overhead**: Moderate synchronization overhead due to work queue locking.
   - **Optimal Use**: Non-uniform, irregular workloads (e.g. Mandelbrot fractals, adaptive mesh refinement, sparse matrices).
3. **`schedule(guided, chunk)`**:
   - Starts with large chunks to minimize queue lock contention, exponentially shrinking chunk sizes down to `chunk` to balance load towards the end.

---

### 2.3 Synchronization & Race Condition Elimination
A **Data Race** occurs when two concurrent threads access the same memory location, at least one access is a write, and no synchronization is enforced.

- **`#pragma omp critical`**:
  - Enforces mutual exclusion via a heavyweight software mutex.
  - High cycle overhead (~50–100ns per lock/unlock); serializes thread execution.
- **`#pragma omp atomic`**:
  - Leverages single hardware atomic assembly instructions (e.g. `LOCK XADD`, `CMPXCHG`).
  - Low cycle overhead (~5–10ns); does not serialize independent variables.
- **`reduction(operator : list)`**:
  - The gold standard for associative operations (`+`, `*`, `min`, `max`).
  - Creates a private accumulator for each thread initialized to the operator identity (e.g. 0 for `+`), accumulating locally without lock overhead, and atomically combining values at loop exit.

---

### 2.4 The Silent Killer: False Sharing (Cache Line Bouncing)
Modern CPUs read and write memory in discrete **64-byte Cache Lines**, not individual bytes or words.
- **The Pathology**: If Thread 0 on Core 0 repeatedly writes to `counter[0]`, and Thread 1 on Core 1 repeatedly writes to `counter[1]`, and both elements reside in the same 64-byte slice of RAM:
  1. Core 0 modifies its local L1 cache line, setting the MESI protocol flag to `Modified`.
  2. The hardware cache controller transmits a broadcast invalidation across the inter-core ring bus to Core 1.
  3. Core 1's local cache line is marked `Invalid`, forcing Core 1 to stall and re-fetch the entire 64-byte line from L3 or DRAM.
  4. Core 1 modifies `counter[1]`, invalidating Core 0's cache line.
- **The Impact**: This 'cache line bouncing' drops throughput by 10x to 50x despite zero logical race condition.
- **The Remedy**: Pad variables or align to cache boundary:
```cpp
struct alignas(64) ThreadAccumulator {
    double sum;
    // 56 bytes of padding automatically inserted to span full 64-byte cache line
};
```

---

## 3. Distributed-Memory Computing: Message Passing Interface (MPI)

In distributed-memory clusters, compute nodes share no common physical address space. Processes coordinate exclusively through message passing over network interconnects.

### 3.1 Point-to-Point Communication & Deadlock Dynamics
- **Blocking (`MPI_Send` / `MPI_Recv`)**: Returns only when the buffer has been safely copied to the network subsystem or local buffer.
- **The Classic Deadlock**:
```cpp
// DEADLOCK SCENARIO:
if (rank == 0) {
    MPI_Recv(buf, count, MPI_FLOAT, 1, 0, MPI_COMM_WORLD, &status); // Waiting for 1
    MPI_Send(buf, count, MPI_FLOAT, 1, 0, MPI_COMM_WORLD);
} else if (rank == 1) {
    MPI_Recv(buf, count, MPI_FLOAT, 0, 0, MPI_COMM_WORLD, &status); // Waiting for 0
    MPI_Send(buf, count, MPI_FLOAT, 0, 0, MPI_COMM_WORLD);
}
```
Both processes block indefinitely. To prevent deadlock:
1. Re-order sends and receives (even ranks send first, odd ranks receive first).
2. Utilize combined `MPI_Sendrecv`.
3. Utilize non-blocking primitives (`MPI_Isend` / `MPI_Irecv`) followed by `MPI_Wait`.

---

### 3.2 Overlapping Communication with Computation
Non-blocking calls decouple message transfer initiation from completion:
```python
# Overlapping in Python with mpi4py
req = comm.Isend(send_data, dest=target_rank)
# The CPU performs independent heavy floating-point calculation:
compute_internal_grid_cells()
# Synchronize network transfer:
req.Wait()
```
The InfiniBand network card transfers the message via zero-copy RDMA in the background while the CPU cores execute arithmetic instructions, hiding network latency.

---

### 3.3 MPI Collective Operations
Collectives involve all processes in an `MPI_Comm` communicator:
1. **`MPI_Bcast`**: One-to-all broadcast of identical data.
2. **`MPI_Scatter`**: One-to-all distribution of disjoint data partitions.
3. **`MPI_Gather`**: All-to-one aggregation of disjoint data partitions.
4. **`MPI_Allreduce`**: Global reduction operation (SUM, MAX, MIN) where the reduced scalar or array is distributed to all ranks. Implemented using logarithmic tree algorithms ($O(\\log N)$ latency).

---

## 4. Intel oneDAL & The Intel AI Analytics Toolkit

### 4.1 The Architecture of Intel oneDAL
Intel oneDAL (oneAPI Data Analytics Library) is an algorithmic library engineered to accelerate all stages of data analysis:
- **Preprocessing**: Dimensionality reduction (PCA, t-SNE), normalization, correlation.
- **Supervised Learning**: Support Vector Machines (SVM), Random Forests, Gradient Boosted Decision Trees, Ridge/Lasso.
- **Unsupervised Learning**: k-Means clustering, DBSCAN.

### 4.2 The 30x Secret: Intel Extension for Scikit-learn (`sklearnex`)
Standard Scikit-learn is implemented in Python and single-threaded Cython. When patched with `sklearnex`:
```python
from sklearnex import patch_sklearn
patch_sklearn()
# Standard Scikit-learn estimators are dynamically monkey-patched
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
```
- **Vectorized Kernel Evaluations**: Distance matrices and kernel evaluations (RBF, Polynomial) are computed using AVX-512 vector units.
- **Multi-Threaded Split Finding**: Random Forest decision tree construction utilizes parallel histogram binning across all physical NUMA cores.
- **Cache-Blocked SMO**: SVM Sequential Minimal Optimization utilizes cache blocking to maintain active working sets inside L2/L3 cache.
""")

# ==============================================================================
# DAY 3 EXPANSIONS
# ==============================================================================

write_f("Day-03_DeepLearning_TF_Slurm_Horovod/theory_notes/day03_tensorflow_slurm_horovod.md", """# Day 3 Master Theory: Deep Learning on HPC Clusters with Slurm & Horovod
**Program**: GLA University Block Teaching | High Performance Computing (Intel & NEC Edition)  
**Lead Trainer**: Shivam Gupta | Edulateral Foundation Master Curriculum  

---

## 1. Deep Learning Compute Anatomy & The Memory Wall

### 1.1 The Dominance of Matrix Multiplication (GEMM)
Over 85% of compute cycles in deep learning (Convolutional Networks, Transformers, Vision Transformers) are consumed by General Matrix Multiply (GEMM) operations:
$$C = \\alpha (A \\times B) + \\beta C$$
- **Operational Intensity**:
$$\\text{Operational Intensity} = \\frac{\\text{FLOPs}}{\\text{Bytes Transferred}}$$
- **Compute-Bound Operations**: Large GEMMs in fully-connected and projection layers possess high operational intensity, saturating vector execution units (AVX-512, AMX, GPU XMX).
- **Memory-Bound Operations**: Activations (GELU, ReLU), LayerNorm, and Softmax possess low operational intensity, saturating DRAM bandwidth.

---

### 1.2 Numerical Precision Formats: Why Bfloat16 Dominates
```
IEEE FP32:  [Sign: 1] [Exponent: 8 bits] [Mantissa: 23 bits]          (32 bits)
IEEE FP16:  [Sign: 1] [Exponent: 5 bits] [Mantissa: 10 bits]          (16 bits - Prone to underflow)
Bfloat16:   [Sign: 1] [Exponent: 8 bits] [Mantissa: 7 bits]           (16 bits - Same dynamic range as FP32!)
INT8:       [Sign: 1] [Integer: 7 bits]                               (8 bits)
```
- **The Bfloat16 Advantage**: Bfloat16 maintains the full 8-bit dynamic exponent range of FP32 while halving memory footprint from 4 bytes to 2 bytes. Deep learning backpropagation gradients never underflow, eliminating the need for complex loss-scaling algorithms required by FP16.

---

## 2. Intel oneDNN & TensorFlow-MKL Acceleration

### 2.1 Operator Fusion Mechanics
In standard deep learning runtimes:
```
[Conv2D Kernel] ──(DRAM Write)──► DRAM ──(DRAM Read)──► [BiasAdd Kernel] ──(DRAM Write)──► DRAM ──(DRAM Read)──► [ReLU Kernel]
```
Round-tripping intermediate activation tensors to slow main DRAM wastes over 70% of execution time.

**Intel oneDNN Operator Fusion**:
```
┌────────────────────────────────────────────────────────┐
│              Fused oneDNN Super-Kernel                 │
│  [ Conv2D (AVX-512/AMX) ──► BiasAdd ──► ReLU In-Place] │
└────────────────────────────────────────────────────────┘
          (All intermediate tensors remain inside L1/L2 cache!)
```
Activates via:
```bash
export TF_ENABLE_ONEDNN_OPTS=1
```

### 2.2 Tuning TensorFlow Thread Pools on Xeon
TensorFlow on multi-core servers manages two distinct thread pools:
1. **`intra_op_parallelism_threads`**: Governs how many threads cooperate to compute an individual tensor operator (e.g. parallelizing a large GEMM). Set equal to the physical core count of the local NUMA socket.
2. **`inter_op_parallelism_threads`**: Governs how many independent nodes in the TensorFlow computation graph execute concurrently. Typically set to 2.

---

## 3. Slurm Workload Manager Architecture

```
Slurm Cluster Control Topology
                     [ slurmctld ] (Master Controller Daemon)
                     [ slurmdbd  ] (Database Accounting Daemon)
                           │
         ┌─────────────────┼─────────────────┐
         ▼                 ▼                 ▼
   [ Compute Node 1 ] [ Compute Node 2 ] [ Compute Node 3 ]
   • slurmd daemon    • slurmd daemon    • slurmd daemon
   • cgroup isolation • cgroup isolation • cgroup isolation
```

### 3.1 Slurm Daemons & Roles
- **`slurmctld`**: Central management daemon running on the cluster head node. Monitors node health, prioritizes pending jobs, enforces fair-share policies, and dispatches job allocations.
- **`slurmd`**: Node daemon running on every compute node. Monitors local CPU/RAM/GPU resources, spawns tasks, enforces cgroups, and streams stdout/stderr back to the user.
- **`slurmdbd`**: Secure database daemon tracking historical job accounting, user allocations, and QoS limits.

### 3.2 Anatomy of a Production Slurm Script
```bash
#!/bin/bash
#SBATCH --job-name=tf_distributed_hpc
#SBATCH --nodes=4                   # Reserve 4 physical nodes
#SBATCH --ntasks-per-node=2         # Launch 2 MPI ranks per node (8 total)
#SBATCH --cpus-per-task=16          # Allocate 16 CPU cores per rank (128 total)
#SBATCH --mem=64G                   # 64 GB RAM per node
#SBATCH --time=04:00:00             # 4-hour hard walltime limit
#SBATCH --partition=compute         # Submit to compute partition
#SBATCH --output=slurm_job_%j.log   # Log stdout and stderr (%j = Job ID)

module load intel/oneapi/latest
source activate hpc-edulateral

srun python horovod_tf_training.py
```

---

## 4. Distributed Training: Horovod & Ring-AllReduce

```
Ring-AllReduce Architecture (Baidu / Horovod Algorithm)
                   ┌──────────┐
         ┌────────►│ Worker 0 ├────────┐
         │         └──────────┘        │
         │                             ▼
   ┌─────┴────┐                   ┌────┴─────┐
   │ Worker 3 │                   │ Worker 1 │
   └─────▲────┘                   └────┬─────┘
         │         ┌──────────┐        │
         └─────────┤ Worker 2 |◄───────┘
                   └──────────┘
```

### 4.1 Ring-AllReduce Mathematical Bandwidth Optimality
In traditional **Parameter Server** architectures, all $N$ workers transmit gradients to central servers, saturating server network interfaces as $O(N)$.

In **Ring-AllReduce**:
- Workers are arranged in a logical unidirectional ring.
- Gradients of size $M$ are divided into $N$ equal chunks.
- **Phase 1: Scatter-Reduce**: Workers transmit chunks around the ring for $N - 1$ steps. Each step transfers $\\frac{M}{N}$ data.
- **Phase 2: AllGather**: Workers transmit reduced chunks around the ring for $N - 1$ steps.
- **Total Data Transferred per Worker**:
$$\\text{Total Transfer} = 2 \\times \\left( \\frac{N - 1}{N} \\right) \\times M$$
As $N \\to \\infty$, total data transfer per node asymptotically approaches **$2M$**, which is completely independent of cluster size $N$! This enables linear scaling across thousands of nodes.
""")

print("[SUCCESS] Day 2 and Day 3 Master Upgrades applied successfully!")
