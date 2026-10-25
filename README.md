# 🚀 GLA University — High Performance Computing & Heterogeneous AI Systems
### 5-Day Intensive Masterclass | Course Code: `GLA-HPC-BCSG701`
**Technical Alliance:** Edulateral Foundation & Intel / NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta (~SEED~) | **Co-Trainer:** Rajat Garg (Ramāpriya Das)  
**Host Institution:** Department of Computer Engineering & Applications, GLA University, Mathura  

---

## ⚡ Direct 1-Click Interactive Google Colab Labs

Launch the complete hands-on supercomputing laboratories directly in your browser with zero local installation:

| Day | Topic | Interactive Lab Badge |
| :---: | :--- | :---: |
| **Day 1** | **HPC Foundations, Linux Performance, Intel oneAPI & HPC Toolkit** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb) |
| **Day 5** | **Generative AI, LLMs on Intel Xeon, Habana Gaudi & OpenVINO Optimization** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS/Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb) |

---

## 🧭 Master 5-Day Curriculum Directory

Every Day folder in [`HPC_Master_Curriculum/`](./HPC_Master_Curriculum) is standardized with:
1. `00_DAY_0X_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md` (Complete Encyclopedia)
2. `01_DAY_0X_3_HOUR_MASTER_TRAINER_PLAYBOOK.md` (Minute-by-minute trainer execution guide)
3. `02_DAY_0X_HANDS_ON_LAB_AND_COMMANDS.md` (Copy-pasteable code, setups & troubleshooting)
4. `03_DAY_0X_STUDENT_CHEATSHEET_AND_MCQS.md` (1-page quick cheatsheet + evaluated MCQ bank)
5. `04_DAY_0X_COMPLETE_TOPIC_BY_TOPIC_STUDY_GUIDE.md` (Exhaustive first-principles notes)

---

## 🛠️ Automated Setup in Google Colab

When opening the notebook in Google Colab, execute Cell 1 to automatically mount your Google Drive and provision the full folder hierarchy:

```python
# Automatically provision Day 1 HPC environment and sync to Google Drive
from google.colab import drive
import os
from pathlib import Path

# Mount Google Drive
drive.mount('/content/drive')
drive_hpc = Path('/content/drive/MyDrive/GLA_HPC_Masterclass_Day01')
drive_hpc.mkdir(parents=True, exist_ok=True)

# Provision local workspace
workspace = Path('/content/hpc_day01')
for sub in ['scripts', 'data', 'logs', 'bin']:
    (workspace / sub).mkdir(parents=True, exist_ok=True)

print("✅ HPC Workspace & Google Drive successfully initialized!")
```

---
**Maintained by:** Shivam Gupta | Intel & NEC Supercomputing Alliance
