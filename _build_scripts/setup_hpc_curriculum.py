# setup_hpc_curriculum.py
import os
import sys

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum"

def write_file(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"Created: {rel_path}")

# ==============================================================================
# DAY 1 FILES
# ==============================================================================
write_file("Day-01_HPC_Linux_Shell_oneAPI/theory_notes.md", """
# Day 1: HPC Foundations, Silicon Architecture & Linux Mastery

## 1. High Performance Computing (HPC) First Principles
- **The Limit of Single Machines**: Dennard scaling collapsed around 2005. CPU clock frequencies cannot exceed ~5 GHz without melting silicon due to thermal leakage and quantum tunneling.
- **HPC Solution**: Scale-Out Parallelism. Hundreds or thousands of compute servers (nodes) connected via high-speed, low-latency fabric (InfiniBand / RoCE) behaving as a unified supercomputer.
- **Performance Metrics**:
  - FLOPS (Floating Point Operations Per Second):
    - GigaFLOPS ($10^9$) -> TeraFLOPS ($10^{12}$) -> PetaFLOPS ($10^{15}$) -> ExaFLOPS ($10^{18}$).
- **The 3 System Pillars**:
  1. **Compute**: Multi-socket Intel Xeon CPUs and specialized accelerators.
  2. **Memory Bandwidth**: Multi-channel DDR5 / HBM (High Bandwidth Memory).
  3. **Interconnect**: InfiniBand (200-400 Gbps, sub-microsecond latency, Zero-Copy RDMA).

## 2. Intel HPC Silicon Architecture
- **Intel Xeon Scalable Processors**:
  - Multi-socket configurations (2 to 8 sockets connected via UPI).
  - NUMA (Non-Uniform Memory Access): Memory latency depends on which socket the core belongs to.
  - SIMD Vector Engines:
    - **AVX-512**: 512-bit registers (ZMM0-ZMM31), sixteen 32-bit floats per clock cycle.
    - **Intel AMX (Advanced Matrix Extensions)**: 2D hardware matrix multiplication engine (TMUL) for BF16/INT8.
- **Intel Data Center GPUs (Max Series / Ponte Vecchio)**:
  - 128 GB HBM2e memory delivering over 3.2 TB/s bandwidth.
  - XMX (Xe Matrix Extensions) systolic arrays for deep learning tensor contractions.
- **Habana Gaudi (Gaudi 2 / 3)**:
  - Dedicated AI ASIC (Application-Specific Integrated Circuit).
  - Integrated 24x 100GbE RoCE ports directly on the silicon die (eliminates external NICs).

## 3. HPC Linux & Environment Mechanics
- **File Systems**:
  - `/home`: NFS (Network File System) - slow, for configuration and scripts only.
  - `/scratch` or `/tmp`: High-throughput parallel storage (Lustre / GPFS) for datasets and checkpoints.
- **Environment Modules**:
  - `module avail` / `module load intel/oneapi` / `module list`
- **Passwordless SSH**:
  - Ed25519 elliptic curve keys (`ssh-keygen -t ed25519`).
  - `~/.ssh/config` multiplexing and persistent connections.
""")

write_file("Day-01_HPC_Linux_Shell_oneAPI/live_demo/orchestrator.sh", """
#!/usr/bin/env bash
# ==============================================================================
# Project: Automated HPC Node Profiler & Benchmark Orchestrator
# Author : Shivam Gupta
# ==============================================================================
set -eo pipefail

LOG_DIR="./hpc_runs"
mkdir -p "$LOG_DIR"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
LOG_FILE="$LOG_DIR/run_$TIMESTAMP.log"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "=========================================================="
echo "    HIGH PERFORMANCE COMPUTING AUTOMATED PIPELINE         "
echo "=========================================================="
echo "Host Machine : $(hostname)"
echo "Current User : $(whoami)"
echo "Timestamp    : $(date '+%Y-%m-%d %H:%M:%S')"
echo "Kernel       : $(uname -r)"

echo "----------------------------------------------------------"
echo "[1] Analyzing Silicon Microarchitecture..."
CORES=$(nproc)
echo "[+] Detected Accessible CPU Cores: $CORES"

if grep -q "avx512" /proc/cpuinfo 2>/dev/null; then
    echo "[+] Silicon Feature: AVX-512 (512-bit SIMD Ultra Vector Engine Active)"
elif grep -q "avx2" /proc/cpuinfo 2>/dev/null; then
    echo "[+] Silicon Feature: AVX2 (256-bit Vector Engine Active)"
else
    echo "[-] Standard x86 Vector Instructions"
fi

echo "----------------------------------------------------------"
echo "[2] Tuning Parallel Environment Variables..."
export OMP_NUM_THREADS=$CORES
export PYTHONUNBUFFERED=1
echo "[+] Set OMP_NUM_THREADS to $CORES"

echo "----------------------------------------------------------"
echo "[3] Running Side-by-Side Benchmark..."
python3 compute_engine.py standard
python3 compute_engine.py accelerated

echo "----------------------------------------------------------"
echo "[+] Pipeline Completed Successfully. Archived to: $LOG_FILE"
echo "=========================================================="
""")

write_file("Day-01_HPC_Linux_Shell_oneAPI/live_demo/compute_engine.py", """
# compute_engine.py
import sys
import time
import os

mode = sys.argv[1] if len(sys.argv) > 1 else "standard"
SIZE = 5000000

if mode == "standard":
    print("[-] Running STANDARD (Single-threaded Python) Mode...")
    t0 = time.time()
    data = list(range(SIZE))
    result = [x * 1.00001 for x in data]
    total = sum(result)
    elapsed = time.time() - t0
    print(f"[-] Standard Execution Time : {elapsed:.3f}s | Sum: {total:.2f}")

elif mode == "accelerated":
    print("[+] Running HPC ACCELERATED (Intel Vectorized) Mode...")
    import numpy as np
    t0 = time.time()
    data = np.arange(SIZE, dtype=np.float64)
    result = data * 1.00001
    total = np.sum(result)
    elapsed = time.time() - t0
    print(f"[+] HPC Vectorized Time     : {elapsed:.3f}s | Sum: {total:.2f}")
""")

write_file("Day-01_HPC_Linux_Shell_oneAPI/student_lab_practice/day01_challenges.md", """
# Day 1: Student Lab Practice Challenges

### Challenge 1: The Silicon Audit (Level: Easy)
- Write a bash command pipeline to extract and display:
  1. Total physical sockets
  2. Cores per socket
  3. L1d, L1i, L2, and L3 cache sizes in KB/MB
- **Verification**: Output must be formatted into a clean markdown table.

### Challenge 2: Passwordless Cluster Login (Level: Medium)
- Generate a 256-bit Ed25519 SSH key without password.
- Write a `~/.ssh/config` file with host alias `hpc-node`.
- Connect using `ssh hpc-node` and execute `uptime` non-interactively.

### Challenge 3: The Parallel Workload Launcher (Level: Hard)
- Write a bash script `launch_matrix.sh` that:
  1. Takes two arguments: `<threads>` and `<iterations>`
  2. Sets `OMP_NUM_THREADS` dynamically
  3. Runs 4 background worker processes simultaneously using `&` and waits with `wait`
  4. Measures wall-clock execution time and logs CPU temperature/utilization.
""")

write_file("Day-01_HPC_Linux_Shell_oneAPI/curated_resources.md", """
# Day 1: Curated Learning Resources

### For Students:
1. **Intel oneAPI Official Onboarding**: [software.intel.com/oneapi](https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html)
2. **Linux Command Line for HPC**: [HPC Carpentry Tutorial](https://carpentries-incubator.github.io/hpc-intro/)
3. **Intel DevCloud / Tiber AI Cloud Registration**: [cloud.intel.com](https://cloud.intel.com) (Free access to Xeon & Gaudi)

### For Shivam (Personal Master Prep):
- **YouTube**: "Introduction to High Performance Computing" - LLNL (Lawrence Livermore National Laboratory) series.
- **YouTube**: "Intel oneAPI Architecture Deep Dive" by Intel Software Channel.
- **Docs**: Intel 64 and IA-32 Architectures Optimization Reference Manual (Sections on AVX-512 and AMX).
""")

# ==============================================================================
# DAY 2 FILES
# ==============================================================================
write_file("Day-02_Parallel_OpenMP_MPI_oneDAL/theory_notes.md", """
# Day 2: Parallel Computing, OpenMP, MPI & Intel AI Analytics

## 1. Parallel Computing Paradigms
- **Shared Memory (OpenMP)**:
  - All threads access the same physical address space.
  - Fast, zero network communication.
  - Critical Challenges: Race conditions, deadlocks, false sharing (cache line contention).
  - OpenMP Directives: `#pragma omp parallel for`, `private()`, `shared()`, `reduction(+:sum)`.
- **Distributed Memory (MPI - Message Passing Interface)**:
  - Each process has its own isolated memory space across different cluster nodes.
  - Explicit communication via network packets (InfiniBand/Ethernet).
  - Core API Concepts:
    - Communicator: `MPI_COMM_WORLD`
    - Ranks: Unique ID (0 to N-1)
    - Point-to-Point: `MPI_Send()`, `MPI_Recv()`
    - Collective Communications:
      - `MPI_Bcast()`: One node sends data to all.
      - `MPI_Scatter()`: One node divides an array and sends parts to all nodes.
      - `MPI_Gather()`: Reverse of scatter; collects parts from all nodes to master.
      - `MPI_Reduce()` / `MPI_Allreduce()`: Computes sum/max/min across all nodes.

## 2. Intel AI Analytics Toolkit & oneDAL
- **The Python Performance Problem**: Standard Scikit-learn algorithms (KMeans, SVM, Random Forest) use single-threaded or un-vectorized C/Cython loops.
- **`scikit-learn-intelex` (Intel Extension for Scikit-learn)**:
  - Dynamically patches standard Scikit-learn algorithms in-memory.
  - Dispatches math to Intel oneDAL (Data Analytics Library) leveraging AVX-512 / AMX.
  - Yields 10x to 40x speedups with ZERO code rewrite!
""")

write_file("Day-02_Parallel_OpenMP_MPI_oneDAL/live_demo/omp_multithreading.cpp", """
#include <iostream>
#include <omp.h>
#include <vector>
#include <chrono>

int main() {
    const int SIZE = 100000000;
    std::vector<double> a(SIZE, 1.0);
    double sum = 0.0;

    std::cout << "[*] Starting OpenMP Parallel Reduction on " << omp_get_max_threads() << " threads..." << std::endl;
    auto t0 = std::chrono::high_resolution_clock::now();

    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < SIZE; i++) {
        sum += a[i] * 0.5;
    }

    auto t1 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = t1 - t0;

    std::cout << "[+] OpenMP Sum Result: " << sum << std::endl;
    std::cout << "[+] Computation Time : " << elapsed.count() << " seconds" << std::endl;
    return 0;
}
""")

write_file("Day-02_Parallel_OpenMP_MPI_oneDAL/live_demo/mpi_collective.py", """
# mpi_collective.py
# Run with: mpirun -n 4 python3 mpi_collective.py
from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

ARRAY_SIZE = 8

if rank == 0:
    data = np.arange(ARRAY_SIZE * size, dtype='i')
    print(f"[Master Node 0] Master Dataset: {data}")
else:
    data = None

# Scatter: Distribute chunks to every node
local_data = np.empty(ARRAY_SIZE, dtype='i')
comm.Scatter(data, local_data, root=0)

# Each node performs local computation
local_sum = np.sum(local_data)
print(f"[Node {rank}] Received chunk {local_data} | Local Sum = {local_sum}")

# Reduce: Sum all local sums into master rank
global_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

if rank == 0:
    print(f"[Master Node 0] Final Global Reduced Sum: {global_sum}")
""")

write_file("Day-02_Parallel_OpenMP_MPI_oneDAL/live_demo/intel_scikit_speedup.py", """
# intel_scikit_speedup.py
import time
import numpy as np

print("="*60)
print("     INTEL EXTENSION FOR SCIKIT-LEARN SPEEDUP BENCHMARK    ")
print("="*60)

# 1. Generate Synthetic Clustering Dataset (1 Million Points, 32 Features)
print("[*] Generating 1,000,000 Samples with 32 features...")
np.random.seed(42)
X = np.random.randn(1000000, 32).astype(np.float32)

# 2. Benchmark Standard Scikit-Learn
from sklearn.cluster import KMeans
print("\n[1] Running Standard Scikit-Learn KMeans...")
t0 = time.time()
kmeans_std = KMeans(n_clusters=8, max_iter=20, random_state=42, n_init='auto').fit(X)
std_time = time.time() - t0
print(f"[-] Standard KMeans Time : {std_time:.2f} seconds")

# 3. Benchmark with Intel oneDAL Acceleration
from sklearnex import patch_sklearn
patch_sklearn() # Enables Intel hardware vectorization

from sklearn.cluster import KMeans as IntelKMeans
print("\n[2] Running Intel-Accelerated KMeans...")
t0 = time.time()
kmeans_intel = IntelKMeans(n_clusters=8, max_iter=20, random_state=42, n_init='auto').fit(X)
intel_time = time.time() - t0
print(f"[+] Intel-Accelerated Time: {intel_time:.2f} seconds")

print("\n" + "="*60)
print(f"[🔥] SPEEDUP MULTIPLIER: {std_time / intel_time:.2f}x FASTER!")
print("="*60)
""")

write_file("Day-02_Parallel_OpenMP_MPI_oneDAL/curated_resources.md", """
# Day 2: Curated Learning Resources

### For Students:
1. **OpenMP Official Tutorial**: [openmp.org/resources/tutorials-winterschool/](https://www.openmp.org/)
2. **MPI for Python (mpi4py) Documentation**: [mpi4py.readthedocs.io](https://mpi4py.readthedocs.io/)
3. **Intel Extension for Scikit-learn**: [intel.github.io/scikit-learn-intelex/](https://intel.github.io/scikit-learn-intelex/)

### For Shivam (Personal Master Prep):
- **YouTube**: Tim Mattson's "Introduction to OpenMP" (Intel Principal Engineer series - Legendary 8-part tutorial).
- **YouTube**: "MPI Programming in Python" by EuroHPC / Archer2.
- **GitHub**: `intel/scikit-learn-intelex` official samples.
""")

# ==============================================================================
# DAY 3 FILES
# ==============================================================================
write_file("Day-03_DeepLearning_TF_Slurm_Horovod/theory_notes.md", """
# Day 3: Deep Learning on HPC, Slurm & Distributed Training (Horovod)

## 1. Hardware-Aware Deep Learning Optimization
- Standard deep learning operators (Convolutions, GEMM matrix multiplies) spend 80% of time moving tensors between memory and cache.
- **oneDNN (oneAPI Deep Neural Network Library)**:
  - Fuses layers (e.g., Conv2D + BiasAdd + ReLU) into single-pass execution.
  - Automatically targets AVX-512 and AMX (Tile Matrix Multiply).
  - Environment flags: `KMP_BLOCKTIME=0`, `KMP_AFFINITY=granularity=fine,compact,1,0`.

## 2. Slurm Workload Manager Architecture
- **Slurm Daemons**:
  - `slurmctld`: Central controller daemon running on head node.
  - `slurmd`: Worker node daemon listening for job execution.
- **Core Commands**:
  - `sinfo`: Node status and partition allocations.
  - `squeue`: Monitoring running/pending jobs.
  - `sbatch`: Asynchronous batch script submission.
  - `srun`: Synchronous step execution across allocated nodes.
  - `scancel <id>`: Job termination.

## 3. Distributed Training with Horovod (Ring-AllReduce)
- **Why Parameter Server Fails**: Bandwidth bottlenecks on the master node when scaling to 16+ nodes.
- **Ring-AllReduce (Horovod)**:
  - Logical ring topology where each node communicates only with immediate neighbors.
  - Bandwidth consumption is independent of cluster size: $2 \times \frac{N-1}{N} \times \text{Size}$.
  - Framework neutral: Works seamlessly across TensorFlow, Keras, and PyTorch.
""")

write_file("Day-03_DeepLearning_TF_Slurm_Horovod/live_demo/slurm_batch_template.slurm", """
#!/bin/bash
# ==============================================================================
# Project: Distributed Deep Learning via Slurm & Horovod
# Author : Shivam Gupta
# ==============================================================================
#SBATCH --job-name=gla_hpc_dl_train
#SBATCH --output=logs/dl_train_%j.out
#SBATCH --error=logs/dl_train_%j.err
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --time=01:00:00
#SBATCH --partition=compute_cluster

module load intel/oneapi
module load python/3.11-mkl

echo "=========================================================="
echo "Job ID       : $SLURM_JOB_ID"
echo "Nodes        : $SLURM_JOB_NODELIST"
echo "Tasks/Node   : $SLURM_NTASKS_PER_NODE"
echo "CPUs/Task    : $SLURM_CPUS_PER_TASK"
echo "=========================================================="

# Launch Horovod across allocated cluster nodes
srun python3 horovod_tf_training.py
""")

write_file("Day-03_DeepLearning_TF_Slurm_Horovod/live_demo/horovod_tf_training.py", """
# horovod_tf_training.py
import tensorflow as tf
import horovod.tensorflow as hvd
import time

# 1. Initialize Horovod
hvd.init()
print(f"[Worker Rank {hvd.rank()}/{hvd.size()}] Initialized Horovod process.")

# 2. Pin to CPU/GPU threads
tf.config.threading.set_inter_op_parallelism_threads(2)
tf.config.threading.set_intra_op_parallelism_threads(4)

# 3. Create Synthetic Dataset
(x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
x_train = x_train[..., tf.newaxis] / 255.0

# Partition dataset shards across workers
dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train))
dataset = dataset.shard(num_shards=hvd.size(), index=hvd.rank())
dataset = dataset.shuffle(1000).batch(64)

# 4. Define Deep Learning Model
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10)
])

# 5. Scale learning rate with cluster worker count
scaled_lr = 0.001 * hvd.size()
opt = tf.keras.optimizers.Adam(scaled_lr)

# 6. Wrap with DistributedOptimizer (Performs Ring-AllReduce)
opt = hvd.DistributedOptimizer(opt)

model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=opt,
    metrics=['accuracy'],
    experimental_run_tf_function=False
)

# 7. Broadcast initial random weights from Rank 0
callbacks = [
    hvd.callbacks.BroadcastGlobalVariablesCallback(0),
    hvd.callbacks.MetricAverageCallback()
]

# Only Rank 0 saves checkpoints and prints progress
verbose = 1 if hvd.rank() == 0 else 0

t0 = time.time()
model.fit(dataset.take(50), epochs=1, callbacks=callbacks, verbose=verbose)
if hvd.rank() == 0:
    print(f"[Master Rank 0] Distributed Training Step Completed in: {time.time() - t0:.2f}s")
""")

write_file("Day-03_DeepLearning_TF_Slurm_Horovod/curated_resources.md", """
# Day 3: Curated Learning Resources

### For Students:
1. **Slurm Workload Manager Official Quickstart**: [slurm.schedmd.com/quickstart.html](https://slurm.schedmd.com/quickstart.html)
2. **Horovod Distributed Deep Learning**: [horovod.readthedocs.io](https://horovod.readthedocs.io/)
3. **Intel oneDNN Architecture Overview**: [oneapi-src.github.io/oneDNN/](https://oneapi-src.github.io/oneDNN/)

### For Shivam (Personal Master Prep):
- **YouTube**: "Deep Learning with Horovod: Uber's Open Source Distributed Training Framework" by Alex Sergeev.
- **YouTube**: "Slurm Tutorial: Building and Submitting Batch Jobs on HPC" by Harvard FAS Research Computing.
""")

# ==============================================================================
# DAY 4 FILES
# ==============================================================================
write_file("Day-04_Distributed_Slurm_VTune_Profiling/theory_notes.md", """
# Day 4: Distributed AI Training & Profiling with Intel VTune

## 1. Multi-Node Distributed Training Verification
- Analyzing network latency vs compute time during Ring-AllReduce gradient transfers.
- Scaling Efficiency Formula:
  $$\\text{Scaling Efficiency} = \\frac{\\text{Throughput on } N \\text{ Nodes}}{N \\times \\text{Throughput on 1 Node}} \\times 100$$
- Linear scaling vs Communication overhead saturation.

## 2. Profiling with Intel VTune Profiler
- **Hardware Performance Monitoring Units (PMU)**: Hardware registers inside CPU silicon that count clock cycles, instructions retired, cache misses, and pipeline stalls.
- **Top-Down Microarchitecture Analysis Method (TMAM)**:
  1. **Retiring**: Percentage of cycles spent executing useful instructions (Target: >50%).
  2. **Frontend Bound**: Instruction fetch/decode stalls (Branch targets, icache misses).
  3. **Bad Speculation**: Branch mispredictions that flush the execution pipeline.
  4. **Backend Bound**:
     - *Core Bound*: High latency compute operations (division, dependency chains).
     - *Memory Bound*: Waiting for RAM loads, L1/L2/L3 cache misses.
- **VTune Analysis Types**:
  - Hotspots Analysis: Identifies exact source code lines and functions consuming execution time.
  - Memory Access: Uncovers NUMA remote memory latency and bus saturation.
  - Threading: Identifies lock contention and thread starvation.
""")

write_file("Day-04_Distributed_Slurm_VTune_Profiling/live_demo/cpu_bottleneck_demo.py", """
# cpu_bottleneck_demo.py
# Designed to demonstrate Memory-Bound vs Compute-Bound profiles in VTune
import time
import numpy as np

SIZE = 50000000

print("[*] Running Cache-Thrashing Memory Access (Inefficient)...")
t0 = time.time()
# Stride access causes L1/L2/L3 cache misses
arr = np.ones(SIZE, dtype=np.int32)
stride_sum = np.sum(arr[::64])
print(f"[-] Stride Sum: {stride_sum} in {time.time() - t0:.3f}s")

print("[*] Running Memory-Contiguous Vectorized Access (Optimized)...")
t0 = time.time()
contiguous_sum = np.sum(arr[:SIZE//64])
print(f"[+] Contiguous Sum: {contiguous_sum} in {time.time() - t0:.3f}s")
""")

write_file("Day-04_Distributed_Slurm_VTune_Profiling/live_demo/run_vtune_analysis.sh", """
#!/usr/bin/env bash
# run_vtune_analysis.sh
set -eo pipefail

echo "=========================================================="
echo "           INTEL VTUNE PROFILING AUTOMATION               "
echo "=========================================================="

RESULT_DIR="./vtune_hotspots_report"
rm -rf "$RESULT_DIR"

echo "[*] Collecting Hotspots on target workload..."
vtune -collect hotspots -result-dir "$RESULT_DIR" -- python3 cpu_bottleneck_demo.py

echo "[*] Generating Summary Report from PMU Hardware Counters..."
vtune -report summary -result-dir "$RESULT_DIR"

echo "=========================================================="
echo "[+] VTune Profiling Completed! Open in GUI with: vtune-gui $RESULT_DIR"
""")

write_file("Day-04_Distributed_Slurm_VTune_Profiling/curated_resources.md", """
# Day 4: Curated Learning Resources

### For Students:
1. **Intel VTune Profiler User Guide**: [intel.com/vtune](https://www.intel.com/content/www/us/en/developer/tools/oneapi/vtune-profiler.html)
2. **Top-Down Microarchitecture Analysis Method**: [Intel TMAM Paper by Ahmad Yasin](https://hal.archives-ouvertes.fr/hal-01188371/document)

### For Shivam (Personal Master Prep):
- **YouTube**: "Intel VTune Profiler: Getting Started & Finding Performance Bottlenecks" (Intel Software).
- **YouTube**: "CPU Microarchitecture and Top-Down Profiling" by Denis Bakhvalov (Author of Performance Analysis and Tuning on Modern CPUs).
""")

# ==============================================================================
# DAY 5 FILES
# ==============================================================================
write_file("Day-05_GenAI_LLMs_Gaudi_OpenVINO/theory_notes.md", """
# Day 5: Generative AI, LLMs on HPC, Habana Gaudi & OpenVINO

## 1. LLM System Demands & The Memory Wall
- **Static Parameter Memory**: Parameters $\\times$ Bytes per param (FP16 = 2B, INT8 = 1B, INT4 = 0.5B).
- **The Two Inference Phases**:
  1. *Prefill Phase (Prompt Ingestion)*: Compute-Bound matrix-matrix GEMM multiplication.
  2. *Decode Phase (Autoregressive Generation)*: Memory-Bandwidth-Bound matrix-vector GEMV. Requires streaming every single parameter from RAM per token!
- **KV-Cache (Key-Value Cache)**: Stores attention matrices to convert $O(N^2)$ recomputation to $O(1)$ token steps.

## 2. Intel LLM Hardware Architecture
- **Intel Xeon Scalable**:
  - AMX (Advanced Matrix Extensions): Dedicated 2D systolic hardware tiles in silicon for BF16/INT8 matrix contractions.
  - Multi-Terabyte system memory (1TB-4TB DDR5) allowing 70B+ parameter models to fit in CPU RAM.
- **Habana Gaudi (Gaudi 2 / 3)**:
  - Custom Tensor Processing Cores (TPC) + Matrix Multiplication Engines (MME).
  - 24 integrated 100GbE RoCE ports directly on-chip for seamless cluster scale-out without external NICs.

## 3. OpenVINO Inference Optimization
- Converts models to OpenVINO Intermediate Representation (IR):
  - `model.xml`: Computational graph topology and fused operator kernels.
  - `model.bin`: Binary weights and biases.
- NNCF Weight-Only Quantization (WOQ): Compresses weights to INT4/INT8 to bypass the Memory Bandwidth wall during generation.

## 4. Fine-Tuning LLMs via LoRA (Low-Rank Adaptation)
- Decomposes weight updates $\\Delta W$ into low-rank matrices $B \\times A$ ($r \\ll d$).
- Reduces trainable parameters by 99.8% (from 7B to ~15M), enabling multi-node fine-tuning on HPC clusters.
""")

write_file("Day-05_GenAI_LLMs_Gaudi_OpenVINO/live_demo/openvino_llm_benchmark.py", """
# openvino_llm_benchmark.py
import time
from optimum.intel.openvino import OVModelForCausalLM
from transformers import AutoTokenizer, TextStreamer

MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
PROMPT = "<|system|>\nYou are an HPC expert.<|user|>\nWhat is the difference between latency and throughput in LLMs?<|assistant|>\n"

print("="*65)
print("     INTEL OPENVINO LOCAL LLM HARDWARE-ACCELERATED BENCHMARK   ")
print("="*65)

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
inputs = tokenizer(PROMPT, return_tensors="pt")

print(f"[*] Exporting and Compiling {MODEL_ID} with OpenVINO IR...")
t0 = time.time()
model = OVModelForCausalLM.from_pretrained(
    MODEL_ID,
    export=True,
    compile=True,
    device="CPU"
)
print(f"[+] Model compiled in {time.time() - t0:.2f} seconds.")

streamer = TextStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
print("\n--- Live Streaming Generation from Intel Silicon ---")
start_gen = time.time()
output = model.generate(**inputs, max_new_tokens=80, streamer=streamer, temperature=0.7)
gen_time = time.time() - start_gen

tokens_generated = len(output[0]) - inputs['input_ids'].shape[1]
print(f"\n" + "-"*65)
print(f"[+] Tokens Generated : {tokens_generated}")
print(f"[+] Total Time       : {gen_time:.2f}s")
print(f"[+] Real-Time Speed  : {tokens_generated / gen_time:.2f} tokens/second")
print("="*65)
""")

write_file("Day-05_GenAI_LLMs_Gaudi_OpenVINO/live_demo/llm_fastapi_server.py", """
# llm_fastapi_server.py
# Launch with: python3 llm_fastapi_server.py
from fastapi import FastAPI
from pydantic import BaseModel
from optimum.intel.openvino import OVModelForCausalLM
from transformers import AutoTokenizer
import uvicorn

app = FastAPI(title="Local Intel-Accelerated AI Backend")

print("[*] Initializing Intel OpenVINO AI Engine...")
MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = OVModelForCausalLM.from_pretrained(MODEL_ID, export=True, compile=True, device="CPU")
print("[+] AI Engine Ready to serve requests on port 8000!")

class ChatRequest(BaseModel):
    user_message: str

@app.post("/api/chat")
async def chat_endpoint(req: ChatRequest):
    prompt = f"<|system|>\nYou are an AI assistant for a final year project.<|user|>\n{req.user_message}<|assistant|>\n"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100, temperature=0.6)
    full_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    assistant_reply = full_text.split("<|assistant|>")[-1].strip()
    return {"reply": assistant_reply, "engine": "Intel-OpenVINO-Accelerated"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
""")

write_file("Day-05_GenAI_LLMs_Gaudi_OpenVINO/curated_resources.md", """
# Day 5: Curated Learning Resources

### For Students:
1. **Intel OpenVINO Generative AI Notebooks**: [github.com/openvinotoolkit/openvino_notebooks](https://github.com/openvinotoolkit/openvino_notebooks) (The #1 hands-on repo for LLMs).
2. **Hugging Face Optimum Intel**: [huggingface.co/docs/optimum/main/en/intel/index](https://huggingface.co/docs/optimum/main/en/intel/index)
3. **Habana Gaudi SynapseAI Documentation**: [docs.habana.ai](https://docs.habana.ai/)

### For Shivam (Personal Master Prep):
- **YouTube**: "Accelerating LLMs with Intel OpenVINO" (Intel Software AI Academy).
- **YouTube**: "Efficient LLM Fine-Tuning with LoRA and PEFT" by Hugging Face.
- **GitHub**: `openvinotoolkit/openvino_notebooks` - Run notebook `llm-question-answering.ipynb` directly in JupyterLab!
""")

print("\n===========================================================")
print("ALL 5 DAYS HPC MASTER FILES GENERATED WITH 100% COMPLETION!")
print("===========================================================")
