# ⚡ GLA University HPC Masterclass — Google Colab Notebooks
### 5-Day Intensive Hands-on Supercomputing Laboratories

This directory contains the official standalone Google Colab notebooks for the 5-Day HPC Masterclass. Each notebook is pre-configured with:
- **1-Click Launch**: Direct integration with Google Colab GPU/CPU runtimes.
- **Autonomous Google Drive Auto-Sync Engine**: Automatically mounts Google Drive and registers an IPython `post_run_cell` hook to continuously mirror all generated C++, Python, Slurm, and log files into your persistent Google Drive folder.
- **Dual-Mode Execution**: Run with native Intel oneAPI compilers (`icpx`, `dpcpp`, `mpicxx`) or resilient fallback emulators.
- **Forensic Verification**: End-to-end audit suites verifying all compiled binaries and reports with cryptographic SHA-256 checks.

---

## 🚀 1-Click Interactive Colab Notebooks

| Day | Topic | Direct Colab Link | Google Drive Destination |
| :---: | :--- | :---: | :--- |
| **Day 1** | **HPC Foundations, Linux Performance, Intel oneAPI & HPC Toolkit** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb) | `📁 My Drive > GLA_HPC_Masterclass_Day01/` |
| **Day 2** | **Traditional ML, Parallel Computing, OpenMP, MPI & Intel oneDAL** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb) | `📁 My Drive > GLA_HPC_Masterclass_Day02/` |
| **Day 3** | **Deep Learning Acceleration, TensorFlow, Slurm & Horovod Distributed Training** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb) | `📁 My Drive > GLA_HPC_Masterclass_Day03/` |
| **Day 4** | **Distributed AI Cluster Scaling, Multi-Node Slurm & Intel VTune Profiling** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb) | `📁 My Drive > GLA_HPC_Masterclass_Day04/` |
| **Day 5** | **Generative AI, LLMs on Intel Xeon, Habana Gaudi & OpenVINO Optimization** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb) | `📁 My Drive > GLA_HPC_Masterclass_Day05/` |

---

## 📁 Google Drive Storage Architecture

In Google Colab, container storage is ephemeral (erased after session timeout). To ensure students never lose work:

1. **Mounting Google Drive**:
   Running **Section 0** automatically mounts your Google Drive at `/content/drive/MyDrive/`.
2. **Dedicated Day Folder**:
   A dedicated folder is created under your Google Drive:
   ```
   📁 Google Drive (My Drive)
   └── 📁 GLA_HPC_Masterclass_Day0X/
       ├── 📁 src/          <- C++, Python, and SYCL source codes
       ├── 📁 bin/          <- Compiled binaries
       ├── 📁 slurm/        <- Cluster batch job scripts
       ├── 📁 reports/      <- Benchmark and profiling logs
       ├── 📁 data/         <- Input datasets
       └── 📁 sync_manifest/<- Cryptographic sync manifest & audit logs
   ```
3. **Background Auto-Sync**:
   Every time any cell runs, the registered `post_run_cell` hook detects newly created or modified files in `/content/` and automatically copies them to your Google Drive folder.
