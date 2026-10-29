# High Performance Computing: A Practical Approach (Intel & NEC Edition)
### Official Master Training Repository @ GLA University
**Partner Organizations**: Edulateral Foundation & Intel & NEC Supercomputing  
**Client / University**: GLA University, Mathura (Department of Computer Science & Engineering)  
**Program Dates**: November 16th – November 20th, 2026 (5 Days | 6 Hours Per Day = 30 Total Class Hours)  
**Daily Schedule**: Session 1: Morning 3h Theory & Architecture | Session 2: Afternoon 3h Hands-On Server Lab  
**Lead Trainer**: Shivam Gupta (~Shivam 🌱SEED🐍) | **Co-Trainer / Counterpart**: Rajat Garg (Ramāpriya Das)  
**Operations Lead**: Pedina Sreeja (+91 9861773390 | sreeja@edulateral.com)  

---

## 🏛️ Executive Curriculum Architecture (6 Hours Per Day)

This repository contains the streamlined, highly practical 5-day curriculum for High Performance Computing (HPC), AI acceleration, and distributed deep learning, engineered specifically for **6-Hour Daily Masterclass Delivery** (3 Hours Morning Architecture & Theory + 3 Hours Afternoon Server Lab) at GLA University, Mathura.

---

## 🗂️ Clean, Structured Day-Wise Architecture (Zero Clutter)

All presentation slide decks (`.pptx`) are centralized in [`MAIN_PRESENTATIONS/`](file:///c:/Users/Rose/Videos/GLA%20Trainings/MAIN_PRESENTATIONS).  
Inside `HPC_Master_Curriculum/`, every day follows an identical, standardized layout with **6 comprehensive guide files + 1 lab activities directory + 1 assessment suite**:

```text
HPC_Master_Curriculum/
├── 📁 00_ADMIN_AND_TRAINER_DOSSIERS/                  (Compliance & Strategy)
│
├── 📁 Day-01_HPC_Linux_Shell_oneAPI/                 [SHIVAM EXPERT LEAD - DAY 1]
│   ├── 00_DAY_01_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md
│   ├── 01_DAY_01_6_HOUR_MASTER_TRAINER_PLAYBOOK.md   (Complete 6-Hour Script, Whiteboard Sketches, Gotchas)
│   ├── 02_DAY_01_HANDS_ON_LAB_AND_COMMANDS.md        (Step-by-Step Hands-On Commands & Output Verification)
│   ├── 03_DAY_01_STUDENT_CHEATSHEET_AND_MCQS.md     (Cheat Sheet + 50 Evaluated Pre/In-Class MCQs)
│   ├── 04_DAY_01_COMPLETE_TOPIC_BY_TOPIC_STUDY_GUIDE.md
│   ├── 05_DAY_01_ARROW_WORKFLOWS_AND_TOPIC_TREES.md
│   ├── 📁 lab_activities/                            (Interactive Colab Lab & Standalone code/)
│   └── 📁 quizzes_and_assessments/                   (Pre-Assessment, In-Class Checkpoints & Post-Assessment MCQs, Excel, CSV)
│
├── 📁 Day-02_Parallel_OpenMP_MPI_oneDAL/             [DAY 2: PARALLEL COMPUTING]
│   ├── 00_DAY_02_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md
│   ├── 01_DAY_02_6_HOUR_MASTER_TRAINER_PLAYBOOK.md   (Complete 6-Hour Script, OpenMP Pragmas, oneDAL)
│   ├── 02_DAY_02_HANDS_ON_LAB_AND_COMMANDS.md        (Step-by-Step OpenMP C++ & sklearnex Benchmarks)
│   ├── 03_DAY_02_STUDENT_CHEATSHEET_AND_MCQS.md     (Cheat Sheet + Evaluated MCQs)
│   ├── 04_DAY_02_COMPLETE_TOPIC_BY_TOPIC_STUDY_GUIDE.md
│   ├── 05_DAY_02_ARROW_WORKFLOWS_AND_TOPIC_TREES.md
│   ├── 📁 lab_activities/                            (Interactive Colab Lab & Standalone code/)
│   └── 📁 quizzes_and_assessments/                   (Pre-Assessment, In-Class Checkpoints & Post-Assessment MCQs, Excel, CSV)
│
├── 📁 Day-03_DeepLearning_TF_Slurm_Horovod/          [DAY 3: DEEP LEARNING, SLURM & HOROVOD]
│   ├── 00_DAY_03_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md
│   ├── 01_DAY_03_6_HOUR_MASTER_TRAINER_PLAYBOOK.md   (Complete 6-Hour Script, oneDNN Fusion, Slurm & Horovod)
│   ├── 02_DAY_03_HANDS_ON_LAB_AND_COMMANDS.md        (Step-by-Step oneDNN TF & #SBATCH Slurm Scripts)
│   ├── 03_DAY_03_STUDENT_CHEATSHEET_AND_MCQS.md     (Cheat Sheet + Evaluated MCQs)
│   ├── 04_DAY_03_COMPLETE_TOPIC_BY_TOPIC_STUDY_GUIDE.md
│   ├── 05_DAY_03_ARROW_WORKFLOWS_AND_TOPIC_TREES.md
│   ├── 📁 lab_activities/                            (Interactive Colab Lab & Standalone code/)
│   └── 📁 quizzes_and_assessments/                   (Pre-Assessment, In-Class Checkpoints & Post-Assessment MCQs, Excel, CSV)
│
├── 📁 Day-04_Distributed_Slurm_VTune_Profiling/      [DAY 4: DISTRIBUTED SLURM & VTUNE PROFILING]
│   ├── 00_DAY_04_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md
│   ├── 01_DAY_04_6_HOUR_MASTER_TRAINER_PLAYBOOK.md   (Complete 6-Hour Script, Top-Down TMAM & Slurm Scaling)
│   ├── 02_DAY_04_HANDS_ON_LAB_AND_COMMANDS.md        (Step-by-Step VTune CLI Profiling & Diagnostics)
│   ├── 03_DAY_04_STUDENT_CHEATSHEET_AND_MCQS.md     (Cheat Sheet + Evaluated MCQs)
│   ├── 04_DAY_04_COMPLETE_TOPIC_BY_TOPIC_STUDY_GUIDE.md
│   ├── 05_DAY_04_ARROW_WORKFLOWS_AND_TOPIC_TREES.md
│   ├── 📁 lab_activities/                            (Interactive Colab Lab & Standalone code/)
│   └── 📁 quizzes_and_assessments/                   (Pre-Assessment, In-Class Checkpoints & Post-Assessment MCQs, Excel, CSV)
│
├── 📁 Day-05_GenAI_LLMs_Gaudi_OpenVINO/              [SHIVAM EXPERT LEAD - DAY 5 CAPSTONE]
│   ├── 00_DAY_05_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md
│   ├── 01_DAY_05_6_HOUR_MASTER_TRAINER_PLAYBOOK.md   (Complete 6-Hour Script, Xeon AMX, Gaudi 2/3, OpenVINO INT4 & LoRA)
│   ├── 02_DAY_05_HANDS_ON_LAB_AND_COMMANDS.md        (Step-by-Step OpenVINO NNCF, FastAPI & Slurm Multi-Node)
│   ├── 03_DAY_05_STUDENT_CHEATSHEET_AND_MCQS.md     (Cheat Sheet + Evaluated MCQs)
│   ├── 04_DAY_05_COMPLETE_TOPIC_BY_TOPIC_STUDY_GUIDE.md
│   ├── 05_DAY_05_ARROW_WORKFLOWS_AND_TOPIC_TREES.md
│   ├── 📁 lab_activities/                            (Interactive Colab Lab & Standalone code/)
│   └── 📁 quizzes_and_assessments/                   (Pre-Assessment, In-Class Checkpoints & Post-Assessment MCQs, Excel, CSV)
│
├── 📁 EDULATERAL_OFFICIAL_MCQ_BANK/                  (Consolidated 125 Evaluative MCQs & Quiz Engine)
├── 📁 OFFLINE_PENDRIVE_TOOLKIT/                      (Offline Pen Drive Safeguard)
├── 📄 MASTER_CURRICULUM_AND_KNOWLEDGE_GRAPH_INDEX.md (Master Navigational Index)
└── 📄 README.md                                      (This Document)
```

---

## ⚡ Verification & Execution Directives

1. **All Python code**: 100% compiled with zero syntax errors (`python -m py_compile`).
2. **Offline autonomy**: 100% executable without campus Wi-Fi or internet.
3. **Legal compliance**: 100% adherent to Edulateral Foundation branding, non-disclosure, and anti-competitor mandates.
