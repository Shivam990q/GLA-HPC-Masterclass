# 📝 GLA UNIVERSITY // DAY 1 IN-CLASS CONCEPT CHECKPOINT (STUDENT QUESTION PAPER)
## High Performance Computing & Heterogeneous AI Systems (`GLA-HPC-BCSG701`)
**Date:** Day 1 Masterclass | **Duration:** Active Lecture Checkpoints | **Total Marks:** 25 Marks  

**Instructions for Students:**
1. Select the single best answer (a, b, c, or d) for each question as presented during the lecture.
2. Note your reasoning before the instructor reveals the architectural mechanism.

---

#### Question 01: Why do large AI models (e.g., 70-Billion parameter LLMs) fail to train efficiently on high-end consumer laptops despite having fast CPUs?
- **a)** Laptops lack sufficient DDR memory channels and bandwidth (choked by the Memory Wall)
- **b)** Laptops do not support floating-point arithmetic
- **c)** Windows OS permanently limits memory allocation to 4 GB
- **d)** Laptop CPUs cannot execute C++ code

---

#### Question 02: Under Flynn's classical computer architecture taxonomy, which architectural model best describes modern GPUs and CPU vector execution units (AVX-512)?
- **a)** SISD (Single Instruction, Single Data)
- **b)** SIMD (Single Instruction, Multiple Data)
- **c)** MISD (Multiple Instruction, Single Data)
- **d)** MIMD (Multiple Instruction, Multiple Data)

---

#### Question 03: An HPC simulation contains a sequential fraction of 10% that cannot be parallelized. According to Amdahl's Law, what is the theoretical maximum speedup limit, even with an infinite number of processor cores?
- **a)** 100x speedup
- **b)** 10x speedup
- **c)** 50x speedup
- **d)** Infinite speedup

---

#### Question 04: In an enterprise heterogeneous supercomputing cluster, what is the primary architectural responsibility of Intel Xeon Scalable processors?
- **a)** High-latency batch graphics rendering only
- **b)** Orchestrating workflows, managing OS scheduling, preprocessing tensors, and handling irregular sequential logic
- **c)** Replacing all network switches in the datacenter
- **d)** Acting exclusively as passive memory controllers

---

#### Question 05: What specific hardware capability is introduced on 4th Gen Intel Xeon Scalable processors (Sapphire Rapids) via Intel AMX (Advanced Matrix Extensions)?
- **a)** Integrated liquid nitrogen cooling controllers
- **b)** Dedicated 2D tile registers (TMM0-TMM7) and matrix multiplication units (TMUL) accelerating deep learning on the CPU die
- **c)** Hardware emulation of 8-bit retro video game graphics
- **d)** Direct connection to SATA-1 mechanical hard drives

---

#### Question 06: Which computational workload is the Intel Data Center GPU Max Series (formerly code-named Ponte Vecchio) primarily architected to accelerate?
- **a)** Massive parallel floating-point vector/matrix simulations and high-density FP64/FP32 scientific computing
- **b)** Single-threaded shell script execution
- **c)** Low-speed serial ASCII text parsing
- **d)** Managing Linux user account passwords

---

#### Question 07: How does the Habana Gaudi 2 AI accelerator achieve scale-out multi-node cluster training without requiring external discrete InfiniBand PCIe host channel adapters (HCAs)?
- **a)** By transmitting data across standard USB 2.0 cables
- **b)** By integrating 24x 100GbE RoCE (RDMA over Converged Ethernet) ports directly onto each Gaudi silicon die
- **c)** By compressing all neural weights into local CPU L1 cache
- **d)** By running software emulated WiFi bridges

---

#### Question 08: Which fundamental design philosophy of the Linux operating system enables hardware devices, running processes, and network sockets to be manipulated using standard file commands (cat, read, write)?
- **a)** Everything is an executable script
- **b)** Everything is a file (Virtual File System abstraction)
- **c)** Everything is a Windows registry entry
- **d)** Everything is a shared cloud database

---

#### Question 09: An HPC cluster administrator runs 'chmod 750 run_simulation.sh'. What exact permissions are granted to Owner, Group, and Others?
- **a)** Owner: rwx, Group: r-x, Others: ---
- **b)** Owner: rw-, Group: r--, Others: r--
- **c)** Owner: rwx, Group: rwx, Others: rwx
- **d)** Owner: r-x, Group: ---, Others: ---

---

#### Question 10: If an HPC user's shell profile sets 'umask 027', what default octal permissions will be assigned to newly created directories and text files respectively?
- **a)** Directory: 750 (rwxr-x---), File: 640 (rw-r-----)
- **b)** Directory: 777 (rwxrwxrwx), File: 666 (rw-rw-rw-)
- **c)** Directory: 755 (rwxr-xr-x), File: 644 (rw-r--r--)
- **d)** Directory: 700 (rwx------), File: 600 (rw-------)

---

#### Question 11: In Linux cluster navigation, what does the command 'cd ../../data' instruct the shell to do?
- **a)** Search for the word 'data' across all files in the system
- **b)** Move up two directory levels from the current location, then enter the 'data' directory
- **c)** Delete two parent folders and format the disk
- **d)** Open a graphical file manager window

---

#### Question 12: Why is '#!/usr/bin/env bash' widely considered a best practice over hardcoded '#!/bin/bash' on enterprise HPC clusters?
- **a)** It compiles the bash script into machine code before running
- **b)** It dynamically searches the user's $PATH to locate the bash binary across diverse Linux distributions
- **c)** It forces bash to run with superuser (root) privileges
- **d)** It automatically translates bash code into Python

---

#### Question 13: What is the critical defensive engineering purpose of placing 'set -euo pipefail' at the beginning of an automated cluster orchestration script?
- **a)** It increases CPU clock frequency by 15%
- **b)** It causes the script to abort immediately if any command errors (-e), any unset variable is used (-u), or any pipe step fails (pipefail)
- **c)** It ignores all syntax errors and suppresses terminal logging
- **d)** It encrypts the script using AES-256

---

#### Question 14: Why will the shell command 'BATCH_SIZE = 64' produce a 'command not found' error in Bash?
- **a)** Bash does not support numbers larger than 32
- **b)** Bash treats spaces around '=' as argument delimiters, interpreting 'BATCH_SIZE' as a command name
- **c)** Variable names in bash must start with a dollar sign ($)
- **d)** Variables can only be declared inside compiled C++ code

---

#### Question 15: In the command './hpc_node_audit.sh > audit.log 2>&1', what is the exact effect of '2>&1'?
- **a)** It multiplies the output volume by 2
- **b)** It redirects standard error (file descriptor 2) to the same destination as standard output (file descriptor 1)
- **c)** It runs the script twice on core 1
- **d)** It delays script execution by 2 seconds

---

#### Question 16: When generating cluster access credentials via 'ssh-keygen -t ed25519', why is the Ed25519 algorithm preferred over standard RSA 2048/4096?
- **a)** Ed25519 uses shorter 256-bit elliptic-curve keys, achieves faster handshakes, and provides superior resistance to side-channel attacks
- **b)** RSA is incompatible with Linux operating systems
- **c)** Ed25519 does not require a private key
- **d)** Ed25519 allows passwords to be transmitted in plain text

---

#### Question 17: To enable passwordless automated job submission from a local machine to a remote cluster node, into which remote file must your client's public key (~/.ssh/id_ed25519.pub) be appended?
- **a)** /etc/passwd
- **b)** ~/.ssh/authorized_keys
- **c)** ~/.ssh/known_hosts
- **d)** /tmp/public_keys.txt

---

#### Question 18: A student attempts to connect to an HPC node and receives: 'Permissions 0644 for id_ed25519 are too open. It is required that your private key files are NOT accessible by others.' What command resolves this?
- **a)** chmod 777 ~/.ssh/id_ed25519
- **b)** chmod 600 ~/.ssh/id_ed25519
- **c)** rm -rf ~/.ssh
- **d)** chmod 000 ~/.ssh/id_ed25519

---

#### Question 19: What is the primary industry objective of the Intel oneAPI software ecosystem?
- **a)** To replace the Linux kernel with a custom proprietary operating system
- **b)** To provide an open, standards-based unified programming model across heterogeneous architectures (CPUs, GPUs, FPGAs) without vendor lock-in
- **c)** To convert Python scripts directly into hardware circuits
- **d)** To eliminate the need for computer RAM

---

#### Question 20: What is SYCL (pronounced 'sickle') in the context of high performance computing with Intel oneAPI?
- **a)** A high-level Khronos standard C++ programming model for single-source heterogeneous programming
- **b)** A relational database query engine
- **c)** An alternative to the Linux Bash shell
- **d)** A network cabling standard for InfiniBand

---

#### Question 21: In SYCL/DPC++, what is the principal architectural advantage of allocating memory via 'sycl::malloc_shared' (Unified Shared Memory)?
- **a)** It doubles the available storage capacity of hard disks
- **b)** It provides a single virtual pointer accessible by both CPU (Host) and GPU/Accelerator (Device) with automatic page migration
- **c)** It permanently disables CPU cache coherence
- **d)** It translates floating point numbers into integers

---

#### Question 22: Which shell command initializes the Intel oneAPI development environment, populating $PATH, $LD_LIBRARY_PATH, and compiler binaries (icpx, ifx)?
- **a)** source /opt/intel/oneapi/setvars.sh
- **b)** python3 /opt/intel/install.py
- **c)** systemctl restart oneapi
- **d)** apt install oneapi-now

---

#### Question 23: What is the defining distinction between the Intel oneAPI Base Toolkit and the Intel HPC Toolkit?
- **a)** Base Toolkit is for single-node development (SYCL, MKL, DAL); HPC Toolkit adds multi-node cluster tools (Intel MPI, Fortran ifx, Inspector, ITAC)
- **b)** Base Toolkit is paid commercial software; HPC Toolkit is open-source
- **c)** Base Toolkit is for Python; HPC Toolkit is for Java
- **d)** There is no difference; they are exact duplicates

---

#### Question 24: Which Linux terminal utility provides immediate introspection of CPU architecture, hardware thread count, cache hierarchy (L1/L2/L3), and NUMA topology?
- **a)** lscpu
- **b)** ping
- **c)** chmod
- **d)** grep

---

#### Question 25: When compiling an HPC benchmark with the Intel oneAPI C++ Compiler (icpx), which optimization flag instructs the compiler to generate instructions matching the host processor's highest SIMD capability (e.g., AVX-512)?
- **a)** -xHost
- **b)** -O0
- **c)** -w
- **d)** -g

---

