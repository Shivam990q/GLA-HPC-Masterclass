# ⚡ Day 2: Parallel Computing, OpenMP, MPI & Intel Accelerated Machine Learning (oneDAL)
### GLA University HPC Masterclass | Course Code: `GLA-HPC-BCSG701`

[![Course Status](https://img.shields.io/badge/Course_Status-Production_Ready-brightgreen?style=for-the-badge&logo=intel)](https://github.com/Shivam990q/GLA-HPC-Masterclass)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb)
[![Target Platform](https://img.shields.io/badge/Platform-Intel_oneAPI_|_Xeon_|_OpenMP_|_MPI_|_oneDAL-blue?style=for-the-badge&logo=linux)](https://github.com/Shivam990q/GLA-HPC-Masterclass)

**Host Institution:** Department of Computer Engineering & Applications, Faculty of Engineering & Technology, GLA University, Mathura  
**Industry & Supercomputing Alliance:** Edulateral Foundation & Intel / NEC Supercomputing Alliance  
**Instruction Team & Domain Ownership:**
- **Lead Trainer & Applied AI / Automation Architect:** [Shivam Gupta](https://github.com/Shivam990q) (~SEED~) — *Owner: Afternoon Session (Applied AI/ML & oneDAL)*
- **Co-Trainer & Systems / Parallel Computing Specialist:** Rajat Garg (Ramāpriya Das) — *Owner: Morning Session (HPC Systems, OpenMP & MPI)*

---

## 🚀 1-Click Interactive Google Colab Deployment

Run the complete Day 02 laboratory in your browser without local software installation:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb)

> 💡 **Master Colab Highlights:**
> - **Unified Full-Day Lab:** Covers both Morning (Systems & Concurrency) and Afternoon (Intel oneDAL & ML) in one continuous, verified notebook.
> - **Persistent Google Drive Auto-Sync:** Automatically mounts Google Drive (`/content/drive/MyDrive/`) and mirrors all C++ source files, binaries, benchmarks, and plots to `📁 GLA_HPC_Masterclass_Day02/` via an IPython `post_run_cell` hook.
> - **Intel oneDAL Dynamic Import Fix:** Uses dynamic runtime sys.path recovery (`site.main()`, `site.getsitepackages()`) ensuring `scikit-learn-intelex` activates instantly in Colab without needing a runtime restart.
> - **Complete 8/8 Deliverable Verification:** End-to-end automated audit suite confirming 100% compliance across all code, binaries, and exported datasets.

---

## 🏛️ The Dual-Trainer Curriculum Division of Labor

Day 2 delivers 6 hours of high-performance computing instruction strictly bifurcated into two specialized 3-hour tracks:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 DAY 02 MASTERCLASS ARCHITECTURE                                        │
├─────────────────────────────────────────────────┬──────────────────────────────────────────────────────┤
│       PART 1: MORNING (09:30 AM – 12:30 PM)     │       PART 2: AFTERNOON (01:30 PM – 04:30 PM)        │
│       3 Hours | Architecture, Concurrency & MPI │       3 Hours | Intel oneDAL & Accelerated ML        │
├─────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│  👨‍🏫 COVERED BY: THEM (CO-TRAINER / RAJAT)        │  👨‍🏫 COVERED BY: ME (LEAD TRAINER / SHIVAM GUPTA)     │
│  • Flynn's Taxonomy (SISD, SIMD, MISD, MIMD)    │  • Intel AI Analytics Toolkit Architecture           │
│  • Amdahl's Law vs Gustafson's Law Scaling      │  • Python GIL Bottleneck & Memory Indirection        │
│  • OpenMP Shared-Memory Multithreading (C++)    │  • Intel oneDAL C++ Native Vectorized Engine         │
│  • Fork-Join Model & Parallel Loop Reductions   │  • Zero-Code Monkey-Patching (`patch_sklearn()`)     │
│  • 64-Byte Cache Lines & MESI Invalidation      │  • NumPy MKL BLAS/LAPACK GEMM Acceleration           │
│  • False Sharing Elimination via `alignas(64)`  │  • 100k-Sample Random Forest Acceleration (~4.8x)    │
│  • Distributed Memory Systems with MPI          │  • Mathematical Parity Verification ($R^2 > 0.999$)  │
│  • MPI Communicators, `Scatter` & `Reduce`      │  • Student Coding Challenges (Parallel Pi & KMeans)  │
│  • Core Scaling Benchmarks (1, 2, 4, 8 threads) │  • Automated 8/8 Deliverable Evaluation (100% Pass)  │
└─────────────────────────────────────────────────┴──────────────────────────────────────────────────────┘
```

---

## ☀️ Part 1: Morning Session (09:30 AM – 12:30 PM) — Covered by Them (Co-Trainer)
*Domain: Low-Level Parallel Computing, Silicon Cache Coherence, Shared-Memory OpenMP & Distributed MPI.*

### 1. Parallel Computing Principles & Amdahl's Law
- **Flynn's Taxonomy:** Classification of computer architectures into SISD, SIMD, MISD, and MIMD. Understanding how modern Intel Xeon processors combine multi-core MIMD execution with AVX-512 SIMD vector pipelines.
- **Amdahl's Law (Strong Scaling):** The mathematical ceiling of parallel acceleration when problem size is fixed:
  $$S(N) = \frac{1}{(1-P) + \frac{P}{N}}$$
  Where $P$ is the parallel fraction and $N$ is processor count. As $N \to \infty$, speedup asymptotically approaches $\frac{1}{1-P}$.
- **Gustafson's Law (Weak Scaling):** Scaling problem size proportionally with compute resources: $S(N) = N - \alpha(N - 1)$.
- **Interactive Scaling Curve Visualization:** Generates and exports high-resolution scaling curves across varying parallel fractions ($P = 0.50, 0.75, 0.90, 0.95, 0.99$) to Google Drive at `reports/amdahl_scaling_curve.png`.

### 2. C++ OpenMP Shared-Memory Multithreading
- **The Fork-Join Execution Model:** Master thread spawning worker thread teams upon encountering `#pragma omp parallel` directives.
- **Work-Sharing Constructs:** Distributing loop iterations across threads using `#pragma omp parallel for`.
- **Parallel Reductions:** Preventing data races during multi-threaded summation using the `reduction(+:sum)` clause.
- **Core Scaling Benchmark:** C++ implementation [`openmp_vector_sum.cpp`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/lab_activities/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb) compiled with `g++ -O3 -fopenmp` benchmarking execution across 1, 2, 4, and 8 threads.

### 3. Data Decomposition & False Sharing Elimination
- **Cache Line Physics:** Modern x86 processors fetch memory in 64-byte chunks.
- **The MESI Invalidation Storm:** When multiple threads write to distinct variables located on the *same* 64-byte cache line, the hardware MESI cache coherence protocol repeatedly invalidates L1/L2 caches across all cores, causing catastrophic performance collapse.
- **The Silicon Solution:** Aligning per-thread accumulators to 64-byte boundaries:
  ```cpp
  struct alignas(64) ThreadSum {
      double value;
      char padding[56]; // Enforce isolated 64-byte cache line
  };
  ```
- **Empirical Proof:** Unaligned vs aligned benchmarks proving immediate 3x-6x speedup by eliminating cache bounce.

### 4. Distributed Systems with MPI (Message Passing Interface)
- **Distributed Memory Model:** Scaling across discrete compute nodes with no shared physical RAM.
- **Communicators & Ranks:** Initializing the environment via `MPI_Init`, querying process identity with `MPI_Comm_rank`, and sizing the cluster with `MPI_Comm_size`.
- **Collective Operations:** Splitting large arrays across worker ranks using `MPI_Scatter` and aggregating partial sums to rank 0 using `MPI_Reduce` with `MPI_SUM`.

---

## 🌙 Part 2: Afternoon Session (01:30 PM – 04:30 PM) — Covered by Me (Lead Trainer: Shivam Gupta)
*Domain: Intel AI Analytics Toolkit, oneDAL Acceleration, Zero-Code Monkey-Patching, Production ML Benchmarks & Verification.*

### 1. Intel AI Analytics Toolkit & oneDAL Architecture
- **The Python Bottleneck:** Python's Global Interpreter Lock (GIL), dynamic typing overhead, and fragmented memory pointer chasing.
- **Intel oneDAL (oneAPI Data Analytics Library):** C++ engine providing optimized building blocks for all data analysis stages (preprocessing, transformation, modeling, prediction).
- **Vectorized Instruction Sets:** Direct utilization of AVX-512, Intel AMX, and multi-core thread scheduling under the hood.
- **Intel Extension for Scikit-learn (`sklearnex`):** High-level Python drop-in wrapper that dynamically redirects standard `sklearn` estimator calls into native oneDAL C++ routines.

### 2. Dynamic Runtime Sys.Path Recovery (Colab Resiliency Fix)
- **The Colab Package Isolation Issue:** Installing `scikit-learn-intelex` via pip in a live Google Colab runtime previously required a manual kernel restart because `site-packages` updates were not picked up by the active interpreter.
- **The Autonomous Solution:** Integrated dynamic sys.path recovery into Section 5:
  ```python
  import site, sys
  site.main()
  for sp in site.getsitepackages():
      if sp not in sys.path:
          sys.path.insert(0, sp)
  from sklearnex import patch_sklearn
  patch_sklearn()
  ```
- Guarantees **zero-restart, 100% automated activation** during live classroom execution.

### 3. Zero-Code-Change Monkey Patching (`patch_sklearn()`)
- Monkey-patches standard algorithms: `RandomForestClassifier`, `KMeans`, `PCA`, `SVC`, `KNeighborsClassifier`, `LinearRegression`, `LogisticRegression`.
- Seamless toggle: `patch_sklearn()` activates oneDAL acceleration, `unpatch_sklearn()` restores stock scikit-learn for comparative benchmarking.

### 4. Real-World Accelerated ML Benchmark: Random Forest Classifier
- **Dataset:** 100,000 synthetic samples, 20 features, 4 target classes generated via `make_classification`.
- **Model:** 100 parallel decision trees (`n_estimators=100`, `max_depth=12`, `n_jobs=-1`).
- **Empirical Measured Speedup:**
  * Stock Scikit-Learn Time: **~2.86 seconds**
  * Intel oneDAL Accelerated Time: **~0.60 seconds**
  * **Net Speedup Factor:** **~4.77x Faster**
  * **Accuracy Parity:** Test accuracy **100% identical** (0.8665 vs 0.8665) — zero numerical degradation.
- **Artifact Export:** Automatically writes full benchmark telemetry to Google Drive: `reports/day02_random_forest_benchmark.csv`.

### 5. Hands-on Student Coding Challenges
- **Challenge 1 (OpenMP):** Calculating $\pi$ via numerical integration ($\int_0^1 \frac{4}{1+x^2} dx$) using `#pragma omp parallel for reduction(+:pi)`.
- **Challenge 2 (oneDAL):** Clustering 150,000 multi-dimensional customer vectors using `sklearnex.cluster.KMeans` and measuring inertia convergence speed.

### 6. Automated 8-Point Concept Mastery Evaluation
Every student's notebook verifies and confirms 8 tangible deliverables before session completion:
1. `[PASS]` Google Drive Directory Structure initialized (`📁 GLA_HPC_Masterclass_Day02/`)
2. `[PASS]` Amdahl's Law Scaling Curve Plot generated (`reports/amdahl_scaling_curve.png`)
3. `[PASS]` OpenMP Vector Sum C++ Source written (`src/openmp_vector_sum.cpp`)
4. `[PASS]` OpenMP Vector Sum Binary compiled (`bin/openmp_vector_sum`)
5. `[PASS]` False Sharing Demonstration Source written (`src/false_sharing_demo.cpp`)
6. `[PASS]` MPI Scatter-Reduce C++ Source written (`src/mpi_scatter_reduce.cpp`)
7. `[PASS]` Random Forest Benchmark Telemetry CSV exported (`reports/day02_random_forest_benchmark.csv`)
8. `[PASS]` Intel oneDAL Dynamic Import & Patch Verification confirmed
**Score:** `8/8 Deliverables (100% Completion)`

---

## 📁 Day 2 Directory Structure & Artifacts

```
📁 Day-02_Parallel_OpenMP_MPI_oneDAL/
├── README.md                                             <- This master curriculum navigation document
├── Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb  <- Master Unified 24-Cell Colab Notebook (Deployed)
├── Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb <- Afternoon Specialized Colab Notebook
│
├── 00_DAY_02_KANTHAST_TRAINER_WAR_ROOM_RUNBOOK.md        <- Internal trainer war-room timeline & script
├── 00_DAY_02_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md   <- Complete 50+ term glossary (Amdahl, MESI, oneDAL)
├── 01_DAY_02_6_HOUR_MASTER_TRAINER_PLAYBOOK.md          <- Minute-by-minute 6-hour instructional roadmap
├── 02_DAY_02_HANDS_ON_LAB_AND_COMMANDS.md               <- Shell commands, compiler flags & test scripts
├── 03_DAY_02_STUDENT_CHEATSHEET_AND_MCQS.md              <- High-density student reference & 30 MCQs
├── 04_DAY_02_COMPLETE_TOPIC_BY_TOPIC_STUDY_GUIDE.md     <- In-depth academic textbook-style reading guide
├── 05_DAY_02_ARROW_WORKFLOWS_AND_TOPIC_TREES.md         <- Visual ASCII & Mermaid concept diagrams
│
├── 📁 Collab AI Updated/                                 <- Verified master notebook with pre-executed outputs
│   └── Copy_of_Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb
│
├── 📁 INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/ <- Dedicated 3-hour afternoon teaching kit
│   ├── README.md
│   ├── 01_THEORY_AND_TRAINER_LECTURE_GUIDE.md
│   ├── 02_LIVE_DEMOS_AND_CODE_WALKTHROUGH.md
│   ├── 03_HANDS_ON_STUDENT_LAB_ACTIVITIES.md
│   ├── 04_STUDENT_PRACTICE_SCRIPTS/
│   ├── 05_MCQ_ASSESSMENT_BANK.md
│   └── 06_QUICK_REFERENCE_CHEAT_SHEET.md
│
├── 📁 lab_activities/                                    <- Synchronized student laboratory workspace
│   └── Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb
│
└── 📁 quizzes_and_assessments/                           <- Pre-lab and post-lab evaluative instruments
```

---

*Curated with engineering rigor for GLA University by **Shivam Gupta (~SEED~)** & the HPC Masterclass Team.*
