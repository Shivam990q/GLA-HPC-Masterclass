# 🎯 GLA UNIVERSITY — DAY 1 IN-CLASS SOCRATIC CHECKPOINT MCQS (OFFICIAL INSTRUCTOR KEY)
## High Performance Computing & Heterogeneous AI Systems (`GLA-HPC-BCSG701`)
**Lead Trainer:** Shivam Gupta | **Target Session:** Day 1 Lectures & Labs (Interactive In-Class Checkpoints)  
**Total Questions:** 25 Multi-Choice Questions | **Modules Covered:** 1 through 7  

---

## 📌 Pedagogical Delivery Strategy (Socratic In-Class Checkpointing)
Do NOT administer these 25 questions as a single sit-down exam!
Instead, weave 3-4 questions into each module as you teach. When you finish explaining a concept (e.g., Amdahl's Law, `chmod 750`, or Intel AMX), project the corresponding question, give students 30 seconds to commit to an answer, and use the explanation to **connect the dots** to the next architectural concept!

---

### Question 01 [Module 1: Introduction to HPC & Scientific Parallelism | Easy | Foundational]
**Topic:** Memory Wall & HPC Constraint  
**Question:** Why do large AI models (e.g., 70-Billion parameter LLMs) fail to train efficiently on high-end consumer laptops despite having fast CPUs?

- **a)** Laptops lack sufficient DDR memory channels and bandwidth (choked by the Memory Wall)
- **b)** Laptops do not support floating-point arithmetic
- **c)** Windows OS permanently limits memory allocation to 4 GB
- **d)** Laptop CPUs cannot execute C++ code

> [!TIP]
> **Correct Answer: [a]** — Laptops lack sufficient DDR memory channels and bandwidth (choked by the Memory Wall)  
> **Technical Explanation:** Consumer laptops typically have 2 memory channels providing 50-80 GB/s bandwidth, creating a massive Memory Wall bottleneck. Dual-socket enterprise HPC nodes provide 16 DDR5 channels delivering over 600 GB/s bandwidth.

---

### Question 02 [Module 1: Introduction to HPC & Scientific Parallelism | Medium | Conceptual]
**Topic:** Flynn's Taxonomy  
**Question:** Under Flynn's classical computer architecture taxonomy, which architectural model best describes modern GPUs and CPU vector execution units (AVX-512)?

- **a)** SISD (Single Instruction, Single Data)
- **b)** SIMD (Single Instruction, Multiple Data)
- **c)** MISD (Multiple Instruction, Single Data)
- **d)** MIMD (Multiple Instruction, Multiple Data)

> [!TIP]
> **Correct Answer: [b]** — SIMD (Single Instruction, Multiple Data)  
> **Technical Explanation:** SIMD describes hardware where a single machine instruction controls multiple execution units simultaneously processing a vector of distinct data points (e.g., eight 64-bit doubles in a single AVX-512 clock cycle).

---

### Question 03 [Module 1: Introduction to HPC & Scientific Parallelism | Medium | Numerical]
**Topic:** Amdahl's Law Speedup Limit  
**Question:** An HPC simulation contains a sequential fraction of 10% that cannot be parallelized. According to Amdahl's Law, what is the theoretical maximum speedup limit, even with an infinite number of processor cores?

- **a)** 100x speedup
- **b)** 10x speedup
- **c)** 50x speedup
- **d)** Infinite speedup

> [!TIP]
> **Correct Answer: [b]** — 10x speedup  
> **Technical Explanation:** By Amdahl's Law: Speedup_max = 1 / (1 - P) = 1 / S. Here sequential fraction S = 0.10, so Speedup_max = 1 / 0.10 = 10x maximum speedup regardless of core count.

---

### Question 04 [Module 2: Intel HPC Architecture & Hardware Accelerators | Medium | Technical]
**Topic:** Intel Xeon Role in Heterogeneous Clusters  
**Question:** In an enterprise heterogeneous supercomputing cluster, what is the primary architectural responsibility of Intel Xeon Scalable processors?

- **a)** High-latency batch graphics rendering only
- **b)** Orchestrating workflows, managing OS scheduling, preprocessing tensors, and handling irregular sequential logic
- **c)** Replacing all network switches in the datacenter
- **d)** Acting exclusively as passive memory controllers

> [!TIP]
> **Correct Answer: [b]** — Orchestrating workflows, managing OS scheduling, preprocessing tensors, and handling irregular sequential logic  
> **Technical Explanation:** Intel Xeon CPUs excel at low-latency sequential execution, kernel memory management, I/O dispatch, and data orchestration, feeding structured tensor batches to parallel accelerators.

---

### Question 05 [Module 2: Intel HPC Architecture & Hardware Accelerators | Medium | Technical]
**Topic:** Intel AMX Hardware Function  
**Question:** What specific hardware capability is introduced on 4th Gen Intel Xeon Scalable processors (Sapphire Rapids) via Intel AMX (Advanced Matrix Extensions)?

- **a)** Integrated liquid nitrogen cooling controllers
- **b)** Dedicated 2D tile registers (TMM0-TMM7) and matrix multiplication units (TMUL) accelerating deep learning on the CPU die
- **c)** Hardware emulation of 8-bit retro video game graphics
- **d)** Direct connection to SATA-1 mechanical hard drives

> [!TIP]
> **Correct Answer: [b]** — Dedicated 2D tile registers (TMM0-TMM7) and matrix multiplication units (TMUL) accelerating deep learning on the CPU die  
> **Technical Explanation:** Intel AMX integrates eight 1KB 2D tile registers (8 KB total) and Tile Matrix Multiply (TMUL) accelerators, performing up to 2048 INT8 operations per cycle per core directly on the CPU.

---

### Question 06 [Module 2: Intel HPC Architecture & Hardware Accelerators | Medium | Technical]
**Topic:** Intel Data Center GPU Max Architecture  
**Question:** Which computational workload is the Intel Data Center GPU Max Series (formerly code-named Ponte Vecchio) primarily architected to accelerate?

- **a)** Massive parallel floating-point vector/matrix simulations and high-density FP64/FP32 scientific computing
- **b)** Single-threaded shell script execution
- **c)** Low-speed serial ASCII text parsing
- **d)** Managing Linux user account passwords

> [!TIP]
> **Correct Answer: [a]** — Massive parallel floating-point vector/matrix simulations and high-density FP64/FP32 scientific computing  
> **Technical Explanation:** Intel Data Center GPU Max Series features up to 128 Xe cores with integrated high-bandwidth memory (HBM2e) providing massive throughput for parallel FP64, FP32, and matrix workloads.

---

### Question 07 [Module 2: Intel HPC Architecture & Hardware Accelerators | Hard | Technical]
**Topic:** Habana Gaudi 2 Interconnect Fabric  
**Question:** How does the Habana Gaudi 2 AI accelerator achieve scale-out multi-node cluster training without requiring external discrete InfiniBand PCIe host channel adapters (HCAs)?

- **a)** By transmitting data across standard USB 2.0 cables
- **b)** By integrating 24x 100GbE RoCE (RDMA over Converged Ethernet) ports directly onto each Gaudi silicon die
- **c)** By compressing all neural weights into local CPU L1 cache
- **d)** By running software emulated WiFi bridges

> [!TIP]
> **Correct Answer: [b]** — By integrating 24x 100GbE RoCE (RDMA over Converged Ethernet) ports directly onto each Gaudi silicon die  
> **Technical Explanation:** Gaudi 2 integrates twenty-four 100 Gigabit Ethernet RoCE RDMA interfaces directly on the processor die, providing 2.4 Tbps (300 GB/s) bi-directional network fabric throughput natively.

---

### Question 08 [Module 3: Linux OS Architecture & Filesystem Internals | Easy | Foundational]
**Topic:** UNIX File System Philosophy  
**Question:** Which fundamental design philosophy of the Linux operating system enables hardware devices, running processes, and network sockets to be manipulated using standard file commands (cat, read, write)?

- **a)** Everything is an executable script
- **b)** Everything is a file (Virtual File System abstraction)
- **c)** Everything is a Windows registry entry
- **d)** Everything is a shared cloud database

> [!TIP]
> **Correct Answer: [b]** — Everything is a file (Virtual File System abstraction)  
> **Technical Explanation:** In UNIX/Linux, 'everything is a file' allows the VFS to represent hardware devices (/dev), kernel status tables (/proc), and system properties (/sys) as accessible file streams.

---

### Question 09 [Module 3: Linux OS Architecture & Filesystem Internals | Medium | Technical]
**Topic:** Octal Permission Bitmask  
**Question:** An HPC cluster administrator runs 'chmod 750 run_simulation.sh'. What exact permissions are granted to Owner, Group, and Others?

- **a)** Owner: rwx, Group: r-x, Others: ---
- **b)** Owner: rw-, Group: r--, Others: r--
- **c)** Owner: rwx, Group: rwx, Others: rwx
- **d)** Owner: r-x, Group: ---, Others: ---

> [!TIP]
> **Correct Answer: [a]** — Owner: rwx, Group: r-x, Others: ---  
> **Technical Explanation:** In octal: 7 = 4+2+1 (read, write, execute for Owner); 5 = 4+0+1 (read, execute for Group); 0 = no permissions for Others (secure cluster practice).

---

### Question 10 [Module 3: Linux OS Architecture & Filesystem Internals | Medium | Numerical]
**Topic:** Dual umask Calculation  
**Question:** If an HPC user's shell profile sets 'umask 027', what default octal permissions will be assigned to newly created directories and text files respectively?

- **a)** Directory: 750 (rwxr-x---), File: 640 (rw-r-----)
- **b)** Directory: 777 (rwxrwxrwx), File: 666 (rw-rw-rw-)
- **c)** Directory: 755 (rwxr-xr-x), File: 644 (rw-r--r--)
- **d)** Directory: 700 (rwx------), File: 600 (rw-------)

> [!TIP]
> **Correct Answer: [a]** — Directory: 750 (rwxr-x---), File: 640 (rw-r-----)  
> **Technical Explanation:** Base directory mode is 777; subtracting 027 yields 750 (rwxr-x---). Base file mode is 666; subtracting 027 (and stripping execute) yields 640 (rw-r-----).

---

### Question 11 [Module 3: Linux OS Architecture & Filesystem Internals | Easy | Foundational]
**Topic:** Path Navigation  
**Question:** In Linux cluster navigation, what does the command 'cd ../../data' instruct the shell to do?

- **a)** Search for the word 'data' across all files in the system
- **b)** Move up two directory levels from the current location, then enter the 'data' directory
- **c)** Delete two parent folders and format the disk
- **d)** Open a graphical file manager window

> [!TIP]
> **Correct Answer: [b]** — Move up two directory levels from the current location, then enter the 'data' directory  
> **Technical Explanation:** In relative path syntax, '..' refers to the parent directory. Doing '../../' navigates two levels up the directory tree before descending into 'data'.

---

### Question 12 [Module 4: Linux Shell Scripting & HPC Workflows | Easy | Technical]
**Topic:** Shebang Portability  
**Question:** Why is '#!/usr/bin/env bash' widely considered a best practice over hardcoded '#!/bin/bash' on enterprise HPC clusters?

- **a)** It compiles the bash script into machine code before running
- **b)** It dynamically searches the user's $PATH to locate the bash binary across diverse Linux distributions
- **c)** It forces bash to run with superuser (root) privileges
- **d)** It automatically translates bash code into Python

> [!TIP]
> **Correct Answer: [b]** — It dynamically searches the user's $PATH to locate the bash binary across diverse Linux distributions  
> **Technical Explanation:** On heterogeneous clusters and custom operating environments, bash may be located in /bin, /usr/bin, or a custom environment module; 'env' dynamically resolves the active interpreter.

---

### Question 13 [Module 4: Linux Shell Scripting & HPC Workflows | Medium | Technical]
**Topic:** Defensive Bash set Flags  
**Question:** What is the critical defensive engineering purpose of placing 'set -euo pipefail' at the beginning of an automated cluster orchestration script?

- **a)** It increases CPU clock frequency by 15%
- **b)** It causes the script to abort immediately if any command errors (-e), any unset variable is used (-u), or any pipe step fails (pipefail)
- **c)** It ignores all syntax errors and suppresses terminal logging
- **d)** It encrypts the script using AES-256

> [!TIP]
> **Correct Answer: [b]** — It causes the script to abort immediately if any command errors (-e), any unset variable is used (-u), or any pipe step fails (pipefail)  
> **Technical Explanation:** In batch supercomputing workflows, silent failures cause corrupted data or wasted cluster node-hours. 'set -euo pipefail' guarantees fail-fast deterministic execution.

---

### Question 14 [Module 4: Linux Shell Scripting & HPC Workflows | Easy | Technical]
**Topic:** Bash Variable Assignment Syntax  
**Question:** Why will the shell command 'BATCH_SIZE = 64' produce a 'command not found' error in Bash?

- **a)** Bash does not support numbers larger than 32
- **b)** Bash treats spaces around '=' as argument delimiters, interpreting 'BATCH_SIZE' as a command name
- **c)** Variable names in bash must start with a dollar sign ($)
- **d)** Variables can only be declared inside compiled C++ code

> [!TIP]
> **Correct Answer: [b]** — Bash treats spaces around '=' as argument delimiters, interpreting 'BATCH_SIZE' as a command name  
> **Technical Explanation:** In Bash, assignment syntax must have zero spaces around the '=' operator: 'BATCH_SIZE=64'. Spaces cause Bash to parse 'BATCH_SIZE' as an executable command.

---

### Question 15 [Module 4: Linux Shell Scripting & HPC Workflows | Medium | Technical]
**Topic:** Standard Stream Redirection  
**Question:** In the command './hpc_node_audit.sh > audit.log 2>&1', what is the exact effect of '2>&1'?

- **a)** It multiplies the output volume by 2
- **b)** It redirects standard error (file descriptor 2) to the same destination as standard output (file descriptor 1)
- **c)** It runs the script twice on core 1
- **d)** It delays script execution by 2 seconds

> [!TIP]
> **Correct Answer: [b]** — It redirects standard error (file descriptor 2) to the same destination as standard output (file descriptor 1)  
> **Technical Explanation:** File descriptor 1 is stdout and 2 is stderr. '2>&1' merges the stderr stream into stdout, ensuring that both normal logs and runtime error messages are written into 'audit.log'.

---

### Question 16 [Module 5: Secure Remote Access & Cluster Environments | Medium | Technical]
**Topic:** SSH Cryptographic Algorithms  
**Question:** When generating cluster access credentials via 'ssh-keygen -t ed25519', why is the Ed25519 algorithm preferred over standard RSA 2048/4096?

- **a)** Ed25519 uses shorter 256-bit elliptic-curve keys, achieves faster handshakes, and provides superior resistance to side-channel attacks
- **b)** RSA is incompatible with Linux operating systems
- **c)** Ed25519 does not require a private key
- **d)** Ed25519 allows passwords to be transmitted in plain text

> [!TIP]
> **Correct Answer: [a]** — Ed25519 uses shorter 256-bit elliptic-curve keys, achieves faster handshakes, and provides superior resistance to side-channel attacks  
> **Technical Explanation:** Ed25519 uses the Edwards-curve Digital Signature Algorithm (EdDSA) over Curve25519. It offers equivalent security to 3072-bit RSA with only 256-bit key length and faster execution.

---

### Question 17 [Module 5: Secure Remote Access & Cluster Environments | Easy | Technical]
**Topic:** SSH Remote Key Storage  
**Question:** To enable passwordless automated job submission from a local machine to a remote cluster node, into which remote file must your client's public key (~/.ssh/id_ed25519.pub) be appended?

- **a)** /etc/passwd
- **b)** ~/.ssh/authorized_keys
- **c)** ~/.ssh/known_hosts
- **d)** /tmp/public_keys.txt

> [!TIP]
> **Correct Answer: [b]** — ~/.ssh/authorized_keys  
> **Technical Explanation:** The SSH server inspects ~/.ssh/authorized_keys on the remote host to match incoming signature challenges against authorized client public keys.

---

### Question 18 [Module 5: Secure Remote Access & Cluster Environments | Medium | Technical]
**Topic:** SSH Private Key Permissions  
**Question:** A student attempts to connect to an HPC node and receives: 'Permissions 0644 for id_ed25519 are too open. It is required that your private key files are NOT accessible by others.' What command resolves this?

- **a)** chmod 777 ~/.ssh/id_ed25519
- **b)** chmod 600 ~/.ssh/id_ed25519
- **c)** rm -rf ~/.ssh
- **d)** chmod 000 ~/.ssh/id_ed25519

> [!TIP]
> **Correct Answer: [b]** — chmod 600 ~/.ssh/id_ed25519  
> **Technical Explanation:** SSH enforces strict security: private keys must be accessible only by the owner (read/write = 600). Group and others must have 0 access, or the SSH client refuses to use the key.

---

### Question 19 [Module 6: Intel oneAPI Ecosystem & oneAPI HPC Toolkit | Easy | Conceptual]
**Topic:** oneAPI Unified Architecture Purpose  
**Question:** What is the primary industry objective of the Intel oneAPI software ecosystem?

- **a)** To replace the Linux kernel with a custom proprietary operating system
- **b)** To provide an open, standards-based unified programming model across heterogeneous architectures (CPUs, GPUs, FPGAs) without vendor lock-in
- **c)** To convert Python scripts directly into hardware circuits
- **d)** To eliminate the need for computer RAM

> [!TIP]
> **Correct Answer: [b]** — To provide an open, standards-based unified programming model across heterogeneous architectures (CPUs, GPUs, FPGAs) without vendor lock-in  
> **Technical Explanation:** oneAPI provides cross-architecture developer freedom through the open Khronos SYCL standard, enabling a single codebase to compile across diverse compute targets.

---

### Question 20 [Module 6: Intel oneAPI Ecosystem & oneAPI HPC Toolkit | Medium | Technical]
**Topic:** SYCL Language Standard  
**Question:** What is SYCL (pronounced 'sickle') in the context of high performance computing with Intel oneAPI?

- **a)** A high-level Khronos standard C++ programming model for single-source heterogeneous programming
- **b)** A relational database query engine
- **c)** An alternative to the Linux Bash shell
- **d)** A network cabling standard for InfiniBand

> [!TIP]
> **Correct Answer: [a]** — A high-level Khronos standard C++ programming model for single-source heterogeneous programming  
> **Technical Explanation:** SYCL is a modern C++ template library standard defined by the Khronos Group, allowing developers to write both host orchestration code and accelerator device kernels in standard C++.

---

### Question 21 [Module 6: Intel oneAPI Ecosystem & oneAPI HPC Toolkit | Medium | Technical]
**Topic:** Unified Shared Memory (USM)  
**Question:** In SYCL/DPC++, what is the principal architectural advantage of allocating memory via 'sycl::malloc_shared' (Unified Shared Memory)?

- **a)** It doubles the available storage capacity of hard disks
- **b)** It provides a single virtual pointer accessible by both CPU (Host) and GPU/Accelerator (Device) with automatic page migration
- **c)** It permanently disables CPU cache coherence
- **d)** It translates floating point numbers into integers

> [!TIP]
> **Correct Answer: [b]** — It provides a single virtual pointer accessible by both CPU (Host) and GPU/Accelerator (Device) with automatic page migration  
> **Technical Explanation:** USM shared allocations provide a pointer valid on both host and device; the SYCL runtime and OS driver automatically handle page fault migration between system RAM and device memory.

---

### Question 22 [Module 6: Intel oneAPI Ecosystem & oneAPI HPC Toolkit | Easy | Technical]
**Topic:** oneAPI Environment Sourcing  
**Question:** Which shell command initializes the Intel oneAPI development environment, populating $PATH, $LD_LIBRARY_PATH, and compiler binaries (icpx, ifx)?

- **a)** source /opt/intel/oneapi/setvars.sh
- **b)** python3 /opt/intel/install.py
- **c)** systemctl restart oneapi
- **d)** apt install oneapi-now

> [!TIP]
> **Correct Answer: [a]** — source /opt/intel/oneapi/setvars.sh  
> **Technical Explanation:** Executing 'source /opt/intel/oneapi/setvars.sh' (or 'oneapi-vars.sh') dynamically updates environment paths to make oneAPI compilers and libraries accessible in the active terminal session.

---

### Question 23 [Module 7: Hands-on Lab Environment & Diagnostics | Easy | Foundational]
**Topic:** Base Toolkit vs HPC Toolkit  
**Question:** What is the defining distinction between the Intel oneAPI Base Toolkit and the Intel HPC Toolkit?

- **a)** Base Toolkit is for single-node development (SYCL, MKL, DAL); HPC Toolkit adds multi-node cluster tools (Intel MPI, Fortran ifx, Inspector, ITAC)
- **b)** Base Toolkit is paid commercial software; HPC Toolkit is open-source
- **c)** Base Toolkit is for Python; HPC Toolkit is for Java
- **d)** There is no difference; they are exact duplicates

> [!TIP]
> **Correct Answer: [a]** — Base Toolkit is for single-node development (SYCL, MKL, DAL); HPC Toolkit adds multi-node cluster tools (Intel MPI, Fortran ifx, Inspector, ITAC)  
> **Technical Explanation:** The Base Toolkit provides foundational single-node compilers and domain libraries. The HPC Toolkit layers on cluster-scale supercomputing components: Intel MPI, Classic/LLVM Compilers, and debuggers.

---

### Question 24 [Module 7: Hands-on Lab Environment & Diagnostics | Easy | Technical]
**Topic:** Hardware Introspection CLI  
**Question:** Which Linux terminal utility provides immediate introspection of CPU architecture, hardware thread count, cache hierarchy (L1/L2/L3), and NUMA topology?

- **a)** lscpu
- **b)** ping
- **c)** chmod
- **d)** grep

> [!TIP]
> **Correct Answer: [a]** — lscpu  
> **Technical Explanation:** 'lscpu' parses sysfs and /proc/cpuinfo to display processor architecture, socket count, threads per core, NUMA nodes, and vector instruction flags.

---

### Question 25 [Module 7: Hands-on Lab Environment & Diagnostics | Medium | Technical]
**Topic:** Intel Compiler Host Optimization Flag  
**Question:** When compiling an HPC benchmark with the Intel oneAPI C++ Compiler (icpx), which optimization flag instructs the compiler to generate instructions matching the host processor's highest SIMD capability (e.g., AVX-512)?

- **a)** -xHost
- **b)** -O0
- **c)** -w
- **d)** -g

> [!TIP]
> **Correct Answer: [a]** — -xHost  
> **Technical Explanation:** The '-xHost' flag tells the Intel compiler to interrogate the compilation machine's microarchitecture and enable all supported SIMD vector extensions (AVX-512, AMX, AVX2) for maximum throughput.

---

