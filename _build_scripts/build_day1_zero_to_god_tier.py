"""
build_day1_zero_to_god_tier.py
Constructs the exhaustive 00_ZERO_TO_GOD_TIER_MASTER_DOSSIER for Day 1:
HPC Fundamentals, Linux Systems Architecture & Intel oneAPI DPC++/SYCL.
Written assuming Shivam knows ZERO, building up to an authoritative, master-level systems engineer.
"""

import os
from pathlib import Path

DAY1_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\Day-01_HPC_Linux_Shell_oneAPI\00_ZERO_TO_GOD_TIER_MASTER_DOSSIER")

# Subdirectories
d_concept = DAY1_DIR / "01_Concept_From_Absolute_Scratch"
d_script = DAY1_DIR / "02_Minute_By_Minute_Trainer_Script"
d_defense = DAY1_DIR / "03_Student_Cross_Questioning_Defense"
d_code = DAY1_DIR / "04_Step_By_Step_CLI_And_Code_Breakdown"
d_debug = DAY1_DIR / "05_Lab_Challenges_And_Error_Debugging"

for d in [d_concept, d_script, d_defense, d_code, d_debug]:
    d.mkdir(parents=True, exist_ok=True)

print(f"[*] Building Day 1 Zero-to-God-Tier Dossier in: {DAY1_DIR}")

# ==============================================================================
# 1. Concept from Absolute Scratch
# ==============================================================================
f1_1 = d_concept / "concept_breakdown_intuitive_analogy.md"
f1_1.write_text("""# Day 1: HPC Fundamentals & Intel oneAPI - Intuitive Analogies (Zero to Mastery)

## 1. What Actually is "High Performance Computing" (HPC)?
If you ask a normal software developer what computing is, they think of a laptop opening a browser or a web server responding to an API call.
In that world, if a program takes 2 seconds to run, nobody cares.

Now imagine you are:
1. Simulating the aerodynamics of an ISRO rocket reentry into Earth's atmosphere.
2. Forecasting the monsoon rainfall pattern across Uttar Pradesh using millions of atmospheric pressure sensors.
3. Training an AI model with 70 billion parameters on 10 trillion words of text.

If you run those calculations on a single laptop CPU, it will take **470 years** to finish.
**HPC (High Performance Computing)** is the science and engineering of taking a calculation that would take 400 years and completing it in **4 hours**.

How do we do that? Not by buying one magical CPU that runs at 1,000 GHz (silicon physics prevents CPUs from exceeding ~5 GHz due to thermal limits).
Instead, we do it by:
- Organizing thousands of CPU cores and GPU execution units to work simultaneously in parallel.
- Structuring data so the memory bus never starves the compute cores.
- Using specialized compilers (Intel oneAPI) that speak directly to the silicon's vector hardware.

---

## 2. The Kitchen Analogy: Latency vs Throughput (CPU vs GPU vs Memory)

Imagine you run an elite restaurant during a massive wedding dinner with 1,000 guests:
- **The Master Chef (The CPU Core)**:
  - An Olympic-level master chef who can slice an onion in 0.5 seconds with millimeter precision.
  - Can make complex decisions: *"Is the sauce too salty? Add cream. Is the oven too hot? Lower the flame."* (Branch prediction, speculative execution, low latency).
  - Problem: The master chef only has two hands. If 1,000 guests all order soup at the same moment, the chef is overwhelmed.
- **The Army of 500 Line Cooks (The GPU / Accelerator)**:
  - 500 line cooks who know only ONE thing: stir the pot in unison.
  - They cannot decide recipes; they cannot handle complex logic. But when you say *"Everyone chop 1 carrot simultaneously"*, 500 carrots are chopped in 1 second. That is High Throughput (SIMD/Data Parallelism).
- **The Grocery Store Down the Street (Main Memory / DRAM)**:
  - Where the ingredients are stored.
  - If the master chef has to walk to the grocery store every time they need a pinch of salt, they spend 99% of their day walking down the street instead of cooking.
  - **The Spice Rack on the Counter (The L1/L2/L3 CPU Cache)**:
    - Right next to the cutting board. Access time is instantaneous (1 nanosecond).
    - HPC is the art of keeping the spice rack full so the chef NEVER walks down the street.

---

## 3. What is Intel oneAPI? (The Universal Translator)
Historically, the world was fractured:
- To program an Intel CPU, you wrote C++ with OpenMP.
- To program an NVIDIA GPU, you had to write proprietary CUDA.
- To program an AMD GPU, you had to write ROCm / HIP.
- To program an FPGA, you had to write VHDL or Verilog.

If your company bought $2 million worth of NVIDIA GPUs and wrote 100,000 lines of CUDA code, you were trapped. You could never switch to Intel or AMD hardware without rewriting your entire codebase.

**Intel oneAPI** is an open, cross-architecture programming model based on **SYCL** (an open C++ standard from Khronos Group).
- You write ONE C++ codebase using SYCL abstractions.
- The oneAPI compiler (`icpx -fsycl`) compiles that single code to run natively on:
  - Intel Xeon CPUs
  - Intel Arc / Data Center Max GPUs
  - NVIDIA GPUs (via Codeplay oneAPI plugins)
  - AMD GPUs (via open-source LLVM SYCL backends)
- It destroys vendor lock-in.
""", encoding="utf-8")

f1_2 = d_concept / "low_level_silicon_and_mathematical_foundations.md"
f1_2.write_text("""# Day 1: Low-Level Silicon & Mathematical Foundations

## 1. The Von Neumann Bottleneck & The Memory Wall
In classical computer architecture (Von Neumann model, 1945), the Central Processing Unit (CPU) and Memory (DRAM) are physically separated and connected by a shared bus.

### The Physics of the Memory Wall
Over the last 40 years:
- CPU compute performance grew by ~55% per year (Moore's Law + Dennard Scaling).
- Memory bus latency improved by only ~7% per year.

```
Access Latency Spectrum on Intel Xeon Scalable:
- CPU Registers:        ~0.3 ns  (1 cycle)
- L1 Data Cache (32KB): ~1.0 ns  (4-5 cycles)
- L2 Cache (1-2MB):     ~3.5 ns  (14 cycles)
- L3 Cache (LLC, 30MB): ~14.0 ns (40-50 cycles)
- Main Memory (DDR5):   ~75-90 ns (200-250 cycles)
- NVMe SSD:             ~10-50 microseconds (10,000 - 50,000 cycles)
```

### The Arithmetic Operational Intensity (Flops/Byte)
Let:
- $W$ = Number of floating-point operations (FLOPs) performed by the algorithm.
- $Q$ = Total bytes of data transferred to/from DRAM.

The **Operational Intensity** $I$ is defined as:
$$I = \\frac{W}{Q} \\quad \\left[\\frac{\\text{FLOPs}}{\\text{Byte}}\\right]$$

- If an algorithm has low operational intensity (e.g., Vector Addition: $y[i] = a[i] + b[i]$, 1 FLOP for 3 memory reads/writes = $1 / (3 \\times 4) = 0.083$ FLOPs/Byte), it is strictly **Memory-Bound**. The CPU arithmetic logic units (ALUs) spend 90% of their time stalled waiting for DDR5 bus lines to charge.
- If an algorithm has high operational intensity (e.g., Matrix-Matrix Multiplication $C = A \\times B$: $2N^3$ FLOPs for $3N^2$ memory words, $I = O(N)$), it is **Compute-Bound**.

---

## 2. SIMD Vectorization Microarchitecture (AVX-512)
Modern x86-64 processors feature Single Instruction, Multiple Data (SIMD) vector execution units.

### Register Layout
- GPR (General Purpose Registers): `RAX`, `RBX`, ... (64-bit scalar integers).
- SSE: `XMM0` - `XMM15` (128-bit: 4 x 32-bit float).
- AVX/AVX2: `YMM0` - `YMM15` (256-bit: 8 x 32-bit float).
- AVX-512: `ZMM0` - `ZMM31` (512-bit: 16 x 32-bit float or 8 x 64-bit double).

### Fused Multiply-Add (FMA) Instruction
The fundamental workhorse of modern HPC, linear algebra, and deep learning is the FMA instruction:
$$r = (a \\times b) + c$$
An AVX-512 core has two 512-bit FMA execution ports (Port 0 and Port 5 on Intel Skylake/Ice Lake/Sapphire Rapids).
- Each 512-bit FMA unit computes 16 single-precision FMAs per cycle.
- Each FMA counts as 2 FLOPs (1 multiply + 1 add).
- Total theoretical peak compute per clock cycle per core:
$$\\text{Peak FLOPs/cycle/core} = 2 \\text{ (FMA units)} \\times 16 \\text{ (elements)} \\times 2 \\text{ (FLOPs/FMA)} = 64 \\text{ FLOPs/cycle}$$

On a 32-core Intel Xeon operating at 3.0 GHz:
$$\\text{Theoretical Peak} = 32 \\times 3.0 \\times 10^9 \\times 64 = 6.144 \\text{ TFLOPS (TeraFLOPs per second)}$$

If your code is written in naive unvectorized C/Python, it executes 1 scalar add per cycle, achieving only ~0.096 TFLOPS — **wasting 98.4% of the silicon you paid for**.

---

## 3. Intel oneAPI & SYCL Execution Model
SYCL breaks heterogeneous programming into three explicit tiers:
1. **Host (CPU)**: Executes standard C++ control flow, manages allocations, schedules kernels.
2. **Device (Accelerator / CPU Core)**: Executes massive parallel workitems.
3. **Queue (`sycl::queue`)**: An asynchronous channel connecting the Host to the Device.

### Work-Item Hierarchy:
- **Work-Item**: The smallest unit of execution (an individual thread executing the kernel on one data element).
- **Work-Group**: A collection of work-items that execute concurrently on the same compute unit, share local high-speed scratchpad memory (`sycl::local_accessor`), and can synchronize with barriers.
- **ND-Range**: The N-dimensional grid covering the entire problem space.
""", encoding="utf-8")

# ==============================================================================
# 2. Minute-by-Minute Trainer Script
# ==============================================================================
f1_3 = d_script / "morning_session_trainer_script.md"
f1_3.write_text("""# Day 1: Morning Session Trainer Script (9:00 AM - 12:30 PM)

## 09:00 AM - 09:15 AM: Room Takeover & Energy Calibration
- **Action**: Stand at the podium. Do not touch the mouse. Do not turn on the projector yet. Look across the room, make eye contact with the front row and back row.
- **Spoken Script**:
  > *"Good morning, everyone. Welcome to the High Performance Computing Master Class, organized by Edulateral Foundation in technical alignment with Intel and NEC Supercomputing.
  >
  > Over the next five days, we are going to look past high-level abstractions and see how computing actually happens at the silicon level.
  > 
  > In your four years of computer science, you have learned how to write code that works. In this room, we are going to learn how to write code that screams on hardware. We are going to explore why a naive Python or C script leaves 95% of your processor completely idle, how modern supercomputers like Frontier and Aurora breach the Exaflop barrier, and how every major AI breakthrough from GPT-4 to Llama-3 is fundamentally an HPC scaling victory.
  > 
  > Let's start with a blank board."*

## 09:15 AM - 09:45 AM: The Whiteboard Breakdown (The Memory Wall)
- **Action**: Walk to the whiteboard. Pick up a black marker. Draw the CPU Core, Registers, L1, L2, L3, and DRAM.
- **Spoken Script**:
  > *"Look at this diagram. In modern computing, an Intel CPU arithmetic logic unit executes an instruction in roughly 0.3 nanoseconds.
  > 
  > But when your code asks for a variable that is sitting in main DRAM memory, how long does the CPU have to wait?
  > 
  > It waits 70 to 90 nanoseconds.
  > 
  > In human terms: if 0.3 nanoseconds is 1 second of a chef's time, 80 nanoseconds is 4 and a half minutes of standing still staring at an empty cutting board.
  > 
  > Every time your code causes a cache miss, your CPU cores stall. High Performance Computing is not just about writing algorithms; it is about memory orchestration. It is about understanding cache lines, vector registers, and data locality."*

## 09:45 AM - 10:30 AM: Linux Architecture for Systems Engineers
- **Action**: Turn on projector. Switch to Linux terminal.
- **Spoken Script**:
  > *"Let's open our terminals. If you want to do HPC, you must understand your operating system down to kernel data structures.
  > 
  > Let's run `lscpu`. Look at the output:
  > - Architecture: x86_64
  > - CPU(s): Count the hardware threads.
  > - Thread(s) per core: 1 or 2 (Hyperthreading / SMT).
  > - L1d cache, L1i cache, L2 cache, L3 cache.
  > - Flags: Look for `avx2`, `avx512f`, `fma`.
  > 
  > These flags are not decorative strings. They tell the compiler which hardware arithmetic units physically exist on the die."*

## 10:30 AM - 10:45 AM: Official Edulateral Tea Break
- Pacing cue: Release students exactly at 10:30. Stand near the podium, converse with curious students.

## 10:45 AM - 12:30 PM: Compilation, Vectorization & Intel oneAPI DPC++ Intro
- **Action**: Demonstrate scalar vs vectorized C++ code on screen. Show assembly output using `objdump -d` or Compiler Explorer.
- **Spoken Script**:
  > *"Watch what happens when we compile with standard `gcc -O0` versus Intel oneAPI `icpx -O3 -xHost`.
  > 
  > In `-O0`, the compiler emits scalar `addss` instructions: one 32-bit addition per instruction.
  > In `-O3 -xHost`, the compiler unrolls the loop and emits `vaddps %zmm0, %zmm1, %zmm2`.
  > That single `vaddps` instruction processes sixteen 32-bit floating point numbers in one single tick of the clock.
  > 
  > That is a 16x throughput improvement from a single compiler switch. That is the power of hardware alignment."*
""", encoding="utf-8")

f1_4 = d_script / "afternoon_session_trainer_script.md"
f1_4.write_text("""# Day 1: Afternoon Session Trainer Script (1:30 PM - 4:30 PM)

## 01:30 PM - 02:00 PM: Live SYCL/DPC++ Kernel Walkthrough
- **Action**: Open `dpcpp_vector_add.cpp` in VS Code / Vim on the projection screen.
- **Spoken Script**:
  > *"Welcome back. In this afternoon lab, you are writing your first modern heterogeneous kernel using SYCL and Intel DPC++.
  > 
  > Look at line 14: `sycl::queue q(sycl::default_selector_v);`
  > What is this queue?
  > It is the bridge between host memory and compute silicon. When we pass `default_selector_v`, the SYCL runtime inspects the system at startup. If an Intel GPU or accelerator exists, it selects it; otherwise, it falls back to the host CPU multicore engine.
  > 
  > Now look at line 20: `sycl::malloc_shared<float>(N, q);`
  > This is Unified Shared Memory (USM). The pointer returned can be dereferenced by BOTH the CPU host code AND the device kernel code. The underlying oneAPI Level Zero driver migrates pages transparently between host RAM and device memory."*

## 02:00 PM - 03:45 PM: Guided Hands-On Lab (Lab 1 & 2 Execution)
- **Action**: Students begin coding Lab 1 (Linux process monitoring & CPU pinning) and Lab 2 (SYCL vector add).
- **Trainer Pacing & Floor Movement**:
  - Walk the aisles continuously. Do not sit at the teacher's desk.
  - When a student hits an error (e.g., `dpcpp: command not found`), don't type it for them. Prompt them: *"Did you source the oneAPI environment variables? Run `source /opt/intel/oneapi/setvars.sh`."*
  - Point out cache behavior using `perf stat -e cache-misses,cache-references ./benchmark_bin`.

## 03:45 PM - 04:15 PM: Speed Benchmark Showdown (Student Competition)
- **Spoken Script**:
  > *"Who has the fastest vector add on their workstation? Let's inspect the timings.
  > 
  > Look at the student in Row 3: their single-threaded scalar code took 420 milliseconds for 50 million elements.
  > Their SYCL vectorized kernel took 18 milliseconds.
  > That is a **23.3x speedup**.
  > 
  > Notice what we did: we did not buy a new computer. We did not spend a single rupee on new hardware. We simply stopped writing software that treats a modern multi-gigahertz superscalar vector processor like an 8-bit calculator from 1982."*

## 04:15 PM - 04:30 PM: Daily Debrief & Day 2 Teaser
- **Spoken Script**:
  > *"Today we conquered single-node hardware architecture, Linux process affinity, and vector SIMD execution.
  > 
  > Tomorrow, we take the gloves off: we enter Parallel Computing. We will see how multiple CPU cores coordinate without corrupting memory using OpenMP, how supercomputer nodes talk across networks using MPI, and how Intel oneDAL accelerates machine learning by 40x.
  > 
  > Review your lab notes tonight. I will see everyone at 9:00 AM sharp."*
""", encoding="utf-8")

f1_5 = d_script / "whiteboard_sketches_and_visual_prompts.md"
f1_5.write_text("""# Day 1: Whiteboard Sketches & Visual Architecture Prompts

## Sketch 1: The Multi-Tier Memory Latency Pyramid
```
      /\
     /  \       Registers (~0.3 ns, 1 cycle)
    /----\      ---------------------------------
   /  L1  \     L1 Data Cache (32 KB, ~1.0 ns, 4 cycles)
  /--------\    ---------------------------------
 /    L2    \   L2 Cache (1 MB, ~3.5 ns, 14 cycles)
/------------\  ---------------------------------
/     L3      \ L3 Shared LLC (30-50 MB, ~14 ns, 50 cycles)
/--------------\---------------------------------
/  DRAM / DDR5  \ Main Memory (64-512 GB, ~80 ns, 200+ cycles)
/----------------\---------------------------------
/ NVMe SSD / Disk \ Non-Volatile Storage (10,000+ ns latency)
```

## Sketch 2: AVX-512 Register Packing (Single-Precision Floats)
```
ZMM0 (512 bits = 64 bytes):
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
| f0  | f1  | f2  | f3  | f4  | f5  | f6  | f7  | f8  | f9  | f10 | f11 | f12 | f13 | f14 | f15 |
+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  32b   32b   32b   32b   32b   32b   32b   32b   32b   32b   32b   32b   32b   32b   32b   32b
```

## Sketch 3: SYCL Unified Shared Memory (USM) Architecture
```
+-------------------------------------------------------------------+
|                        HOST APPLICATION                           |
|  float* data = sycl::malloc_shared<float>(N, q);                  |
+-------------------------------------------------------------------+
                  |                                 |
       (Pointer dereference)               (Pointer dereference)
                  v                                 v
+-------------------------------+   +-------------------------------+
|          HOST CPU             |   |        DEVICE / ACCEL         |
|  Initializes data array       |   |  Executes parallel_for kernel |
|  Reads final computed result  |   |  Level Zero driver migrates   |
|                               |   |  pages across PCIe / CXL bus  |
+-------------------------------+   +-------------------------------+
```
""", encoding="utf-8")

# ==============================================================================
# 3. Student Cross-Questioning Defense
# ==============================================================================
f1_6 = d_defense / "nasty_trap_questions_and_killer_answers.md"
f1_6.write_text("""# Day 1: Student Cross-Questioning Defense - Nasty Trap Questions & Killer Answers

### Trap Q1: "Sir, isn't Python faster to develop in? Why waste time with low-level C++ and oneAPI when time-to-market is what companies care about?"
- **The Student's Angle**: Appealing to startup agility and modern development velocity.
- **The Killer Response**:
  > *"Time-to-market matters when building a prototype. Energy and compute efficiency matter when operating at scale.
  > 
  > Let's look at the financial numbers: Training a model like GPT-3 cost an estimated $4.6 million in electricity and server time. If your code is 10x slower because of high-level runtime overhead, your training run costs $46 million instead of $4.6 million.
  > 
  > Furthermore, every major high-level Python library—TensorFlow, PyTorch, NumPy, scikit-learn—is a thin Python wrapper around high-performance C++, CUDA, and oneAPI backends.
  > 
  > If you only know Python, you can only use what others build. If you master oneAPI and systems architecture, you are the engineer who builds the infrastructure that everyone else's Python runs on. That is why systems engineers command the highest compensation bands in engineering."*

### Trap Q2: "Why does `dpcpp` use unified shared memory (USM) instead of explicit buffers and accessors? Isn't USM slower due to page fault overhead?"
- **The Student's Angle**: Attempting to catch you on SYCL specification differences between Buffer/Accessor and USM.
- **The Killer Response**:
  > *"You are asking an insightful architectural question.
  > 
  > SYCL provides two memory models:
  > 1. **Buffer and Accessor model**: Constructs a formal Directed Acyclic Graph (DAG) of dependencies before kernel execution. The SYCL runtime analyzes data dependencies across read/write accessors and can overlap independent kernel execution automatically. However, buffers cannot encapsulate standard raw C++ pointers, making integration with existing legacy C++ codebases cumbersome.
  > 2. **Unified Shared Memory (USM)**: Provides standard C++ pointer syntax (`malloc_shared`, `malloc_device`, `malloc_host`).
  > 
  > You are correct that `malloc_shared` relies on OS/driver page migration engines which incur page-fault latency during the initial page migration across the PCIe bus.
  > 
  > That is precisely why in production HPC, we do not use `malloc_shared` for latency-critical tight loops. We use **`malloc_device`** with explicit `q.memcpy()` asynchronous memory copies. This gives zero page-fault overhead, predictable PCIe burst DMA transfers, and raw pointer ergonomics."*

### Trap Q3: "What is the difference between SMT (Simultaneous Multi-Threading / Hyper-Threading) and real physical CPU cores in an HPC workload?"
- **The Student's Angle**: Testing understanding of hardware threads vs physical silicon cores.
- **The Killer Response**:
  > *"In an Intel core with Hyper-Threading enabled, there is only **ONE physical set of execution units** (ALUs, FPUs, vector registers).
  > 
  > Hyper-Threading duplicates only the **architectural state** (Instruction Pointer, register state, thread context). When Thread 0 stalls on a cache miss waiting for DRAM, the hardware scheduler swaps execution to Thread 1 so the ALUs don't sit idle.
  > 
  > In web servers (I/O heavy, lots of waiting), Hyper-Threading improves throughput by ~20-30%.
  > 
  > But in **compute-bound HPC workloads** (like heavy AVX-512 matrix math where both threads are hammering the vector units at 100%), both threads compete for the exact same physical execution ports. This causes resource contention, cache thrashing, and pipeline stalls.
  > 
  > That is why on world-class supercomputers, Hyper-Threading is frequently disabled in the BIOS or jobs are pinned strictly to 1 thread per physical core."*
""", encoding="utf-8")

f1_7 = d_defense / "live_terminal_counter_demos.md"
f1_7.write_text("""# Day 1: Live Terminal Counter-Demos (Empirical Silencing Tools)

When a student argues or doubts a concept, execute these exact terminal one-liners to display live, empirical hardware truth.

## Demo 1: Proving Cache Line Size and Cache Hierarchy
```bash
# Display exact hardware cache dimensions in real-time
lscpu | grep -E "L1d|L1i|L2|L3"

# Inspect exact cache line size (64 bytes)
cat /sys/devices/system/cpu/cpu0/cache/index0/coherency_line_size
```

## Demo 2: Proving Hardware Vector Extensions
```bash
# Check if the host CPU supports AVX-512 or AVX2
grep -m1 -o -E "avx512[a-z0-9_]*|avx2|fma|sse4_2" /proc/cpuinfo
```

## Demo 3: Live Hardware Performance Counters (Cache Misses)
```bash
# Run a quick matrix or array command and measure hardware cache misses live
perf stat -e cycles,instructions,cache-references,cache-misses,branches,branch-misses \
  python3 -c "import numpy as np; a = np.random.randn(2000, 2000); b = np.dot(a, a)"
```
""", encoding="utf-8")

# ==============================================================================
# 4. Step-by-Step CLI & Code Breakdown
# ==============================================================================
f1_8 = d_code / "line_by_line_code_walkthrough.md"
f1_8.write_text("""# Day 1: Line-by-Line Code Walkthrough (DPC++ Vector Add)

Let's examine the foundational DPC++/SYCL program `dpcpp_vector_add.cpp` line by line:

```cpp
// Line 1: Include the unified SYCL header file
#include <sycl/sycl.hpp>
#include <iostream>
#include <vector>
#include <chrono>

// Line 6: Problem size: 10 Million floating-point numbers
constexpr size_t N = 10000000;

int main() {
    // Line 10: Initialize a SYCL execution queue
    // sycl::default_selector_v queries the system at runtime.
    // If an Intel GPU exists, it targets it; otherwise, targets multicore CPU.
    sycl::queue q(sycl::default_selector_v);
    
    std::cout << "[*] Running on device: " 
              << q.get_device().get_info<sycl::info::device::name>() 
              << std::endl;

    // Line 17: Allocate Unified Shared Memory (USM)
    // Allocates memory accessible by both Host (CPU) and Device (GPU/CPU).
    float* a = sycl::malloc_shared<float>(N, q);
    float* b = sycl::malloc_shared<float>(N, q);
    float* c = sycl::malloc_shared<float>(N, q);

    // Line 23: Initialize input arrays on Host
    for (size_t i = 0; i < N; ++i) {
        a[i] = 1.0f;
        b[i] = 2.0f;
        c[i] = 0.0f;
    }

    auto start = std::chrono::high_resolution_clock::now();

    // Line 32: Submit an asynchronous kernel to the SYCL queue
    q.submit([&](sycl::handler& h) {
        // Line 34: parallel_for executes across N work-items
        h.parallel_for(sycl::range<1>(N), [=](sycl::id<1> idx) {
            c[idx] = a[idx] + b[idx];
        });
    });

    // Line 40: Wait for kernel completion (Synchronize queue)
    q.wait();

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> duration = end - start;

    std::cout << "[+] Completed 10M element vector add in: " 
              << duration.count() << " ms" << std::endl;

    // Line 48: Free USM memory
    sycl::free(a, q);
    sycl::free(b, q);
    sycl::free(c, q);

    return 0;
}
```
""", encoding="utf-8")

f1_9 = d_code / "compilation_and_execution_pipeline.md"
f1_9.write_text("""# Day 1: Compilation & Execution Pipeline (Compiler Switches Demystified)

## 1. Sourcing Intel oneAPI Environment Variables
Before invoking any oneAPI tool, you must initialize the compiler environment variables:
```bash
source /opt/intel/oneapi/setvars.sh
```
What this does under the hood:
- Adds `icx`, `icpx`, `dpcpp` to `$PATH`.
- Appends oneAPI dynamic shared objects (`.so`) to `$LD_LIBRARY_PATH`.
- Sets `$CMPLR_ROOT` and `$ONEAPI_ROOT`.

## 2. Compilation Flags Breakdown
```bash
icpx -fsycl -O3 -xHost -qopt-report=3 dpcpp_vector_add.cpp -o dpcpp_vector_add
```

| Flag | Meaning | Silicon Effect |
| :--- | :--- | :--- |
| `icpx` | Intel oneAPI C++ Compiler driver | Invokes LLVM front-end with Intel code-gen backend. |
| `-fsycl` | Enables SYCL heterogeneous compilation | Splices AST into host code and SPIR-V device kernels. |
| `-O3` | Aggressive optimization level | Enables loop unrolling, vectorization, and function inlining. |
| `-xHost` | Target host machine's highest instruction set | Emits AVX-512 or AVX2 instructions native to the CPU. |
| `-qopt-report=3` | Generate comprehensive optimization report | Outputs exact loops that were vectorized and reasons why others were not. |
""", encoding="utf-8")

# ==============================================================================
# 5. Lab Challenges & Error Debugging
# ==============================================================================
f1_10 = d_debug / "student_lab_challenges_with_solutions.md"
f1_10.write_text("""# Day 1: Student Lab Challenges with Step-by-Step Solutions

## Challenge 1 (Beginner): Vector Triad ($C[i] = A[i] + s \\times B[i]$)
- **Goal**: Implement the classical HPC Vector Triad benchmark with a scalar multiplier $s = 2.5f$.
- **Solution**:
```cpp
float scalar = 2.5f;
q.parallel_for(sycl::range<1>(N), [=](sycl::id<1> idx) {
    c[idx] = a[idx] + scalar * b[idx];
}).wait();
```

## Challenge 2 (Intermediate): Device Query Utility
- **Goal**: Write a SYCL program that iterates over all available platforms and devices on the system and prints their Compute Units, Max Clock Frequency, and Global Memory Size.
- **Solution**:
```cpp
#include <sycl/sycl.hpp>
#include <iostream>

int main() {
    auto platforms = sycl::platform::get_platforms();
    for (auto& p : platforms) {
        std::cout << "Platform: " << p.get_info<sycl::info::platform::name>() << "\\n";
        for (auto& d : p.get_devices()) {
            std::cout << "  Device: " << d.get_info<sycl::info::device::name>() << "\\n"
                      << "  Compute Units: " << d.get_info<sycl::info::device::max_compute_units>() << "\\n"
                      << "  Global Mem (MB): " << d.get_info<sycl::info::device::global_mem_size>() / (1024*1024) << "\\n";
        }
    }
    return 0;
}
```

## Challenge 3 (Boss Level): Two-Dimensional 2D Grid Stencil Initialization
- **Goal**: Launch a 2D SYCL range `sycl::range<2>(1024, 1024)` to initialize a 2D temperature grid with boundary conditions.
""", encoding="utf-8")

f1_11 = d_debug / "common_student_syntax_errors_and_5_sec_fixes.md"
f1_11.write_text("""# Day 1: Common Student Errors & 5-Second Instant Fixes

### Error 1: `dpcpp: command not found` or `icpx: command not found`
- **Cause**: Student did not source the oneAPI environment variables in their current shell session.
- **5-Second Fix**:
  ```bash
  source /opt/intel/oneapi/setvars.sh
  ```

### Error 2: `error: no device available of type default`
- **Cause**: The SYCL runtime cannot locate an OpenCL or Level Zero driver backend.
- **5-Second Fix**:
  ```bash
  # Force host CPU execution device
  export ONEAPI_DEVICE_SELECTOR=opencl:cpu
  # Or verify available backends
  sycl-ls
  ```

### Error 3: Segmentation fault (core dumped) immediately after kernel launch
- **Cause**: Student accessed `c[idx]` on the Host CPU *before* calling `q.wait()`. The kernel was still running asynchronously on the device.
- **5-Second Fix**:
  Ensure `q.wait()` is invoked before any `std::cout` or host array reading loop!

### Error 4: `fatal error: sycl/sycl.hpp: No such file or directory`
- **Cause**: Student compiled with standard `g++` instead of `icpx -fsycl`.
- **5-Second Fix**:
  ```bash
  icpx -fsycl source.cpp -o executable
  ```
""", encoding="utf-8")

print("[SUCCESS] Day 1: Zero-to-God-Tier Master Dossier Built Completely!")
