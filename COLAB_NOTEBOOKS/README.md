# ⚡ GLA University HPC Masterclass — Official Google Colab Hub
### 5-Day Intensive Hands-on Supercomputing, Applied AI & Accelerated Analytics Laboratories

Welcome to the centralized **Google Colab Deployment Hub** for the **GLA University 5-Day High-Performance Computing (HPC) & Intel oneAPI Masterclass**.

Every notebook in this directory has been engineered for **zero-friction, 1-click cloud execution**, eliminating local environment setup hurdles. Whether running on a cloud GPU/CPU instance in Google Colab or an on-premises Intel Xeon cluster node, these notebooks provide identical, production-hardened workflows.

---

## 🚀 Master 1-Click Interactive Google Colab Matrix

Each day is bifurcated into two specialized tracks: **Session 1 (Morning 3h: HPC Systems, Silicon Architecture & C++ Parallelism)** and **Session 2 (Afternoon 3h: Applied AI/ML Acceleration, Automation & Hands-on Production Labs)**. Click any badge below to launch immediately in Google Colab:

| Day & Track | Session & Module Title | Focus & Core Technologies | 1-Click Launch |
| :---: | :--- | :--- | :---: |
| **Day 1 (Morning)** | **HPC Architecture, Linux & Intel oneAPI Base & HPC Toolkit** | Supercomputer architecture, Memory Wall, Intel oneAPI ecosystem, `icx`/`icpx`, SYCL, DPC++ device query. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb) |
| **Day 1 (Afternoon)** | **Linux Systems, Shell Scripting & Secured Shell (SSH) Automation** | Applied Linux filesystem, Heredocs, pipes/filters, defensive bash automation (`hpc_node_audit.sh`), Ed25519 SSH keys, cluster config. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_01_Linux_Basics_Shell_Scripting_and_SSH_Colab.ipynb) |
| **Day 2 (Unified Master)** | **Parallel Computing (OpenMP/MPI) & Intel oneDAL Accelerated ML** | **All-in-One Master Lab (Both Parts):** Amdahl's Law, OpenMP shared memory, 64-byte false sharing mitigation, MPI distributed systems, oneDAL C++ engine, `patch_sklearn()` Random Forest benchmark (~4.8x speedup). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb) |
| **Day 2 (Specialized)** | **Intel AI Analytics Toolkit & oneDAL: Accelerated ML on CPUs** | Afternoon specialized module: NumPy MKL BLAS/LAPACK, oneDAL C++ engine, `patch_sklearn()` monkey-patching, 5 accelerated algorithms (K-Means, PCA, Random Forest, KNN, SVM). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb) |
| **Day 3 (Full Day)** | **Deep Learning on HPC: Intel oneDNN, TensorFlow & Slurm Cluster Jobs** | Hardware-aware DL, Intel oneDNN primitives, operator fusion, Intel-optimized TensorFlow, Slurm batch job scripts (`#SBATCH`), Horovod distributed training. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb) |
| **Day 4 (Full Day)** | **Distributed AI Cluster Scaling & Intel VTune Performance Profiling** | Multi-node scaling theory, Top-Down Microarchitecture Analysis (TMAM), Intel VTune Profiler hotspots, memory bandwidth bottlenecks, Intel Advisor roofline modeling. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb) |
| **Day 5 (Full Day)** | **Generative AI, LLMs on Intel Xeon, Habana Gaudi & OpenVINO Quantization** | Transformer memory wall physics, KV-cache math, Xeon AMX vs Gaudi 2/3 matrix engines, OpenVINO NNCF INT4 quantization, real-time TTFT/TPS latency benchmarks. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb) |

---

## ⚡ Day 2 Master Lab Breakdown: Division of Labor & Improvements

The primary Day 2 laboratory notebook ([`Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb`](file:///c:/Users/Rose/Videos/GLA%20Trainings/COLAB_NOTEBOOKS/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb)) is a comprehensive, production-grade 24-cell master lab deployed directly from [`HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/Collab AI Updated/Copy_of_Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/Collab%20AI%20Updated/Copy_of_Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb). It includes full pre-computed outputs and passes 8/8 automated deliverable checks.

### 🏛️ The Dual-Trainer Division of Labor
```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 DAY 02 LAB CURRICULUM ARCHITECTURE                                     │
├─────────────────────────────────────────────────┬──────────────────────────────────────────────────────┤
│       PART 1: MORNING (09:30 AM – 12:30 PM)     │       PART 2: AFTERNOON (01:30 PM – 04:30 PM)        │
│       3 Hours | Architecture, Concurrency & MPI │       3 Hours | Intel oneDAL & Accelerated ML        │
├─────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│  👨‍🏫 COVERED BY: THEM (CO-TRAINER / RAJAT GARG)   │  👨‍🏫 COVERED BY: ME (LEAD TRAINER / SHIVAM GUPTA)     │
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

### 🔬 Key Technical Breakthroughs & Enhancements in Day 2 Master Notebook
1. **Dynamic Runtime Sys.Path Recovery (Zero-Restart oneDAL Activation)**:
   - Resolves the classic Colab limitation where pip-installed packages (`scikit-learn-intelex`) are invisible to the active interpreter without a kernel restart.
   - Code snippet embedded in Section 5:
     ```python
     import site, sys
     site.main()
     for sp in site.getsitepackages():
         if sp not in sys.path:
             sys.path.insert(0, sp)
     from sklearnex import patch_sklearn
     patch_sklearn()
     ```
   - Automatically activates Intel oneDAL acceleration seamlessly in cloud memory.
2. **Amdahl's Law Scaling Curve Generation**:
   - Plots theoretical speedup curves across core counts ($N = 1$ to $64$) and parallel fractions ($P = 0.50, 0.75, 0.90, 0.95, 0.99$).
   - Automatically saves high-res visualization to local workspace: `reports/amdahl_scaling_curve.png`.
3. **100,000-Sample Random Forest Benchmark**:
   - Compares stock Scikit-Learn vs Intel oneDAL on a 100k-sample, 20-feature classification task.
   - Achieves **~4.77x speedup** (~2.86s down to ~0.60s) with **100% identical test accuracy** (0.8665).
   - Exports benchmark telemetry to local workspace: `reports/day02_random_forest_benchmark.csv`.
4. **End-to-End 8/8 Deliverable Automated Validation**:
   - Validates all 8 deliverables with automated assertions: Drive structure, Amdahl plot, OpenMP vector sum source & binary, False sharing demo, MPI scatter-reduce, RF benchmark CSV, and oneDAL dynamic patch.
   - For complete curriculum notes, see [`HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/README.md`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/README.md).

---

## 🛠️ General Architectural Invariants Across All Colabs

1. **Persistent Google Drive Auto-Sync Engine**:
   - Section 0 in every notebook mounts Google Drive (`/content/drive/MyDrive/`).
   - Registers an automatic IPython `post_run_cell` hook that continuously mirrors all newly generated source files, compiled binaries, SLURM logs, and benchmarking plots to your personal Google Drive (`📁 GLA_HPC_Masterclass_Day0X/`).
   - Ensures **zero data loss** even when Colab runtimes disconnect or recycle.

2. **Dual-Mode Resilient Execution**:
   - Automatically detects whether Intel oneAPI native compilers (`icpx`, `dpcpp`, `mpicxx`) or specialized toolkits (`scikit-learn-intelex`, `openvino`) are present.
   - If oneAPI packages take time to download or are unavailable, high-fidelity native GNU/Clang fallback emulators seamlessly activate so students can execute all parallel OpenMP/MPI loops, benchmark algorithms, and analyze performance profiles without stoppage.

3. **Self-Contained Executable Bash Cells**:
   - Uses `%%bash` cell magics and inline python scripting to test Linux commands, generate real SSH Ed25519 cryptographic keys, simulate multi-node cluster topologies, and launch mock Slurm controllers (`slurmctld` / `slurmd`) directly in cloud memory.

4. **Forensic Verification & Benchmarking Suites**:
   - Every lab concludes with a multi-point verification suite checking output directories, exit codes, throughput speedups, and SHA-256 binary digests.

---

## 📁 Google Drive Directory Layout

When running on Google Colab, files are automatically mirrored to your Google Drive in the following hierarchy:

```
📁 Google Drive (My Drive)
└── 📁 GLA_HPC_Masterclass_Day0X/
    ├── 📁 src/               <- C++, Python, Shell, and SYCL source codes
    ├── 📁 bin/               <- Compiled binary executables
    ├── 📁 slurm/             <- Slurm batch scripts & submission logs
    ├── 📁 reports/           <- Benchmark speedup charts & profiling reports
    ├── 📁 data/              <- Input datasets & synthetic training matrices
    └── 📁 sync_manifest/     <- Automated session audit logs & digests
```

---

*Curated with precision for GLA University by **Shivam Gupta (~SEED~)** & the HPC Masterclass Instruction Team.*
