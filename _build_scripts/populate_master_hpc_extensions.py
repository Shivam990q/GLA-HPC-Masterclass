# populate_master_hpc_extensions.py
import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# MASTER README & INSTRUCTOR PLAYBOOK
# ==============================================================================
write_f("README.md", """
# High Performance Computing: A Practical Approach (Intel & NEC Edition)
### Official Master Training Repository @ GLA University
**Partner Organizations**: Edulateral Foundation & Intel & NEC Corporation  
**Audience**: 7th Semester B.Tech Computer Science & Engineering  
**Lead Trainer**: Shivam Gupta | **Co-Trainer**: Mr. Nikhil / Mr. Kumaraguru  

---

## 🏛️ Executive Curriculum Architecture

This repository contains the complete, production-grade 5-day syllabus for High Performance Computing (HPC), AI acceleration, and distributed deep learning, aligned directly with the curriculum guidelines of **Intel oneAPI** and **NEC SX-Aurora TSUBASA** supercomputing architectures.

```mermaid
graph TD
    subgraph Day1["Day 1: Foundations & Silicon"]
        D1A["HPC Architecture & Limits of Moore's Law"]
        D1B["Intel Xeon + NEC Vector Host (VH)"]
        D1C["Linux Performance CLI & Passwordless SSH"]
        D1D["Intel oneAPI Base & HPC Toolkit Setup"]
    end

    subgraph Day2["Day 2: Parallelism & oneDAL"]
        D2A["Shared Memory OpenMP Multi-threading"]
        D2B["Distributed Memory MPI Message Passing"]
        D2C["Intel oneDAL & scikit-learn-intelex (30x Speedup)"]
    end

    subgraph Day3["Day 3: Deep Learning on Clusters"]
        D3A["oneDNN Layer Fusion & AVX-512/AMX Math"]
        D3B["Slurm Workload Manager (#SBATCH Queues)"]
        D3C["Horovod Ring-AllReduce Distributed Training"]
    end

    subgraph Day4["Day 4: Performance Engineering"]
        D4A["Multi-Node Scaling Efficiency Verification"]
        D4B["Intel VTune Hardware PMU Counter Profiling"]
        D4C["Top-Down Microarchitecture Analysis (TMAM)"]
    end

    subgraph Day5["Day 5: Generative AI & LLMs"]
        D5A["LLM Inference Bottlenecks (Prefill vs Decode)"]
        D5B["Intel Xeon AMX & Habana Gaudi 2/3 Accelerators"]
        D5C["OpenVINO INT4 Weight-Only Quantization (WOQ)"]
        D5D["Local REST API Deployment for Capstones"]
    end

    Day1 --> Day2 --> Day3 --> Day4 --> Day5
```

---

## 💻 Hardware Ecosystem (Intel & NEC Synergy)

In modern enterprise supercomputing, **NEC and Intel** work in tight architectural tandem:
1. **Vector Host (VH)**: **Intel Xeon Scalable Processors** serve as the primary host nodes, managing Linux OS functions, distributed file system I/O (Lustre), cluster scheduling (Slurm), and multi-core execution.
2. **Vector Engine (VE) / Accelerators**: **NEC SX-Aurora TSUBASA** PCIe vector cards, **Intel Data Center GPU Max (Ponte Vecchio)**, and **Habana Gaudi** handle massive memory-bandwidth vector operations and deep learning tensor contractions.
3. **Unified Programming**: **Intel oneAPI** and standard **OpenMP/MPI** ensure code written once compiles and dispatches efficiently across CPUs, vector engines, and discrete GPUs.

---

## 📂 Daily Repository Navigation

* **[Day 1: HPC, Linux, Shell & oneAPI](./Day-01_HPC_Linux_Shell_oneAPI/)**: Core hardware inspection, Linux performance tuning, passwordless SSH, and oneAPI setup.
* **[Day 2: Parallel Computing, OpenMP, MPI & oneDAL](./Day-02_Parallel_OpenMP_MPI_oneDAL/)**: Shared vs distributed memory, C++ OpenMP pragmas, Python MPI collectives, and Intel Scikit-Learn acceleration.
* **[Day 3: Deep Learning, Slurm & Horovod](./Day-03_DeepLearning_TF_Slurm_Horovod/)**: Intel-optimized TensorFlow, oneDNN operator fusion, Slurm job submission, and Ring-AllReduce scaling.
* **[Day 4: Distributed Training & Intel VTune](./Day-04_Distributed_Slurm_VTune_Profiling/)**: Scaling efficiency measurement, PMU hardware counters, and Top-Down memory bottleneck profiling.
* **[Day 5: Generative AI, LLMs & OpenVINO](./Day-05_GenAI_LLMs_Gaudi_OpenVINO/)**: Local LLM quantization (INT4), KV-cache optimization, Habana Gaudi architecture, and FastAPI microservice deployment.
""")

write_f("INSTRUCTOR_PLAYBOOK.md", """
# 🎙️ Shivam Gupta's Master Instructor Playbook
### The Definitive Guide to Captivating 7th Semester B.Tech Students

---

## 🧠 Part 1: Classroom Psychology & Setting the Tone

### 1. The 7th-Semester Student Mindset:
* 7th-semester students consider themselves senior engineers. They are skeptical of generic PPT presentations.
* They are actively worried about:
  1. **Upcoming Placement Drives** (Technical interview rounds at top tech companies).
  2. **Final Year Capstone Projects** (Major projects that determine their degree).
  3. **Industry Relevance** (Is this syllabus used in real companies or just college theory?).

### 2. The Golden Rule of Credibility:
> **"Never read a slide. Draw the architecture on the whiteboard, open the Linux terminal, and let the code fail and succeed live in front of their eyes."**

---

## ⚡ Part 2: Minute-by-Minute Room Management Rules

1. **The 20-Minute Theory Cap**:
   * Never speak theoretical concepts for more than 20 continuous minutes.
   * Every 20 minutes MUST be followed by a terminal command, an interactive question, or a live benchmark showdown.
2. **The "Before vs After" Shock Value**:
   * Always show the unoptimized, slow way first (e.g. single-threaded loop taking 4 seconds).
   * Then apply the HPC / oneAPI optimization and show the result (0.05 seconds).
   * Point directly at the terminal execution time and say: *"This is the difference between a junior developer and a High-Performance Systems Engineer."*
3. **Handling the "Oversmart" Student**:
   * If a student asks: *"Sir, isn't CUDA better than oneAPI?"* or *"Why not just buy Nvidia H100s?"*
   * **Do NOT dismiss them.** Validate them: *"Brilliant question! You are thinking like a systems architect."*
   * Then give the killer enterprise answer: *"CUDA is proprietary vendor lock-in. If your company spends $10M on Nvidia hardware, you are trapped. Intel oneAPI is based on open standard SYCL—it compiles across Intel CPUs, GPUs, AMD chips, and FPGAs. Plus, 70% of enterprise servers already have Intel Xeon CPUs. Repurposing existing hardware saves companies millions."*
4. **Co-Trainer Synergy (Shivam + Nikhil)**:
   * **Lead Trainer (Shivam)**: Drives the projector, whiteboard diagrams, conceptual hooks, and live coding terminal.
   * **Floor Support (Nikhil)**: Roams the lab aisles, fixing syntax errors, Python environment PATH issues, and SSH connection drops within 30 seconds so the lead trainer never has to pause the class lecture.

---

## 🛠️ Part 3: Live Coding Emergency Fail-Safes

* **If internet drops**: Have local offline Python virtual environments and pre-downloaded wheels ready on a USB drive.
* **If a student's code won't compile**: Direct them to the `solutions_and_code/` directory in that day's folder.
* **If lab PC has restricted permissions**: Use Docker (`docker run -it intel/oneapi-hpckit:latest`) or browser-based Intel Developer Cloud JupyterLab.
""")

# ==============================================================================
# DAY 1 EXTENSIONS
# ==============================================================================
write_f("Day-01_HPC_Linux_Shell_oneAPI/theory_notes/intel_nec_architecture_spec.md", """
# Intel & NEC HPC Synergy: Vector Host & Vector Engine Architecture

## 1. The Hybrid Supercomputing Model
In traditional computing, processors are designed as either general-purpose scalar engines (CPUs) or massively parallel graphics engines (GPUs).
**NEC and Intel** pioneered the **VH + VE (Vector Host + Vector Engine)** architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                    NEC SX-Aurora TSUBASA                    │
├──────────────────────────────┬──────────────────────────────┤
│      VECTOR HOST (VH)        │     VECTOR ENGINE (VE)       │
│  [ Intel Xeon Scalable CPU ] │   [ NEC Vector Processor ]   │
├──────────────────────────────┼──────────────────────────────┤
│ • Runs standard Linux OS     │ • Dedicated PCIe card        │
│ • Handles file I/O & Lustre  │ • Ultra-wide vector pipeline │
│ • Manages Slurm scheduler    │ • High-Bandwidth Memory HBM2 │
│ • Compiles code via oneAPI   │ • Massive memory throughput  │
└──────────────────────────────┴──────────────────────────────┘
```

## 2. Architectural Role Division
* **Intel Xeon (Vector Host)**:
  - Executes operating system daemons, network communication (InfiniBand/Ethernet drivers), database management, and scalar execution branches.
  - Features **AVX-512** (16 single-precision floats/cycle) and **AMX** (Advanced Matrix Extensions) for hardware matrix math.
* **NEC Vector Engine (Accelerator)**:
  - Contains up to 10 vector cores, each with 32 vector registers of 256 elements (16,384 bits wide per core!).
  - Features memory bandwidth up to **1.53 Terabytes/second** using High-Bandwidth Memory (HBM2).
* **Programming Synergy**:
  - Code compiled on the Intel Xeon host can automatically offload vectorized loops to the NEC engine or Intel GPUs using **OpenMP pragmas** (`#pragma omp target`) and **Intel oneAPI SYCL/DPC++**.
""")

write_f("Day-01_HPC_Linux_Shell_oneAPI/student_cheatsheets/quick_reference_card.md", """
# Day 1 Quick Reference Card: HPC & Linux Diagnostics

### 1. Silicon & Hardware Inspection
```bash
lscpu                           # Complete CPU architecture overview
lscpu -C                        # Display L1d, L1i, L2, L3 cache hierarchy
lscpu | grep -i -E "avx|amx"    # Check for hardware vector and matrix engines
numactl --hardware              # View NUMA node memory locality and distances
```

### 2. Linux Performance & Memory Commands
```bash
free -h                         # Real-time memory and swap allocation
top -b -n 1 | head -n 25        # High-precision process snapshot
df -hT                          # View filesystems and mounted parallel storage
ulimit -a                       # Check open file descriptor and process limits
ulimit -n 65536                 # Expand file limits for massive distributed jobs
```

### 3. SSH Configuration & Multiplexing
```bash
# Generate modern Elliptic Curve key
ssh-keygen -t ed25519 -N "" -f ~/.ssh/id_ed25519

# Configure persistent multiplexed connection in ~/.ssh/config:
Host hpc-cluster
    HostName headnode.glau.ac.in
    User student
    IdentityFile ~/.ssh/id_ed25519
    ServerAliveInterval 60
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h-%p
    ControlPersist 4h
```

### 4. Intel oneAPI Environment Setup
```bash
source /opt/intel/oneapi/setvars.sh   # Load oneAPI environment variables
icx --version                         # Verify Intel oneAPI C/C++ compiler
mpiicx --version                      # Verify Intel MPI wrapper
```
""")

write_f("Day-01_HPC_Linux_Shell_oneAPI/presentation_scripts/trainer_speaking_script.md", """
# Day 1 Trainer Script: Shivam Gupta's Live Classroom Guide

### ⏰ 09:00 AM - 09:15 AM: The Hook & Opening
* **Action**: Stand in front of the board. Write in large bold letters: `120 YEARS`.
* **Say**:
  > *"Good morning, everyone! Look at this number on the board: 120 Years. If you take the latest LLaMA-3 70-Billion parameter AI model and try to train it on your high-end gaming laptop or Core i7 PC, it will take exactly 120 years to finish.*
  > 
  > *Around 2005, something fundamental broke in computer science. It was called the Death of Dennard Scaling. For decades, chipmakers doubled clock speeds every two years. But at 4 to 5 GHz, silicon began melting from thermal dissipation and quantum leakage.*
  > 
  > *Single computers hit the physics wall. The only way humanity could build ChatGPT, simulate climate change, and discover life-saving drugs was through High Performance Computing (HPC)—connecting hundreds of multi-core servers over sub-microsecond InfiniBand fabric to act as a single giant supercomputer.*
  > 
  > *Over the next 5 days, we are going to look under the hood of supercomputers. By 5 PM today, you will know how to inspect CPU silicon registers, automate cluster workloads, and set up the Intel oneAPI toolchain."*

### ⏰ 09:45 AM - 10:15 AM: Live Silicon Audit
* **Action**: Open your terminal on the projector.
* **Say**:
  > *"Open your terminals right now. Type `lscpu`. Don't just look at the core count. Look at the line that says 'Flags'. Type `lscpu | grep -i avx`. If you see 'avx512', your CPU has 512-bit vector registers. That means while a standard program calculates 1 number at a time, your silicon can calculate 16 floating-point numbers in a single clock cycle! Let me prove it to you live."*
* **Action**: Execute `orchestrator.sh` and show the 80x speedup.
""")

write_f("Day-01_HPC_Linux_Shell_oneAPI/student_lab_practice/solutions_and_code/solution_challenge1.sh", """
#!/usr/bin/env bash
# Solution for Challenge 1: Silicon & Cache Inspection
set -eo pipefail

echo "=========================================================="
echo "                 SILICON HARDWARE AUDIT                   "
echo "=========================================================="
SOCKETS=$(lscpu | awk -F: '/Socket\(s\):/ {print $2}' | xargs)
CORES_PER_SOCKET=$(lscpu | awk -F: '/Core\(s\) per socket:/ {print $2}' | xargs)
THREADS_PER_CORE=$(lscpu | awk -F: '/Thread\(s\) per core:/ {print $2}' | xargs)
NUMA_NODES=$(lscpu | awk -F: '/NUMA node\(s\):/ {print $2}' | xargs)

echo "Physical Sockets     : $SOCKETS"
echo "Cores per Socket     : $CORES_PER_SOCKET"
echo "Threads per Core     : $THREADS_PER_CORE"
echo "NUMA Nodes           : $NUMA_NODES"
echo "----------------------------------------------------------"
echo "Cache Hierarchy Breakdown:"
lscpu -C
echo "=========================================================="
""")

# ==============================================================================
# DAY 2 EXTENSIONS
# ==============================================================================
write_f("Day-02_Parallel_OpenMP_MPI_oneDAL/student_cheatsheets/quick_reference_card.md", """
# Day 2 Quick Reference Card: OpenMP, MPI & Intel oneDAL

### 1. OpenMP Compiler Directives (C/C++)
```c
#pragma omp parallel               // Fork worker threads
#pragma omp parallel for           // Parallelize loop iterations
#pragma omp parallel for reduction(+:sum) // Thread-safe accumulation
#pragma omp critical               // Mutex block (only 1 thread at a time)
#pragma omp barrier                // Explicit synchronization barrier
#pragma omp single                 // Executed by only 1 thread
```

### 2. OpenMP Environment Tuning
```bash
export OMP_NUM_THREADS=16          // Set worker thread count
export OMP_SCHEDULE="dynamic,64"   // Dynamic load balancing chunks
export KMP_AFFINITY=compact        // Bind threads close for cache reuse
```

### 3. MPI Python Commands (`mpi4py`)
```python
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()             # Process ID (0 to N-1)
size = comm.Get_size()             # Total process count

# Collective operations
comm.bcast(data, root=0)           # Broadcast from Rank 0
comm.Scatter(sendbuf, recvbuf, root=0) # Scatter chunks
comm.Gather(sendbuf, recvbuf, root=0)  # Gather chunks
comm.reduce(local_val, op=MPI.SUM, root=0) # Reduce to root
comm.Allreduce(sendbuf, recvbuf, op=MPI.SUM) # Reduce to all
```

### 4. Intel oneDAL Python Patch (Scikit-Learn)
```python
from sklearnex import patch_sklearn
patch_sklearn()                    # Automatically accelerates KMeans, SVM, PCA, RF
```
""")

write_f("Day-02_Parallel_OpenMP_MPI_oneDAL/presentation_scripts/trainer_speaking_script.md", """
# Day 2 Trainer Script: Parallel Computing & Intel oneDAL

### ⏰ 09:00 AM - 09:20 AM: The Opening Hook
* **Action**: Draw two big boxes on the whiteboard: Box 1 = "One Giant Room (Shared Memory)", Box 2 = "Different Buildings (Distributed Memory)".
* **Say**:
  > *"Imagine you have to count 1,000,000 votes. Option A: You put 16 people in one room with a single giant whiteboard. Everyone writes on the whiteboard. That is OpenMP (Shared Memory). It's fast, but if two people write on the same box at the same time, you get a race condition!*
  > 
  > *Option B: You put 16 people in 16 different buildings. Each person counts their own stack and sends WhatsApp messages to the manager. That is MPI (Message Passing Interface). There is zero memory corruption, but network communication takes time.*
  > 
  > *Today, we will master both: OpenMP for multi-core CPUs and MPI for supercomputing clusters!"*
""")

# ==============================================================================
# DAY 3 EXTENSIONS
# ==============================================================================
write_f("Day-03_DeepLearning_TF_Slurm_Horovod/student_cheatsheets/quick_reference_card.md", """
# Day 3 Quick Reference Card: Slurm & Horovod Distributed DL

### 1. Essential Slurm Commands
```bash
sinfo                              # Cluster partition & node states
squeue                             # View active & pending jobs
squeue -u $USER                    # View your own queued jobs
sbatch my_job.slurm                # Submit batch job script
srun -n 4 -p gpu --pty bash        # Interactive allocation
scancel <job_id>                   # Terminate job
scontrol show job <job_id>         # Deep job diagnosis & allocated nodes
```

### 2. Slurm Batch Header Directives (`#SBATCH`)
```bash
#SBATCH --job-name=dl_train        # Job identifier
#SBATCH --output=logs/%j.out       # Standard output log (%j = Job ID)
#SBATCH --error=logs/%j.err        # Standard error log
#SBATCH --nodes=2                  # Physical node count
#SBATCH --ntasks-per-node=4        # MPI tasks per node
#SBATCH --cpus-per-task=8          # CPU cores allocated per task
#SBATCH --time=02:00:00            # Maximum wall-clock time limit
#SBATCH --partition=compute        # Target hardware partition
```

### 3. Horovod Ring-AllReduce Python Pattern
```python
import horovod.tensorflow as hvd
hvd.init()

# Scale learning rate by cluster size
opt = tf.keras.optimizers.Adam(0.001 * hvd.size())

# Wrap optimizer for Ring-AllReduce
opt = hvd.DistributedOptimizer(opt)

# Synchronize starting weights
callbacks = [hvd.callbacks.BroadcastGlobalVariablesCallback(0)]
```
""")

write_f("Day-03_DeepLearning_TF_Slurm_Horovod/presentation_scripts/trainer_speaking_script.md", """
# Day 3 Trainer Script: Slurm & Distributed Deep Learning

### ⏰ 09:00 AM - 09:20 AM: The Slurm & Horovod Hook
* **Say**:
  > *"When you train a deep neural network on a supercomputer, you don't double-click a Python icon. If 50 students run heavy models on the head node at the same time, the server crashes. That's why every supercomputer in the world uses Slurm—the traffic controller of cluster computing.*
  > 
  > *And when your model is too large for one machine, how do you train it across 4 nodes? Traditional parameter servers choke on network traffic. Today, we will study Horovod's Ring-AllReduce—the mathematical breakthrough that allowed Uber and Baidu to scale deep learning linearly across hundreds of GPUs!"*
""")

# ==============================================================================
# DAY 4 EXTENSIONS
# ==============================================================================
write_f("Day-04_Distributed_Slurm_VTune_Profiling/student_cheatsheets/quick_reference_card.md", """
# Day 4 Quick Reference Card: Intel VTune Profiler & TMAM

### 1. Intel VTune CLI Commands
```bash
# Collect Hotspots (CPU time per function/line)
vtune -collect hotspots -result-dir ./vtune_hotspots -- ./my_program

# Collect Memory Access (Cache misses, bandwidth, NUMA)
vtune -collect memory-access -result-dir ./vtune_mem -- ./my_program

# Collect Microarchitecture Exploration (Top-Down TMAM)
vtune -collect uarch-exploration -result-dir ./vtune_uarch -- ./my_program

# Generate summary text report
vtune -report summary -result-dir ./vtune_hotspots

# Launch GUI Viewer
vtune-gui ./vtune_hotspots &
```

### 2. Top-Down TMAM Metrics Interpretation
* **Retiring (>50%)**: Healthy execution. The CPU is retiring real instructions.
* **Frontend Bound (>15%)**: Instruction cache misses or branch target stalls. Remedy: Inline functions, optimize code layout.
* **Bad Speculation (>10%)**: Branch mispredictions. Remedy: Remove unpredictable branching in inner loops, use compiler branch hints.
* **Backend Bound - Memory (>20%)**: Waiting for L3 cache or DRAM. Remedy: Contiguous memory layouts, blocked matrix multiplication, prefetching.
* **Backend Bound - Core (>20%)**: Long latency math (division, square roots). Remedy: Vectorize with AVX-512, reciprocal approximations.
""")

write_f("Day-04_Distributed_Slurm_VTune_Profiling/presentation_scripts/trainer_speaking_script.md", """
# Day 4 Trainer Script: Systems Performance Engineering & VTune

### ⏰ 09:00 AM - 09:20 AM: The Hardware PMU Hook
* **Say**:
  > *"Junior programmers measure speed with print(time.time()). Senior systems engineers look at silicon hardware performance monitoring counters (PMUs).*
  > 
  > *Today, you will learn to read the CPU's internal diary using Intel VTune Profiler. We will discover exactly how many clock cycles were wasted because of an L1 cache miss, and why jumping through memory arrays costs you 10x in performance compared to contiguous access!"*
""")

# ==============================================================================
# DAY 5 EXTENSIONS
# ==============================================================================
write_f("Day-05_GenAI_LLMs_Gaudi_OpenVINO/student_cheatsheets/quick_reference_card.md", """
# Day 5 Quick Reference Card: LLM Inference, OpenVINO & LoRA

### 1. LLM Parameter Memory Formulas
$$\\text{Weight Memory (GB)} = \\text{Parameters} \\times \\text{Bytes per Param}$$
* **FP16 / BF16**: 2 Bytes/param (8B model = 16 GB).
* **INT8**: 1 Byte/param (8B model = 8 GB).
* **INT4**: 0.5 Bytes/param (8B model = 4 GB).
* **Mixed Precision Training**: 16 Bytes/param (Weights + Gradients + Adam states).

### 2. Intel OpenVINO LLM Quantization & Inference
```python
from optimum.intel.openvino import OVModelForCausalLM
from transformers import AutoTokenizer

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Convert, optimize and compile to OpenVINO IR (.xml + .bin)
model = OVModelForCausalLM.from_pretrained(
    model_id,
    export=True,
    compile=True,
    device="CPU"
)
tokenizer = AutoTokenizer.from_pretrained(model_id)

inputs = tokenizer("Explain HPC:", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=60)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### 3. PEFT / LoRA Low-Rank Adaptation
```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=16,                           # Low rank dimension
    lora_alpha=32,                  # Scaling factor
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)
model = get_peft_model(base_model, lora_config)
model.print_trainable_parameters()  # Demonstrates 99.8% parameter reduction!
```
""")

write_f("Day-05_GenAI_LLMs_Gaudi_OpenVINO/presentation_scripts/trainer_speaking_script.md", """
# Day 5 Trainer Script: Generative AI, Habana Gaudi & OpenVINO

### ⏰ 09:00 AM - 09:20 AM: The Capstone AI Hook
* **Say**:
  > *"Welcome to the final day of HPC Master Training! Today is where everything connects. We will take everything we learned about hardware, memory bandwidth, and compilation, and apply it to Generative AI.*
  > 
  > *You will learn why token generation is a memory bandwidth problem, how Intel AMX and Habana Gaudi accelerate matrix multiplication, and how to use Intel OpenVINO to run high-speed quantized LLMs locally on your laptop CPU—complete with a local REST API that you can plug into your Final Year B.Tech project today!"*
""")

print("\n===========================================================")
print("ALL EXTENDED HPC MASTER CURRICULUM ASSETS GENERATED!")
print("===========================================================")
