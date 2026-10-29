# 🔬 DAY 1: HANDS-ON LAB ACTIVITIES & RUNTIMES
## GLA University — High Performance Computing & Heterogeneous AI Systems
**Course Code:** `GLA-HPC-BCSG701` | **Lead Trainer:** Shivam Gupta  
**Official Curriculum Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 📌 Directory Contents & Execution Artifacts

This directory contains the complete practical execution environment for Day 1:

| Artifact | Type | Description |
| :--- | :---: | :--- |
| [`Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/lab_activities/Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb) | Jupyter Notebook | **Master Colab Lab (34 Cells):** Silicon introspection (`lscpu`, cache lines, AMX flags), shell automation (`hpc_node_audit.sh`), SYCL device queries, 10M vector add, GEMM matrix multiply, loop vectorization flags, and self-grading interactive quiz runner. |
| [`code/`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/lab_activities/code) | Directory | Standalone scripts and code templates for running directly on Linux cluster nodes (`idc-vm` / server VMs). |

---

## 🚀 Dual-Lab Execution Modes

### Mode 1: Google Colab (Zero-Friction Student Sandbox)
* Open [`Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/lab_activities/Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb) in Google Colab.
* Run cells sequentially. Every DPC++/SYCL cell includes an automatic high-performance C++20 / OpenMP fallback, guaranteeing 100% execution success even if Intel packages are not pre-installed.

### Mode 2: Dedicated Enterprise Server VM (`idc-vm`)
* SSH into the bare-metal Intel Developer Cloud node: `ssh idc-vm`.
* Run the node audit script: `./hpc_node_audit.sh`.
* Source the oneAPI environment: `source /opt/intel/oneapi/setvars.sh`.
* Inspect genuine Xeon Sapphire Rapids hardware flags: `lscpu | grep -E 'avx512|amx'`.
