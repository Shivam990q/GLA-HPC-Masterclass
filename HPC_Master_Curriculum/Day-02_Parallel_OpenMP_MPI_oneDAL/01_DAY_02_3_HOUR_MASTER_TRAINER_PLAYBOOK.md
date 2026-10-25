# ⏱️ DAY 2: 3-HOUR COMPLETE MASTER TRAINER PLAYBOOK
## Traditional Machine Learning & Parallel Computing using Intel oneAPI
**Course Code:** `GLA-HPC-BCSG701` | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Session:** Day 2 (Strictly 3 Hours / 180 Minutes)  
**Official Syllabus Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 🎯 1. Official Syllabus Scope (Day 2 Topics)
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
|  00:00 - 00:30 (30m) │ PART 1: Parallel Computing Fundamentals                           |
|                      │        (Amdahl's Law, Moore's Law Wall, Task vs Data Parallelism) |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  00:30 - 01:10 (40m) │ PART 2: Shared-Memory Multithreading with OpenMP                  |
|                      │        (Fork-Join, Pragmas, Reduction Clause, False Sharing Demo) |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:10 - 01:20 (10m) │ ☕ REJUVENATION BREAK (10 Minutes)                                |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:20 - 01:50 (30m) │ PART 3: Distributed Systems with MPI                              |
|                      │        (Ranks, Communicators, Point-to-Point vs Collective Trees) |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:50 - 02:40 (50m) │ PART 4: Intel AI Analytics Toolkit & oneDAL ML Acceleration      |
|                      │        (NumPy MKL, Modin Pandas, sklearnex patch_sklearn 20x demo)|
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:40 - 03:00 (20m) │ PART 5: Student Coding Challenge, 25 MCQs & Wrap-Up               |
|                      │        (Live K-Means & Random Forest Benchmark, Q&A, Day 3 Lead)  |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 🎙️ 3. Line-by-Line Minute-by-Minute Trainer Delivery Script

### PART 1: Parallel Computing Fundamentals (00:00 - 00:30 | 30 Mins)
* **Slide Alignment:** Day 2 Slide Deck (Slides 1–5: Introduction to Parallelism & Amdahl's Law).
* **Concept:** Breaking the serial bottleneck; mathematical bounds on multi-core speedup.
* **Trainer Script:**
  > "Good morning, class! Yesterday we mastered the Linux operating system, remote SSH keys, and initialized our Intel oneAPI toolchains.
  > Today on Day 2, we tackle the core physics of why High Performance Computing exists: **breaking the serial bottleneck**.
  > Why can't Intel build a single 25 GHz CPU core? Because of the **Power Wall** ($P = C \cdot V^2 \cdot f$)—a chip running at 25 GHz would melt its silicon package.
  > Instead of one ultra-fast core, modern Intel Xeon processors feature **32, 64, or 128 physical cores**.
  > But here is the catch: if you write standard serial Python or C++ code, your program runs on **ONLY ONE CORE**, leaving the other 63 cores completely idle!
  > Look at **Amdahl's Law**:
  > $$\text{Speedup} = \frac{1}{(1 - P) + \frac{P}{N}}$$
  > If 10% of your program is serial ($1 - P = 0.10$), even if I give you 10,000 Xeon cores ($N \to \infty$), your theoretical maximum speedup can **NEVER exceed 10x**!
  > That is why we must learn data decomposition and parallel programming."

---

### PART 2: Shared-Memory Multithreading with OpenMP (00:30 - 01:10 | 40 Mins)
* **Slide Alignment:** Day 2 Slide Deck (Slides 6–10: OpenMP Fork-Join & Memory Primitives).
* **Concept:** Fork-join execution, compiler pragmas, reduction clauses, and false sharing.
* **Trainer Script:**
  > "Now let's see how we parallelize code on a single multi-core server using **OpenMP**.
  > OpenMP uses simple compiler directives: `#pragma omp`.
  > In the **Fork-Join Model**, the program begins as a single master thread. When it hits `#pragma omp parallel for`, the master thread **forks** a team of worker threads across CPU cores.
  > But watch out for **Race Conditions**! If two threads execute `total_sum += a[i]` simultaneously, they overwrite each other's register values, corrupting the final answer.
  > To solve this with zero locking overhead, we use the **reduction clause**:
  > `#pragma omp parallel for reduction(+:total_sum)`
  > Each thread gets a private accumulator in its L1 cache, and OpenMP combines them in a tree reduction at the end.
  > Now look at **False Sharing**: if two threads write to adjacent array elements that sit on the same 64-byte cache line, the CPU cache coherence protocol (MESI) bounces that cache line back and forth between cores, dropping performance by 80x!"
* **Live Whiteboard Sketch:** Draw a 64-byte cache line containing `array[0]` (Core 0) and `array[1]` (Core 1) and show the bus invalidation cycle.

---

### ☕ BREAK (01:10 - 01:20 | 10 Minutes)

---

### PART 3: Distributed Systems with MPI (01:20 - 01:50 | 30 Mins)
* **Slide Alignment:** Day 2 Slide Deck (Slides 11–14: Distributed Systems & MPI Architecture).
* **Concept:** Message passing across independent servers, ranks, point-to-point, and collective trees.
* **Trainer Script:**
  > "Welcome back. OpenMP works on a single computer where all cores share the same RAM.
  > But what happens when your dataset is 5 Terabytes and exceeds one server's memory?
  > You must distribute the job across multiple separate compute nodes connected by an InfiniBand network.
  > These nodes **do not share memory**. Here, we use **MPI (Message Passing Interface)**.
  > In MPI:
  > - Each process has its own private memory and a unique ID called a **Rank** (`0, 1, 2, ... N-1`).
  > - Point-to-Point: `MPI_Send` and `MPI_Recv` between two ranks.
  > - Collectives: `MPI_Bcast` (one sends to all), `MPI_Scatter` (splits data among ranks), and `MPI_Reduce` (aggregates partial sums from all ranks into Rank 0).
  > Today we demonstrate how 4 simulated MPI ranks compute a distributed sum reduction in parallel!"

---

### PART 4: Intel AI Analytics Toolkit & Scikit-learn Acceleration (01:50 - 02:40 | 50 Mins)
* **Slide Alignment:** Day 2 Slide Deck (Slides 15–20: AI Kit, oneDAL, and sklearnex).
* **Concept:** Zero-code-change Scikit-learn acceleration via Intel oneDAL dynamic monkey patching.
* **Trainer Script:**
  > "Now we transition into the AI layer.
  > Standard Scikit-learn is single-threaded and struggles on large datasets because Python is bound by the Global Interpreter Lock (GIL).
  > Intel created the **AI Analytics Toolkit** containing **Intel Extension for Scikit-learn (`sklearnex`)**.
  > Under the hood, `sklearnex` calls **Intel oneDAL**—a high-performance C++ library compiled with AVX-512 vectorization and cache-conscious matrix operations.
  > How do you use it? Look at these two lines of code:
  > ```python
  > from sklearnex import patch_sklearn
  > patch_sklearn()
  > ```
  > That's it! Zero changes to your Scikit-learn model code.
  > When you call `kmeans.fit(X)` or `RandomForestClassifier.fit(X)`, it executes in parallel across all 64 Xeon cores.
  > In our live lab right now, we will train a K-Means model on **500,000 samples with 32 features** and compare stock Scikit-learn vs. Intel oneDAL. You will see a **15× to 35× measured speedup** right on your screen!"

---

### PART 5: Student Hands-On Challenge, 25 MCQs & Wrap-Up (02:40 - 03:00 | 20 Mins)
* **Activities:**
  1. Have students run the K-Means and Random Forest benchmark in their Colab notebook.
  2. Ask students to calculate their measured speedup and report it in the chat.
  3. Review the 5 core MCQs from [`03_DAY_02_STUDENT_CHEATSHEET_AND_MCQS.md`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/03_DAY_02_STUDENT_CHEATSHEET_AND_MCQS.md).
  4. **Day 3 Teaser:** *"Tomorrow on Day 3, we leave traditional ML and enter Deep Learning on HPC with Intel-optimized TensorFlow, oneDNN, Slurm job scheduling, and distributed training with Horovod across GPUs and Habana Gaudi!"*

---
**Playbook Status:** 100% Complete & Verified | GLA University HPC Masterclass Day 2
