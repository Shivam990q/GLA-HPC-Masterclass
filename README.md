# 🚀 GLA University — High Performance Computing & Heterogeneous AI Systems
### 5-Day Intensive Masterclass | Course Code: `GLA-HPC-BCSG701`

[![Course Status](https://img.shields.io/badge/Course_Status-Production_Ready-brightgreen?style=for-the-badge&logo=intel)](https://github.com/Shivam990q/GLA-HPC-Masterclass)
[![Target Platform](https://img.shields.io/badge/Platform-Intel_oneAPI_|_Xeon_|_Gaudi_|_Linux-blue?style=for-the-badge&logo=linux)](https://github.com/Shivam990q/GLA-HPC-Masterclass)
[![Colab Support](https://img.shields.io/badge/Google_Colab-1--Click_Launch_Ready-orange?style=for-the-badge&logo=googlecolab)](https://github.com/Shivam990q/GLA-HPC-Masterclass/tree/main/COLAB_NOTEBOOKS)
[![Curriculum](https://img.shields.io/badge/Curriculum-5_Days_|_30_Hours-purple?style=for-the-badge&logo=bookstack)](https://github.com/Shivam990q/GLA-HPC-Masterclass/tree/main/HPC_Master_Curriculum)

**Host Institution:** Department of Computer Engineering & Applications, Faculty of Engineering & Technology, GLA University, Mathura  
**Industry & Supercomputing Alliance:** Edulateral Foundation & Intel / NEC Supercomputing Alliance  
**Lead Faculty & Trainers:**
- **Lead Trainer & Applied AI / Automation Architect:** [Shivam Gupta](https://github.com/Shivam990q) (~SEED~)
- **Co-Trainer & Systems / Parallel Computing Specialist:** Rajat Garg (Ramāpriya Das)

---

## ⚡ 1-Click Interactive Google Colab Deployment Hub

Eliminate all local compiler, library, and environment setup friction. Launch the complete hands-on supercomputing laboratories directly in your browser on Google Colab with 1-click execution:

| Day & Track | Session & Module Title | Focus & Core Technologies | 1-Click Colab Launch |
| :---: | :--- | :--- | :---: |
| **Day 1 (Morning)** | **HPC Architecture, Linux & Intel oneAPI Base & HPC Toolkit** | Supercomputer topology, Memory Wall, TOP500, Intel oneAPI ecosystem, `icx`/`icpx`, SYCL, DPC++ device discovery. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb) |
| **Day 1 (Afternoon)** | **Linux Systems, Defensive Shell Scripting & SSH Key Automation** | Applied Linux hierarchy, Heredocs, streams (`awk`, `grep`), defensive shell automation (`hpc_node_audit.sh`), Ed25519 SSH keys, cluster config. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_01_Linux_Basics_Shell_Scripting_and_SSH_Colab.ipynb) |
| **Day 2 (Unified Master Lab)** | **Parallel Computing (OpenMP, MPI) & Intel oneDAL Accelerated ML** | **Full-Day Master Lab:** Amdahl's Law scaling curve, OpenMP reduction, 64-byte L1 cache false sharing (`alignas(64)`), MPI message passing, and Intel oneDAL `patch_sklearn()` 100k-sample Random Forest (~4.77x speedup, 100% accuracy parity) with 8/8 automated deliverable checks. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb) |
| **Day 2 (Afternoon Track)** | **Intel AI Analytics Toolkit & oneDAL: Accelerated ML on CPUs** | Dedicated module: NumPy oneMKL BLAS/LAPACK, oneDAL C++ engine, `patch_sklearn()` monkey-patching, and 5 classical ML benchmarks (K-Means, PCA, Random Forest, KNN, SVM). | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb) |
| **Day 3 (Full Day)** | **Deep Learning on HPC: Intel oneDNN, TensorFlow & Slurm Cluster Jobs** | Hardware-aware DL, Intel oneDNN primitives, operator fusion, AMX matrix engines, Intel-optimized TensorFlow, Slurm batch job scripts (`#SBATCH`), Horovod distributed training. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb) |
| **Day 4 (Full Day)** | **Distributed AI Cluster Scaling & Intel VTune Performance Profiling** | Multi-node scaling theory, Data vs Model parallelism, Top-Down Microarchitecture Analysis (TMAM), Intel VTune Profiler hotspots, memory bandwidth bottlenecks, Intel Advisor roofline modeling. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb) |
| **Day 5 (Full Day)** | **Generative AI, LLMs on Intel Xeon, Habana Gaudi & OpenVINO Quantization** | Transformer memory wall physics, KV-cache math, Xeon AMX vs Gaudi 2/3 matrix engines, OpenVINO NNCF INT4 quantization, real-time TTFT/TPS latency benchmarks, Capstone Project. | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb) |

> 💡 **Recent Colab Improvements:**
> - **Persistent Google Drive Auto-Sync:** Section 0 automatically mounts Google Drive and registers an IPython `post_run_cell` hook to continuously mirror all generated C++, Python, Slurm, and log files into `📁 My Drive > GLA_HPC_Masterclass_Day0X/`.
> - **Dual-Mode Resilient Execution:** Notebooks detect native Intel oneAPI compilers (`icpx`, `dpcpp`, `mpicxx`) or activate high-fidelity fallback emulators so that students never experience stopping errors.
> - **Self-Contained Bash Cells:** Real bash scripts (`%%bash`), Ed25519 keypair generation, synthetic cluster simulations, and headless Slurm job executions run smoothly in cloud memory.
> - **Automated Verification:** Every notebook features end-to-end audit cells verifying compilation flags, speedup ratios, exit codes, and output directories.

---

## 🏛️ The Dual-Trainer Architecture & Granular Division of Labor

To deliver a truly world-class, rigorous, and practical curriculum without cognitive overload, each 6-hour training day is strictly bifurcated into two synchronized, high-impact sessions:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 DAILY 6-HOUR MASTERCLASS TIMELINE                                      │
├─────────────────────────────────────────────────┬──────────────────────────────────────────────────────┤
│       SESSION 1: MORNING (09:30 AM – 12:30 PM)  │       SESSION 2: AFTERNOON (01:30 PM – 04:30 PM)     │
│       3 Hours | Architecture, Theory & Systems  │       3 Hours | Applied AI, Automation & Colab Labs  │
├─────────────────────────────────────────────────┼──────────────────────────────────────────────────────┤
│  👨‍🏫 COVERED BY: TRAINER 1 (CO-TRAINER / RAJAT)  │  👨‍🏫 COVERED BY: TRAINER 2 (LEAD TRAINER / SHIVAM)   │
│  • HPC Systems Architecture & Top500 Metrics   │  • Applied Linux Systems Engineering & Terminal Flow │
│  • Silicon Physics, Xeon CPU & Memory Hierarchy│  • Defensive Shell Scripting Automation (`audit.sh`) │
│  • Memory Wall, Cache Coherence & False Sharing│  • Asymmetric SSH Cryptography (`ed25519`) & Config  │
│  • Amdahl's & Gustafson's Laws of Concurrency  │  • Intel AI Analytics Toolkit & NumPy MKL Tuning     │
│  • OpenMP Shared-Memory Primitives (C/C++)     │  • oneDAL `patch_sklearn()` Accelerated ML Suite     │
│  • MPI Distributed Systems (`Scatter`/`Reduce`)│  • Intel-Optimized TensorFlow & Transfer Learning    │
│  • Intel oneDNN Primitives & AMX Matrix Engines│  • Horovod Distributed Training & Multi-Node Cluster │
│  • Slurm Workload Manager Internal Architecture│  • Intel VTune Profiler Hotspots & Memory Access     │
│  • Multi-Node Interconnects (RoCE vs InfiniBand│  • Intel Advisor Roofline Modeling & Vectorization   │
│  • Transformer Silicon Bottlenecks & KV-Cache  │  • OpenVINO NNCF INT4 LLM Quantization & Benchmarks  │
└─────────────────────────────────────────────────┴──────────────────────────────────────────────────────┘
```

### 1. Session 1: Morning Track (09:30 AM – 12:30 PM) — Systems, Architecture & Foundations
- **Lead Instructor:** Trainer 1 (Rajat Garg / Co-Trainer)
- **Primary Domain:** Theoretical Underpinnings, Silicon Physics, Memory Hierarchy, Hardware Accelerators, and Core Systems Programming.
- **Pedagogical Mandate:** Establish the foundational *"Why"* and *"How"* at the hardware and compiler level. Unpack processor microarchitecture, vector registers (AVX-512, AMX), cache line dynamics (L1/L2/L3), network topologies, and mathematical limits of concurrency before students write code.

### 2. Session 2: Afternoon Track (01:30 PM – 04:30 PM) — Applied AI/ML Acceleration & Hands-on Production Labs
- **Lead Instructor:** Trainer 2 (Shivam Gupta / Lead Trainer)
- **Primary Domain:** Applied Machine Learning, Automation, Shell Scripting, Software Optimization, Profiling Tools, and Google Colab Interactive Execution.
- **Pedagogical Mandate:** Deliver direct, hands-on production code with zero hand-waving. Students execute practical scripts, monkey-patch standard ML algorithms for 10x-100x CPU speedups, submit real Slurm cluster jobs, diagnose cache miss bottlenecks in VTune, and quantize 7B+ parameter LLMs for sub-50ms token latency.

---

## 📅 Day-by-Day Detailed Curriculum & Part-by-Part Breakdown

### 🐧 Day 1: HPC Foundations, Linux Systems, Shell Automation & Intel oneAPI
*Theme: Transitioning from Commodity Computing to High-Performance Supercomputing Infrastructure.*

#### ☀️ Part 1: Morning Session (09:30 AM – 12:30 PM) — Covered by Trainer 1
- **HPC Supercomputing Landscape:** Evolution of supercomputing, TOP500 benchmarks (LINPACK, HPL, HPCG), PFLOPS/EFLOPS scale, and modern cluster architecture (Head/Login Node, Compute Nodes, Shared Storage Fabric).
- **Processor & Memory Architecture:** Intel Xeon Scalable Processors, NUMA nodes, socket interconnects (UPI), memory channels (DDR5), cache hierarchy (L1d, L1i, L2, LLC), and the fundamental **Memory Wall** bottleneck ($B/F$ ratio).
- **Intel oneAPI Ecosystem:** The vision of unified cross-architecture programming (CPU, GPU, FPGA, AI accelerators). Overview of Intel oneAPI Base Toolkit and HPC Toolkit.
- **Compiler Suite:** Architecture of `icx` (C), `icpx` (C++), `ifx` (Fortran), DPC++/SYCL single-source heterogeneous programming model, and host-device device query (`sycl-ls`).

#### 🌙 Part 2: Afternoon Session (01:30 PM – 04:30 PM) — Covered by Shivam Gupta
- **Applied Linux Systems Engineering:** Navigating the enterprise HPC Linux hierarchy (`/home`, `/scratch`, `/opt`, `/tmp`). Mastering file permissions (`chmod`, `chown`, octal vs symbolic notation) and process management (`ps aux`, `top`, `kill`, `nohup`).
- **Pipes, Streams & Text Processing:** Stream redirection (`>`, `>>`, `2>&1`), pipelines (`|`), and regex filters with `grep`, `find`, `sort`, `uniq`, `wc`, and `awk` column filtering.
- **Defensive Shell Scripting Automation:** Writing production-grade shell scripts with strict error handling (`set -euo pipefail`), environment exports, shebangs, command-line arguments (`$1`, `$2`), and Heredocs.
- **Cluster Node Health Auditor:** Live development and execution of [`hpc_node_audit.sh`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/LINUX_SHELL_SCRIPTING_AND_SSH_TRAINING_MODULE/scripts/hpc_node_audit.sh), automatically harvesting CPU model, core topology, RAM, disk quotas, and compiler paths into structured logs.
- **Secured Shell (SSH) Cryptography & Cluster Connectivity:** Generating modern Ed25519 asymmetric cryptographic keypairs (`ssh-keygen -t ed25519`), deploying public keys via `ssh-copy-id`, configuring `~/.ssh/config` for jump hosts and aliases, and performing secure data transfers (`scp`, `rsync -avzP`).
- **Interactive Hands-on Lab:** [Day 01 Linux & SSH Colab Notebook](file:///c:/Users/Rose/Videos/GLA%20Trainings/COLAB_NOTEBOOKS/Day_01_Linux_Basics_Shell_Scripting_and_SSH_Colab.ipynb).

---

### ⚡ Day 2: Parallel Computing, OpenMP, MPI & Intel Accelerated Machine Learning
*Theme: Concurrency from Single-Node Multi-Threading to Distributed Systems & Accelerated Classical ML.*  
📖 **Comprehensive Day 2 Guide:** [Day-02 Master Curriculum & Lab Guide](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/README.md)

#### ☀️ Part 1: Morning Session (09:30 AM – 12:30 PM) — Covered by Trainer 1 (Rajat Garg)
- **Foundations of Parallel Computing:** Flynn's Taxonomy (SISD, SIMD, MISD, MIMD). Theoretical limits of parallel speedup: **Amdahl's Law** (strong scaling) vs **Gustafson's Law** (weak scaling).
- **The Power Wall & Multicore Era:** Dennard Scaling breakdown, Moore's Law limits, thermal design power (TDP), and frequency saturation.
- **Shared-Memory Multithreading with OpenMP:** OpenMP programming model, compilation with `-qopenmp`, parallel regions (`#pragma omp parallel`), loop work-sharing (`#pragma omp parallel for`), scheduling policies (`static`, `dynamic`, `guided`), private vs shared variables, reductions, and critical sections.
- **Hardware-Level Pitfalls:** **False Sharing** on 64-byte L1 cache lines, cache invalidation storms under the MESI protocol, and padding data structures with `alignas(64)`.
- **Distributed Computing with MPI:** Message Passing Interface architecture, distributed-memory model, communicators (`MPI_COMM_WORLD`), point-to-point communication (`MPI_Send`, `MPI_Recv`), and collective operations (`MPI_Bcast`, `MPI_Scatter`, `MPI_Gather`, `MPI_Reduce`).

#### 🌙 Part 2: Afternoon Session (01:30 PM – 04:30 PM) — Covered by Trainer 2 (Shivam Gupta)
- **Intel AI Analytics Toolkit Overview:** Purpose-built Python distribution and acceleration libraries designed to maximize compute density on Intel Xeon architectures.
- **Hardware Acceleration without Code Rewrites:** The mechanics of **Monkey-Patching** standard Python libraries via `scikit-learn-intelex` (`from sklearnex import patch_sklearn; patch_sklearn()`).
- **Intel oneDAL C++ Engine:** How the Intel oneAPI Data Analytics Library replaces slow Python loops with multithreaded, AVX-512 vector-aligned native C++ kernels.
- **Dynamic oneDAL Environment Recovery:** Automatic discovery and recovery of oneDAL shared libraries in Google Colab via dynamic `sys.path` injection (`site.main()`, `getsitepackages()`).
- **NumPy oneMKL BLAS/LAPACK Acceleration:** Linking NumPy with Intel Math Kernel Library (oneMKL) for multi-threaded GEMM (General Matrix Multiply) operations.
- **5 Accelerated Classical ML Benchmarks (Hands-On):**
  1. *K-Means Clustering:* High-dimensional centroid convergence across 100,000 samples.
  2. *Principal Component Analysis (PCA):* Covariance matrix decomposition and dimensionality reduction.
  3. *Random Forest Classifier:* High-throughput parallel ensemble decision tree training (~4.77x speedup, 100% accuracy parity).
  4. *k-Nearest Neighbors (KNN):* Fast brute-force and KD-tree spatial neighbor queries.
  5. *Support Vector Machines (SVC):* Quadratic programming optimization speedup.
- **Comparative Benchmarks:** Side-by-side performance profiling measuring execution wall-clock time, CPU core utilization across threads, and verification of exact numerical parity ($R^2 > 0.999$, zero loss in accuracy).
- **Automated Verification & Local Workspace Auto-Sync:** 8/8 passing automated deliverable checks, instant local workspace persistence, and optional 1-click zip export.

#### 🚀 Interactive Hands-on Labs:
- **Unified Master Lab (OpenMP, MPI & oneDAL):** [Day 02 Traditional ML, oneAPI, OpenMP, MPI & oneDAL Colab Notebook](file:///c:/Users/Rose/Videos/GLA%20Trainings/COLAB_NOTEBOOKS/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb) — *Full-day unified master lab with 8/8 automated deliverable checks.*
- **Dedicated AI Analytics Lab:** [Day 02 Intel AI Analytics & Accelerated ML Colab Notebook](file:///c:/Users/Rose/Videos/GLA%20Trainings/COLAB_NOTEBOOKS/Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb) — *Focused module on oneDAL and Scikit-learn acceleration.*

---

### 🧠 Day 3: Deep Learning on HPC, Intel oneDNN, TensorFlow & Slurm Cluster Jobs
*Theme: Scaling Deep Neural Networks on Modern Intel Silicon and Managing Cluster Workloads.*

#### ☀️ Part 1: Morning Session (09:30 AM – 12:30 PM) — Covered by Trainer 1
- **Deep Learning Computational Characteristics:** Floating-point representations (FP32, FP16, BF16, INT8), compute-bound vs memory-bandwidth bound neural network layers.
- **Intel oneDNN (Deep Neural Network Library):** Architecture of oneDNN primitives (Convolutions, Matrix Multiply, Layer Normalization, Activations, Pooling), fused operators (Conv + ReLU + BatchNorm fusion), and zero-overhead memory layouts (`nChw16c`).
- **Intel Advanced Matrix Extensions (AMX):** Dedicated 2D matrix tile registers (`TMM0-TMM7`) and Tile Matrix Multiply (TMUL) hardware on 4th/5th Gen Intel Xeon processors, delivering up to 8x throughput over AVX-512 for BF16/INT8 deep learning workloads.
- **HPC AI Accelerators:** Architectural overview of Intel Data Center GPU Max Series (Ponte Vecchio) and Habana Gaudi 2/Gaudi 3 AI processors.
- **Slurm Workload Manager Architecture:** Supercomputer scheduler design, Central Controller (`slurmctld`), Node Daemon (`slurmd`), Slurm Database (`slurmdbd`), partitions, QoS, node states (`idle`, `alloc`, `drain`), and job allocation lifecycles.

#### 🌙 Part 2: Afternoon Session (01:30 PM – 04:30 PM) — Covered by Shivam Gupta
- **Intel-Optimized TensorFlow:** Setting up and configuring `tensorflow-mkl` for Xeon. Tuning OpenMP and intra/inter-op thread pools (`OMP_NUM_THREADS`, `KMP_BLOCKTIME=0`, `KMP_AFFINITY=granularity=fine,compact,1,0`).
- **Computer Vision & Transfer Learning on CPUs:** Training MobileNetV2 and ResNet-50 architectures with Intel-optimized TensorFlow, comparing stock vs accelerated inference and training throughput.
- **Slurm Batch Script Engineering:** Crafting fault-tolerant `#SBATCH` submission scripts (`#SBATCH --nodes`, `--ntasks-per-node`, `--cpus-per-task`, `--time`, `--partition`, `--output`). Submitting (`sbatch`), monitoring (`squeue`, `scontrol show job`), inspecting node resources (`sinfo`), and canceling (`scancel`) jobs.
- **Horovod Distributed Deep Learning:** Principles of synchronous distributed data parallelism, the Ring-AllReduce communication paradigm, wrapping optimizers with `hvd.DistributedOptimizer`, broadcast initialization (`hvd.broadcast_variables`), and learning rate warmup schedules.
- **Interactive Hands-on Lab:** [Day 03 Deep Learning & Slurm Colab Notebook](file:///c:/Users/Rose/Videos/GLA%20Trainings/COLAB_NOTEBOOKS/Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb).

---

### 🔬 Day 4: Distributed AI Cluster Scaling & Intel VTune Performance Profiling
*Theme: Multi-Node Communication Optimization and Forensic Hardware-Level Application Profiling.*

#### ☀️ Part 1: Morning Session (09:30 AM – 12:30 PM) — Covered by Trainer 1
- **Distributed Training Paradigms:** Data Parallelism, Model Parallelism (Tensor Parallelism, Pipeline Parallelism), and 3D Hybrid Parallelism (Megatron-LM, DeepSpeed).
- **Communication Bottlenecks:** Bandwidth vs Latency, Parameter Server architecture vs Decentralized AllReduce, Tree-based AllReduce, and high-performance interconnects (RoCE v2, InfiniBand HDR/NDR).
- **Hardware Performance Monitoring (PMU):** CPU hardware event counters, uncore counters, instructions retired, clock cycles, cache misses, branch mispredictions, and the **Top-Down Microarchitecture Analysis Method (TMAM)** (Frontend Bound, Bad Speculation, Backend Bound, Retrying).

#### 🌙 Part 2: Afternoon Session (01:30 PM – 04:30 PM) — Covered by Shivam Gupta
- **Intel VTune Profiler Workflow:** Profiling multi-threaded and distributed C++ and Python applications without altering source code.
- **Hotspots Analysis:** Identifying critical functions and CPU loops consuming the greatest share of execution clock cycles.
- **Memory Access & Bandwidth Profiling:** Detecting L1/L2/LLC cache misses, DRAM bandwidth saturation, remote NUMA socket memory access penalties, and lock contention.
- **Intel Advisor Roofline Modeling:** Generating arithmetic intensity ($FLOPs/Byte$) graphs, determining whether an application kernel is compute-bound or memory-bound, and identifying compiler SIMD vectorization opportunities.
- **Distributed Training Performance Tuning:** Eliminating communication stragglers, overlapping gradient computation with communication hooks, and scaling efficiency metrics ($E = S / N$).
- **Interactive Hands-on Lab:** [Day 04 Distributed AI & VTune Colab Notebook](file:///c:/Users/Rose/Videos/GLA%20Trainings/COLAB_NOTEBOOKS/Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb).

---

### 🤖 Day 5: Generative AI, Large Language Models (LLMs) & OpenVINO Quantization
*Theme: Deploying 7B+ Parameter Transformer Models on Enterprise CPUs and Accelerators with Sub-50ms Latency.*

#### ☀️ Part 1: Morning Session (09:30 AM – 12:30 PM) — Covered by Trainer 1
- **The Generative AI Memory Wall:** Transformer architecture review (Self-Attention, Multi-Head Attention, Feed-Forward Networks). Why autoregressive LLM token generation is strictly memory-bandwidth bound ($O(1)$ arithmetic intensity per generated token).
- **KV-Cache Mathematical Scaling:** Calculating GPU/CPU memory consumption for key-value caching across sequence length ($L$), hidden dimension ($D$), and batch size ($B$).
- **Intel Hardware Acceleration for LLMs:** Intel Xeon Scalable Processors with AMX engine vs Habana Gaudi 2/Gaudi 3 Tensor Processing Cores (TPCs) and RoCE-integrated interconnects.
- **OpenVINO Architecture:** The OpenVINO Model Optimizer, Intermediate Representation (`.xml` network topology + `.bin` weights), execution plugins (CPU, GPU), and runtime dynamic shape handling.

#### 🌙 Part 2: Afternoon Session (01:30 PM – 04:30 PM) — Covered by Shivam Gupta
- **Post-Training Quantization with OpenVINO NNCF:** Neural Network Compression Framework (NNCF). Compressing FP32/FP16 transformer weights to **INT4 (AWQ / GPTQ)** with symmetric/asymmetric quantization and group size tuning.
- **Hugging Face Optimum Intel:** Zero-code model conversion and export (`optimum-cli export openvino --model meta-llama/Llama-3.2-3B --weight-format int4`).
- **Real-Time Latency Benchmarking:** Measuring and charting critical production LLM metrics:
  * **TTFT (Time to First Token):** Prompt processing latency and memory transfer overhead.
  * **TPS (Tokens Per Second):** Autoregressive decode throughput under varying concurrency.
  * **RAM Footprint Reduction:** Slashing model memory consumption from 14GB+ to under 3.5GB.
- **Distributed Fine-Tuning Principles:** Low-Rank Adaptation (LoRA) and QLoRA workflows across HPC compute nodes.
- **Capstone Project & Course Evaluation:** Orchestrating an end-to-end multi-threaded or accelerated AI pipeline, final student assessments, and certification review.
- **Interactive Hands-on Lab:** [Day 05 Generative AI & OpenVINO Colab Notebook](file:///c:/Users/Rose/Videos/GLA%20Trainings/COLAB_NOTEBOOKS/Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb).

---

## 🧭 Repository Structure & Curriculum Assets

```
📁 GLA-HPC-Masterclass/
├── 📁 00_ADMIN_AND_TRAINER_DOSSIERS/        <- Official administration dossiers, profiles & faculty bios
│   ├── GLA_HPC_TRAINER_DOSSIER_AND_MODULE_INDEX.md
│   ├── MASTER_TRAINER_AND_ACADEMIC_LEADERSHIP_DOSSIER.md
│   └── TOPIC_BY_TOPIC_CURRICULUM_INDEX_AND_SYLLABUS_MAP.md
│
├── 📁 COLAB_NOTEBOOKS/                     <- Master 1-Click Interactive Google Colab Notebooks Hub
│   ├── README.md                            <- Comprehensive Colab deployment guide
│   ├── Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb
│   ├── Day_01_Linux_Basics_Shell_Scripting_and_SSH_Colab.ipynb
│   ├── Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb
│   ├── Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb
│   ├── Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb
│   ├── Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb
│   └── Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb
│
├── 📁 HPC_Master_Curriculum/               <- Exhaustive Day-by-Day Masterclass Curriculum
│   ├── 📁 Day-01_HPC_Linux_Shell_oneAPI/
│   │   ├── 00_DAY_01_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md
│   │   ├── 01_DAY_01_6_HOUR_MASTER_TRAINER_PLAYBOOK.md
│   │   ├── 02_DAY_01_HANDS_ON_LAB_AND_COMMANDS.md
│   │   ├── 03_DAY_01_STUDENT_CHEATSHEET_AND_MCQS.md
│   │   ├── 04_DAY_01_COMPLETE_TOPIC_BY_TOPIC_STUDY_GUIDE.md
│   │   ├── 05_DAY_01_ARROW_WORKFLOWS_AND_TOPIC_TREES.md
│   │   ├── 📁 LINUX_SHELL_SCRIPTING_AND_SSH_TRAINING_MODULE/
│   │   │   ├── README.md
│   │   │   ├── LINUX_SHELL_SCRIPTING_AND_SSH_TRAINING_GUIDE.md
│   │   │   ├── Day_01_Linux_Basics_Shell_Scripting_and_SSH_Colab.ipynb
│   │   │   └── 📁 scripts/ (hpc_node_audit.sh, setup_cluster_keys.sh)
│   │   └── 📁 lab_activities/
│   │
│   ├── 📁 Day-02_Parallel_OpenMP_MPI_oneDAL/
│   │   ├── README.md                            <- Comprehensive Day 2 syllabus & lab deployment guide
│   │   ├── Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb <- Unified Master Lab (OpenMP, MPI & oneDAL)
│   │   ├── 00_DAY_02_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md
│   │   ├── 01_DAY_02_6_HOUR_MASTER_TRAINER_PLAYBOOK.md
│   │   ├── 02_DAY_02_HANDS_ON_LAB_AND_COMMANDS.md
│   │   ├── 03_DAY_02_STUDENT_CHEATSHEET_AND_MCQS.md
│   │   ├── 04_DAY_02_COMPLETE_TOPIC_BY_TOPIC_STUDY_GUIDE.md
│   │   ├── 05_DAY_02_ARROW_WORKFLOWS_AND_TOPIC_TREES.md
│   │   ├── 📁 Collab AI Updated/                <- Verified master Colab notebook source
│   │   ├── 📁 INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/
│   │   │   ├── README.md
│   │   │   ├── INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_GUIDE.md
│   │   │   ├── Day_02_Intel_AI_Analytics_and_Accelerated_ML_Colab.ipynb
│   │   │   └── 📁 scripts/ (benchmark_classical_ml_acceleration.py)
│   │   └── 📁 lab_activities/
│   │
│   ├── 📁 Day-03_DeepLearning_TF_Slurm_Horovod/
│   ├── 📁 Day-04_Distributed_Slurm_VTune_Profiling/
│   └── 📁 Day-05_GenAI_LLMs_Gaudi_OpenVINO/
│
├── 📁 MAIN_PRESENTATIONS/                  <- High-Impact HTML/Slide Decks for Projected Display
│   ├── 01_DAY_01_HPC_LINUX_ONEAPI_SLIDES.html
│   ├── 02_DAY_02_PARALLEL_OPENMP_MPI_ONEDAL_SLIDES.html
│   ├── 03_DAY_03_DEEP_LEARNING_TF_SLURM_SLIDES.html
│   ├── 04_DAY_04_DISTRIBUTED_AI_VTUNE_SLIDES.html
│   └── 05_DAY_05_GENAI_LLMS_GAUDI_OPENVINO_SLIDES.html
│
└── 📁 MASTER_TRAINER_PLAYBOOKS/            <- Integrated 30-Hour Master Teaching Execution Blueprints
```

---

## 🛠️ Quickstart Guide for Students & Participants

### Option A: 1-Click Cloud Execution (Google Colab)
1. Navigate to the [Colab Deployment Table](#-1-click-interactive-google-colab-deployment-hub) above.
2. Click the **"Open In Colab"** badge for the day and session you are attending.
3. Once the notebook opens in Google Colab, select **Runtime > Change runtime type** and ensure you are on a Python 3 runtime (T4 GPU recommended for Day 3 and Day 5).
4. Run **Section 0** to initialize your local Colab workspace and register the automated auto-sync engine (zero Drive mount required).

### Option B: On-Premises Linux Cluster / Intel Developer Cloud (IDC)
Clone the repository and explore the local modules:

```bash
# Clone the master repository
git clone https://github.com/Shivam990q/GLA-HPC-Masterclass.git
cd GLA-HPC-Masterclass

# Source Intel oneAPI environment variables (if oneAPI is installed)
source /opt/intel/oneapi/setvars.sh

# Run the automated Linux node auditor (Day 1 Afternoon lab)
bash HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/LINUX_SHELL_SCRIPTING_AND_SSH_TRAINING_MODULE/scripts/hpc_node_audit.sh

# Run the accelerated classical ML benchmark (Day 2 Afternoon lab)
python3 HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/INTEL_AI_ANALYTICS_AND_ACCELERATED_ML_TRAINING_MODULE/scripts/benchmark_classical_ml_acceleration.py
```

---

## 📜 Academic Integrity & Citation

This curriculum and its associated codebases are licensed for educational and instructional delivery at **GLA University, Mathura**. When referencing this curriculum in academic papers, theses, or technical reports, please cite:

```bibtex
@manual{gla_hpc_masterclass_2026,
  title        = {High Performance Computing & Heterogeneous AI Systems Masterclass},
  author       = {Gupta, Shivam and Garg, Rajat},
  organization = {GLA University, Department of Computer Engineering & Applications},
  year         = {2026},
  note         = {Course Code: GLA-HPC-BCSG701, in partnership with Edulateral Foundation and Intel/NEC Supercomputing Alliance}
}
```

---
*Curated and maintained with engineering rigor by **Shivam Gupta (~SEED~)** & the HPC Masterclass Team.*
