"""
build_day4_zero_to_god_tier.py
Constructs the exhaustive 00_ZERO_TO_GOD_TIER_MASTER_DOSSIER for Day 4:
Distributed Cluster Architecture, Advanced Slurm & Intel VTune Performance Profiling.
Written assuming Shivam knows ZERO, building up to an authoritative, master-level systems engineer.
"""

import os
from pathlib import Path

DAY4_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\Day-04_Distributed_Slurm_VTune_Profiling\00_ZERO_TO_GOD_TIER_MASTER_DOSSIER")

# Subdirectories
d_concept = DAY4_DIR / "01_Concept_From_Absolute_Scratch"
d_script = DAY4_DIR / "02_Minute_By_Minute_Trainer_Script"
d_defense = DAY4_DIR / "03_Student_Cross_Questioning_Defense"
d_code = DAY4_DIR / "04_Step_By_Step_CLI_And_Code_Breakdown"
d_debug = DAY4_DIR / "05_Lab_Challenges_And_Error_Debugging"

for d in [d_concept, d_script, d_defense, d_code, d_debug]:
    d.mkdir(parents=True, exist_ok=True)

print(f"[*] Building Day 4 Zero-to-God-Tier Dossier in: {DAY4_DIR}")

# ==============================================================================
# 1. Concept from Absolute Scratch
# ==============================================================================
f4_1 = d_concept / "concept_breakdown_intuitive_analogy.md"
f4_1.write_text("""# Day 4: Distributed Computing, Advanced Slurm & Intel VTune - Intuitive Analogies (Zero to Mastery)

## 1. What is Performance Profiling? (The Formula 1 Telemetry Analogy)

Imagine you are managing a Formula 1 racing car:
- The driver finishes a lap and says: *"The car feels slow."*
- What does the race engineer do?
  - Do they guess? *"Maybe the tires are bad? Maybe the engine is cold? Maybe the driver should press the gas harder?"*
  - No! If you guess, you lose the championship.
  - The team pulls the **Telemetry Data**:
    - Fuel pressure: 300 bar.
    - Tire temperature: 105 degrees Celsius.
    - Aero downforce: 1,200 kg.
    - Telemetry reveals: In Turn 4, the gearbox shifted down 0.2 seconds too late, losing 40 km/h of corner exit speed.

In software engineering, when a developer says *"My code is slow"*, they usually guess: *"Let me rewrite it in another language"* or *"Let me throw more threads at it"*.
**Intel VTune Profiler** is the Formula 1 Telemetry System for silicon:
- It connects to the CPU's on-die sensors (Performance Monitoring Units).
- It measures exactly how many nanoseconds the CPU spent:
  - Waiting for DDR5 RAM (Memory-Bound).
  - Stalled on a branch prediction error (Bad Speculation).
  - Actively retiring useful vector instructions (Retiring).
- It shows you the exact line of C++ or Python code that is causing the bottleneck.

---

## 2. What is NUMA (Non-Uniform Memory Access)? (The Desks Across the Hallway Analogy)

Imagine a large research laboratory with two giant desks:
- **Desk 0 (Socket 0)**: 32 researchers sit here. Right next to Desk 0 is **Cabinet 0 (DRAM Node 0)**.
  - If Researcher on Desk 0 reaches into Cabinet 0, it takes **1 second** (Local Memory Access, ~70 ns).
- **Desk 1 (Socket 1)**: 32 researchers sit here. Right next to Desk 1 is **Cabinet 1 (DRAM Node 1)**.
- **The NUMA Problem**:
  - What happens if Researcher on Desk 0 needs a folder from Cabinet 1 across the hallway?
  - They have to stand up, walk through the crowded door, navigate the hallway (Intel Ultra Path Interconnect - UPI bus), and walk back.
  - That trip takes **2.5 seconds** (Remote Memory Access, ~140 ns).
  - If all 32 researchers on Desk 0 keep walking across the hallway to Cabinet 1, the hallway gets jammed, everyone bumps into each other, and the entire lab stops working!
- **HPC Solution**:
  - We use **`numactl`** to lock threads to Desk 0 and keep their data strictly inside Cabinet 0.
""", encoding="utf-8")

f4_2 = d_concept / "low_level_silicon_and_mathematical_foundations.md"
f4_2.write_text("""# Day 4: Low-Level Silicon & Mathematical Foundations (VTune & Roofline Analysis)

## 1. Top-Down Microarchitecture Analysis (TMA) Methodology
Developed by Ahmad Yasin (Intel Corporation), TMA breaks down 100% of the CPU core pipeline slots into four mutually exclusive categories:

$$\\text{Pipeline Slots} = \\text{Retiring} + \\text{Bad Speculation} + \\text{Frontend Bound} + \\text{Backend Bound}$$

```
                           [ Pipeline Slots ]
                                   |
         +-------------------------+-------------------------+
         |                                                   |
   [ Issued uOps ]                                     [ Unissued uOps ]
         |                                                   |
   +-----+-----+                                       +-----+-----+
   |           |                                       |           |
[Retiring] [Bad Speculation]                    [Frontend Bound] [Backend Bound]
                                                                   |
                                                             +-----+-----+
                                                             |           |
                                                      [Memory Bound] [Core Bound]
```

### Metrics Definitions:
1. **Retiring**: uOps (micro-operations) that successfully execute and commit their results to architectural registers. Ideal target: > 70%.
2. **Bad Speculation**: uOps allocated because the Branch Target Buffer (BTB) or Direction Predictor mispredicted a branch. The CPU fetched and executed speculative instructions that had to be canceled.
3. **Frontend Bound**: The CPU execution units were ready, but the Instruction Fetch / Decode units failed to deliver uOps (e.g., L1 Instruction Cache misses or iTLB misses).
4. **Backend Bound**:
   - **Memory Bound**: Pipeline stalled waiting for data loads/stores from L1D, L2, L3, or DRAM.
   - **Core Bound**: Pipeline stalled because of port saturation or execution dependency chains inside the ALU.

---

## 2. The Cache-Aware Roofline Model
The Roofline Model visualizes an application's performance relative to the theoretical hardware limits of the target system.

### Mathematical Parameters:
- $P_{\\text{peak}}$ = Theoretical Peak Floating-Point Performance of the CPU (in GFLOPS/sec).
- $B_{\\text{peak}}$ = Theoretical Peak Memory Bandwidth (in GB/sec).
- $I$ = Operational Intensity of the algorithm (in FLOPs / Byte).

The attainable performance $P_{\\text{attainable}}$ is bounded by:
$$P_{\\text{attainable}} = \\min(P_{\\text{peak}}, \\; I \\times B_{\\text{peak}})$$

### The Inflection Point ($I^*$)
The boundary between being **Memory-Bound** and **Compute-Bound** is the inflection point:
$$I^* = \\frac{P_{\\text{peak}}}{B_{\\text{peak}}}$$

- On a modern Intel Xeon Scalable processor:
  - $P_{\\text{peak}} \\approx 3,000$ GFLOPS (3 TFLOPS)
  - $B_{\\text{peak}} \\approx 250$ GB/sec (8-channel DDR5)
  - Inflection point: $I^* = \\frac{3000}{250} = 12$ FLOPs/Byte.
- **Rule of Thumb**:
  - If your algorithm performs fewer than 12 FLOPs per byte transferred from DRAM, **you are strictly Memory-Bound**.
  - Adding more cores or higher GHz will NOT make your program faster! You must increase cache reuse via loop blocking and tiling!
""", encoding="utf-8")

# ==============================================================================
# 2. Minute-by-Minute Trainer Script
# ==============================================================================
f4_3 = d_script / "morning_session_trainer_script.md"
f4_3.write_text("""# Day 4: Morning Session Trainer Script (9:00 AM - 12:30 PM)

## 09:00 AM - 09:30 AM: Opening Provocation (Guessing vs Measuring)
- **Spoken Script**:
  > *"Good morning. Today is the day we separate amateur programmers from professional systems performance engineers.
  > 
  > In amateur programming, when a system is slow, people guess. They add a cache here, they multithread there, they blame the operating system.
  > 
  > In High Performance Computing, guessing is forbidden.
  > We measure.
  > 
  > Modern processors contain hundreds of hardware performance registers inside the silicon. Every cache miss, every branch misprediction, every clock cycle where an ALU sits starving for data is recorded down to the exact machine instruction.
  > 
  > Today, we learn Intel VTune Profiler and the Roofline Model."*

## 09:30 AM - 10:30 AM: Top-Down Microarchitecture Analysis (TMA)
- **Action**: Draw the 4 TMA quadrants on the whiteboard: Retiring, Bad Speculation, Frontend Bound, Backend Bound.
- **Spoken Script**:
  > *"Look at this board. When an instruction enters an Intel core, it enters the pipeline.
  > At the end of every clock cycle, that pipeline slot has four possible fates:
  > 
  > 1. Did it do useful work? That is **Retiring**.
  > 2. Did the CPU guess wrong on an `if` condition and throw the work in the trash? That is **Bad Speculation**.
  > 3. Did the instruction decoder fail to feed instructions? That is **Frontend Bound**.
  > 4. Was the ALU frozen waiting for DDR5 RAM to deliver data? That is **Memory Bound**.
  > 
  > When we launch VTune, it doesn't give us opinions; it gives us percentages."*

## 10:30 AM - 10:45 AM: Tea Break

## 10:45 AM - 12:30 PM: Live VTune Profiling Demo & Roofline Analysis
- **Action**: Run `vtune -collect hotspots` and `vtune -collect memory-access` on a live matrix multiplication binary.
- **Spoken Script**:
  > *"Watch this terminal. We run:
  > `vtune -collect memory-access ./naive_matrix_mult`
  > 
  > Look at the report:
  > - Memory Bound: 74.2% of pipeline slots!
  > - DRAM Bandwidth: Saturated at 95% of peak.
  > - L1 Cache Hit Rate: Only 42%!
  > 
  > The CPU is spending nearly three-quarters of its life waiting for RAM.
  > Now watch what happens when we apply loop tiling and blocking to fit the matrix into the L2 cache.
  > L1 Cache Hit Rate jumps to 96%.
  > Execution time drops from 14 seconds to 0.8 seconds.
  > 
  > That is a **17.5x speedup** achieved simply by understanding cache dimensions."*
""", encoding="utf-8")

f4_4 = d_script / "afternoon_session_trainer_script.md"
f4_4.write_text("""# Day 4: Afternoon Session Trainer Script (1:30 PM - 4:30 PM)

## 01:30 PM - 02:15 PM: NUMA Interleaving & Thread Affinity Lab
- **Spoken Script**:
  > *"Welcome back. In this afternoon lab, we are going to explore NUMA (Non-Uniform Memory Access).
  > 
  > If you have a dual-socket motherboard:
  > Socket 0 has its own memory channels.
  > Socket 1 has its own memory channels.
  > 
  > If a thread on Socket 0 allocates memory on Socket 1, every memory read must cross the UPI bus.
  > Let's test this with `numactl`:
  > - `numactl --membind=0 --cpunodebind=0 ./stream_benchmark` (Local access: 80 ns latency)
  > - `numactl --membind=1 --cpunodebind=0 ./stream_benchmark` (Cross-socket remote access: 140 ns latency)
  > 
  > You will see a 40% performance collapse in real time simply from crossing sockets."*

## 02:15 PM - 04:00 PM: Guided Hands-On Lab (Profiling & Roofline Generation)
- **Action**: Students profile their own C++/Python codes using `vtune` and `perf`.
- **Spoken Script**:
  > *"Generate your Roofline chart. Identify whether your current implementation sits under the memory-bound diagonal or the compute-bound ceiling."*

## 04:00 PM - 04:30 PM: Day 5 Grand Finale Teaser
- **Spoken Script**:
  > *"Today we mastered microarchitecture profiling and cluster interconnects.
  > 
  > Tomorrow is the grand finale of our 5-day masterclass: Generative AI and Large Language Models on Intel HPC.
  > We will calculate the exact mathematics of LLM KV-cache memory, examine Intel Gaudi AI accelerators, optimize LLMs with OpenVINO INT8/INT4 quantization, and build high-throughput FastAPI inference pipelines.
  > See you tomorrow at 9:00 AM sharp."*
""", encoding="utf-8")

f4_5 = d_script / "whiteboard_sketches_and_visual_prompts.md"
f4_5.write_text("""# Day 4: Whiteboard Sketches & Visual Architecture Prompts

## Sketch 1: Dual-Socket NUMA Architecture
```
+------------------------------------+   +------------------------------------+
|          SOCKET 0 (NUMA 0)         |   |          SOCKET 1 (NUMA 1)         |
|  [Cores 0-31] <-> [L3 Cache 48MB]  |   |  [Cores 32-63] <-> [L3 Cache 48MB] |
|                 |                  |   |                 |                  |
|        [Memory Controller]         |   |        [Memory Controller]         |
+-----------------+------------------+   +-----------------+------------------+
                  |                                        |
            Local Access                             Local Access
               (70 ns)                                  (70 ns)
                  v                                        v
        +-------------------+                    +-------------------+
        |  DRAM Channel 0-3 |                    |  DRAM Channel 4-7 |
        |     (Node 0)      |                    |     (Node 1)      |
        +-------------------+                    +-------------------+
                  ^                                        ^
                  |           Intel UPI Interconnect       |
                  +========================================+
                             Remote Cross-Socket Access
                                      (140 ns!)
```

## Sketch 2: Loop Tiling / Blocking for Cache Locality
```
NAIVE MATRIX MULTIPLICATION (Row-Column):
Traversing Column of B jumps across DRAM pages! (Cache Misses on every element!)
B: [ x ] -> (jump N elements) -> [ x ] -> (jump N elements) -> [ x ]

TILED / BLOCKED MATRIX MULTIPLICATION:
Block of A (B x B) and Block of B (B x B) fit ENTIRELY inside L1/L2 Cache!
+---------+     +---------+
| Block A |  *  | Block B |  --> 100% Cache Hits! Zero DRAM bus traffic!
+---------+     +---------+
```
""", encoding="utf-8")

# ==============================================================================
# 3. Student Cross-Questioning Defense
# ==============================================================================
f4_6 = d_defense / "nasty_trap_questions_and_killer_answers.md"
f4_6.write_text("""# Day 4: Student Cross-Questioning Defense - Nasty Trap Questions & Killer Answers

### Trap Q1: "What is the difference between InfiniBand and 100GbE (Gigabit Ethernet) in supercomputing?"
- **The Student's Angle**: Challenging the necessity of expensive InfiniBand interconnects.
- **The Killer Response**:
  > *"Bandwidth is only half the story; **Latency and CPU Offload** are where InfiniBand dominates.
  > 
  > 1. **Latency**: Standard Ethernet has a latency of 10 to 50 microseconds (due to OS kernel TCP/IP stack traversal). InfiniBand has a latency of **under 1 microsecond (600 to 800 nanoseconds)**. In distributed MPI or Horovod AllReduce, where processes synchronize thousands of times per second, that 20x latency difference destroys Ethernet performance.
  > 2. **Kernel Bypass & RDMA**: Ethernet requires the OS kernel to receive the packet, interrupt the CPU, and copy data into user space. InfiniBand uses **RDMA (Remote Direct Memory Access)**: the Host Channel Adapter (HCA) writes data directly into the remote server's RAM over PCIe without waking up or interrupting the remote CPU! Zero kernel overhead, zero CPU cycles wasted on networking."*

### Trap Q2: "Can VTune profile Python scripts, or is it only for C++ and Fortran?"
- **The Student's Angle**: Questioning VTune's applicability to modern AI workflows.
- **The Killer Response**:
  > *"Intel VTune has first-class native support for Python mixed-mode profiling.
  > 
  > When you run `vtune -collect hotspots python train.py`, VTune unwinds the call stack across both the Python bytecode interpreter AND native C/C++ extension libraries (`.so` / `.pyd`) simultaneously!
  > 
  > In the VTune GUI, it displays the exact Python function name (e.g., `model.forward()`) and lets you double-click directly down into the underlying native C++ GEMM kernel (`libtorch_cpu.so` or `libmkl_avx512.so`), showing exact CPU clock cycles spent per line of Python and C++."*
""", encoding="utf-8")

f4_7 = d_defense / "live_terminal_counter_demos.md"
f4_7.write_text("""# Day 4: Live Terminal Counter-Demos

## Demo 1: Inspecting NUMA Topology and Socket Distances
```bash
# Query NUMA nodes, cores per node, and memory sizes
numactl --hardware
```

## Demo 2: Command-Line VTune Hotspots Collection
```bash
# Collect hotspots profile with summary report
vtune -collect hotspots -result-dir=./vtune_results -- ./my_binary
vtune -report summary -result-dir=./vtune_results
```
""", encoding="utf-8")

# ==============================================================================
# 4. Step-by-Step CLI & Code Breakdown
# ==============================================================================
f4_8 = d_code / "line_by_line_code_walkthrough.md"
f4_8.write_text("""# Day 4: Line-by-Line Code Walkthrough (Loop Tiling & Blocking)

Let's inspect how loop blocking transforms matrix multiplication:

```cpp
#include <iostream>
#include <vector>

constexpr int N = 1024;
constexpr int BLOCK_SIZE = 64; // Tuned to fit into L1 Data Cache (32-48 KB)

void tiled_matrix_multiply(const float* A, const float* B, float* C) {
    // Outer loops iterate over blocks
    for (int bi = 0; bi < N; bi += BLOCK_SIZE) {
        for (int bj = 0; bj < N; bj += BLOCK_SIZE) {
            for (int bk = 0; bk < N; bk += BLOCK_SIZE) {
                // Inner loops execute within the local cache-resident block
                for (int i = bi; i < bi + BLOCK_SIZE; ++i) {
                    for (int k = bk; k < bk + BLOCK_SIZE; ++k) {
                        float rA = A[i * N + k]; // Kept in vector register
                        for (int j = bj; j < bj + BLOCK_SIZE; ++j) {
                            C[i * N + j] += rA * B[k * N + j];
                        }
                    }
                }
            }
        }
    }
}
```
""", encoding="utf-8")

f4_9 = d_code / "compilation_and_execution_pipeline.md"
f4_9.write_text("""# Day 4: Compilation & Execution Pipeline

## Profiling with `perf` and VTune
```bash
# Compile with debug symbols for accurate symbol resolution in profilers
icpx -O3 -g -xHost tiled_matmul.cpp -o tiled_matmul

# Profile hardware cache misses with Linux perf
perf stat -e L1-dcache-loads,L1-dcache-load-misses,LLC-loads,LLC-load-misses ./tiled_matmul

# Profile with Intel VTune
vtune -collect memory-access -result-dir=./vtune_mem_report ./tiled_matmul
```
""", encoding="utf-8")

# ==============================================================================
# 5. Lab Challenges & Error Debugging
# ==============================================================================
f4_10 = d_debug / "student_lab_challenges_with_solutions.md"
f4_10.write_text("""# Day 4: Student Lab Challenges with Step-by-Step Solutions

## Challenge 1: Find the Optimal Block Size ($B$) for Your System's L1 Cache
- **Goal**: Measure wall-clock execution time for block sizes $B \\in \\{16, 32, 64, 128, 256\\}$ and plot performance to find the cache sweet spot.
- **Solution Strategy**: Block size 64 generally provides the best trade-off for 32 KB L1D caches ($64 \\times 64 \\times 4 \\text{ bytes} = 16 \\text{ KB}$, leaving half the cache free for other variables).

## Challenge 2: Slurm Job Array for Hyperparameter Sweep
- **Goal**: Write a Slurm script that executes an array of 5 jobs with distinct learning rates:
```bash
#!/bin/bash
#SBATCH --job-name=sweep
#SBATCH --array=0-4
#SBATCH --output=sweep_%A_%a.out

RATES=(0.1 0.01 0.001 0.0001 0.00001)
LR=${RATES[$SLURM_ARRAY_TASK_ID]}
python3 train.py --lr=$LR
```
""", encoding="utf-8")

f4_11 = d_debug / "common_student_syntax_errors_and_5_sec_fixes.md"
f4_11.write_text("""# Day 4: Common Student Errors & 5-Second Instant Fixes

### Error 1: `vtune: error: [Instrumentation Engine]: Hardware event-based sampling driver is not loaded`
- **Cause**: Linux kernel PMU driver (`sep` or `perf`) requires root or elevated sampling permissions.
- **5-Second Fix**:
  ```bash
  # Enable user-space perf events
  sudo sysctl -w kernel.perf_event_paranoid=1
  # Or use VTune user-mode sampling
  vtune -collect hotspots -knob enable-user-tasks=true ./my_bin
  ```

### Error 2: `numactl: command not found`
- **Cause**: The `numactl` package is missing.
- **5-Second Fix**: `sudo apt-get install -y numactl` or `sudo yum install -y numactl`.
""", encoding="utf-8")

print("[SUCCESS] Day 4: Zero-to-God-Tier Master Dossier Built Completely!")
