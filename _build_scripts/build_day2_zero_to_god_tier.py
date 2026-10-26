"""
build_day2_zero_to_god_tier.py
Constructs the exhaustive 00_ZERO_TO_GOD_TIER_MASTER_DOSSIER for Day 2:
Parallel Computing Paradigms (OpenMP, MPI) & Intel oneDAL Machine Learning Acceleration.
Written assuming Shivam knows ZERO, building up to an authoritative, master-level systems engineer.
"""

import os
from pathlib import Path

DAY2_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\Day-02_Parallel_OpenMP_MPI_oneDAL\00_ZERO_TO_GOD_TIER_MASTER_DOSSIER")

# Subdirectories
d_concept = DAY2_DIR / "01_Concept_From_Absolute_Scratch"
d_script = DAY2_DIR / "02_Minute_By_Minute_Trainer_Script"
d_defense = DAY2_DIR / "03_Student_Cross_Questioning_Defense"
d_code = DAY2_DIR / "04_Step_By_Step_CLI_And_Code_Breakdown"
d_debug = DAY2_DIR / "05_Lab_Challenges_And_Error_Debugging"

for d in [d_concept, d_script, d_defense, d_code, d_debug]:
    d.mkdir(parents=True, exist_ok=True)

print(f"[*] Building Day 2 Zero-to-God-Tier Dossier in: {DAY2_DIR}")

# ==============================================================================
# 1. Concept from Absolute Scratch
# ==============================================================================
f2_1 = d_concept / "concept_breakdown_intuitive_analogy.md"
f2_1.write_text("""# Day 2: Parallel Computing, OpenMP, MPI & Intel oneDAL - Intuitive Analogies (Zero to Mastery)

## 1. Shared Memory (OpenMP) vs Distributed Memory (MPI): The Office Analogy

Imagine an accounting firm that must audit 100,000 tax receipts in a single day:

### Scenario A: Shared Memory (OpenMP)
- You have **one large conference room**.
- In the center of the room sits **one giant conference table** holding all 100,000 receipts in neat folders (Shared RAM / Main Memory).
- You hire **8 accountants** (CPU Cores / Threads) sitting around this single table.
- Every accountant can immediately reach out their hand and grab any receipt on the table.
- **The Problem (Race Conditions & Collisions)**:
  - If Accountant 1 and Accountant 2 both try to write the subtotal on the *same ledger page* at the exact same second, they knock over each other's pens and scribble garbage onto the paper (Data Corruption / Race Condition).
  - If Accountant 1 keeps erasing the title block of the page while Accountant 2 is trying to read it, both waste time (False Sharing / Cache Invalidation).
- **The Physical Limit**:
  - You can only fit so many chairs around one table before accountants are bumping elbows and the room runs out of oxygen (Socket memory bus saturation, NUMA latency).

---

### Scenario B: Distributed Memory (MPI)
- Instead of one room, you have **100 separate branch offices** in 100 different cities (Cluster Compute Nodes).
- Each office has its **own private desk and private file cabinet** (Node Local DRAM).
- Accountant in Office 1 **cannot physically reach** into Office 2's filing cabinet.
- **How do they cooperate?**
  - They must send letters or courier packages to each other (Network Packets / InfiniBand).
  - If Office 1 needs a balance sheet from Office 2, Office 2 must package it, stamp it, courier it across the network, and Office 1 must receive and open the envelope (`MPI_Send` / `MPI_Recv`).
- **The Advantage**:
  - You can scale to 10,000 offices worldwide! No single conference table will ever limit you.
- **The Challenge**:
  - Couriers take time (network latency). If offices spend all day waiting for letters instead of auditing receipts, productivity collapses (Communication Overhead).

---

## 2. What is Intel oneDAL? (The High-Speed Supercharged Accountant)
In machine learning (like k-Means clustering or Random Forest), you are performing millions of distance calculations:
$$d = \\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2 + \\dots}$$
Standard Python `scikit-learn` calculates distances like someone using a hand calculator: it does one dimension, saves it, does the next, and wastes memory round-trips.

**Intel oneDAL (Data Analytics Library)** is like equipping each accountant with an automated laser-scanning optical sorter:
- It arranges data in memory so that cache lines are 100% packed.
- It uses AVX-512 vector units to calculate 16 data points in parallel per clock tick.
- It distributes clusters across all CPU cores without lock contention.
- It delivers a **10x to 40x speedup** on the exact same dataset with zero code restructuring.
""", encoding="utf-8")

f2_2 = d_concept / "low_level_silicon_and_mathematical_foundations.md"
f2_2.write_text("""# Day 2: Low-Level Silicon & Mathematical Foundations (OpenMP, MPI & oneDAL)

## 1. Amdahl's Law vs Gustafson's Law

### Amdahl's Law (Fixed Workload Size)
Let $P$ be the parallelizable fraction of an application, and $(1 - P)$ be the strictly serial fraction.
If we execute the program on $N$ processor cores, the theoretical speedup $S(N)$ is:
$$S(N) = \\frac{1}{(1 - P) + \\frac{P}{N}}$$

As $N \\to \\infty$:
$$S_{\\max} = \\frac{1}{1 - P}$$

**Silicon Takeaway**:
If only 5% of your code is serial ($1 - P = 0.05$), the maximum possible speedup on an infinite number of CPU cores is:
$$S_{\\max} = \\frac{1}{0.05} = 20x$$
Even if you run on a 100,000-core supercomputer, your program can never run faster than 20x! Serial bottlenecks (e.g., I/O, locks) kill HPC scaling.

### Gustafson's Law (Scaled Workload Size)
In real-world HPC, when we get a bigger supercomputer, we don't run the same tiny problem faster; we solve a much larger problem!
$$S(N) = N - (1 - P)(N - 1)$$
Gustafson's Law shows that by scaling problem size proportionally with core count, parallel efficiency can remain near-linear.

---

## 2. Cache Coherence Protocols & False Sharing (The MESI Protocol)
Modern multi-core CPUs use the **MESI cache coherence protocol** to ensure all cores see a consistent view of shared memory:
- **M (Modified)**: Cache line is present only in the current core's cache and is dirty (diverges from DRAM).
- **E (Exclusive)**: Cache line is present only in the current core's cache and is clean (matches DRAM).
- **S (Shared)**: Cache line is present in multiple cores' caches and is clean.
- **I (Invalid)**: Cache line does not contain valid data.

### The Silicon Anatomy of False Sharing
1. Memory is moved between DRAM and CPU caches in chunks of **64 bytes (Cache Line)**.
2. Suppose Thread 0 running on Core 0 modifies `array[0]` (4 bytes).
3. Suppose Thread 1 running on Core 1 modifies `array[1]` (4 bytes).
4. Both variables reside in the same 64-byte cache line.
5. When Core 0 writes to `array[0]`, its hardware cache controller broadcasts an **Invalidate Request** across the inter-core interconnect (Ring Bus or Ultra Path Interconnect).
6. Core 1's copy of the cache line transitions from **Shared (S)** to **Invalid (I)**!
7. When Core 1 tries to read or write `array[1]`, it suffers a **Cache Miss** and must stall while fetching the modified cache line from Core 0.
8. This continuous bouncing of the cache line between cores is known as **Cache Line Bouncing / False Sharing**. It degrades multi-threaded performance by up to 10x!

---

## 3. MPI Point-to-Point Protocols: Eager vs Rendezvous
When `MPI_Send` is executed, the underlying MPI library (Intel MPI / MPICH / OpenMPI) selects one of two protocols based on message payload size:

1. **Eager Protocol (Small Messages, typically < 64 KB)**:
   - The sender transmits the data immediately into a pre-allocated receive buffer on the target rank, without waiting for the receiver to post an `MPI_Recv`.
   - Low latency, but risks buffer exhaustion if many eager messages arrive simultaneously.
2. **Rendezvous Protocol (Large Messages, typically > 64 KB)**:
   - The sender transmits a small handshake request ("Ready to send $X$ megabytes?").
   - The sender stalls until the receiver confirms it has allocated memory and posted `MPI_Recv`.
   - Data is transferred directly via RDMA (Remote Direct Memory Access) without intermediate memory copies.
   - Prevents buffer overflow, but introduces round-trip handshake latency.
""", encoding="utf-8")

# ==============================================================================
# 2. Minute-by-Minute Trainer Script
# ==============================================================================
f2_3 = d_script / "morning_session_trainer_script.md"
f2_3.write_text("""# Day 2: Morning Session Trainer Script (9:00 AM - 12:30 PM)

## 09:00 AM - 09:20 AM: Opening Hook & Yesterday's Debrief
- **Spoken Script**:
  > *"Good morning. Yesterday, we extracted 20x performance from a single core by aligning our data with vector execution units.
  > 
  > Today, we conquer the entire chip and the entire cluster.
  > 
  > Modern servers do not have 1 core; they have 64, 128, or 256 hardware cores. But if you take a standard C or Python program and run it, it uses exactly ONE core. 63 cores sit at 0% utilization, consuming idle electricity while you wait for your results.
  > 
  > Today, we learn the two fundamental pillars of parallel computing:
  > 1. OpenMP: Shared Memory parallelism within a single multi-socket machine.
  > 2. MPI: Distributed Memory parallelism across independent networked servers.
  > 
  > Let's start with a classic experiment on OpenMP."*

## 09:20 AM - 10:00 AM: OpenMP Fork-Join & The False Sharing Trap
- **Action**: Write code on screen showing a naive parallel sum using an array of accumulators `sum[thread_id]`.
- **Spoken Script**:
  > *"Look at this code on the projector. We want to sum 100 million numbers. We create 8 threads. Each thread accumulates into its own index: `sum[tid] += data[i]`.
  > 
  > At first glance, this looks clean: each thread has its own variable, right?
  > Let's run it.
  > 
  > Single-threaded execution time: 120 ms.
  > 8-threaded execution time: 480 ms!
  > 
  > Adding 8 threads made the code FOUR TIMES SLOWER.
  > Why?
  > 
  > (Turn to whiteboard and draw the 64-byte cache line).
  > Because hardware does not know what an integer is. Hardware only knows 64-byte cache lines. This is False Sharing."*

## 10:00 AM - 10:30 AM: Fixing False Sharing & OpenMP Reduction
- **Action**: Replace `sum[tid]` with `#pragma omp parallel for reduction(+:total_sum)`.
- **Spoken Script**:
  > *"Now watch what happens when we use the `reduction` clause.
  > The OpenMP runtime allocates a private register or thread-local accumulator for each core. Cores never invalidate each other's cache lines.
  > At loop termination, the runtime executes a lock-free logarithmic reduction tree.
  > 
  > Execution time: 16 ms.
  > An **8x real speedup** over single-threaded code. That is clean parallel engineering."*

## 10:30 AM - 10:45 AM: Tea Break

## 10:45 AM - 12:30 PM: Distributed Memory & MPI Foundations
- **Action**: Introduce `mpi4py` / C MPI bindings. Launch 4 ranks on terminal using `mpirun -n 4 ./mpi_hello`.
- **Spoken Script**:
  > *"Now we transition from Shared Memory to Distributed Memory.
  > In MPI, each process has its own address space. Rank 0 cannot read Rank 1's memory.
  > 
  > Notice what happens when we execute `mpirun -n 4`:
  > The MPI daemon launches 4 separate OS processes. Each process calls `MPI_Init()`, queries its identity via `MPI_Comm_rank()`, and discovers the cluster size via `MPI_Comm_size()`.
  > 
  > Let's inspect point-to-point communication: `MPI_Send` and `MPI_Recv`."*
""", encoding="utf-8")

f2_4 = d_script / "afternoon_session_trainer_script.md"
f2_4.write_text("""# Day 2: Afternoon Session Trainer Script (1:30 PM - 4:30 PM)

## 01:30 PM - 02:15 PM: Collective Communication & Intel oneDAL Demo
- **Spoken Script**:
  > *"Welcome back. In distributed computing, point-to-point sends are like one-on-one phone calls.
  > Collective communications are like conference calls:
  > - `MPI_Bcast`: One rank broadcasts data to everyone.
  > - `MPI_Scatter`: One rank divides an array and deals slices to all ranks like a deck of cards.
  > - `MPI_Gather`: All ranks send their computed results back to Rank 0 to assemble the final puzzle.
  > - `MPI_Allreduce`: Everyone computes, everyone reduces, and everyone gets the final global answer.
  > 
  > Now, let's see how this transforms Machine Learning with Intel oneDAL."*

## 02:15 PM - 03:45 PM: Guided Hands-On Lab (OpenMP Benchmark + oneDAL Patching)
- **Action**: Students run `intel_scikit_speedup.py` on benchmark datasets (`classification_500k_20feat.npz`).
- **Spoken Script**:
  > *"Open `intel_scikit_speedup.py`. Look at lines 8-10:
  > ```python
  > from sklearnex import patch_sklearn
  > patch_sklearn()
  > ```
  > That is all. Two lines of code.
  > 
  > Now run the benchmark:
  > - Standard scikit-learn k-Means: 42 seconds.
  > - Intel Extension for Scikit-learn (oneDAL): 1.4 seconds.
  > 
  > That is a **30x speedup** on identical hardware. Why? Because oneDAL leverages AVX-512 vectorization and cache-blocked SIMD matrix kernels."*

## 03:45 PM - 04:30 PM: Student Challenge Troubleshooting & Day 3 Teaser
- **Spoken Script**:
  > *"Today we mastered shared-memory thread pools and distributed-memory message passing.
  > 
  > Tomorrow, we combine these two concepts to build modern Deep Learning on supercomputers. We will look at Slurm workload orchestration, Horovod distributed training, and how companies train multi-billion parameter neural networks across multi-node clusters.
  > 
  > Fantastic work today. See you tomorrow at 9:00 AM."*
""", encoding="utf-8")

f2_5 = d_script / "whiteboard_sketches_and_visual_prompts.md"
f2_5.write_text("""# Day 2: Whiteboard Sketches & Visual Architecture Prompts

## Sketch 1: OpenMP Fork-Join Model
```
Master Thread --------------------------> (Sequential Region)
                 \      |      /
                  v     v     v
             Thread 0 Thread 1 Thread 2   (Parallel Region - OMP FORK)
                  |     |     |
                  v     v     v
                  +-----+-----+
                        |
                        v
Master Thread --------------------------> (Join Barrier & Resume Sequential)
```

## Sketch 2: MPI Collective Operations Cheat Sheet
```
MPI_Bcast:
Rank 0: [ A ] ----------> Rank 0: [ A ], Rank 1: [ A ], Rank 2: [ A ]

MPI_Scatter:
Rank 0: [ A | B | C ] --> Rank 0: [ A ], Rank 1: [ B ], Rank 2: [ C ]

MPI_Gather:
Rank 0: [ A ], Rank 1: [ B ], Rank 2: [ C ] --> Rank 0: [ A | B | C ]

MPI_Reduce (Sum):
Rank 0: [ 10 ], Rank 1: [ 20 ], Rank 2: [ 30 ] --> Rank 0: [ 60 ]

MPI_Allreduce (Sum):
Rank 0: [ 10 ], Rank 1: [ 20 ], Rank 2: [ 30 ] --> Rank 0: [ 60 ], Rank 1: [ 60 ], Rank 2: [ 60 ]
```
""", encoding="utf-8")

# ==============================================================================
# 3. Student Cross-Questioning Defense
# ==============================================================================
f2_6 = d_defense / "nasty_trap_questions_and_killer_answers.md"
f2_6.write_text("""# Day 2: Student Cross-Questioning Defense - Nasty Trap Questions & Killer Answers

### Trap Q1: "Why shouldn't I just create 1,000 OpenMP threads if my CPU has lots of cores?"
- **The Student's Angle**: Confusing OS thread count with physical silicon execution capacity.
- **The Killer Response**:
  > *"If you create 1,000 software threads on a machine with 16 physical cores:
  > 1. The Linux kernel scheduler must time-slice 1,000 threads across 16 cores using CFS (Completely Fair Scheduler).
  > 2. Every context switch invalidates L1/L2 caches and pollutes the TLB.
  > 3. Threads spend more CPU time context switching in kernel space than executing user instructions in user space.
  > 
  > In HPC, the golden rule is: **Number of active compute threads should equal the number of physical hardware cores** (or hardware threads if hyperthreading yields a net gain). Set `export OMP_NUM_THREADS=$(nproc)`."*

### Trap Q2: "Can't MPI and OpenMP be used together, and why would you want to?"
- **The Student's Angle**: Testing understanding of Hybrid Parallelism (MPI + OpenMP).
- **The Killer Response**:
  > *"Yes, that is the industry standard called **Hybrid Parallel Programming**.
  > 
  > In a modern supercomputing cluster:
  > - Each compute node has 2 CPU sockets, with 64 cores per socket (128 cores per node).
  > - If you run 128 MPI ranks on a single node, you waste massive memory because each rank duplicates OS runtime structures, buffers, and page tables.
  > - Instead, we launch **1 or 2 MPI ranks per node** (handling inter-node network communication across InfiniBand).
  > - Inside each node, that MPI rank spawns **64 OpenMP threads** to saturate all local CPU cores over shared DRAM memory!
  > This is called 'MPI across nodes, OpenMP inside the node'."*
""", encoding="utf-8")

f2_7 = d_defense / "live_terminal_counter_demos.md"
f2_7.write_text("""# Day 2: Live Terminal Counter-Demos

## Demo 1: Proving OpenMP Thread Pinning and Core Affinity
```bash
# Display core pinning in real-time
export OMP_DISPLAY_ENV=TRUE
export OMP_PROC_BIND=close
export OMP_PLACES=cores
python3 -c "import os; os.system('gcc -fopenmp -O3 ...')"
```

## Demo 2: Measuring OpenMP Scaling vs Thread Count
```bash
# Run with 1, 2, 4, 8 threads and measure wall-clock time
for t in 1 2 4 8; do
  export OMP_NUM_THREADS=$t
  echo -n "Threads: $t -> "
  python3 -c "import time, numpy as np; t0=time.perf_counter(); a=np.random.randn(2000, 2000); np.dot(a, a); print(f'{time.perf_counter()-t0:.4f}s')"
done
```
""", encoding="utf-8")

# ==============================================================================
# 4. Step-by-Step CLI & Code Breakdown
# ==============================================================================
f2_8 = d_code / "line_by_line_code_walkthrough.md"
f2_8.write_text("""# Day 2: Line-by-Line Code Walkthrough (OpenMP Reduction & oneDAL)

### Code 1: Clean OpenMP Reduction in C++
```cpp
#include <omp.h>
#include <iostream>
#include <vector>

int main() {
    const size_t N = 100000000;
    std::vector<double> data(N, 1.0);
    double total_sum = 0.0;

    // Line 11: OpenMP directive to parallelize the for loop
    // reduction(+:total_sum) creates thread-private accumulators
    #pragma omp parallel for reduction(+:total_sum) schedule(static)
    for (size_t i = 0; i < N; ++i) {
        total_sum += data[i];
    }

    std::cout << "Computed Sum: " << total_sum << std::endl;
    return 0;
}
```

### Code 2: Intel oneDAL Accelerated Scikit-Learn
```python
# Line 1: Patch scikit-learn before any other sklearn imports
from sklearnex import patch_sklearn
patch_sklearn()

# Line 5: Standard scikit-learn code runs 30x faster automatically
from sklearn.cluster import KMeans
import numpy as np

X = np.load("classification_500k_20feat.npz")['X']
kmeans = KMeans(n_clusters=8, random_state=42, n_init='auto')
kmeans.fit(X)
print("Cluster Centers:", kmeans.cluster_centers_.shape)
```
""", encoding="utf-8")

f2_9 = d_code / "compilation_and_execution_pipeline.md"
f2_9.write_text("""# Day 2: Compilation & Execution Pipeline

## 1. OpenMP Compilation with Intel oneAPI
```bash
# Compile OpenMP C++ with Intel icpx
icpx -qopenmp -O3 -xHost openmp_reduction.cpp -o openmp_reduction

# Execute with 8 threads pinned to physical cores
export OMP_NUM_THREADS=8
export OMP_PROC_BIND=close
./openmp_reduction
```

## 2. MPI Execution with Intel MPI
```bash
# Compile MPI C++ code
mpiicpc -O3 mpi_ring.cpp -o mpi_ring

# Launch across 4 ranks
mpirun -n 4 ./mpi_ring
```
""", encoding="utf-8")

# ==============================================================================
# 5. Lab Challenges & Error Debugging
# ==============================================================================
f2_10 = d_debug / "student_lab_challenges_with_solutions.md"
f2_10.write_text("""# Day 2: Student Lab Challenges with Step-by-Step Solutions

## Challenge 1: Parallel Pi Approximation using Monte Carlo
- **Goal**: Approximate $\\pi$ using OpenMP parallel reduction.
- **Solution**:
```cpp
#include <omp.h>
#include <random>
#include <iostream>

int main() {
    long num_trials = 50000000;
    long inside_circle = 0;

    #pragma omp parallel reduction(+:inside_circle)
    {
        unsigned int seed = 42 + omp_get_thread_num();
        #pragma omp for
        for (long i = 0; i < num_trials; ++i) {
            double x = (double)rand_r(&seed) / RAND_MAX;
            double y = (double)rand_r(&seed) / RAND_MAX;
            if (x * x + y * y <= 1.0) inside_circle++;
        }
    }
    double pi = 4.0 * inside_circle / num_trials;
    std::cout << "Approx Pi: " << pi << std::endl;
}
```

## Challenge 2: MPI Ring Communication
- **Goal**: Rank 0 sends token 100 to Rank 1; Rank 1 increments and sends to Rank 2; last rank sends back to Rank 0.
""", encoding="utf-8")

f2_11 = d_debug / "common_student_syntax_errors_and_5_sec_fixes.md"
f2_11.write_text("""# Day 2: Common Student Errors & 5-Second Instant Fixes

### Error 1: `undefined reference to 'omp_get_thread_num'`
- **Cause**: Student forgot the `-fopenmp` (gcc) or `-qopenmp` (icpx) compiler flag.
- **5-Second Fix**: Add `-qopenmp` to compiler flags.

### Error 2: OpenMP loop gives incorrect sum on every run
- **Cause**: Student omitted the `reduction(+:sum)` clause, causing a race condition on `sum`.
- **5-Second Fix**: Add `reduction(+:sum)` to `#pragma omp parallel for`.

### Error 3: MPI program crashes with `MPI_ERR_TRUNCATE: message truncated`
- **Cause**: The receiving buffer in `MPI_Recv` was smaller than the incoming message sent by `MPI_Send`.
- **5-Second Fix**: Match buffer lengths or query message size first using `MPI_Probe` and `MPI_Get_count`.
""", encoding="utf-8")

print("[SUCCESS] Day 2: Zero-to-God-Tier Master Dossier Built Completely!")
