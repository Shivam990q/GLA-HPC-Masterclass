# ⏱️ DAY 2: 3-HOUR COMPLETE MASTER TRAINER PLAYBOOK
## Traditional Machine Learning & Parallel Computing using Intel oneAPI
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Session Duration:** Exactly 3 Hours (180 Minutes)  
**Official Syllabus Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 🎯 1. Official Syllabus Scope (Day 2 — Strictly Preserved)

The official curriculum specifies **strictly 5 topics for Day 2**:
1. **Parallel Computing** (Amdahl's law, serial bottleneck, task vs data parallelism)
2. **OpenMP for multithreading, MPI for distributed systems**
3. **Data decomposition and synchronization**
4. **Using Intel AI Analytics Toolkit (Optimized Scikit-learn, Pandas, NumPy)**
5. **Intel Extension for Scikit-learn for optimized ML algorithms**

---

## ⏰ 2. Realistic 180-Minute (3-Hour) Delivery Timeline

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                        DAY 2 TIMELINE (TOTAL: 180 MINUTES)                               |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  00:00 - 00:35 (35m) │ PART 1: Parallel Computing Fundamentals                           |
|                      │        (Amdahl's Law, Multi-Core Scaling, Data Decomposition)     |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  00:35 - 01:10 (35m) │ PART 2: Shared-Memory Multithreading with OpenMP                  |
|                      │        (Pragmas, Parallel For, Reductions, icpx -qopenmp)        |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:10 - 01:20 (10m) │ ☕ REJUVENATION BREAK (10 Minutes)                                |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:20 - 01:50 (30m) │ PART 3: Distributed Systems with Message Passing Interface (MPI)  |
|                      │        (Point-to-Point vs Collectives, Ranks, mpirun)             |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:50 - 02:45 (55m) │ PART 4: Intel AI Analytics Toolkit & Scikit-learn Acceleration   |
|                      │        (oneMKL NumPy/Pandas, sklearnex patch, 10x-30x Benchmark)  |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:45 - 03:00 (15m) │ PART 5: Assessment, 25 MCQs & Wrap-Up                             |
|                      │        (5 Evaluated MCQs + Review & Day 3 Preview)                |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 🎙️ 3. Line-by-Line Minute-by-Minute Trainer Delivery Script

### PART 1: Parallel Computing Fundamentals (00:00 - 00:35 | 35 Mins)
- **Concept:** Moore's Law plateau & Amdahl's Law.
- **What Trainer Says:**
  > "Yesterday we mastered Linux and initialized the oneAPI environment. Today on Day 2, we break the serial bottleneck!
  > Why can't CPU manufacturers make a 20 GHz processor? Because of power density and heat dissipation (the Power Wall). 
  > Instead of one ultra-fast core, CPUs now feature 32 to 64 physical cores.
  > But if your Python code is written sequentially, it only runs on ONE single core, leaving 63 cores completely idle!
  > **Amdahl's Law** tells us the theoretical speedup limit:
  > $$\text{Speedup} = \frac{1}{(1 - P) + \frac{P}{N}}$$
  > If 10% of your program is serial ($P = 0.90$), even if you have 10,000 cores, your maximum theoretical speedup can NEVER exceed 10x!
  > This is why data decomposition and parallel programming are mandatory."

---

### PART 2: Shared-Memory Multithreading with OpenMP (00:35 - 01:10 | 35 Mins)
- **Concept:** Fork-Join execution model in C++.
- **What Trainer Says:**
  > "OpenMP is the industry standard for intra-node multithreading.
  > It uses compiler directives (`#pragma omp`).
  > The master thread encounters `#pragma omp parallel for`, forks a team of worker threads across CPU cores, slices loop iterations across cores, and joins back at the barrier.
  > Let's look at **Race Conditions**: If two threads execute `sum += a[i]` at the exact same clock cycle without synchronization, they overwrite each other!
  > To fix this, OpenMP provides the **reduction clause**:
  > `#pragma omp parallel for reduction(+:sum)`
  > Each thread maintains a private accumulator, and OpenMP safely combines them at the end."

---

### ☕ BREAK (01:10 - 01:20 | 10 Minutes)

---

### PART 3: Distributed Systems with MPI (01:20 - 01:50 | 30 Mins)
- **Concept:** Scaling across multiple physically separate servers.
- **What Trainer Says:**
  > "OpenMP only works on a single server where cores share the same RAM.
  > What if your computation spans 10 different servers across a datacenter rack?
  > They do NOT share RAM. Here, we must use **MPI (Message Passing Interface)**.
  > Every process has a unique identity called a **Rank** (`0, 1, 2, ... N-1`).
  > Processes exchange data across the network using:
  > - Point-to-Point: `MPI_Send` and `MPI_Recv`
  > - Collectives: `MPI_Bcast` (Broadcast to all), `MPI_Scatter` (divide data among ranks), and `MPI_Reduce` (gather and sum)."

---

### PART 4: Intel AI Analytics Toolkit & oneDAL Acceleration (01:50 - 02:45 | 55 Mins)
- **Concept:** Zero-code-change Scikit-Learn acceleration.
- **What Trainer Says:**
  > "Standard Python Scikit-Learn is single-threaded and runs slow on large datasets.
  > **Intel Extension for Scikit-learn (`sklearnex`)** dynamically patches algorithms (k-Means, SVM, PCA, Random Forest) through Intel oneDAL (Data Analytics Library).
  > Look at the code change required:
  > ```python
  > from sklearnex import patch_sklearn
  > patch_sklearn()
  > import sklearn
  > ```
  > That's it! Two lines of code.
  > Under the hood, oneDAL vectorizes computations across AVX-512 registers and multithreads across all available Xeon cores, delivering a massive 15x to 30x speedup!"
- **Hands-on Student Action:** Run k-Means clustering benchmark on 500,000 samples comparing stock vs patched Scikit-Learn.

---

### PART 5: Assessment & Wrap-Up (02:45 - 03:00 | 15 Mins)
- Review 5 core MCQs and connect to Day 3 (Deep Learning & Slurm).
