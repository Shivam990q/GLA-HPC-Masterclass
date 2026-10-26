"""
build_day3_zero_to_god_tier.py
Constructs the exhaustive 00_ZERO_TO_GOD_TIER_MASTER_DOSSIER for Day 3:
Deep Learning on HPC, Slurm Cluster Workload Management & Horovod Distributed Training.
Written assuming Shivam knows ZERO, building up to an authoritative, master-level systems engineer.
"""

import os
from pathlib import Path

DAY3_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\Day-03_DeepLearning_TF_Slurm_Horovod\00_ZERO_TO_GOD_TIER_MASTER_DOSSIER")

# Subdirectories
d_concept = DAY3_DIR / "01_Concept_From_Absolute_Scratch"
d_script = DAY3_DIR / "02_Minute_By_Minute_Trainer_Script"
d_defense = DAY3_DIR / "03_Student_Cross_Questioning_Defense"
d_code = DAY3_DIR / "04_Step_By_Step_CLI_And_Code_Breakdown"
d_debug = DAY3_DIR / "05_Lab_Challenges_And_Error_Debugging"

for d in [d_concept, d_script, d_defense, d_code, d_debug]:
    d.mkdir(parents=True, exist_ok=True)

print(f"[*] Building Day 3 Zero-to-God-Tier Dossier in: {DAY3_DIR}")

# ==============================================================================
# 1. Concept from Absolute Scratch
# ==============================================================================
f3_1 = d_concept / "concept_breakdown_intuitive_analogy.md"
f3_1.write_text("""# Day 3: Deep Learning on HPC, Slurm & Horovod - Intuitive Analogies (Zero to Mastery)

## 1. Why is Deep Learning Fundamentally an HPC Problem?
Students think Deep Learning is "magic AI."
In reality, Deep Learning is **linear algebra on steroids**.

When you train a Convolutional Neural Network (CNN) or a Transformer:
1. **Forward Pass**: You multiply giant matrices of weights ($W$) by matrices of activations ($X$).
   $$Y = W \\times X + B$$
   This is General Matrix Multiply (GEMM).
2. **Backward Pass (Backpropagation)**: You compute partial derivatives (gradients) using the chain rule. This requires two more matrix multiplications:
   $$\\frac{\\partial L}{\\partial X} = W^T \\times \\frac{\\partial L}{\\partial Y}, \\quad \\frac{\\partial L}{\\partial W} = \\frac{\\partial L}{\\partial Y} \\times X^T$$
3. **Weight Update**: You adjust millions or billions of parameters:
   $$W_{\\text{new}} = W_{\\text{old}} - \\eta \\times \\nabla_W L$$

For a modest model, a single epoch requires **$10^{15}$ floating point operations (1 PetaFLOP)**.
On a normal laptop CPU, your computer will overheat and take weeks.
Deep Learning became possible *only* because HPC engineers figured out how to map GEMM operations onto massively parallel vector systolic arrays and distributed clusters.

---

## 2. What is Slurm? (The Airport Air Traffic Controller Analogy)

Imagine Indira Gandhi International Airport in New Delhi:
- You have **50 runways** (Compute Nodes).
- You have **500 airplanes** wanting to land or take off (Compute Jobs submitted by researchers).
- If there is no air traffic controller:
  - Pilots would land on whatever runway they felt like.
  - Two planes would land on Runway 1 at the same time and explode (Process collision, Out-Of-Memory kernel crash).
  - A small 2-seater Cessna would block a massive Boeing 777 carrying 400 passengers for 3 hours (Resource starvation).

**Slurm (Simple Linux Utility for Resource Management)** is the Air Traffic Controller:
- **`slurmctld` (The Control Tower)**: Tracks which compute nodes are idle, which have free GPUs, and how much RAM is available.
- **The Queue (`squeue`)**: Prioritizes jobs based on fair share, user quotas, and job priority.
- **`slurmd` (The Ground Crew on each Runway)**: Enforces physical boundaries using Linux **cgroups** so Job A cannot touch Job B's memory.

---

## 3. What is Horovod / Ring-AllReduce? (The Bucket Brigade Analogy)

Imagine a forest fire where 8 firefighters need to fill a massive water reservoir:
- **Approach A (The Central Well / Parameter Server)**:
  - All 8 firefighters run back and forth to a single water well in the center.
  - What happens? They crash into each other around the well. The well's pipe cannot pump water fast enough (Network bottleneck).
- **Approach B (The Bucket Brigade / Ring-AllReduce)**:
  - The firefighters stand in a neat circle.
  - Firefighter 1 passes a bucket to Firefighter 2; Firefighter 2 adds water and passes to Firefighter 3, and so on around the ring.
  - No one runs back and forth. No single well is overwhelmed. The water flows around the ring smoothly at constant speed regardless of whether there are 4 firefighters or 4,000!
  - That is Horovod Ring-AllReduce.
""", encoding="utf-8")

f3_2 = d_concept / "low_level_silicon_and_mathematical_foundations.md"
f3_2.write_text("""# Day 3: Low-Level Silicon & Mathematical Foundations (Deep Learning & Slurm)

## 1. General Matrix Multiply (GEMM) & Systolic Tensor Engines
The BLAS routine `SGEMM` computes:
$$C = \\alpha (A \\times B) + \\beta C$$
Where:
- $A \\in \\mathbb{R}^{M \\times K}$, $B \\in \\mathbb{R}^{K \\times N}$, $C \\in \\mathbb{R}^{M \\times N}$
- Total FLOP count: $2 M N K$ operations.

### Intel AMX (Advanced Matrix Extensions)
On 4th & 5th Gen Intel Xeon Scalable processors (Sapphire Rapids / Emerald Rapids):
- Intel introduced **AMX**: a dedicated 2D hardware matrix coprocessor built directly into each CPU core.
- **TMM Registers (Tiles)**: 8 two-dimensional registers (`TMM0` - `TMM7`), each holding up to 1 KB of matrix data (16 rows $\\times$ 64 bytes).
- **TMUL (Tile Matrix Multiply Unit)**: An execution engine that computes a $16 \\times 64$ matrix multiplied by a $64 \\times 16$ matrix in BF16 or INT8 precision.
- **Throughput**: Computes **2,048 INT8 operations or 1,024 BF16 operations per clock cycle per core**!
- Compare this with scalar execution: 2,048x higher throughput at the hardware register level!

---

## 2. Distributed Training Mathematical Formulations

### Data Parallelism
Let:
- $D$ = Total training dataset.
- $W$ = Model weight tensor.
- $P$ = Number of worker nodes.
- $B$ = Global batch size. Local batch size per worker $b = B / P$.

At each step $t$:
1. Each worker $k$ receives a distinct mini-batch $D_k$.
2. Worker $k$ computes local gradient:
   $$g_k = \\nabla_W \\mathcal{L}(W_t; D_k)$$
3. Workers synchronize gradients via **AllReduce**:
   $$\\bar{g} = \\frac{1}{P} \\sum_{k=1}^P g_k$$
4. Each worker updates local weights identically:
   $$W_{t+1} = W_t - \\eta \\bar{g}$$

### Communication Volume of Ring-AllReduce
Let $S$ be the total size of the gradient tensor in bytes.
In a logical ring of $P$ processes:
1. **Scatter-Reduce Phase**:
   - The tensor is partitioned into $P$ equal segments of size $S / P$.
   - The ring requires $P - 1$ steps.
   - At each step, each process sends and receives $S / P$ bytes.
   - Total transferred per process: $(P - 1) \\times (S / P) = \\frac{P-1}{P} S$.
2. **Allgather Phase**:
   - The reduced segments are shared around the ring in $P - 1$ steps.
   - Total transferred per process: $\\frac{P-1}{P} S$.

Total data transferred per process:
$$\\text{Total Bandwidth} = 2 \\times \\left(\\frac{P - 1}{P}\\right) \\times S$$

As $P \\to \\infty$, the total data transferred per process asymptotically approaches **$2S$**!
The communication time is **independent of cluster size $P$**, bound only by point-to-point network link bandwidth!
""", encoding="utf-8")

# ==============================================================================
# 2. Minute-by-Minute Trainer Script
# ==============================================================================
f3_3 = d_script / "morning_session_trainer_script.md"
f3_3.write_text("""# Day 3: Morning Session Trainer Script (9:00 AM - 12:30 PM)

## 09:00 AM - 09:30 AM: Opening Provocation (AI is HPC)
- **Spoken Script**:
  > *"Good morning. Today is the bridge where High Performance Computing meets Modern Artificial Intelligence.
  > 
  > A lot of people believe AI is just prompt engineering or calling an API.
  > But when you look at the engineering reality:
  > GPT-4 was trained on roughly 25,000 GPUs running continuously for 100 days.
  > Llama-3 was trained on 16,000 GPUs over 15 million GPU hours.
  > 
  > At that scale, if your gradient communication drops by 5% because of network congestion, you lose $200,000 of compute budget in a single afternoon.
  > 
  > Today, we examine how distributed AI training actually functions, how Slurm manages supercomputing clusters, and how Intel AMX accelerates neural networks on CPUs."*

## 09:30 AM - 10:30 AM: Slurm Workload Manager Architecture
- **Action**: Open terminal. Submit a sample job script using `sbatch`.
- **Spoken Script**:
  > *"Look at this Slurm submission script on the screen:
  > ```bash
  > #!/bin/bash
  > #SBATCH --job-name=hpc_dl_train
  > #SBATCH --nodes=2
  > #SBATCH --ntasks-per-node=4
  > #SBATCH --cpus-per-task=8
  > #SBATCH --mem=32G
  > #SBATCH --time=02:00:00
  > ```
  > Notice what we are declaring:
  > We are requesting 2 physical compute nodes.
  > On each node, 4 tasks (MPI/PyTorch ranks).
  > For each task, 8 CPU cores (OpenMP worker threads).
  > 32 Gigabytes of RAM.
  > 
  > When we execute `sbatch submit.sh`, Slurm's controller evaluates the cluster state. The moment resources are available, it dispatches the job via `slurmd`, creates Linux kernel cgroups to lock the process into its assigned cores, and executes."*

## 10:30 AM - 10:45 AM: Tea Break

## 10:45 AM - 12:30 PM: Distributed Training & Ring-AllReduce Deep Dive
- **Action**: Whiteboard drawing of Parameter Server vs Ring-AllReduce.
- **Spoken Script**:
  > *"Why did Horovod and NCCL replace Parameter Servers?
  > Look at the whiteboard:
  > In Parameter Server architecture, all communication converges on one central node. That creates an $O(N)$ network bottleneck.
  > In Ring-AllReduce, every worker node communicates only with its immediate neighbors in a ring.
  > 
  > Total data sent per node is strictly $2 \\times \\frac{P-1}{P} \\times S$.
  > Regardless of whether you have 4 nodes or 4,000 nodes, communication volume per link never blows up.
  > This is the algorithm that unlocked modern deep learning."*
""", encoding="utf-8")

f3_4 = d_script / "afternoon_session_trainer_script.md"
f3_4.write_text("""# Day 3: Afternoon Session Trainer Script (1:30 PM - 4:30 PM)

## 01:30 PM - 02:15 PM: Intel Extension for PyTorch (IPEX) & BF16 Mixed Precision
- **Spoken Script**:
  > *"Welcome back. In this afternoon lab, we are running PyTorch on Intel hardware with native acceleration.
  > 
  > Look at the code:
  > ```python
  > import intel_extension_for_pytorch as ipex
  > model, optimizer = ipex.optimize(model, optimizer=optimizer, dtype=torch.bfloat16)
  > ```
  > What does this single line do?
  > 1. It fuses operators: conv + relu becomes a single execution kernel.
  > 2. It casts weights to BFloat16 (Brain Floating Point).
  > 3. It routes matrix multiplications to Intel AMX systolic hardware tiles.
  > 
  > You get a **3x to 5x speedup** on CPU training without losing model accuracy."*

## 02:15 PM - 04:00 PM: Guided Hands-On Lab (Slurm Simulation + PyTorch DDP)
- **Action**: Students execute multi-process PyTorch training using `torchrun`.
- **Spoken Script**:
  > *"Run `torchrun --nproc_per_node=4 distributed_training_mnist.py`.
  > Open another terminal window and run `htop`.
  > Look at the core utilization: all 4 processes are pinned, computing forward and backward passes independently, and synchronizing gradients seamlessly via PyTorch DDP."*

## 04:00 PM - 04:30 PM: Lab Q&A & Day 4 Preview
- **Spoken Script**:
  > *"Today we scaled deep learning across processes and nodes.
  > Tomorrow, we become performance detectives: we will use Intel VTune Profiler to look directly into the CPU pipeline, detect cache misses, find NUMA bottlenecks, and read hardware performance counters.
  > See you tomorrow morning."*
""", encoding="utf-8")

f3_5 = d_script / "whiteboard_sketches_and_visual_prompts.md"
f3_5.write_text("""# Day 3: Whiteboard Sketches & Visual Architecture Prompts

## Sketch 1: Slurm Controller-Daemon Architecture
```
+-------------------------------------------------------------+
|               SLURM CONTROLLER NODE                         |
|   [slurmctld daemon]  <--- Reads slurm.conf                 |
|   [Scheduler Queue]   <--- sbatch / srun / squeue / scancel |
+-------------------------------------------------------------+
               |                               |
               | (Munge Authentication)        | (Munge Authentication)
               v                               v
+-----------------------------+ +-----------------------------+
|       COMPUTE NODE 1        | |       COMPUTE NODE 2        |
|  [slurmd daemon]            | |  [slurmd daemon]            |
|  Linux cgroups (mem, cpu)   | |  Linux cgroups (mem, cpu)   |
|  [Job Step: Task 0, Task 1] | |  [Job Step: Task 2, Task 3] |
+-----------------------------+ +-----------------------------+
```

## Sketch 2: BFloat16 vs Float32 Dynamic Range
```
FP32 (32 bits):
[ Sign: 1b ] [ Exponent: 8b ] [ Mantissa: 23b ]

FP16 (16 bits):
[ Sign: 1b ] [ Exponent: 5b ] [ Mantissa: 10b ]  <-- Small dynamic range, overflows easily!

BF16 (16 bits - Brain Float):
[ Sign: 1b ] [ Exponent: 8b ] [ Mantissa: 7b ]   <-- SAME dynamic range as FP32, zero overflow!
```
""", encoding="utf-8")

# ==============================================================================
# 3. Student Cross-Questioning Defense
# ==============================================================================
f3_6 = d_defense / "nasty_trap_questions_and_killer_answers.md"
f3_6.write_text("""# Day 3: Student Cross-Questioning Defense - Nasty Trap Questions & Killer Answers

### Trap Q1: "Why use BFloat16 instead of standard FP16 for deep learning?"
- **The Student's Angle**: Testing knowledge of floating-point representations in deep learning.
- **The Killer Response**:
  > *"Look at the bit allocation of BFloat16 versus standard IEEE FP16:
  > - Standard FP16 has an **8-bit exponent and 10-bit mantissa**? No! FP16 has a **5-bit exponent and 10-bit mantissa**. Because the exponent is only 5 bits, its maximum representable value is roughly $65,504$. In deep learning gradients, values routinely exceed this or underflow below $10^{-7}$, causing NaN crashes and underflow unless you write complex dynamic loss-scaling algorithms.
  > - **BF16 (Brain Floating Point)** has an **8-bit exponent and 7-bit mantissa** — exactly the same 8-bit exponent dynamic range as full FP32!
  > 
  > This means BF16 can represent values from $10^{-38}$ to $10^{38}$ without any loss scaling or numerical overflow, while using exactly half the memory bandwidth of FP32."*

### Trap Q2: "What is the difference between PyTorch `DataParallel` (DP) and `DistributedDataParallel` (DDP)?"
- **The Student's Angle**: A classic interview gotcha question.
- **The Killer Response**:
  > *"Never use `DataParallel` in production.
  > - `DataParallel` (DP) runs as a **single Python process** with multiple threads. Because of the Python Global Interpreter Lock (GIL), all threads fight for GIL execution. Furthermore, in DP, the primary GPU/Core gathers all outputs and calculates the loss alone on every forward pass, creating a massive single-device bottleneck.
  > - `DistributedDataParallel` (DDP) spawns **completely independent OS processes** (1 per device/socket) via `torchrun`. There is zero GIL contention. Each process computes its own loss, computes its own backward pass, and synchronizes gradients in the background using asynchronous Ring-AllReduce ring operations overlapped with backward pass computation."*
""", encoding="utf-8")

f3_7 = d_defense / "live_terminal_counter_demos.md"
f3_7.write_text("""# Day 3: Live Terminal Counter-Demos

## Demo 1: Inspecting Slurm Cluster State
```bash
# Query node partitions and status
sinfo

# Query running and queued jobs with custom format
squeue -o "%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R"
```

## Demo 2: Checking Intel AMX Silicon Support
```bash
# Check if CPU supports Intel AMX (Sapphire Rapids or newer)
grep -m1 -o -E "amx_bf16|amx_tile|amx_int8" /proc/cpuinfo
```
""", encoding="utf-8")

# ==============================================================================
# 4. Step-by-Step CLI & Code Breakdown
# ==============================================================================
f3_8 = d_code / "line_by_line_code_walkthrough.md"
f3_8.write_text("""# Day 3: Line-by-Line Code Walkthrough (PyTorch DDP)

```python
import os
import torch
import torch.nn as nn
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

def setup_distributed():
    # Line 8: Read cluster environment variables provided by torchrun / Slurm
    rank = int(os.environ["RANK"])
    world_size = int(os.environ["WORLD_SIZE"])
    
    # Line 12: Initialize process group using Gloo (CPU) or NCCL/oneCCL (GPU/Intel)
    dist.init_process_group(backend="gloo", rank=rank, world_size=world_size)
    return rank, world_size

def train():
    rank, world_size = setup_distributed()
    
    # Line 19: Build standard PyTorch model
    model = nn.Sequential(nn.Linear(20, 64), nn.ReLU(), nn.Linear(64, 2))
    
    # Line 22: Wrap model in DDP for automated gradient synchronization
    ddp_model = DDP(model)
    
    optimizer = torch.optim.Adam(ddp_model.parameters(), lr=0.01)
    
    # Line 27: Synthetic batch computation
    inputs = torch.randn(32, 20)
    targets = torch.randint(0, 2, (32,))
    
    optimizer.zero_grad()
    outputs = ddp_model(inputs)
    loss = nn.CrossEntropyLoss()(outputs, targets)
    
    # Line 35: Backward pass automatically triggers Ring-AllReduce under the hood
    loss.backward()
    optimizer.step()
    
    if rank == 0:
        print(f"[Rank 0] Training step complete. Loss: {loss.item():.4f}")
        
    dist.destroy_process_group()

if __name__ == "__main__":
    train()
```
""", encoding="utf-8")

f3_9 = d_code / "compilation_and_execution_pipeline.md"
f3_9.write_text("""# Day 3: Compilation & Execution Pipeline

## Launching Distributed Training with `torchrun`
```bash
# Launch across 4 local CPU ranks
torchrun --standalone --nproc_per_node=4 distributed_training.py
```

## Submitting via Slurm Batch Script (`submit_dl.sh`)
```bash
#!/bin/bash
#SBATCH --job-name=ipex_train
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --cpus-per-task=4
#SBATCH --time=01:00:00

srun python3 distributed_training.py
```
Submit with:
```bash
sbatch submit_dl.sh
```
""", encoding="utf-8")

# ==============================================================================
# 5. Lab Challenges & Error Debugging
# ==============================================================================
f3_10 = d_debug / "student_lab_challenges_with_solutions.md"
f3_10.write_text("""# Day 3: Student Lab Challenges with Step-by-Step Solutions

## Challenge 1: Custom Slurm Batch Script with Resource Constraints
- **Goal**: Write a Slurm script that requests 2 nodes, 8 cores per node, 16 GB RAM, and prints hostnames of assigned nodes.
- **Solution**:
```bash
#!/bin/bash
#SBATCH --nodes=2
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --output=slurm_%j.log

srun hostname
```

## Challenge 2: Implement Distributed Gradient AllReduce Manually
- **Goal**: Use `dist.all_reduce(tensor, op=dist.ReduceOp.SUM)` to synchronize a local loss value across all ranks and print the mean loss on Rank 0.
""", encoding="utf-8")

f3_11 = d_debug / "common_student_syntax_errors_and_5_sec_fixes.md"
f3_11.write_text("""# Day 3: Common Student Errors & 5-Second Instant Fixes

### Error 1: `RuntimeError: Default process group has not been initialized`
- **Cause**: Student called `DDP(model)` or `dist.all_reduce()` before invoking `dist.init_process_group()`.
- **5-Second Fix**: Call `dist.init_process_group(...)` first!

### Error 2: `Slurm: sbatch: error: Batch job submission failed: Invalid account or partition`
- **Cause**: Student specified a partition name that doesn't exist on the cluster.
- **5-Second Fix**: Run `sinfo` to view active partition names, then update `#SBATCH -p <valid_partition>`.

### Error 3: PyTorch training hangs indefinitely at `loss.backward()`
- **Cause**: One rank encountered an exception or exited early, leaving remaining ranks blocked forever waiting for the AllReduce handshake.
- **5-Second Fix**: Wrap rank code in `try...finally` with `dist.destroy_process_group()` or set `os.environ["TORCH_DISTRIBUTED_DEBUG"] = "DETAIL"`.
""", encoding="utf-8")

print("[SUCCESS] Day 3: Zero-to-God-Tier Master Dossier Built Completely!")
