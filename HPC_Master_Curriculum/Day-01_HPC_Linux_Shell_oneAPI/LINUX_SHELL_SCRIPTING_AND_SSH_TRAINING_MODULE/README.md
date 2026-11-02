# 🐧 Linux Basics, Shell Scripting for Automation & Secured Shell (SSH)
## Complete Master Training Package & Curriculum Kit

**Target Audience:** Engineering Students, HPC Practitioners & Cloud Engineers  
**Institutional Track:** GLA University — High Performance Computing & System Engineering  
**Curriculum Alignment:** Day 1 Official Syllabus Core (Linux Basics, Shell Automation, SSH)  
**Lead Trainer:** Shivam Gupta  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/Day_01_Linux_Basics_Shell_Scripting_and_SSH_Colab.ipynb)
[![GitHub Repository](https://img.shields.io/badge/GitHub-GLA--HPC--Masterclass-181717?logo=github)](https://github.com/Shivam990q/GLA-HPC-Masterclass)

---

## 🚀 Interactive Google Colab Notebook (Zero Setup Required)

Students can launch the complete hands-on interactive laboratory directly in their web browser without installing anything locally:

👉 **[Launch Interactive Colab: `Day_01_Linux_Basics_Shell_Scripting_and_SSH_Colab.ipynb`](https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/Day_01_Linux_Basics_Shell_Scripting_and_SSH_Colab.ipynb)**

- **Scope:** Basic to Medium hands-on practice (Zero fluff, zero cognitive overload).
- **Environment:** Ubuntu Linux runtime on Google Cloud VM using `%%bash` cell execution.
- **Coverage:**
  1. Linux Filesystem Navigation, File Inspection & Permissions Math (755/644/600).
  2. Linux Streams, Redirection (`>`, `>>`, `2>&1`, `/dev/null`) & Pipelines (`grep`, `awk`, `sort`, `uniq`).
  3. Environment Variables, Custom Tools, `$PATH` Export & `.bashrc` Configuration.
  4. Bash Scripting (Shebang, `$1`, `$#`, `$@`, `$?`, `if/else`, `for/while` loops, and Automated Backup Script).
  5. Secured Shell (SSH) Ed25519 Keypairs, `authorized_keys`, `~/.ssh/config` Aliases, and `scp`/`rsync`.
  6. Three Interactive Student Challenges with automated verification checks.

---

## 📂 Module Package Directory Structure

This dedicated module folder contains everything required for a world-class training delivery—from conceptual classroom theory and step-by-step whiteboard notes to live terminal demos, runnable automation scripts, hands-on student lab activities, an interactive Google Colab notebook, and an exhaustive 50-question MCQ assessment bank.

```
LINUX_SHELL_SCRIPTING_AND_SSH_TRAINING_MODULE/
│
├── README.md                                   # Master Navigation & Module Blueprint
├── Day_01_Linux_Basics_Shell_Scripting_and_SSH_Colab.ipynb # Interactive Google Colab Notebook
│
├── 01_THEORY_AND_TRAINER_LECTURE_GUIDE.md      # Complete Lecture Notes, Concept Deconstructions & Pedagogy
│   ├── Topic 1: Linux Architecture & Filesystem Hierarchy Standard (FHS)
│   ├── Topic 2: Essential Linux Command Ergonomics & VFS Mechanics
│   ├── Topic 3: Linux Permissions, Ownership & Security (chmod, chown, umask)
│   ├── Topic 4: Linux Environment Setup ($PATH, startup files, export, .bashrc)
│   ├── Topic 5: Shell Scripting Foundations (Shebang, variables, parameters, return codes)
│   ├── Topic 6: Shell Control Flow (Conditionals, loops, functions, error handling)
│   ├── Topic 7: Streams, Redirection, Pipes & Text Processing (grep, sed, awk)
│   └── Topic 8: Secured Shell (SSH) Architecture, Crypto, Keys, Config, Tunneling & Hardening
│
├── 02_LIVE_DEMOS_AND_CODE_WALKTHROUGH.md       # Exact Terminal Commands to Project on Screen Live
│   ├── Demo 1: Filesystem Navigation & Hardware Introspection
│   ├── Demo 2: File Creation, Heredocs & Permission Math (755/644/600)
│   ├── Demo 3: Environment Setup, Custom Binaries & $PATH Export
│   ├── Demo 4: Interactive vs Non-Interactive Shell Script Execution
│   ├── Demo 5: Streams, Pipeline Chaining & sed/awk Filtering
│   ├── Demo 6: Asymmetric Cryptography & Passwordless SSH Key Pair Generation
│   ├── Demo 7: SSH Client Config Optimization (~/.ssh/config)
│   └── Demo 8: Remote File Sync (rsync/scp) & Local/Dynamic Port Forwarding
│
├── 03_HANDS_ON_STUDENT_LAB_ACTIVITIES.md       # 8 Graded Hands-On Student Lab Challenges
│   ├── Lab 1: Linux Filesystem Scavenger Hunt & Permissions Fixer
│   ├── Lab 2: Custom Environment Setup & Binary Path Extension
│   ├── Lab 3: Interactive System Greeting & Hardware Probe Script
│   ├── Lab 4: Log File Extraction & Forensic Filtering with grep/awk
│   ├── Lab 5: Production Log Rotation & Timestamped Backup Engine
│   ├── Lab 6: End-to-End Passwordless SSH Cluster Key Exchange
│   ├── Lab 7: Multi-Host SSH Config Optimization & Alias Routing
│   └── Lab 8: SSH Port Forwarding Tunnel for Remote Web/Jupyter Dashboard
│
├── 04_AUTOMATION_SCRIPTS_COLLECTION/           # 5 Standalone, Production-Grade Runnable Bash Scripts
│   ├── 01_system_health_audit.sh              # Real-time Hardware, RAM, Disk, CPU & Load Monitor
│   ├── 02_automated_backup_and_archive.sh     # Compressed Tar/Gzip Archiver with SHA256 & 7-Day Purge
│   ├── 03_batch_user_provisioning.sh          # Enterprise Batch User & Group Creator with Skeletal rc
│   ├── 04_log_analyzer_report.sh              # Forensic Log Parser (Failed SSH Logins, HTTP Codes)
│   └── 05_ssh_cluster_node_sync.sh            # Cluster Multi-Node SSH Health & Config Sync Probe
│
├── 05_MCQ_ASSESSMENT_BANK.md                   # 50 High-Yield MCQs with Forensic Rationales
│   ├── Section A: Linux Basics, FHS & Environment (15 Questions)
│   ├── Section B: Shell Scripting, Control Flow & Text Processing (20 Questions)
│   └── Section C: Secured Shell (SSH), Keys, Tunneling & Security (15 Questions)
│
└── 06_QUICK_REFERENCE_CHEAT_SHEET.md          # 2-Page High-Density Command & Syntax Reference Card
```

---

## 🎯 Pedagogical Delivery Flow (3-Hour Theory + 3-Hour Lab)

| Stage | Duration | Core Focus | Supporting File |
|:---:|:---:|:---|:---|
| **Phase 1** | 60 mins | **Linux Basics & Environment**: Philosophy, FHS, core commands, permissions (octal 755/600), `$PATH` variable & `.bashrc`. | `01_THEORY...` & `02_LIVE_DEMOS...` (Demos 1-3) |
| **Phase 2** | 60 mins | **Shell Scripting for Automation**: Shebang, variables, positional args, exit codes, conditionals, loops, functions, pipes & `awk/sed`. | `01_THEORY...` & `02_LIVE_DEMOS...` (Demos 4-5) |
| **Phase 3** | 60 mins | **Secured Shell (SSH)**: Public/private keys, `ssh-keygen`, `ssh-copy-id`, `~/.ssh/config`, permissions (700/600), tunneling & hardening. | `01_THEORY...` & `02_LIVE_DEMOS...` (Demos 6-8) |
| **Phase 4** | 120 mins| **Student Hands-On Lab Drills**: Students work through Labs 1 to 8 with real-time trainer guidance. | `03_HANDS_ON_STUDENT_LAB_ACTIVITIES.md` |
| **Phase 5** | 30 mins | **Live Script Execution & Code Review**: Running and customizing the 5 production automation scripts. | `04_AUTOMATION_SCRIPTS_COLLECTION/` |
| **Phase 6** | 30 mins | **Final Knowledge Assessment**: Administering the 50 MCQs with live concept debriefing. | `05_MCQ_ASSESSMENT_BANK.md` |

---

## ⚡ Quick Start for Trainers
1. Open [`01_THEORY_AND_TRAINER_LECTURE_GUIDE.md`](./01_THEORY_AND_TRAINER_LECTURE_GUIDE.md) as your teaching guide during lecture delivery.
2. Open [`02_LIVE_DEMOS_AND_CODE_WALKTHROUGH.md`](./02_LIVE_DEMOS_AND_CODE_WALKTHROUGH.md) in your secondary terminal to project live demonstrations.
3. Distribute [`03_HANDS_ON_STUDENT_LAB_ACTIVITIES.md`](./03_HANDS_ON_STUDENT_LAB_ACTIVITIES.md) and [`06_QUICK_REFERENCE_CHEAT_SHEET.md`](./06_QUICK_REFERENCE_CHEAT_SHEET.md) to students.
4. Run the automated scripts in [`04_AUTOMATION_SCRIPTS_COLLECTION/`](./04_AUTOMATION_SCRIPTS_COLLECTION/) to showcase industrial automation.
5. Evaluate students using [`05_MCQ_ASSESSMENT_BANK.md`](./05_MCQ_ASSESSMENT_BANK.md).
