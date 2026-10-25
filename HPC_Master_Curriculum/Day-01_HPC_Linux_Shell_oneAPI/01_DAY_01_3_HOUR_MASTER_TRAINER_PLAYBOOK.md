# ⏱️ DAY 1: 3-HOUR COMPLETE MASTER TRAINER PLAYBOOK
## GLA University — High Performance Computing & Heterogeneous AI Systems
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Session Duration:** Exactly 3 Hours (180 Minutes)  
**Official Syllabus Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)  
**Day 1 Complete Terminology Glossary:** [`00_DAY_01_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/00_DAY_01_MASTER_TERMINOLOGY_AND_CONCEPT_GLOSSARY.md)

---

## 🎯 1. Official Syllabus Scope (Page 2 of PDF — Strictly Preserved)

The official curriculum specifies **strictly 7 topics for Day 1**:
1. **Introduction to HPC**
2. **Intel HPC architecture (Xeon, GPUs, AI accelerators)**
3. **Linux basics: File system, commands, environment setup**
4. **Shell scripting for automation**
5. **Secured Shell (SSH)**
6. **Intel oneAPI toolkit**
7. **Introduction to Intel HPC Toolkit**

> [!IMPORTANT]
> **3-Hour Scope Discipline:**
> Topics like **OpenMP**, **MPI cluster communications**, **Machine Learning / oneDAL**, **TensorFlow-MKL**, **Slurm job queues**, **Horovod**, and **LLMs** belong strictly to Days 2 through 5. Do NOT introduce them on Day 1. Day 1 is dedicated to making 60 students completely fluent in Linux, Shell automation, SSH, and the oneAPI environment.

---

## ⏰ 2. Realistic 180-Minute (3-Hour) Delivery Timeline

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                        DAY 1 TIMELINE (TOTAL: 180 MINUTES)                               |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  00:00 - 00:30 (30m) │ PART 1: Introduction to HPC & Intel Silicon Architecture          |
|                      │        (Concepts, Xeon vs GPU vs Gaudi, Slides 1 - 9)            |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  00:30 - 01:15 (45m) │ PART 2: Linux Basics (Filesystem, Commands & Environment Setup)   |
|                      │        (Hands-on in Colab / Terminal, Slide 10)                   |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:15 - 01:45 (30m) │ PART 3: Shell Scripting for Automation                            |
|                      │        (Variables, Redirection, hpc_node_audit.sh, Slide 11)     |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:45 - 01:55 (10m) │ ☕ REJUVENATION BREAK (10 Minutes)                                |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:55 - 02:20 (25m) │ PART 4: Secured Shell (SSH) & Cluster Remote Access               |
|                      │        (Keygen, authorized_keys, Live `ssh idc-vm` Demo)         |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:20 - 02:45 (25m) │ PART 5: Intel oneAPI Toolkit & Intel HPC Toolkit                  |
|                      │        (Unified Vision, setvars.sh, Compilers, Slides 12 - 14)    |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:45 - 03:00 (15m) │ PART 6: Assessment, 22-Point Checklist & Wrap-Up                  |
|                      │        (5 Quick Student MCQs + Preview of Day 2, Slide 15)        |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 🎙️ 3. Line-by-Line Minute-by-Minute Trainer Delivery Script

### PART 1: Introduction to HPC & Intel Architecture (00:00 - 00:30 | 30 Mins)
*Slides Mapped: 1 to 9 in `Day-01_Master_Presentation.pptx`*

#### [00:00 - 00:10] Welcome, Program Pedagogy & Scope (Slides 1 - 6)
- **What Trainer Shivam Says (Hinglish/English):**
  > "Good morning everyone! Welcome to Day 1 of our intensive High Performance Computing and Heterogeneous AI Systems training at GLA University. 
  > Over the next 5 days, we are bridging the gap between writing simple code on personal laptops and engineering high-throughput cluster-scale applications.
  > Today is Day 1. Our entire objective today is to build an unbreakable foundation: understanding why HPC exists, how Intel Xeon CPUs, GPUs, and Habana Gaudi accelerators differ, mastering Linux command line, automating tasks with Shell scripts, connecting securely over SSH, and initializing the Intel oneAPI development environment.
  > Let's start with the fundamental question: Why can't we just run big AI models on our laptops?"

#### [00:10 - 00:20] Topic 1: Introduction to HPC (Slides 7 - 8)
- **Concept:** HPC vs Ordinary Computing.
- **What Trainer Shivam Says:**
  > "Look at your laptop right now. If you train a model on 10,000 rows, it works. But if you have 500 million rows or a 70-Billion parameter LLM, what happens?
  > First, your RAM runs out. Second, your memory bandwidth is choked. A typical laptop has 2 memory channels giving around 50 to 80 GB/s bandwidth. 
  > An enterprise Dual-Socket Intel Xeon Scalable server has 16 DDR5 memory channels giving over 600 GB/s bandwidth!
  > In HPC, we don't just buy a bigger laptop — we connect dozens of enterprise compute nodes using high-speed interconnects (InfiniBand or 100GbE RoCE) and shared parallel filesystems. HPC combines compute power to solve problems that are computationally impossible on single workstations."
- **Whiteboard Sketch 1 (Draw on board):**
  ```
  [ Laptop / Workstation ]                 [ HPC Cluster Architecture ]
  +----------------------+                 +------------+     +------------+
  | CPU (8-16 Cores)     |                 | Head Node  |     | Compute 01 |
  | RAM: 16 GB (Dual-Ch) |                 +-----+------+     +-----+------+
  | Local NVMe: ~3 GB/s  |                       | (High-Speed Fabric) |
  +----------------------+                 +-----+------+     +-----+------+
  (Bottlenecked by single node)            | Compute 02 | ... | Compute N  |
                                           +------------+     +------------+
                                           (Shared Parallel Storage: Lustre/GPFS)
  ```

#### [00:20 - 00:30] Topic 2: Intel HPC Architecture (Slide 9)
- **Concept:** CPU vs GPU vs AI Accelerators.
- **What Trainer Shivam Says:**
  > "Modern supercomputers are heterogeneous. There is no single chip that is best at everything. Intel's architecture divides workloads across three distinct silicon engines:
  > 1. **Intel Xeon Scalable CPUs (Sapphire Rapids / Emerald Rapids):**
  >    - Few, very heavy, high-clock cores (32 to 64 cores per socket).
  >    - Built for low-latency sequential logic, OS orchestration, data preprocessing, and high-precision FP64 math.
  >    - Secret Weapon: **Intel AMX (Advanced Matrix Extensions)** — built-in hardware matrix acceleration on the CPU die!
  > 2. **Intel Data Center GPUs (Max Series / Ponte Vecchio):**
  >    - Thousands of lightweight SIMD vector cores executing millions of threads in parallel.
  >    - Built for massive FP32/FP16 matrix multiplication and computer vision.
  > 3. **AI Accelerators (Habana Gaudi 2 / Gaudi 3):**
  >    - Built from the silicon up purely for AI tensors and Transformers.
  >    - Features 24 Tensor Processor Cores (TPCs) and integrated 24x 100GbE RoCE networking directly on-die!
  > Remember this rule: Xeon orchestrates and preprocesses; GPUs accelerate graphics and general matrix math; Gaudi accelerates massive LLM training."

---

### PART 2: Linux Basics (00:30 - 01:15 | 45 Mins)
*Slide Mapped: 10 in `Day-01_Master_Presentation.pptx` | Colab Cells: 1 to 6*

#### [00:30 - 00:45] Filesystem Hierarchy & Paths
- **What Trainer Shivam Says:**
  > "Open your Google Colab notebook right now. Notice: Google Colab is running on an Ubuntu Linux container!
  > In Windows, you have drive letters: `C:\`, `D:\`. In Linux, there are no drive letters. **Everything is a tree starting at the root `/`**.
  > And the core rule of UNIX is: *Everything is a file!*
  > Let's understand paths:
  > - **Absolute Path:** Starts from the root `/`. Example: `/home/user/project/script.sh`. Unambiguous from anywhere.
  > - **Relative Path:** Starts from where you currently are (Current Working Directory). Example: `./script.sh` or `../data/file.csv`.
  > Let's run `pwd` (Print Working Directory) and `ls -la` in our notebook."

#### [00:45 - 01:00] Core Linux Commands & Practice
- **Commands Taught:** `pwd`, `cd`, `ls -la`, `mkdir -p`, `touch`, `cp`, `mv`, `rm`, `cat`, `head`, `tail`, `grep`.
- **Live Hands-on Sequence:**
  ```bash
  # 1. Check working directory
  pwd

  # 2. Create structured directories
  mkdir -p ~/hpc_workspace/day01/{scripts,data,logs}

  # 3. Create a test configuration file
  cat << 'EOF' > ~/hpc_workspace/day01/scripts/config.env
  CLUSTER_NAME="GLA_Intel_HPC"
  NODE_COUNT=4
  MAX_THREADS=32
  EOF

  # 4. View and filter contents
  cat ~/hpc_workspace/day01/scripts/config.env
  grep "NODE_COUNT" ~/hpc_workspace/day01/scripts/config.env
  ```
- **Trainer Gotcha Warning:**
  > "Caution: In Linux, `rm` is permanent! There is no Recycle Bin or Trash can on a remote HPC terminal. Once deleted, your file is gone."

#### [01:00 - 01:15] Environment Setup & `$PATH`
- **What Trainer Shivam Says:**
  > "How does Linux know what to do when you type `python` or `gcc`? It searches the `$PATH` environment variable!
  > An environment variable is a dynamic named value stored in system memory.
  > Let's see our current path: `echo $PATH`.
  > Notice it is a colon-separated list of directories: `/usr/local/bin:/usr/bin:/bin`. Linux scans these folders from left to right.
  > If we install Intel oneAPI in `/opt/intel/oneapi`, our system won't find `icpx` until we add it to `$PATH`! This is why environment setup is critical."

---

### PART 3: Shell Scripting for Automation (01:15 - 01:45 | 30 Mins)
*Slide Mapped: 11 in `Day-01_Master_Presentation.pptx` | Colab Cells: 7 to 9*

#### [01:15 - 01:30] The Shebang, Variables, and Permissions
- **What Trainer Shivam Says:**
  > "Why do supercomputing engineers write Shell scripts instead of typing commands manually?
  > Because in HPC, workflows have 20 steps: loading modules, allocating nodes, copying weights, launching jobs, and collecting logs. Doing that manually causes human errors. A Shell script guarantees 100% reproducible execution.
  > Every bash script starts with line 1: `#!/bin/bash`. This is called the **Shebang**. It tells the operating system kernel which interpreter to use.
  > Second rule: `VAR="value"` — NEVER put spaces around `=` in bash!
  > Third rule: `chmod +x script.sh` — by default, newly created files do NOT have execute permissions. You must add `+x`."

#### [01:30 - 01:45] Hands-On: Writing the Node Audit Script
- **What Students Run in Colab (Cell 8):**
  ```bash
  cat << 'EOF' > hpc_node_audit.sh
  #!/bin/bash
  set -e
  echo "=========================================="
  echo "  HPC NODE HARDWARE AUDIT REPORT"
  echo "  Timestamp: $(date)"
  echo "=========================================="
  echo "1. Hostname:      $(hostname)"
  echo "2. Kernel:        $(uname -r)"
  echo "3. CPU Model:     $(lscpu | grep 'Model name:' | sed 's/Model name:[ \t]*//')"
  echo "4. Total Cores:   $(nproc)"
  echo "5. Total Memory:  $(free -h | awk '/^Mem:/ {print $2}')"
  echo "=========================================="
  EOF

  chmod +x hpc_node_audit.sh
  ./hpc_node_audit.sh
  ```
- **Trainer Check:** Ensure all 60 students execute this script and see their Colab CPU and RAM specs on screen!

---

### ☕ BREAK (01:45 - 01:55 | 10 Minutes)
*Students stretch, check Colab status, and prepare for the remote cluster demonstration.*

---

### PART 4: Secured Shell (SSH) & Remote Access (01:55 - 02:20 | 25 Mins)
*Slide Mapped: 11 in `Day-01_Master_Presentation.pptx` | Live Terminal Demo*

#### [01:55 - 02:10] Local vs Remote, SSH Architecture & Key Pairs
- **What Trainer Shivam Says:**
  > "Nobody sits in an air-conditioned datacenter with a monitor plugged into a supercomputer. Every supercomputer in the world is managed remotely over **SSH (Secure Shell)** on TCP Port 22.
  > How does SSH work?
  > - **Password Authentication:** Slow, prone to brute-force attacks, cannot be automated easily.
  > - **Key-Based Authentication (Asymmetric Cryptography):**
  >   1. You generate an `ed25519` key pair on your machine using `ssh-keygen`.
  >   2. You get two keys: `id_ed25519` (Private Key — NEVER share!) and `id_ed25519.pub` (Public Key).
  >   3. The public key is placed in the remote server's `~/.ssh/authorized_keys`.
  >   4. When connecting, the server encrypts a challenge with your public key; your client proves identity using your private key. Fast, 100% secure, passwordless!"

#### [02:10 - 02:20] Live Trainer Demo: Connecting to Enterprise Intel Cluster (`idc-vm`)
- **Trainer Action (Show on Projector):**
  ```bash
  ssh idc-vm
  ```
- **Trainer Script:**
  > "Watch my terminal screen on the projector right now. I just typed `ssh idc-vm`. 
  > I am now connected live via Tailscale to our bare-metal Intel Developer Cloud node running a real **4th Gen Intel Xeon Gold 6442Y (Sapphire Rapids)** processor!
  > Let's verify: `lscpu | grep -E 'Model name|avx512|amx'`.
  > Notice the flags: `avx512_bf16` and `amx_tile`. This is genuine enterprise supercomputing hardware."

---

### PART 5: Intel oneAPI Toolkit & HPC Toolkit (02:20 - 02:45 | 25 Mins)
*Slides Mapped: 12 - 14 in `Day-01_Master_Presentation.pptx` | Colab Cells: 10 - 15*

#### [02:20 - 02:35] Topic 6: Intel oneAPI Toolkit (Slide 12)
- **Concept:** Cross-architecture programming model.
- **What Trainer Shivam Says:**
  > "Historically, if you wrote GPU code for NVIDIA, you had to use proprietary CUDA. If you wrote for Intel or AMD, you had to rewrite everything in OpenCL.
  > **Intel oneAPI is an open, standards-based, cross-architecture programming model**.
  > It uses **SYCL** (Standard C++ heterogeneous abstraction). You write single-source modern C++ code, and oneAPI compiles it to run on CPUs, GPUs, and FPGAs!
  > To activate oneAPI in any terminal, you run:
  > `source /opt/intel/oneapi/setvars.sh`
  > This script automatically configures `$PATH`, `$LD_LIBRARY_PATH`, and compiler environment variables."

#### [02:35 - 02:45] Topic 7: Introduction to Intel HPC Toolkit (Slide 13 - 14)
- **Concept:** Base Toolkit vs HPC Toolkit.
- **What Trainer Shivam Says:**
  > "What is the difference between the Base oneAPI Toolkit and the HPC Toolkit?
  > - **Base Toolkit:** Core DPC++/SYCL compiler, oneMKL (Math Kernel Library), oneDAL (Data Analytics), and oneDNN (Deep Learning).
  > - **HPC Toolkit:** Layers on top of Base Toolkit for cluster supercomputing. It includes:
  >   1. `icx` & `icpx` (Intel C/C++ Compilers with advanced vectorization)
  >   2. `ifx` (Intel Fortran Compiler for legacy scientific simulations)
  >   3. `Intel MPI Library` (Multi-fabric message passing for multi-node communication)
  >   4. `Intel Inspector` (Memory and thread error debugger)
  > Tomorrow on Day 2, we will use these exact tools to write parallel OpenMP and MPI programs!"

---

### PART 6: Assessment, 22-Point Checklist & Wrap-Up (02:45 - 03:00 | 15 Mins)
*Slide Mapped: 15 in `Day-01_Master_Presentation.pptx` | Colab Cells: 25 - 26*

#### [02:45 - 02:55] 5-Question Quick Classroom Check
1. *Q1: What does HPC stand for and why do ordinary laptops fail on large AI models?*  
   **Answer:** High Performance Computing. Laptops fail due to memory wall (limited DDR bandwidth) and single-node compute limits.
2. *Q2: Name the 3 hardware pillars of Intel HPC architecture and their primary roles.*  
   **Answer:** Intel Xeon CPUs (orchestration/preprocessing), Intel GPUs (massive parallel matrix/vector math), Habana Gaudi (deep learning/LLM training).
3. *Q3: What is the difference between an absolute path and a relative path in Linux?*  
   **Answer:** Absolute path starts from root `/`; relative path starts from Current Working Directory.
4. *Q4: Why is key-based SSH authentication preferred over passwords in HPC clusters?*  
   **Answer:** Key-based uses asymmetric cryptography (`ed25519`), eliminates brute-force vulnerability, and enables passwordless automated batch jobs.
5. *Q5: What command initializes the Intel oneAPI development environment?*  
   **Answer:** `source /opt/intel/oneapi/setvars.sh`.

#### [02:55 - 03:00] Day 1 Wrap-Up & Preview of Day 2
- **What Trainer Shivam Says:**
  > "Outstanding work today everyone! In exactly 3 hours, we covered all 7 topics of Day 1: HPC concepts, Intel silicon architecture, Linux filesystem, Shell automation, SSH remote access, and oneAPI environment setup.
  > Tomorrow on Day 2, we break the serial bottleneck! We will learn OpenMP multithreading, MPI distributed computing, and accelerate Scikit-Learn models using Intel oneDAL. Have a great evening, see you tomorrow morning at 9:00 AM sharp!"

---

## 🛠️ 4. Top 5 Student Gotchas & 30-Second Rapid Fixes

| Issue Encountered | Why It Happened | 30-Second Trainer Fix |
| :--- | :--- | :--- |
| `bash: ./script.sh: Permission denied` | Created file lacks executable bit | Run `chmod +x script.sh` |
| `command not found: VAR="val"` | Student put spaces around `=` | Explain: Bash treats spaces as delimiters; use `VAR="val"` |
| `cd: No such file or directory` | Used relative path from wrong folder | Run `pwd` first, then use absolute path `cd ~/hpc_workspace` |
| `icpx: command not found` | oneAPI environment not sourced | Run `source /opt/intel/oneapi/setvars.sh` |
| Colab disconnected / kernel died | Memory exceeded in background | Restart runtime (`Runtime -> Restart session`) and re-run cell |
