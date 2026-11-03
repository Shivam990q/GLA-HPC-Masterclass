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
| **Day 2 (Morning)** | **Parallel Computing, Amdahl's Law, OpenMP & MPI Systems** | Amdahl's Law, shared memory OpenMP (`#pragma omp parallel for`), 64-byte L1 cache line false sharing mitigation, distributed MPI (`MPI_Scatter`/`Reduce`). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb) |
| **Day 2 (Afternoon)** | **Intel AI Analytics Toolkit & oneDAL: Accelerated ML on CPUs** | NumPy MKL BLAS/LAPACK, oneDAL C++ engine, `patch_sklearn()` monkey-patching, 5 accelerated algorithms (K-Means, PCA, Random Forest, KNN, SVM). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb) |
| **Day 3 (Full Day)** | **Deep Learning on HPC: Intel oneDNN, TensorFlow & Slurm Cluster Jobs** | Hardware-aware DL, Intel oneDNN primitives, operator fusion, Intel-optimized TensorFlow, Slurm batch job scripts (`#SBATCH`), Horovod distributed training. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb) |
| **Day 4 (Full Day)** | **Distributed AI Cluster Scaling & Intel VTune Performance Profiling** | Multi-node scaling theory, Top-Down Microarchitecture Analysis (TMAM), Intel VTune Profiler hotspots, memory bandwidth bottlenecks, Intel Advisor roofline modeling. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb) |
| **Day 5 (Full Day)** | **Generative AI, LLMs on Intel Xeon, Habana Gaudi & OpenVINO Quantization** | Transformer memory wall physics, KV-cache math, Xeon AMX vs Gaudi 2/3 matrix engines, OpenVINO NNCF INT4 quantization, real-time TTFT/TPS latency benchmarks. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb) |

---

## 🛠️ Key Architectural Improvements in Latest Colabs

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

*Curated with precision for GLA University by **Shivam Gupta** & the HPC Masterclass Instruction Team.*
