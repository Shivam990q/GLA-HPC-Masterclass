# 🥋 DAY 2: KANTHAST MASTER TRAINER WAR-ROOM RUNBOOK & SYNC MAP
## Complete Step-by-Step Delivery Playbook, Presentation Sync, Trainer Division of Labor & Hands-On Lab Defense
**Institution:** Department of Computer Engineering & Applications, GLA University, Mathura (AB12 Building)  
**Alliance:** Intel & NEC Supercomputing Alliance × Edulateral Foundation  
**Morning Lead (Trainer 1):** HPC & Systems Lead (Parallel Computing, Amdahl's Law, OpenMP, MPI)  
**Afternoon Lead (Trainer 2):** Applied AI/ML Acceleration Lead — Shivam Gupta (Intel AI Analytics Toolkit, oneDAL, `sklearnex`, Accelerated ML)  
**Coordinator:** Pedina Sreeja (GLA University Training Helper)  
**Official Curriculum Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)  
**Morning Master Presentation:** [`Day-02_Master_Presentation.pptx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/MAIN_PRESENTATIONS/Day-02_Traditional_Machine_Learning_using_oneAPI/Day-02_Master_Presentation.pptx)  
**Afternoon Master Presentation (Trainer 2):** [`Day-02_Master_Presentation_Intel_AI_Analytics_and_oneDAL.pptx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/Day-02_Master_Presentation_Intel_AI_Analytics_and_oneDAL.pptx)  
**Dedicated Afternoon Training Module:** [`INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE)  
**Day 2 Google Colab Lab Notebooks:**  
- Top-Level Root: [`Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb)  
- Full Parallel HPC Lab: [`Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb)  

---

## 🎯 EXECUTIVE GROUND TRUTH & DAY 2 BOUNDARIES

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                           STRICT SYLLABUS BOUNDARY INVARIANT                             |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  IN SCOPE TODAY (DAY 2 ONLY - 5 OFFICIAL TOPICS):                                        |
|  1. Parallel Computing (Amdahl's Law, serial bottleneck, task vs data parallelism)       |
|  2. OpenMP for multithreading (Fork-join model, reduction clause, false sharing physics)  |
|  3. Distributed Systems with MPI (Ranks, communicators, point-to-point, collective trees)|
|  4. Using Intel AI Analytics Toolkit (NumPy MKL, Modin Pandas, oneDAL acceleration)      |
|  5. Intel Extension for Scikit-learn (patch_sklearn() dynamic monkey-patching, 10x-100x)  |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  STRICT DIVISION OF LABOR (TRAINER 1 VS TRAINER 2):                                      |
|  • TRAINER 1 (MORNING 3 HOURS | 09:30 AM - 12:30 PM):                                    |
|    - Heavy HPC Architecture & Theoretical Parallel Foundations                           |
|    - Mathematical derivation of Amdahl's Law and Gustafson's Law                         |
|    - OpenMP shared-memory multithreading & compiler pragmas                              |
|    - False sharing physics & 64-byte L1 cache line padding                               |
|    - MPI distributed message passing, communicators, ranks, and tree reductions          |
|                                                                                          |
|  • TRAINER 2 / SHIVAM GUPTA (AFTERNOON 3 HOURS | 01:30 PM - 04:30 PM):                   |
|    - Applied Python, AI Analytics Toolkit & Machine Learning Acceleration                |
|    - Located in: INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/                  |
|    - Intel oneDAL architecture & Cython/C++ dynamic dispatch engine                      |
|    - 2-line zero-code-change drop-in monkey-patching (patch_sklearn())                   |
|    - Benchmarking 5 classic ML algorithms: KMeans, PCA, Random Forest, KNN, and SVM      |
|    - Hands-on Google Colab lab execution with 500,000 samples and live student metrics    |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  STRICTLY OUT OF SCOPE TODAY (DO NOT PRE-EMPT):                                          |
|  • Day 3: Deep Learning on HPC, TensorFlow-MKL, PyTorch oneDNN, Slurm batch scheduling   |
|  • Day 4: Distributed AI Training with Horovod, Intel VTune profiler, roofline analysis  |
|  • Day 5: Generative AI, LLM fine-tuning on Habana Gaudi, OpenVINO inference deployment  |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## ⏰ THE GRAND OPERATIONAL TIMELINE (09:30 AM – 05:00 PM)

*Synchronized with Pedina Sreeja's WhatsApp schedule (Car pickup <09:30 AM from Guest House to AB12 Building)*

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                             DAY 2 MASTER TIMELINE MAP                                    |
+──────────────────────────┬───────────────────────────────────────────────────────────────+
| 09:00 AM - 09:30 AM      | Guest House to AB12 Transit, Lab Preflight, Projector & Wi-Fi |
+──────────────────────────┼───────────────────────────────────────────────────────────────+
| 🌅 MORNING SESSION       | LEAD: TRAINER 1 | CO-PILOT: TRAINER 2 (SHIVAM GUPTA)          |
| 09:30 AM - 10:15 AM (45m)| BLOCK 1: Parallel Computing Fundamentals & Amdahl's Law        |
| 10:15 AM - 11:00 AM (45m)| BLOCK 2: Shared-Memory Multithreading with OpenMP              |
| 11:00 AM - 11:10 AM (10m)| ☕ Bio & Rejuvenation Break                                   |
| 11:10 AM - 11:45 AM (35m)| BLOCK 3: Distributed Systems with MPI                          |
| 11:45 AM - 12:15 PM (30m)| BLOCK 4: Data Decomposition & Synchronization Concepts         |
| 12:15 PM - 12:30 PM (15m)| BLOCK 5: Morning Review, 5 Socratic Checkpoint MCQs & Handoff  |
+──────────────────────────┼───────────────────────────────────────────────────────────────+
| 🍱 12:30 PM - 01:30 PM   | LUNCH BREAK (60 Mins) — Trainer Handoff, Colab Pre-Warming    |
+──────────────────────────┼───────────────────────────────────────────────────────────────+
| 💻 AFTERNOON SESSION     | LEAD: TRAINER 2 (SHIVAM GUPTA) | LAB CO-PILOT: TRAINER 1      |
| 01:30 PM - 02:15 PM (45m)| BLOCK 1: Intel AI Analytics Toolkit Architecture & NumPy MKL  |
| 02:15 PM - 02:45 PM (30m)| BLOCK 2: Intel oneDAL & The 2-Line Dynamic Patch Revolution   |
| 02:45 PM - 03:45 PM (60m)| BLOCK 3: Hands-On Big Data ML Lab Drill (500k Sample Benchmarks)|
| 03:45 PM - 04:15 PM (30m)| BLOCK 4: Multi-Core Scaling, Thread Saturation & Intel Modin  |
| 04:15 PM - 04:45 PM (30m)| 🎯 25 EVALUATED CHECKPOINT MCQS & 22-POINT CHECKLIST SIGN-OFF |
| 04:45 PM - 05:00 PM (15m)| Day 2 Wrap-up, Q&A, and Day 3 Preview (Deep Learning & Slurm) |
+──────────────────────────┴───────────────────────────────────────────────────────────────+
```

---

## 🤝 TRAINER DIVISION OF LABOR & FORMAL HANDOFF PROTOCOL

### Why This Division is Optimal:
1. **Trainer 1 (Morning HPC Systems Lead):**
   - Takes the heavy, mathematically rigorous, compiled C++ HPC systems concepts (Amdahl's law, OpenMP thread mechanics, compiler optimization flags, MPI communicators, point-to-point and collective communications).
   - Establishes the hard-science foundation of multi-core parallelism and distributed clusters.
2. **Trainer 2 / Shivam Gupta (Afternoon Applied AI/ML Acceleration Lead):**
   - Takes the applied, high-impact, visual, interactive Python and Machine Learning acceleration.
   - Operates inside the self-contained module: [`INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE).
   - Easily sustains 3 full hours with engaging live screen benchmarks, interactive student Colab activities, zero-friction monkey patching demonstrations, and immediate 10x-100x speedup metrics.

### Formal 12:30 PM Lunch Handoff Protocol:
At 12:25 PM, Trainer 1 concludes the morning review and initiates the verbal handoff:
> **Trainer 1:** *"This morning, we mastered the core physics of parallel computing. We saw how OpenMP scales across threads on a single node, and how MPI communicates across independent cluster nodes. But here is the multi-million dollar industry question: When you enter corporate data science teams, are you going to rewrite all your scikit-learn machine learning algorithms from scratch in C++ and MPI? Absolutely not! When you return from lunch at 01:30 PM, Trainer Shivam will demonstrate how Intel gives you that exact same C++ supercomputing speed directly inside Python using just two lines of code via the Intel AI Analytics Toolkit and oneDAL. Enjoy your lunch, and get ready for live benchmarks!"*

---

## 🧠 THE "KANTHASTH" 7-PILLAR MEMORIZATION ENGINE
*(Both trainers must have these 7 core pillars committed to memory — instant recall, zero hesitation)*

### 1. Amdahl's Law vs Gustafson's Law
* **Amdahl's Law (Fixed Workload / Strong Scaling):**
  $$\text{Speedup} = \frac{1}{(1 - P) + \frac{P}{N}}$$
  - Where $P$ is the parallel fraction and $N$ is the number of processing cores.
  - As $N \to \infty$, the maximum theoretical speedup is capped at $\frac{1}{1 - P}$.
  - *Example:* If $P = 0.90$ (90% parallel), even on a 100,000-core supercomputer, max speedup can **never exceed 10x**!
* **Gustafson's Law (Scaled Workload / Weak Scaling):**
  $$\text{Speedup} = (1 - P) + P \cdot N$$
  - Assumes problem size scales with available processing cores.

### 2. OpenMP Shared-Memory Fork-Join Model & Reductions
* **Execution Model:** Master thread executes sequentially until encountering an OpenMP parallel directive (`#pragma omp parallel`), where it **forks** a team of worker threads. At the end of the region, threads synchronize and **join** back into the master.
* **Race Condition Hazard:** When multiple threads update a shared variable concurrently (`total += x`), CPU registers overwrite each other without atomicity.
* **The Reduction Clause:** `#pragma omp parallel for reduction(+:total)` allocates private thread-local accumulators in L1 cache and performs an $O(\log N)$ tree reduction at the join barrier with zero lock contention.

### 3. False Sharing Physics & 64-Byte Cache Line Padding
* **Physical Cause:** Two or more CPU cores concurrently write to independent variables located on the **same 64-byte L1 cache line**.
* **MESI Protocol Invalidation:** The hardware cache coherence protocol (Modified, Exclusive, Shared, Invalid) detects writes and marks the line Invalid across other cores. The cache line bounces between cores over the interconnect bus (80ns latency per bounce vs 1ns L1 access), degrading performance by 4x to 8x.
* **The Fix:** Memory alignment and padding via `alignas(64)` in C++ or structuring data so each thread operates on an isolated cache line.

### 4. MPI Architecture: Ranks, Communicators & Collective Trees
* **Distributed Memory Model:** Each MPI process has its own private virtual address space and separate physical RAM. Processes communicate exclusively via explicit network message packets.
* **Core Primitives:**
  - `MPI_COMM_WORLD`: Default communicator encompassing all running processes.
  - `Rank`: Unique zero-based integer ID (`0, 1, ... N-1`). Rank 0 typically acts as the coordinator/master.
  - Point-to-Point: `MPI_Send` and `MPI_Recv` (directed buffer copy between two ranks).
  - Collectives: `MPI_Bcast` (one-to-all broadcast), `MPI_Scatter` (partition array chunks across ranks), `MPI_Gather` (recombine chunks), `MPI_Reduce` (distributed tree reduction into Rank 0), `MPI_Allreduce` (reduce and broadcast to all ranks).

### 5. Intel AI Analytics Toolkit Architecture
* **The Problem:** Standard Python data science libraries (Scikit-learn, NumPy, Pandas) suffer from the Global Interpreter Lock (GIL), unvectorized loops, and single-threaded default routines.
* **The Solution:** A drop-in ecosystem pre-compiled with:
  1. **Intel oneMKL:** Optimized Basic Linear Algebra Subprograms (BLAS), LAPACK, and FFTW utilizing AVX-512 and AMX hardware instructions.
  2. **Intel oneDAL:** Data Analytics Acceleration Library written in native C++ for high-throughput machine learning.
  3. **Intel Modin:** Distributed Pandas running on Ray/Dask backends to utilize all CPU cores automatically.

### 6. Intel Extension for Scikit-learn (`sklearnex`) Dynamic Monkey-Patching
* **The 2-Line Revolution:**
  ```python
  from sklearnex import patch_sklearn
  patch_sklearn()
  ```
* **How It Works Under the Hood:**
  - `patch_sklearn()` dynamically alters Python's runtime `sys.modules` table.
  - When `from sklearn.cluster import KMeans` is imported, it silently redirects the class binding to `daal4py.sklearn.cluster.KMeans`.
  - The Python objects serialize NumPy arrays directly into native memory buffers without copying, invoking oneDAL's multi-threaded C++ engine.
  - If an algorithm or hyperparameter configuration is unsupported by oneDAL, it seamlessly falls back to standard stock Scikit-learn with zero errors.

### 7. 5 Key Accelerated Machine Learning Algorithms & Speedup Ratios
| Algorithm | Stock Scikit-Learn Bottleneck | Intel oneDAL Optimization | Measured Speedup Range |
| :--- | :--- | :--- | :--- |
| **K-Means Clustering** | Single-threaded distance matrix calculation | Lloyd's algorithm with SIMD vectorization & blocked centroids | **15× to 35×** |
| **Principal Component Analysis (PCA)** | SVD computation stalled on memory bandwidth | Blocked covariance QR factorization via Intel oneMKL LAPACK | **10× to 25×** |
| **Random Forest (Classifier/Regressor)** | GIL contention during decision tree splitting | Lock-free histogram-based feature splitting across threads | **8× to 20×** |
| **K-Nearest Neighbors (KNN)** | Brute-force Euclidean distance loops | kd-tree spatial indexing with AVX-512 distance kernels | **12× to 40×** |
| **Support Vector Machines (SVM/SVC)** | Quadratic $O(N^2)$ SMO solver stalls on large data | Fast SMO solver with cache-conscious kernel matrix tiling | **20× to 100×** |

---

## 📽️ PRESENTATION SYNC: SLIDE-BY-SLIDE DELIVERY SCRIPT

### 🌅 MORNING SESSION (TRAINER 1: PARALLEL COMPUTING, OPENMP & MPI)
*Slide Deck:* [`Day-02_Master_Presentation.pptx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/MAIN_PRESENTATIONS/Day-02_Traditional_Machine_Learning_using_oneAPI/Day-02_Master_Presentation.pptx)

#### 🔹 SLIDE 1: Title & Day 2 Architecture
* **Time:** 09:30 AM – 09:35 AM (5 Mins) | **Speaker:** Trainer 1
* **Script:**
  > "Good morning, class! Welcome to Day 2 of our Intel & NEC Supercomputing Masterclass.
  > Yesterday, we mastered the Linux OS, SSH remote connectivity, and initialized the oneAPI environment.
  > Today, we tackle the fundamental physics of supercomputing: **Parallel Computing, OpenMP, MPI, and Machine Learning Acceleration**.
  > By the end of today, you will know how to take serial code, parallelize it across multiple CPU cores, scale it across cluster nodes, and accelerate Python machine learning by over 20x!"

#### 🔹 SLIDE 2: The Serial Bottleneck & Amdahl's Law
* **Time:** 09:35 AM – 10:15 AM (40 Mins) | **Speaker:** Trainer 1
* **Script:**
  > "Why can't we just make a single CPU core run at 100 GHz? Because of the Power Wall.
  > Instead, Intel gives us 64 or 128 cores per server.
  > But if your program is serial, 63 cores sit completely idle.
  > Look at Amdahl's Law: $S = \frac{1}{(1-P) + P/N}$.
  > If 10% of your code is strictly serial, your maximum possible speedup can NEVER exceed 10x, even with an infinite number of cores!
  > Our entire engineering objective today is maximizing the parallel fraction $P$."
* **Whiteboard Action:** Derive Amdahl's formula on the board for $P = 0.50$, $P = 0.90$, and $P = 0.99$.

#### 🔹 SLIDE 3: OpenMP & Shared-Memory Multithreading
* **Time:** 10:15 AM – 11:00 AM (45 Mins) | **Speaker:** Trainer 1
* **Script:**
  > "On a single machine where all cores share RAM, we use OpenMP.
  > Look at the Fork-Join model: The master thread forks worker threads using `#pragma omp parallel for`.
  > But watch out for Race Conditions! If two threads write to `sum += a[i]`, data is corrupted.
  > We solve this using the `reduction(+:sum)` clause.
  > Now look at False Sharing: When two threads write to adjacent array elements residing on the same 64-byte cache line, CPU cache coherence bounces the line between cores, destroying your speedup. We fix this by padding data with `alignas(64)`."
* **Whiteboard Action:** Draw the 64-byte cache line and MESI bus invalidation bounce.

#### ☕ 11:00 AM – 11:10 AM: REJUVENATION BREAK (10 Mins)

#### 🔹 SLIDE 4: Distributed Computing with MPI
* **Time:** 11:10 AM – 11:45 AM (35 Mins) | **Speaker:** Trainer 1
* **Script:**
  > "When your dataset exceeds the RAM of a single machine, we scale out to multiple nodes using MPI.
  > In MPI, processes do not share memory. Each process has an isolated rank (`0, 1, 2, ... N-1`).
  > We communicate using point-to-point calls (`MPI_Send`/`MPI_Recv`) and collective trees (`MPI_Scatter` to distribute work, `MPI_Reduce` to aggregate results into Rank 0)."

#### 🔹 SLIDE 5: Morning Review & 5 Checkpoint Questions
* **Time:** 11:45 AM – 12:30 PM (45 Mins) | **Speaker:** Trainer 1 & Trainer 2
* **5 Questions Conducted Live:**
  1. *What is the maximum speedup possible for a program that is 80% parallel?* (Answer: $1 / (1 - 0.8) = 5\times$).
  2. *Which OpenMP clause eliminates race conditions on sum accumulators without locks?* (Answer: `reduction(+:sum)`).
  3. *What hardware structure causes false sharing when threads write to adjacent indices?* (Answer: 64-byte L1 CPU cache line).
  4. *What is the default MPI communicator encompassing all processes?* (Answer: `MPI_COMM_WORLD`).
  5. *Which collective operation distributes equal array chunks across all ranks?* (Answer: `MPI_Scatter`).
* **Verbal Handoff to Trainer 2 (12:25 PM):** Trainer 1 introduces Trainer 2 for the afternoon applied ML module.

---

### 💻 AFTERNOON SESSION (TRAINER 2 / SHIVAM GUPTA: INTEL AI ANALYTICS & ACCELERATED ML)
*Slide Deck:* [`INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/Day-02_Master_Presentation_Intel_AI_Analytics_and_oneDAL.pptx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/Day-02_Master_Presentation_Intel_AI_Analytics_and_oneDAL.pptx)  
*Colab Notebook:* [`Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb)

#### 🔹 SLIDE 1–3: Title & The Traditional ML Crisis on Supercomputers
* **Time:** 01:30 PM – 01:45 PM (15 Mins) | **Speaker:** Shivam Gupta
* **Script:**
  > "Welcome back, everyone! This morning, you saw how supercomputer hardware operates at the C++ and MPI level.
  > Now, let's step into the shoes of an Enterprise AI Engineer.
  > You build a machine learning model using Python's standard Scikit-learn. On your laptop with 5,000 rows, it runs in 2 seconds.
  > But when you deploy it to a cluster with 500,000 or 10,000,000 rows, what happens?
  > The training job spins for 45 minutes! Python's Global Interpreter Lock (GIL) freezes multi-threading, and your 64-core Intel Xeon processor sits at 1.5% utilization!
  > Over the next 3 hours, we will eliminate this bottleneck completely. You will learn how to unlock the full power of your CPU without rewriting a single line of your scikit-learn model code!"

#### 🔹 SLIDE 4–7: Intel AI Analytics Toolkit & NumPy MKL Under the Hood
* **Time:** 01:45 PM – 02:15 PM (30 Mins) | **Speaker:** Shivam Gupta
* **Script:**
  > "Look at the software stack: Standard NumPy uses reference BLAS, which performs matrix multiplications in basic scalar loops.
  > Intel AI Analytics Toolkit replaces this with **Intel oneMKL**.
  > When you run `np.dot(A, B)`, oneMKL uses AVX-512 512-bit registers to calculate 8 double-precision numbers per CPU clock cycle!
  > In our first live demo, we will multiply two 2000x2000 matrices and verify that Intel MKL outperforms reference implementations by 8x."
* **Screen Projection Action:** Open terminal, run `python 04_STUDENT_PRACTICE_SCRIPTS/02_numpy_mkl_verification.py`.

#### 🔹 SLIDE 8–12: The 2-Line Dynamic Patch Revolution (`patch_sklearn()`)
* **Time:** 02:15 PM – 02:45 PM (30 Mins) | **Speaker:** Shivam Gupta
* **Script:**
  > "How do we accelerate Scikit-learn?
  > Look at your screen:
  > ```python
  > from sklearnex import patch_sklearn
  > patch_sklearn()
  > ```
  > That's it! Two lines of code at the top of your script.
  > How does this work? It is called **dynamic monkey-patching**.
  > At runtime, `patch_sklearn()` intercepts Python's `sys.modules`. When you import `KMeans` or `RandomForestClassifier`, Python dynamically loads Intel oneDAL's compiled C++ engine.
  > Zero code changes. Zero algorithm rewriting. 100% mathematical parity!"
* **Whiteboard Action:** Draw the Dynamic Dispatch Redirection diagram (Python API ──► sklearnex wrapper ──► Cython C-Bridge ──► oneDAL C++ Engine ──► AVX-512 Silicon).

#### 🔹 SLIDE 13–18: Benchmarking 5 Classic ML Algorithms on 500k Samples
* **Time:** 02:45 PM – 03:45 PM (60 Mins) | **Speaker:** Shivam Gupta
* **Classroom Activity:** Students open [`Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb) on their laptops.
* **Script:**
  > "Everyone open Section 4 in your Colab notebook. We are generating 500,000 synthetic samples with 32 features.
  > We will benchmark 5 core algorithms:
  > 1. **K-Means Clustering:** Watch stock scikit-learn take ~18.5 seconds. Now run the patched oneDAL cell... boom! ~0.9 seconds! That is a **20.5x measured speedup**!
  > 2. **PCA:** Watch oneDAL compute covariance matrices with SIMD vectorization: 12x speedup!
  > 3. **Random Forest:** Notice how oneDAL constructs decision trees across all CPU cores without GIL lock contention: 10x speedup!
  > 4. **KNN:** Notice how Euclidean distance searches drop from 30 seconds to under 2 seconds!
  > 5. **SVM:** Notice how oneDAL's cache-tiled SMO solver handles thousands of support vectors!"
* **Live Classroom Poll:** Have students type their measured speedup numbers in the lab chat.

#### 🔹 SLIDE 19–22: Multi-Core Thread Scaling & Intel Modin
* **Time:** 03:45 PM – 04:15 PM (30 Mins) | **Speaker:** Shivam Gupta
* **Script:**
  > "Does adding more threads always give linear speedup?
  > Look at thread scaling: When we go from 1 thread to 2, 4, 8, and 16 threads, speedup increases, but then flattens due to memory bus saturation and Amdahl's serial fraction.
  > Now look at Pandas: standard Pandas is single-threaded. Intel Modin (`import modin.pandas as pd`) automatically distributes dataframe operations across all available cores."

#### 🔹 SLIDE 23–25: Review, 25 Assessment MCQs & Daily Wrap-Up
* **Time:** 04:15 PM – 05:00 PM (45 Mins) | **Speaker:** Shivam Gupta & Trainer 1
* **Activity:** Administer the 25 Evaluated Checkpoint MCQs from [`05_MCQ_ASSESSMENT_BANK.md`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/05_MCQ_ASSESSMENT_BANK.md).
* **Closing Teaser for Day 3:**
  > "Congratulations! Today you mastered both sides of supercomputing: raw C++ OpenMP/MPI parallelism with Trainer 1, and production Python machine learning acceleration with oneDAL.
  > Tomorrow on Day 3, we enter Deep Learning on HPC! We will explore Intel-optimized TensorFlow, PyTorch with oneDNN, Habana Gaudi 2/3 tensor processor cores, and how cluster workload managers like Slurm schedule multi-node training jobs. Be here at 09:30 AM sharp!"

---

## 💻 AFTERNOON HANDS-ON LAB EXECUTION PHASES (3 HOURS)

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                    AFTERNOON HANDS-ON LAB EXECUTION PHASES (3 HOURS)                     |
+──────────────────────────────────────────────────────────────────────────────────────────+
| 01:30 PM - 02:00 PM (30m) │ Phase 1: Environment Readiness & Silicon Introspection       |
| 02:00 PM - 02:30 PM (30m) │ Phase 2: NumPy MKL vs Stock BLAS Matrix Multiply Benchmark   |
| 02:30 PM - 03:30 PM (60m) │ Phase 3: The 2-Line Dynamic Patch Revolution & 5 ML Demos    |
| 03:30 PM - 04:15 PM (45m) │ Phase 4: Student Lab Drills (6 Automation Scripts Execution) |
| 04:15 PM - 04:45 PM (30m) │ Phase 5: 25 Evaluated MCQs & 22-Point Checklist Sign-Off     |
| 04:45 PM - 05:00 PM (15m) │ Phase 6: Daily Wrap-Up, Q&A, and Day 3 Strategic Bridge      |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

### Phase 1: Environment Readiness & Silicon Introspection
Students verify that Intel Extension for Scikit-learn is correctly installed:
```bash
python -c "import sklearnex; print('sklearnex version:', sklearnex.__version__)"
python -c "import daal4py; print('daal4py status: operational')"
```

### Phase 2: NumPy MKL Matrix Multiply Verification
Students execute [`02_numpy_mkl_verification.py`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/04_STUDENT_PRACTICE_SCRIPTS/02_numpy_mkl_verification.py):
```bash
python 04_STUDENT_PRACTICE_SCRIPTS/02_numpy_mkl_verification.py
```
*Expected Output:* Confirms `mkl_rt` backend and reports GFLOPS achieved during 2000x2000 matrix multiplication.

### Phase 3: The 2-Line Dynamic Patch Revolution
Students run the dynamic patching inspection script:
```python
from sklearnex import patch_sklearn, unpatch_sklearn
# Show patching in action
patch_sklearn()
from sklearn.cluster import KMeans
print("Patched KMeans:", KMeans.__module__) # Output: daal4py.sklearn.cluster.k_means

unpatch_sklearn()
from sklearn.cluster import KMeans
print("Unpatched KMeans:", KMeans.__module__) # Output: sklearn.cluster._kmeans
```

### Phase 4: Student Lab Drills (500,000 Sample Benchmarks)
Students execute the automated test runner:
```bash
bash 04_STUDENT_PRACTICE_SCRIPTS/run_all_benchmarks.sh
```
Or run the master benchmark suite:
```bash
python 04_STUDENT_PRACTICE_SCRIPTS/06_full_benchmark_suite.py
```

---

## 🛠️ TOP 5 STUDENT GOTCHAS & 30-SECOND RAPID FIXES

| Issue Encountered | Why It Happened | 30-Second Trainer Fix |
| :--- | :--- | :--- |
| **1. `patch_sklearn()` shows 1.0x speedup** | Student called `patch_sklearn()` **AFTER** importing `from sklearn.cluster import KMeans` | Move `from sklearnex import patch_sklearn; patch_sklearn()` to **Lines 1 & 2** of the script before any `sklearn` imports! |
| **2. Colab crashes with "Out of Memory" (OOM)** | Dataset size exceeded free RAM (e.g., trying to generate 10,000,000 samples with 128 features) | Reduce sample count to `500,000` samples with `32` features, or use `dtype=np.float32` instead of `float64`. |
| **3. `daal4py` fallback warning in console** | Used an unsupported hyperparameter (e.g., `algorithm='full'` in KMeans instead of `algorithm='lloyd'`) | Revert to standard default parameters (`algorithm='lloyd'`); oneDAL accelerates default Scikit-learn configurations. |
| **4. OpenMP undefined reference error in C++** | Student omitted `-fopenmp` in compiler invocation | Ensure compilation flag is included: `g++ -O3 -fopenmp script.cpp -o script`. |
| **5. MPI runtime refuses to launch as root** | Running inside Docker container or Colab without root override flag | Add `--allow-run-as-root` flag: `mpirun --allow-run-as-root -np 4 ./mpi_program`. |

---

## 📋 DAY 2 TO DAY 3 STRATEGIC BRIDGE

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                              CURRICULUM BRIDGE: DAY 2 ──► DAY 3                          |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  DAY 2 COMPLETED TODAY:                                                                  |
|  ✔ Multi-core thread scaling with OpenMP & race-condition elimination                    |
|  ✔ Cache-conscious programming (alignas(64) false sharing elimination)                   |
|  ✔ Multi-process distributed communication with MPI (Ranks, Broadcast, Reduction)        |
|  ✔ Intel oneDAL C++ engine & zero-code-change sklearnex dynamic patching                 |
|  ✔ 10x to 100x speedup measured across classic Machine Learning algorithms               |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  DAY 3 ADVANCEMENT TOMORROW:                                                             |
|  ➡ Deep Learning on HPC Clusters (Convolutional Networks, Transformers)                  |
|  ➡ Intel-Optimized Deep Learning Frameworks (TensorFlow-MKL, PyTorch oneDNN)             |
|  ➡ Intel Data Center GPUs & Habana Gaudi 2/3 Tensor Processor Silicon                    |
|  ➡ Slurm Workload Manager (Writing batch job scripts: sbatch, squeue, srun, sacct)       |
|  ➡ Distributed Deep Learning Foundations (Data Parallelism, Gradient AllReduce)         |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 🏆 THE TRAINER'S 5 NON-NEGOTIABLE LAB GOLDEN RULES
1. **Never Show Placeholder Code:** Every demo must run live and output real execution times down to the millisecond.
2. **Never Let Students Get Stuck on Imports:** If a student imports `sklearn` before `patch_sklearn()`, correct their code order immediately.
3. **Always Highlight Silicon:** Point out that oneDAL's speedup is not software magic—it is AVX-512 vector register execution in physical hardware.
4. **Celebrate Speedup Multipliers:** Have students vocalize their speedups (e.g., "I got 22x on KMeans!"). This builds tangible enthusiasm.
5. **Protect Daily Boundaries:** If a student asks about PyTorch or Slurm, acknowledge it and state: *"Brilliant question—that is our exact focus tomorrow on Day 3!"*
