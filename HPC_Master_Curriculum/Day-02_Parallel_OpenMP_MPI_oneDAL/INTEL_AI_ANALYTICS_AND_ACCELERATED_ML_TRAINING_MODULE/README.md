# 🚀 Intel® AI Analytics Toolkit & Accelerated Machine Learning (oneDAL / sklearnex)
## Complete 3-Hour Master Training Package & Curriculum Kit (Day 2 Afternoon Session)

**Target Audience:** Engineering Students, Data Scientists, Machine Learning Engineers & HPC Practitioners  
**Institutional Track:** GLA University — High Performance Computing & Intel oneAPI Masterclass  
**Curriculum Alignment:** Day 2 Official Syllabus Core (Topics 4 & 5: Intel AI Analytics Toolkit, Optimized Scikit-learn, Pandas, NumPy, oneDAL)  
**Lead Trainer:** Shivam Gupta  
**Session Window:** Day 2 Post-Lunch / Afternoon (3 Hours | 01:30 PM – 04:30 PM)  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb)
[![GitHub Repository](https://img.shields.io/badge/GitHub-GLA--HPC--Masterclass-181717?logo=github)](https://github.com/Shivam990q/GLA-HPC-Masterclass)

---

## ⚡ The Day 2 Dual-Trainer Curriculum Division

Day 2 of the GLA HPC Masterclass is purposefully divided into two complementary 3-hour tracks:

| Session | Trainer | Duration | Focus Area & Syllabus Scope |
|:---|:---|:---:|:---|
| **Morning Track** | **Trainer 1** | **3 Hours** (09:30 AM – 12:30 PM) | **Low-Level Systems & Distributed HPC**:<br>• Parallel Computing Mathematics (Amdahl's & Gustafson's Laws, Serial Bottleneck)<br>• C++ OpenMP Shared-Memory Multithreading (`#pragma omp parallel for reduction`)<br>• Hardware Physics: False Sharing & MESI Cache Coherence Protocol (64-byte padding)<br>• Distributed Systems with C++ MPI (Ranks, Communicators, Point-to-Point & Collective trees) |
| **Afternoon Track** | **Trainer 2 (User)** | **3 Hours** (01:30 PM – 04:30 PM) | **High-Level Applied Acceleration (Intel AI Analytics & oneDAL)**:<br>• The Python GIL Bottleneck & Memory Indirection<br>• Intel® AI Analytics Toolkit Architecture (oneMKL, oneDAL, Intel Python)<br>• Intel® Extension for Scikit-learn (`sklearnex`) & Dynamic Monkey-Patching (`patch_sklearn()`)<br>• Accelerated ML Algorithms: K-Means, Random Forest, PCA, SVM, KNN (15x–35x speedup)<br>• Live Speedup Benchmarking & Bit-Exact Accuracy Verification |

---

## 🌐 Interactive Google Colab Notebook (Zero Setup Required)

Students can launch the complete hands-on interactive laboratory directly in their web browser without installing any software locally:

👉 **[Launch Interactive Colab: `Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb`](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb)**

- **Scope:** Applied, student-friendly, and visual (Zero setup friction, instant gratification).
- **Hardware:** Intel Xeon CPU on Google Cloud VM with AVX-512 / AVX2 vector extensions.
- **Coverage:**
  1. Python GIL bottleneck demonstration and vector hardware introspection.
  2. NumPy MKL matrix multiplication acceleration vs naive Python loops.
  3. 500,000-sample K-Means clustering benchmark (Stock Scikit-learn vs `sklearnex`).
  4. 100,000-sample Random Forest Classifier benchmark (100 estimators).
  5. 50-dimensional Principal Component Analysis (PCA) dimensionality reduction.
  6. Dynamic monkey-patching and bit-exact mathematical parity verification.
  7. Visual speedup charts rendered dynamically with Matplotlib.
  8. Graded student lab challenges with automated assertion testing.

---

## 📂 Module Package Directory Structure

This dedicated folder contains everything required for a flawless 3-hour afternoon delivery:

```
INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/
│
├── README.md                                             # Master Navigation & Session Blueprint
├── Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb # Interactive Google Colab Notebook
│
├── 01_THEORY_AND_TRAINER_LECTURE_GUIDE.md                # 180-Minute Trainer Script, Concepts & Whiteboard
│   ├── Block 1: The Python Bottleneck & Intel AI Analytics Toolkit
│   ├── Block 2: Intel oneDAL Architecture & Hardware Vectorization (AVX-512)
│   ├── Block 3: Dynamic Patching Mechanics (patch_sklearn vs unpatch_sklearn)
│   ├── Block 4: Accelerated Machine Learning Algorithm Deep-Dive
│   └── Block 5: Mathematical Parity, Numerical Stability & Zero Accuracy Loss
│
├── 02_LIVE_DEMOS_AND_CODE_WALKTHROUGH.md                 # 6 Live Screen-Projection Coding Demos
│   ├── Demo 1: Environment & Intel Hardware Introspection
│   ├── Demo 2: NumPy MKL Matrix Multiplication vs Naive Loops (100x+ Speedup)
│   ├── Demo 3: K-Means Clustering on 500k Points (15x-30x Speedup)
│   ├── Demo 4: Random Forest on 100k Samples (10x-25x Speedup)
│   ├── Demo 5: PCA Dimensionality Reduction on High-Dim Vectors (10x-20x Speedup)
│   └── Demo 6: Dynamic Unpatching & Mathematical Parity Verification
│
├── 03_HANDS_ON_STUDENT_LAB_ACTIVITIES.md                 # 6 Step-by-Step Graded Student Lab Exercises
│   ├── Lab 1: Intel Acceleration Environment Audit
│   ├── Lab 2: Accelerated Customer Segmentation via K-Means
│   ├── Lab 3: High-Throughput Financial Fraud Detection via Random Forest
│   ├── Lab 4: Genomic Data Dimensionality Reduction via PCA
│   ├── Lab 5: Dynamic Patching / Selective Patching Verification
│   └── Lab 6: End-to-End Scaled ML Pipeline (StandardScaler + PCA + KNN)
│
├── 04_STUDENT_PRACTICE_SCRIPTS/                          # 7 Standalone Runnable Python Benchmarks
│   ├── 01_verify_intel_env.py                           # Hardware, AVX-512 & oneDAL Configuration Probe
│   ├── 02_numpy_mkl_speedup.py                          # BLAS DGEMM vs Pure Python Matrix Multiplication
│   ├── 03_kmeans_acceleration.py                        # 500k Points K-Means Benchmark & Inertia Check
│   ├── 04_random_forest_acceleration.py                 # 100k Samples Random Forest Multi-Core Scaling
│   ├── 05_pca_reduction_acceleration.py                 # 50-Feature PCA Projection Benchmark
│   ├── 06_full_benchmark_suite.py                       # Automated Multi-Algorithm Execution & CSV Reporter
│   └── run_all_benchmarks.sh                            # One-Click Bash Execution Runner
│
├── 05_MCQ_ASSESSMENT_BANK.md                             # 35 Evaluated MCQs with Forensic Explanations
│   ├── Section A: Python Performance, GIL & oneAPI Architecture (10 Questions)
│   ├── Section B: Intel Extension for Scikit-learn (sklearnex) (15 Questions)
│   └── Section C: Hardware Vectorization, Threads & Tuning (10 Questions)
│
└── 06_QUICK_REFERENCE_CHEAT_SHEET.md                    # 2-Page High-Density Command & Syntax Reference
```

---

## ⏰ Pedagogical Delivery Flow (3-Hour Afternoon Roadmap)

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|           DAY 2 AFTERNOON MASTER SCHEDULE: 01:30 PM - 04:30 PM (180 MINUTES)             |
+──────────────────────────────────────────────────────────────────────────────────────────+
| TIME WINDOW           | FOCUS & PEDAGOGICAL ACTIVITY                                      |
+───────────────────────┼──────────────────────────────────────────────────────────────────+
| 01:30 PM - 02:00 PM   | BLOCK 1: The Python Bottleneck & Intel AI Analytics Toolkit      |
| (30 Minutes)          | • Why Python is slow: The Global Interpreter Lock (GIL) & boxing |
|                       | • Intel oneAPI oneDAL architecture & AVX-512 vectorization        |
|                       | • Intel Distribution for Python & NumPy MKL BLAS acceleration     |
+───────────────────────┼──────────────────────────────────────────────────────────────────+
| 02:00 PM - 02:40 PM   | BLOCK 2: Intel Extension for Scikit-learn (sklearnex)            |
| (40 Minutes)          | • Zero-code-change dynamic monkey-patching: patch_sklearn()       |
|                       | • Supported algorithms: K-Means, Random Forest, PCA, SVM, KNN     |
|                       | • Selective patching vs global patching & unpatch_sklearn()      |
|                       | • Live Demo 1 & 2: Environment inspection & NumPy MKL             |
+───────────────────────┼──────────────────────────────────────────────────────────────────+
| 02:40 PM - 03:20 PM   | BLOCK 3: Live Benchmarks & Screen Walkthrough                     |
| (40 Minutes)          | • Live Demo 3: 500k sample K-Means clustering (25x speedup)       |
|                       | • Live Demo 4: 100k sample Random Forest classification (15x)     |
|                       | • Live Demo 5: 50-dimensional PCA reduction (18x speedup)         |
|                       | • Live Demo 6: Mathematical parity & bit-exact accuracy check    |
+───────────────────────┼──────────────────────────────────────────────────────────────────+
| 03:20 PM - 04:00 PM   | BLOCK 4: Hands-On Student Lab Challenges (Interactive Colab)      |
| (40 Minutes)          | • Students open Google Colab / local Jupyter                      |
|                       | • Students execute Labs 1 through 6 independently                 |
|                       | • Trainer live debugging, troubleshooting & core scaling checks   |
+───────────────────────┼──────────────────────────────────────────────────────────────────+
| 04:00 PM - 04:30 PM   | BLOCK 5: Assessment, Concept Mastery & Wrap-Up                    |
| (30 Minutes)          | • 35 Evaluated MCQs administered with live concept debriefing     |
|                       | • Reviewing the 2-Page Quick Reference Cheat Sheet               |
|                       | • Q&A Session and Preview of Day 3 (Deep Learning & oneDNN)       |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 💻 Local Environment Installation (Optional)

If students or trainers wish to run the code on local workstations rather than Google Colab:

```bash
# 1. Create a dedicated virtual environment
python -m venv intel_ml_env
source intel_ml_env/bin/activate  # On Windows: intel_ml_env\Scripts\activate

# 2. Install Intel Extension for Scikit-learn and standard data science stack
pip install --upgrade pip
pip install scikit-learn-intelex numpy pandas matplotlib seaborn jupyterlab

# 3. Verify Intel acceleration is active
python -c "import sklearnex; print('sklearnex version:', sklearnex.__version__)"
```
