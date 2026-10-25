# 💾 Edulateral Foundation — Official Pen Drive Software Dump Manifest
### Offline Infrastructure & Deployment Kit for GLA University Lab PCs
**Mandate Reference**: Edulateral Operations Clause 3: *"Have dumps of all softwares required in pen drive and everybody has the presentation and necessary documents handy."*  
**Deployment Target**: GLA University Computer Science Labs (Ubuntu 20.04/22.04 LTS or RHEL/CentOS 8/9, 64-bit x86_64)

---

## 📦 1. Pen Drive Root Directory Structure

The USB 3.2 High-Speed Pen Drive (minimum 32 GB recommended, FAT32/exFAT formatted) must be structured as follows:

```
USB_ROOT/
├── 01_INSTALLERS/
│   ├── Miniconda3-latest-Linux-x86_64.sh          (Miniconda standalone installer)
│   ├── l_BaseKit_p_2024.1.0.596_offline.sh        (Intel oneAPI Base Toolkit Offline)
│   └── l_HPCKit_p_2024.1.0.595_offline.sh         (Intel oneAPI HPC Toolkit Offline)
├── 02_PYTHON_WHEELS/                             (Offline wheel repository for pip)
│   ├── numpy-1.26.4-cp310-cp310-manylinux*.whl
│   ├── scipy-1.12.0-cp310-cp310-manylinux*.whl
│   ├── pandas-2.2.1-cp310-cp310-manylinux*.whl
│   ├── scikit_learn-1.4.1.post1-cp310-*.whl
│   ├── scikit_learn_intelex-2024.2.0-*.whl       (Intel Extension for Scikit-learn)
│   ├── intel_openmp-2024.1.0-*.whl               (Intel OpenMP runtime)
│   ├── mkl-2024.1.0-*.whl                        (Intel Math Kernel Library)
│   ├── openvino-2024.1.0-*.whl                   (Intel OpenVINO runtime)
│   ├── optimum_intel-1.16.0-*.whl                (HuggingFace Optimum Intel)
│   ├── transformers-4.39.3-*.whl
│   ├── fastapi-0.110.0-*.whl
│   ├── uvicorn-0.29.0-*.whl
│   ├── horovod-0.28.1-*.whl
│   └── mpi4py-3.1.6-*.whl
├── 03_BENCHMARK_DATASETS/                        (Zero-internet synthetic datasets)
│   ├── classification_500k_20feat.parquet
│   ├── classification_500k_20feat.csv
│   ├── regression_1m_30feat.npz
│   └── mnist_offline_arrays.npz
├── 04_PRESENTATIONS_PPTX/                        (Official Edulateral Presentations)
│   ├── Day-01_HPC_Foundations_Linux_oneAPI.pptx
│   ├── Day-02_Parallel_OpenMP_MPI_oneDAL.pptx
│   ├── Day-03_DeepLearning_TensorFlow_Slurm_Horovod.pptx
│   ├── Day-04_Distributed_AI_Slurm_VTune.pptx
│   └── Day-05_GenAI_LLMs_OpenVINO_Gaudi.pptx
├── 05_STUDENT_HANDOUTS/                          (Offline PDF Reference Cards)
│   ├── Day-01_HPC_Linux_QuickRef.pdf
│   ├── Day-02_OpenMP_MPI_oneDAL_QuickRef.pdf
│   ├── Day-03_TensorFlow_Slurm_QuickRef.pdf
│   ├── Day-04_VTune_Profiling_QuickRef.pdf
│   └── Day-05_GenAI_OpenVINO_QuickRef.pdf
├── 06_EVALUATION_MCQ_BANKS/                      (Coordinator & Faculty MCQs)
│   ├── Day-01_MCQ_Question_Bank.pdf
│   ├── Day-02_MCQ_Question_Bank.pdf
│   ├── Day-03_MCQ_Question_Bank.pdf
│   ├── Day-04_MCQ_Question_Bank.pdf
│   └── Day-05_MCQ_Question_Bank.pdf
└── setup_offline_lab.sh                          (1-Click Automated Setup Bash Script)
```

---

## ⚡ 2. Automated Lab Machine Setup in 60 Seconds

When moving between lab rows or configuring student terminals with zero internet connectivity:

```bash
# 1. Mount pen drive (or navigate to mounted USB path)
cd /media/student/EDULATERAL_USB/

# 2. Execute automated 1-click installer
bash setup_offline_lab.sh

# 3. Activate the isolated training environment
conda activate hpc-edulateral

# 4. Verify Intel extensions
python -c "import sklearnex; sklearnex.patch_sklearn(); print('✅ Intel oneDAL Acceleration Active!')"
```

---

## 🛠️ 3. Verification Commands for Lead Trainer (Shivam)

Before distributing files across the lab room, execute the sanity verification checklist:

| Component | Target Verification Command | Expected Output |
| :--- | :--- | :--- |
| **Python Version** | `python --version` | `Python 3.10.x` or `3.11.x` |
| **Intel oneDAL** | `python -c "from sklearnex import patch_sklearn; patch_sklearn()"` | Patched status message without error |
| **OpenMP Runtime** | `echo $OMP_NUM_THREADS` | Matches hardware core count |
| **OpenVINO Runtime** | `python -c "import openvino as ov; print(ov.__version__)"` | `2024.x.x` |
| **Slurm CLI / Mock**| `sbatch --version` or mock fallback | Valid Slurm version output |
| **Synthetic Data** | `ls -lh 03_BENCHMARK_DATASETS/` | Valid dataset files present |

---

## 🚫 4. Strict Protocol: Zero External Internet Dependencies

In compliance with Edulateral Policy:
- Do NOT instruct students to `pip install` packages from public PyPI over GLA campus Wi-Fi.
- Do NOT instruct students to search Google, ChatGPT, or GeeksforGeeks for code solutions.
- All code exercises, solutions, and syntax references must be served locally from the `05_STUDENT_HANDOUTS/` and `HPC_Master_Curriculum/` directories on the local machine.
