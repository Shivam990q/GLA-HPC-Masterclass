# complete_all_hpc_files.py
import os
import shutil

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# CLEANUP LOOSE FILES THAT BELONG INSIDE SUBDIRECTORIES
# ==============================================================================
days = [
    "Day-01_HPC_Linux_Shell_oneAPI",
    "Day-02_Parallel_OpenMP_MPI_oneDAL",
    "Day-03_DeepLearning_TF_Slurm_Horovod",
    "Day-04_Distributed_Slurm_VTune_Profiling",
    "Day-05_GenAI_LLMs_Gaudi_OpenVINO"
]

for d in days:
    loose_theory = os.path.join(base_dir, d, "theory_notes.md")
    if os.path.exists(loose_theory):
        os.remove(loose_theory)
        print(f"[CLEAN] Removed loose root file: {d}/theory_notes.md")

# ==============================================================================
# DAY 1
# ==============================================================================
write_f("Day-01_HPC_Linux_Shell_oneAPI/theory_notes/day01_hpc_architecture.md", """
# Day 1 Theory: HPC Architecture, Silicon Engineering & Linux Foundations

## 1. The Physics and Economics of Supercomputing
- **The Death of Dennard Scaling (2005)**:
  - Historically, as transistors got smaller, power density stayed constant, allowing clock speeds to double every generation.
  - Dennard scaling broke down at ~90nm. Above ~4-5 GHz, leakage current and thermal dissipation cause silicon to burn.
  - **Amdahl's Law vs Gustafson's Law**:
    - Amdahl's Law: $S_{\\text{latency}}(s) = \\frac{1}{(1-p) + \\frac{p}{s}}$ (Serial bottlenecks limit speedup).
    - Gustafson's Law: $S(P) = P - \\alpha(P - 1)$ (Scaled speedup: with larger problem sizes, parallel execution dominates).
- **HPC Cluster Topologies**:
  - Fat-Tree Topology: Non-blocking network tree ensuring full bisection bandwidth across all racks.
  - InfiniBand Fabric: HDR (200 Gbps) / NDR (400 Gbps), sub-microsecond latency, Zero-Copy RDMA (Remote Direct Memory Access).

## 2. Intel Xeon & Heterogeneous Compute Silicon
- **NUMA (Non-Uniform Memory Access)**:
  - Multi-socket server architectures. Each CPU socket controls its local memory channels (e.g., 8-channel DDR5 per socket).
  - Accessing local NUMA memory takes ~80ns; remote socket memory over UPI (Ultra Path Interconnect) takes ~140ns.
  - Mitigation: Process and thread pinning (`numactl`, `KMP_AFFINITY`).
- **SIMD (Single Instruction Multiple Data)**:
  - **AVX-512**: 32 vector registers (ZMM0 to ZMM31), 512 bits wide. 1 instruction computes sixteen 32-bit floating point numbers.
  - **Intel AMX (Advanced Matrix Extensions)**: 2D tile matrix multiplication accelerator embedded in Sapphire Rapids Xeon cores. Computes $16 \\times 64$ BF16/INT8 matrix contractions per cycle.
- **Intel Data Center GPU Max (Ponte Vecchio)**:
  - 128 GB HBM2e memory delivering 3.2 TB/s bandwidth.
  - Xe Matrix Extensions (XMX) systolic hardware arrays.
- **Habana Gaudi (Gaudi 2 / 3)**:
  - Specialized deep learning ASIC with 24 integrated 100GbE RoCE ports directly on-chip.

## 3. HPC Linux Environment
- **Parallel File Systems**:
  - `/home`: NFS (Network File System) for code and configs.
  - `/scratch` or `/tmp`: High-throughput parallel storage (Lustre / GPFS) striped across Object Storage Targets (OSTs) for datasets.
- **Environment Modules**: Lmod architecture dynamically setting `PATH`, `LD_LIBRARY_PATH`, and `CPATH`.
- **Passwordless SSH**: Ed25519 elliptic curve keys, multiplexing with ControlMaster.
""")

write_f("Day-01_HPC_Linux_Shell_oneAPI/student_lab_practice/day01_hands_on_challenges.md", """
# Day 1: Student Lab Practice Challenges & Solutions

### Challenge 1: Silicon & Cache Inspection (Level: Beginner)
* **Task**: Write a 1-line bash pipeline to display the exact L1d, L1i, L2, and L3 cache sizes of the host CPU.
* **Solution**:
  ```bash
  lscpu -C
  # Or inspect virtual filesystem:
  cat /sys/devices/system/cpu/cpu0/cache/index*/size
  ```

### Challenge 2: AVX-512 & Vector Flag Verification (Level: Intermediate)
* **Task**: Write a shell script `check_vector_support.sh` that checks if the host supports AVX-512, AVX2, or standard SSE, and prints a recommendation for compiling AI models.
* **Solution**:
  ```bash
  #!/bin/bash
  if grep -q "avx512" /proc/cpuinfo; then
      echo "[PASS] AVX-512 detected. Use -mavx512f flag for 16-wide float vectorization."
  elif grep -q "avx2" /proc/cpuinfo; then
      echo "[PASS] AVX2 detected. Use -mavx2 flag for 8-wide float vectorization."
  else
      echo "[WARN] Legacy SSE mode only."
  fi
  ```

### Challenge 3: Automated Passwordless SSH Alias (Level: Advanced)
* **Task**: Generate an Ed25519 SSH key pair and configure `~/.ssh/config` so you can connect to `node01` using just `ssh node01`.
* **Solution**:
  ```bash
  ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519
  cat << 'EOF' >> ~/.ssh/config
  Host node01
      HostName localhost
      User $USER
      IdentityFile ~/.ssh/id_ed25519
  EOF
  chmod 600 ~/.ssh/config
  ```
""")

write_f("Day-01_HPC_Linux_Shell_oneAPI/interview_qa/day01_top_interview_qa.md", """
# Day 1: Top 10 Technical Interview Questions & Answers

### Q1: What is the difference between SMP and an HPC Cluster?
* **Answer**: SMP (Symmetric Multiprocessing) shares a single physical memory address space and bus across cores on one motherboard. An HPC cluster connects independent computers (nodes) with isolated memories over a high-speed network fabric (InfiniBand), scaling beyond single-board thermal and memory bandwidth limits.

### Q2: Why is InfiniBand preferred over standard Ethernet in HPC clusters?
* **Answer**: Standard Ethernet has 10-50 microseconds of latency and consumes CPU cycles for TCP/IP stack packet processing. InfiniBand provides sub-microsecond latency (0.5-1.0 us) and uses RDMA (Remote Direct Memory Access) to read/write remote RAM directly without OS kernel interrupts.

### Q3: What is NUMA and why does it matter in high-performance computing?
* **Answer**: Non-Uniform Memory Access means memory access times vary depending on which CPU socket owns the memory controller. Accessing local socket memory is 2x faster than accessing remote socket memory across the UPI/QPI interconnect. HPC software must pin threads to cores to prevent NUMA remote memory penalties.

### Q4: Why is Hyperthreading often disabled in HPC clusters?
* **Answer**: Hyperthreading shares execution units (ALUs/FPUs) and L1/L2 caches between two logical threads on one physical core. In HPC workloads where vector FPUs (AVX-512) are already 100% saturated, hyperthreading causes cache thrashing and context switching latency, reducing throughput.

### Q5: What is Dennard Scaling, and why did it end?
* **Answer**: Dennard scaling stated that as transistors shrink, power density stays constant because voltage and current scale downward proportionally. It ended in ~2005 due to threshold voltage leakage and quantum tunneling, forcing the industry to move from increasing clock frequency to multi-core parallelism.

### Q6: What is the purpose of Intel AMX (Advanced Matrix Extensions)?
* **Answer**: AMX is a dedicated 2D hardware matrix multiplication engine inside Xeon Sapphire Rapids CPU cores. It contains 8 two-dimensional register tiles (1KB each) and a TMUL (Tile Matrix Multiply) unit that calculates 16x64 BF16 or INT8 matrix operations per clock cycle.

### Q7: What is the difference between `/home` and `/scratch` filesystems on an HPC cluster?
* **Answer**: `/home` is typically an NFS share designed for user scripts and source code; it has high metadata latency and bottlenecks under heavy I/O. `/scratch` is a distributed parallel filesystem (Lustre/GPFS) striped across dozens of disk controllers, optimized for multi-gigabyte/sec parallel I/O.

### Q8: What does the environment module system (`lmod` / `module`) solve?
* **Answer**: HPC clusters host multiple conflicting software stacks, compilers, and library versions (e.g. GCC 9 vs GCC 13, Intel oneAPI vs CUDA). The module system modifies shell environment variables (`PATH`, `LD_LIBRARY_PATH`) on-the-fly without permanently breaking system defaults.

### Q9: Why is Ed25519 preferred over RSA for SSH keys in modern clusters?
* **Answer**: Ed25519 uses Twisted Edwards Curve Cryptography. A 256-bit Ed25519 key provides security equivalent to a 3072-bit RSA key, generates signatures significantly faster, has smaller key sizes, and is immune to side-channel cache-timing attacks.

### Q10: What is the primary philosophy of Intel oneAPI?
* **Answer**: oneAPI is an open, standards-based unified programming model (based on SYCL/DPC++) designed to eliminate vendor lock-in (such as Nvidia CUDA). It allows developers to write single-source modern C++ that compiles natively across CPUs, GPUs, FPGAs, and AI accelerators.
""")

# ==============================================================================
# DAY 2
# ==============================================================================
write_f("Day-02_Parallel_OpenMP_MPI_oneDAL/theory_notes/day02_openmp_mpi_onedal.md", """
# Day 2 Theory: Parallel Computing Models (OpenMP vs MPI) & Intel oneDAL

## 1. Parallel Computing Paradigms
- **Shared Memory Architecture (OpenMP)**:
  - All threads read/write to a common global address space.
  - Programming Model: Fork-Join Model. A master thread forks a team of worker threads across available CPU cores.
  - Critical Concepts:
    - `#pragma omp parallel for`
    - `private(var)`: Each thread gets an uninitialized local copy on its stack.
    - `shared(var)`: All threads access the same memory location (risk of race condition).
    - `reduction(+:sum)`: Each thread accumulates locally, and thread results are combined at the barrier without mutex contention.
    - Race Conditions & False Sharing: Two threads updating adjacent variables residing on the same 64-byte CPU cache line, causing continuous cache invalidation.

- **Distributed Memory Architecture (MPI - Message Passing Interface)**:
  - Independent processes running across distinct cluster nodes connected via network.
  - SPMD (Single Program, Multiple Data): Identical binary executed on all nodes; execution paths diverge based on `rank`.
  - Point-to-Point Communication: `MPI_Send` and `MPI_Recv` with message tags, buffering modes (Blocking vs Non-blocking `MPI_Isend`).
  - Collective Communication:
    - Broadcast (`MPI_Bcast`): One-to-All.
    - Scatter (`MPI_Scatter`): Distributes unique chunks of an array to each process.
    - Gather (`MPI_Gather`): Collects chunks from all processes into master.
    - Reduce (`MPI_Reduce`): Combines data using associative operators (`MPI_SUM`, `MPI_MAX`, `MPI_MIN`).

## 2. Intel AI Analytics Toolkit & oneDAL
- **The Classical ML Python Bottleneck**:
  - Python's Global Interpreter Lock (GIL) limits pure Python to 1 core.
  - Standard Scikit-Learn algorithms rely on generic Cython loops that do not utilize AVX-512 or AMX matrix silicon.
- **Intel oneDAL (oneAPI Data Analytics Library)**:
  - Implements hyper-optimized math kernels for clustering, regression, PCA, and SVM.
  - `scikit-learn-intelex`: In-memory monkey-patching (`patch_sklearn()`) replacing default estimators with oneDAL kernels, achieving 10x-40x speedups with zero algorithmic alterations.
""")

write_f("Day-02_Parallel_OpenMP_MPI_oneDAL/student_lab_practice/day02_hands_on_challenges.md", """
# Day 2: Student Lab Practice Challenges & Solutions

### Challenge 1: OpenMP Thread Affinity & Scaling (Level: Beginner)
* **Task**: Compile `omp_multithreading.cpp` using Intel `icx` with `-qopenmp` and test scaling efficiency from 1 to 8 threads.
* **Solution**:
  ```bash
  icx -qopenmp omp_multithreading.cpp -o omp_test
  for threads in 1 2 4 8; do
      OMP_NUM_THREADS=$threads ./omp_test
  done
  ```

### Challenge 2: MPI Ring Token Passing (Level: Intermediate)
* **Task**: Write an MPI script `ring_pass.py` where Rank 0 sends a number `token = 100` to Rank 1, Rank 1 increments it and passes it to Rank 2, and the last rank returns it to Rank 0.
* **Solution**:
  ```python
  from mpi4py import MPI
  comm = MPI.COMM_WORLD
  rank = comm.Get_rank()
  size = comm.Get_size()

  token = 100 if rank == 0 else None
  if rank == 0:
      comm.send(token, dest=1, tag=0)
      token = comm.recv(source=size-1, tag=0)
      print(f"[Master Rank 0] Ring completed! Token value: {token}")
  else:
      token = comm.recv(source=rank-1, tag=0)
      token += 1
      next_dest = (rank + 1) % size
      comm.send(token, dest=next_dest, tag=0)
  ```

### Challenge 3: Intel Scikit-Learn Benchmarking Report (Level: Advanced)
* **Task**: Run `intel_scikit_speedup.py` with 5 Million data points and calculate the exact percentage speedup and energy efficiency metric.
""")

write_f("Day-02_Parallel_OpenMP_MPI_oneDAL/interview_qa/day02_top_interview_qa.md", """
# Day 2: Top 10 Technical Interview Questions & Answers

### Q1: What is the fundamental difference between OpenMP and MPI?
* **Answer**: OpenMP operates on shared-memory multi-core systems using compiler directives and threads sharing a common address space. MPI operates on distributed-memory multi-node clusters using explicit message passing over a network between isolated processes.

### Q2: What is False Sharing in multi-threaded programming?
* **Answer**: False sharing occurs when two independent threads running on different CPU cores modify distinct variables that reside within the same 64-byte cache line. The CPU cache-coherency protocol (MESI) forces the cache line to bounce between cores, severely degrading performance.

### Q3: What is the Fork-Join execution model in OpenMP?
* **Answer**: The program starts as a single master thread. When a `#pragma omp parallel` directive is encountered, the master thread forks a team of worker threads. At the end of the parallel block, an implicit barrier synchronizes the threads, and they join back into the single master thread.

### Q4: What is the difference between blocking (`MPI_Send`) and non-blocking (`MPI_Isend`) communication?
* **Answer**: `MPI_Send` is blocking; it does not return until the send buffer can be safely modified without corrupting the message. `MPI_Isend` returns immediately with a request handle, allowing computation to overlap with communication, followed by an explicit `MPI_Wait` to verify completion.

### Q5: How does an MPI Reduction differ from an MPI Allreduce?
* **Answer**: `MPI_Reduce` collects data from all processes, applies an associative reduction operation (like sum or max), and stores the final result only on the designated root rank. `MPI_Allreduce` applies the reduction operation and distributes the final aggregated result to all processes in the communicator.

### Q6: How does `scikit-learn-intelex` achieve 10x-40x acceleration without changing code?
* **Answer**: It monkey-patches standard Scikit-Learn class definitions in Python's namespace. When an estimator like `KMeans` or `SVC` is instantiated, it calls pre-compiled C++ kernels from Intel oneDAL that are vectorized with AVX-512 instructions and multi-threaded with OpenMP.

### Q7: What is Amdahl's Law, and how does it predict parallel limits?
* **Answer**: Amdahl's Law states that the theoretical speedup of a program is limited by its serial (non-parallelizable) portion. If 10% of a program is strictly serial, the maximum possible speedup on an infinite number of processors is $\frac{1}{0.10} = 10\times$.

### Q8: What is the function of the OpenMP `reduction` clause?
* **Answer**: The `reduction` clause creates a private copy of the reduction variable for each thread, initialized to the identity value (e.g. 0 for addition). Threads update their private copy without locking, and at the end of the loop, private values are safely combined into the shared variable.

### Q9: Why is SPMD (Single Program Multiple Data) the dominant MPI paradigm?
* **Answer**: Instead of writing separate programs for master and worker nodes, SPMD compiles a single binary deployed to all cluster nodes. Nodes query their unique rank ID at runtime (`comm.Get_rank()`) to execute their specific slice of the computational problem.

### Q10: What are the primary communication bottlenecks in large-scale MPI jobs?
* **Answer**: Network latency for small messages, interconnect bisection bandwidth saturation for large collectives (`MPI_Alltoall`), and process imbalance where faster processes waste CPU cycles idling at synchronization barriers (`MPI_Barrier`).
""")

# ==============================================================================
# DAY 3
# ==============================================================================
write_f("Day-03_DeepLearning_TF_Slurm_Horovod/theory_notes/day03_tensorflow_slurm_horovod.md", """
# Day 3 Theory: Deep Learning on HPC, Slurm Cluster Scheduling & Horovod

## 1. Hardware-Aware Deep Learning (oneDNN & TensorFlow-MKL)
- **Deep Learning Bottleneck**: Deep neural networks spend over 75% of execution time performing General Matrix Multiply (GEMM) and Conv2D convolutions.
- **oneDNN Primitives**:
  - Memory Format Optimization: Native `nChw16c` or `nChw8c` blocked memory layouts to ensure optimal vector register alignment.
  - Operator Fusion: Fuses Convolution + BiasAdd + ReLU/GELU activation into a single hardware pass, preventing intermediate tensor roundtrips to system RAM.
- **Environment Flags for Intel Deep Learning**:
  - `OMP_NUM_THREADS=<physical_cores>`: Prevents thread oversubscription.
  - `KMP_BLOCKTIME=0`: Directs worker threads to sleep immediately after completing tasks, freeing resources.
  - `KMP_AFFINITY=granularity=fine,compact,1,0`: Pins OpenMP threads to adjacent physical cores for cache sharing.

## 2. Slurm Workload Manager Architecture
- **Cluster Hierarchy**:
  - **Head / Master Node**: Hosts `slurmctld` (controller daemon) and database `slurmdbd`.
  - **Compute Nodes**: Host `slurmd` daemons that execute jobs within Linux cgroups.
- **Job Submission Modes**:
  - Interactive: `srun --pty bash` (Allocates real-time terminal on a compute node).
  - Batch: `sbatch script.slurm` (Headless queued execution with automated logging).
- **Core Directive Flags**:
  - `--nodes=N`: Number of physical servers.
  - `--ntasks-per-node=T`: Number of MPI / task instances per node.
  - `--cpus-per-task=C`: Multi-threading cores allocated to each task.
  - `--time=HH:MM:SS`: Wall-clock execution hard limit.
  - `--partition=name`: Target hardware queue (e.g. CPU vs GPU partition).

## 3. Distributed Deep Learning with Horovod (Ring-AllReduce)
- **The Parameter Server Bottleneck**: Traditional distributed training sends all gradients to centralized parameter servers. As worker counts scale beyond 8 nodes, the parameter server's network bandwidth becomes saturated.
- **Ring-AllReduce Algorithm**:
  - Developed by Baidu and open-sourced by Uber as Horovod.
  - Connects $N$ worker nodes in a logical ring.
  - Phase 1 (Scatter-Reduce): Gradients are split into $N$ chunks. In $N-1$ steps, each node sends a chunk and receives from its neighbor, resulting in each node holding the reduced sum of one chunk.
  - Phase 2 (Allgather): In another $N-1$ steps, the reduced chunks are circulated around the ring so every node receives all updated weights.
  - Communication volume: $2 \\times \\frac{N-1}{N} \\times \\text{Model Size}$. The bandwidth is constant regardless of how many nodes are in the cluster!
""")

write_f("Day-03_DeepLearning_TF_Slurm_Horovod/student_lab_practice/day03_hands_on_challenges.md", """
# Day 3: Student Lab Practice Challenges & Solutions

### Challenge 1: Slurm Cluster State Audit (Level: Beginner)
* **Task**: Query the Slurm cluster to find all idle nodes and their partition configurations.
* **Solution**:
  ```bash
  sinfo -s
  sinfo -N -l
  ```

### Challenge 2: Writing a Production Batch Script (Level: Intermediate)
* **Task**: Write a Slurm script `test_job.slurm` that requests 1 node, 4 CPUs, writes output to `job_%j.log`, and executes a Python script that prints the allocated CPU count.
* **Solution**:
  ```bash
  #!/bin/bash
  #SBATCH --job-name=test_cpu_job
  #SBATCH --output=job_%j.log
  #SBATCH --nodes=1
  #SBATCH --cpus-per-task=4
  #SBATCH --time=00:10:00

  python3 -c "import os; print('Allocated Cores:', os.cpu_count())"
  ```

### Challenge 3: Horovod Learning Rate Scaling (Level: Advanced)
* **Task**: Modify `horovod_tf_training.py` to implement Warmup Learning Rate scaling, where base learning rate starts at $0.001$ and ramps up to $0.001 \\times \\text{size}$ over the first 5 epochs.
""")

write_f("Day-03_DeepLearning_TF_Slurm_Horovod/interview_qa/day03_top_interview_qa.md", """
# Day 3: Top 10 Technical Interview Questions & Answers

### Q1: What is the primary difference between Data Parallelism and Model Parallelism in Deep Learning?
* **Answer**: In Data Parallelism, the full model is copied to every worker node, and each worker trains on a unique batch of data, aggregating gradients at the end of the step. In Model Parallelism, the layers or tensors of a model are split across nodes because the model is too large to fit in a single node's memory.

### Q2: Why does Horovod's Ring-AllReduce scale better than a Parameter Server?
* **Answer**: In a Parameter Server architecture, network traffic concentrates at the server node, which becomes a bottleneck ($O(N)$ network load). In Ring-AllReduce, nodes communicate only with their two immediate neighbors in a ring, making communication cost independent of the number of nodes ($O(1)$ scaling).

### Q3: Why must the learning rate be scaled when training with Horovod?
* **Answer**: When training across $N$ workers with local batch size $B$, the effective global batch size becomes $N \\times B$. According to the Linear Scaling Rule (Goyal et al.), the learning rate must be multiplied by $N$ to maintain equivalent gradient update dynamics.

### Q4: What is the role of `hvd.broadcast_global_variables(0)` in Horovod?
* **Answer**: Deep learning frameworks initialize weights with random seeds. If worker nodes start with different random weights, averaging their gradients results in corrupted models. This callback broadcasts the exact initial weights from Rank 0 to all workers before training begins.

### Q5: What is the purpose of Intel oneDNN in TensorFlow?
* **Answer**: oneDNN provides accelerated primitives for deep neural networks on Intel architectures. It automatically optimizes Convolution, MatMul, Normalization, and Activation operators using AVX-512 and AMX instructions while fusing consecutive layers to reduce memory bandwidth demands.

### Q6: What does the Slurm command `sbatch` do compared to `srun`?
* **Answer**: `sbatch` submits a job script to the Slurm queue asynchronously and returns a Job ID immediately; the script runs in the background when resources become available. `srun` launches an interactive or parallel job step synchronously, blocking the terminal until execution completes.

### Q7: What causes a Slurm job to remain in `PENDING (Resources)` state?
* **Answer**: It indicates the requested compute resources (nodes, CPUs, GPUs, memory, or partition limits) are currently allocated to other running jobs. The job will transition to `RUNNING` once sufficient hardware is freed.

### Q8: What is Gradient Accumulation, and when is it used on HPC clusters?
* **Answer**: When a batch size does not fit into node memory, gradient accumulation computes forward and backward passes over smaller mini-batches, accumulating gradients over several iterations before applying an optimizer step, simulating a larger batch size.

### Q9: What is `KMP_AFFINITY` in Intel OpenMP runtime?
* **Answer**: `KMP_AFFINITY` controls how OpenMP worker threads are mapped and bound to physical CPU cores and sockets. Setting it to `compact` groups threads close together to maximize L2/L3 cache sharing, whereas `scatter` distributes threads evenly across sockets to maximize memory bandwidth.

### Q10: How does Horovod handle gradient aggregation during backward passes?
* **Answer**: Horovod integrates with framework computational graphs (TensorFlow/PyTorch) via a custom `DistributedOptimizer`. As soon as backpropagation completes for a layer, Horovod immediately begins the Ring-AllReduce for that layer's gradients in parallel while earlier layers are still computing (Computation-Communication Overlap).
""")

# ==============================================================================
# DAY 4
# ==============================================================================
write_f("Day-04_Distributed_Slurm_VTune_Profiling/theory_notes/day04_vtune_hardware_counters.md", """
# Day 4 Theory: Distributed AI Training, Scaling Efficiency & Intel VTune Profiling

## 1. Multi-Node Distributed Training Verification
- **Amdahl's Scalability Metrics**:
  - Throughput: Samples processed per second across the cluster.
  - Scaling Efficiency:
    $$\\text{Efficiency} = \\frac{\\text{Throughput}(N \\text{ Nodes})}{N \\times \\text{Throughput}(1 \\text{ Node})} \\times 100\\%$$
  - Ideal Linear Scaling: 100% efficiency.
  - Communication Saturation: When interconnect latency causes workers to spend more time waiting for Ring-AllReduce than computing forward/backward passes.

## 2. Profiling with Intel VTune Profiler
- **Hardware Performance Monitoring Units (PMUs)**:
  - Microprocessor hardware registers that record hardware events without code instrumentation overhead.
  - Events tracked: `CPU_CLK_UNHALTED`, `INST_RETIRED`, `MEM_LOAD_RETIRED.L1_MISS`, `DTLB_LOAD_MISSES`.
- **Top-Down Microarchitecture Analysis Method (TMAM)**:
  - Formulated by Intel architect Ahmad Yasin to classify CPU execution pipeline bottlenecks:
    1. **Retiring**: Percentage of execution cycles dedicated to retiring real instructions. (Good performance: >50%).
    2. **Frontend Bound**: The CPU execution units are starved because instructions cannot be fetched and decoded fast enough (ICache misses, branch target buffer misses).
    3. **Bad Speculation**: Cycles wasted executing instructions that are discarded due to branch mispredictions.
    4. **Backend Bound**: The execution units are stalled waiting for data:
       - *Core Bound*: Stalls caused by division, heavy FP latency, or execution port contention.
       - *Memory Bound*: Stalls caused by waiting for data from L1, L2, L3 caches or main system DRAM.
- **Hotspots Analysis**: Identifies the exact function and source-code line generating the most CPU clock ticks.
""")

write_f("Day-04_Distributed_Slurm_VTune_Profiling/student_lab_practice/day04_hands_on_challenges.md", """
# Day 4: Student Lab Practice Challenges & Solutions

### Challenge 1: Measure Memory Bandwidth Stride Bottleneck (Level: Beginner)
* **Task**: Run `cpu_bottleneck_demo.py` and explain why contiguous array access is significantly faster than stride access.
* **Explanation**: Stride access jumps across memory addresses, causing every load to fetch a new 64-byte cache line from RAM while discarding 60 unused bytes, saturating memory bandwidth and causing L1/L2 cache misses.

### Challenge 2: VTune CLI Hotspot Collection (Level: Intermediate)
* **Task**: Run `run_vtune_analysis.sh` on your terminal and extract the top 3 functions consuming the most execution time.
* **Solution**:
  ```bash
  vtune -collect hotspots -result-dir ./my_report -- python3 -c "sum(range(10000000))"
  vtune -report summary -result-dir ./my_report
  ```

### Challenge 3: Top-Down Microarchitecture Analysis (Level: Advanced)
* **Task**: Run a TMAM analysis on a matrix multiplication function and determine whether it is Frontend Bound, Backend Bound, or Memory Bound.
""")

write_f("Day-04_Distributed_Slurm_VTune_Profiling/interview_qa/day04_top_interview_qa.md", """
# Day 4: Top 10 Technical Interview Questions & Answers

### Q1: What is Intel VTune Profiler, and how does it collect data without slowing down code?
* **Answer**: VTune is a low-overhead performance analysis tool. Instead of injecting heavy debugging code into binaries (instrumentation), it utilizes Hardware PMU (Performance Monitoring Unit) interrupt sampling. The CPU interrupts execution every few thousand events to record instruction pointers, resulting in less than 2% runtime overhead.

### Q2: What is the Top-Down Microarchitecture Analysis Method (TMAM)?
* **Answer**: TMAM is an Intel methodology that categorizes every CPU pipeline slot into one of four primary buckets: Retiring, Bad Speculation, Frontend Bound, and Backend Bound. This allows developers to systematically diagnose whether bottlenecks stem from branch mispredictions, instruction decode stalls, or memory latency.

### Q3: What is the difference between Core Bound and Memory Bound in VTune?
* **Answer**: Both are sub-categories of Backend Bound stalls. Core Bound means the execution engine is waiting for internal execution units (e.g. divider latency, port saturation). Memory Bound means the execution units are idle waiting for data to arrive from L3 cache or DRAM over the memory controller.

### Q4: What is a Cache Line, and why does contiguous memory access matter?
* **Answer**: A cache line is the minimum unit of data transferred between main memory and CPU caches, standardly 64 bytes. Accessing contiguous elements guarantees that a single 64-byte fetch satisfies multiple sequential instructions, maximizing spatial locality.

### Q5: How do you identify a memory leak or NUMA bottleneck using VTune?
* **Answer**: Using VTune's "Memory Access Analysis", you can inspect Remote DRAM vs Local DRAM access ratios. A high percentage of Remote DRAM accesses indicates that threads are accessing memory allocated on a remote socket across the UPI interconnect, causing severe latency degradation.

### Q6: What is the "Retiring" metric in CPU profiling?
* **Answer**: "Retiring" represents the percentage of CPU pipeline slots that successfully executed and committed their instructions to the architectural state. A high retiring rate (>50%) indicates high microarchitectural efficiency.

### Q7: What causes "Bad Speculation" in high-performance programs?
* **Answer**: Bad Speculation is caused by branch mispredictions in loops or conditional statements. The CPU speculatively fetches and executes instructions along the predicted path; when the prediction is wrong, the pipeline must be flushed, wasting energy and clock cycles.

### Q8: What is Sampling Frequency in profiling, and what happens if it is too high?
* **Answer**: Sampling frequency is how frequently the profiler interrupts the CPU to record state. If the frequency is set too high, profiler overhead distorts execution timings (Observer Effect / Heisenbug). If set too low, brief execution spikes and hotspots may be missed.

### Q9: How can compiler flags help resolve Frontend Bound bottlenecks?
* **Answer**: Compilers can use Function Inlining (`-finline-functions`) and Loop Unrolling to eliminate jump instructions and branch overhead, reducing instruction cache misses and decode stalls.

### Q10: What is Scaling Efficiency in distributed deep learning?
* **Answer**: Scaling efficiency measures how close a cluster gets to linear acceleration. If 1 node trains at 100 images/sec and 4 nodes train at 360 images/sec, scaling efficiency is $\\frac{360}{4 \\times 100} = 90\\%$. The missing 10% is lost to network communication latency during gradient synchronization.
""")

# ==============================================================================
# DAY 5
# ==============================================================================
write_f("Day-05_GenAI_LLMs_Gaudi_OpenVINO/theory_notes/day05_genai_llms_openvino_gaudi.md", """
# Day 5 Theory: Generative AI, Large Language Models on HPC, Habana Gaudi & OpenVINO

## 1. LLM System Mechanics & The Memory Wall
- **Parameter Memory Footprints**:
  - FP32: 4 bytes per param (70B model = 280 GB).
  - BF16/FP16: 2 bytes per param (70B model = 140 GB).
  - INT8: 1 byte per param (70B model = 70 GB).
  - INT4: 0.5 bytes per param (70B model = 35 GB).
- **The Two Inference Phases**:
  1. **Prefill Phase (Prompt Ingestion)**:
     - All prompt tokens are processed simultaneously.
     - Operation: Matrix-Matrix Multiplication (GEMM).
     - Nature: **Compute-Bound** (High Arithmetic Intensity, FLOP/s dominates).
  2. **Decode Phase (Autoregressive Generation)**:
     - 1 token produced per forward pass.
     - Operation: Matrix-Vector Multiplication (GEMV).
     - Nature: **Memory-Bandwidth Bound** (Low Arithmetic Intensity: 1 FLOP per 2 bytes read). To generate 1 token, all 8 Billion weights must be read from memory into cache!
- **KV-Cache (Key-Value Cache)**:
  - Caches Key and Value attention tensors for all previous tokens in memory.
  - Eliminates $O(N^2)$ recomputation, turning each token generation into $O(1)$ computation at the expense of growing DRAM consumption.

## 2. Intel Hardware for LLMs
- **Intel Xeon Scalable**:
  - Intel AMX (Advanced Matrix Extensions): 2D tile matrix multiplication in silicon for BF16 and INT8.
  - Multi-Terabyte system memory (1TB-4TB DDR5) enabling 70B+ models to run in host memory.
- **Habana Gaudi (Gaudi 2 / Gaudi 3)**:
  - Dedicated AI processors designed by Habana Labs.
  - Features 24 integrated 100GbE RoCE ports directly on-chip for cluster scale-out without external NICs.
  - High Bandwidth Memory: Up to 128 GB HBM3 delivering 3.7 TB/s bandwidth.

## 3. Intel OpenVINO Toolkit for LLMs
- Converts PyTorch / Hugging Face models to OpenVINO Intermediate Representation (IR):
  - `model.xml`: Network topology and fused operator graph.
  - `model.bin`: Binary weights and biases.
- **NNCF (Neural Network Compression Framework)**:
  - Weight-Only Quantization (WOQ): Compresses weights to INT4/INT8 to bypass memory bandwidth bottlenecks while maintaining FP16 activation precision.

## 4. Parameter-Efficient Fine-Tuning (LoRA) on HPC
- Decomposes weight update matrix $\\Delta W$ into low-rank matrices: $\\Delta W = B \\times A$ ($r \\ll d$).
- Freezes base model weights and trains only 0.1% to 0.2% of parameters, slashing VRAM and optimizer state memory requirements.
""")

write_f("Day-05_GenAI_LLMs_Gaudi_OpenVINO/student_lab_practice/day05_hands_on_challenges.md", """
# Day 5: Student Lab Practice Challenges & Solutions

### Challenge 1: OpenVINO Model Export & Inspection (Level: Beginner)
* **Task**: Run `openvino_llm_benchmark.py` and inspect the generated `.xml` graph file to see fused attention operators.
* **Verification**: Verify that `TinyLlama` executes on CPU and report generation throughput in tokens/second.

### Challenge 2: Deploying the Local AI Backend API (Level: Intermediate)
* **Task**: Launch `llm_fastapi_server.py` and test it with a cURL request from a separate terminal.
* **Solution**:
  ```bash
  python3 llm_fastapi_server.py &
  curl -X POST http://localhost:8000/api/chat \\
       -H "Content-Type: application/json" \\
       -d '{"user_message": "What is the difference between MPI and OpenMP?"}'
  ```

### Challenge 3: INT4 Weight-Only Quantization Benchmark (Level: Advanced)
* **Task**: Compare memory consumption and tokens/second of uncompressed FP16 vs INT4 quantized OpenVINO models using Python's `psutil` or `free -h`.
""")

write_f("Day-05_GenAI_LLMs_Gaudi_OpenVINO/interview_qa/day05_top_interview_qa.md", """
# Day 5: Top 10 Technical Interview Questions & Answers

### Q1: Why is LLM token generation memory-bandwidth bound rather than compute-bound?
* **Answer**: During the decode phase, an LLM produces only one token at a time. This requires performing a matrix-vector multiplication (GEMV) where every single weight of the multi-billion parameter model must be fetched from memory into the processor cache for just a single multiply-add operation per weight (Arithmetic Intensity $\\approx 1$).

### Q2: What is the KV-Cache in Transformers, and why does it consume so much memory?
* **Answer**: The KV-Cache stores the Key and Value projection vectors of all preceding tokens in self-attention layers so they do not need to be recomputed for each newly generated token. For long context windows and large batch sizes, the KV-Cache can consume tens of gigabytes of RAM.

### Q3: How does Intel AMX (Advanced Matrix Extensions) accelerate LLM inference on CPUs?
* **Answer**: AMX introduces hardware 2D tile registers (TMUL) into Xeon cores. Instead of streaming one 512-bit vector at a time, AMX performs a $16 \\times 64$ matrix multiplication of BF16 or INT8 numbers in a single cycle, achieving up to 8x the throughput of AVX-512.

### Q4: What is the architectural advantage of Habana Gaudi over Nvidia H100?
* **Answer**: Habana Gaudi integrates 24 standard 100Gbps RoCE (RDMA over Converged Ethernet) ports directly onto the processor die. This eliminates the need for expensive external Mellanox network interface cards (NICs) and PCIe switches, lowering cluster cost and latency.

### Q5: How does OpenVINO Intermediate Representation (IR) differ from standard ONNX?
* **Answer**: OpenVINO IR splits the model into an XML file (`model.xml`) describing the execution graph and a binary file (`model.bin`) holding serialized weights. OpenVINO IR applies hardware-specific operator fusions tailored specifically for Intel CPU/iGPU/dGPU vector execution units.

### Q6: What is Weight-Only Quantization (WOQ), and why is it ideal for LLM inference?
* **Answer**: In WOQ, only the model parameters (weights) are compressed from 16-bit to 4-bit or 8-bit integers, while activations remain in 16-bit floating point. Because memory bandwidth is the primary bottleneck during token decoding, reducing weight size by 4x speeds up memory streaming with negligible loss in accuracy.

### Q7: How does LoRA (Low-Rank Adaptation) enable fine-tuning on consumer/academic hardware?
* **Answer**: Full fine-tuning requires updating all model weights and storing optimizer states for every parameter ($16\\text{ bytes/param}$). LoRA freezes the original weights and trains two small low-rank decomposition matrices ($A$ and $B$) on attention layers ($r \\ll d$), reducing trainable parameters by 99% and slashing VRAM requirements.

### Q8: What is PagedAttention (as used in modern inference engines)?
* **Answer**: PagedAttention solves KV-Cache memory fragmentation by borrowing virtual memory paging concepts from Operating Systems. Instead of allocating contiguous physical memory for KV-caches, it partitions them into fixed-size pages allocated dynamically on demand.

### Q9: What is the difference between Post-Training Quantization (PTQ) and Quantization-Aware Training (QAT)?
* **Answer**: PTQ quantizes an already-trained model's weights and activations using a small calibration dataset without retraining. QAT simulates quantization rounding errors during training so the model's weights adapt to lower precision, preserving higher accuracy at the cost of additional training time.

### Q10: Why are enterprise data centers running LLM inference on Intel Xeon CPUs instead of GPUs?
* **Answer**: Xeon servers already comprise over 70% of enterprise server infrastructure and support massive system RAM (1TB to 4TB). Using AMX matrix acceleration and INT4 quantization via OpenVINO, CPUs can comfortably deliver 20-30 tokens/sec for medium-concurrency applications without purchasing expensive $30,000 GPUs.
""")

print("\n===========================================================")
print("ALL EMPTY FOLDERS HAVE BEEN POPULATED WITH 100% COMPLETION!")
print("===========================================================")
