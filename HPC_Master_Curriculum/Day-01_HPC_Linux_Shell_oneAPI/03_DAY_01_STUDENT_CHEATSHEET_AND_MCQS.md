# 📝 DAY 1: STUDENT QUICK REFERENCE & OFFICIAL MCQ BANK
## 1-Page Cheat Sheet + 50 Official Pre-Assessment Questions (GLA University)
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Audience:** 60 B.Tech / M.Tech CS Students  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 📌 PART 1: 1-Page Student Command Cheat Sheet

> [!TIP]
> ### ⚡ 2-MINUTE INSTANT-RECALL MASTERY BOX (80-90% IMMEDIATE KNOWLEDGE)
> * **HPC Core Physics:** Aggregates compute nodes across high-speed interconnects to bypass single-machine RAM bandwidth bottlenecks (Memory Wall).
> * **Hardware Triad:** Intel Xeon (Host Orchestration & FP64 math) + Intel GPU Max (Dense Matrix Parallelism) + Habana Gaudi (Tensor TPCs & On-Die 24x 100GbE RoCE).
> * **Linux Golden Rule:** Everything is a file starting at root `/`. Paths are Absolute (`/path`) or Relative (`./path`).
> * **Top 5 Life-Saving Commands:**
>   1. `lscpu | grep -E 'Model name|avx512|amx'` (Inspect CPU model & vector/matrix engines)
>   2. `mkdir -p ~/project/{src,bin,logs}` (Create complete clean directory tree in 1 command)
>   3. `chmod +x script.sh` (Add executable permission bit; fixes `Permission denied`)
>   4. `ssh-keygen -t ed25519 -N ""` (Generate modern high-security elliptic curve SSH key)
>   5. `source /opt/intel/oneapi/setvars.sh` (Initialize Intel oneAPI environment, `$PATH`, and compilers)

### 1. Navigation & Inspection
| Command | What It Does | Example |
| :--- | :--- | :--- |
| `pwd` | Print working directory | `pwd` -> `/home/student/hpc` |
| `cd <path>` | Change directory | `cd ..` (up), `cd ~` (home), `cd -` (previous) |
| `ls -la` | List all files with permissions & hidden files | `ls -lh` (human readable sizes) |
| `lscpu` | Display CPU microarchitecture & flags | `lscpu | grep "Model name:"` |
| `free -h` | Display available RAM | `free -h` |

### 2. File & Directory Operations
| Command | What It Does | Example |
| :--- | :--- | :--- |
| `mkdir -p` | Create nested directory tree | `mkdir -p project/{src,data,logs}` |
| `touch` | Create empty file | `touch main.cpp` |
| `cp -r` | Copy file or recursive folder | `cp -r src/ backup_src/` |
| `mv` | Move or rename file | `mv old.txt new.txt` |
| `rm -r` | Remove file or folder (*CAUTION: Permanent!*) | `rm -rf temp_logs/` |
| `cat` / `head` / `tail` | View file contents | `head -n 20 data.csv` |
| `grep -i` | Search text in files | `grep -i "error" output.log` |

### 3. Permissions & Shell Automation
| Command / Syntax | What It Does | Example |
| :--- | :--- | :--- |
| `chmod +x` | Add executable permission to script | `chmod +x run.sh` |
| `#!/bin/bash` | Shebang: Tells OS to use Bash interpreter | First line of every `.sh` file |
| `VAR="val"` | Set variable (*NO SPACES around `=`*) | `THREADS=16` |
| `echo ${VAR}` | Read variable | `echo "Threads: $THREADS"` |
| `>` vs `>>` | Output redirection (overwrite vs append) | `cmd > out.log` vs `cmd >> out.log` |
| `set -e` | Exit script immediately if any command fails | Placed at top of robust scripts |

### 4. SSH Remote Access & oneAPI
| Command / Syntax | What It Does | Example |
| :--- | :--- | :--- |
| `ssh-keygen -t ed25519` | Generate secure SSH key pair | `ssh-keygen -t ed25519 -N ""` |
| `ssh user@host -p 22` | Connect securely to remote HPC node | `ssh shivam@10.100.1.5` |
| `source setvars.sh` | Initialize Intel oneAPI compilers & paths | `source /opt/intel/oneapi/setvars.sh` |
| `icpx --version` | Verify Intel oneAPI C++ Compiler | `icpx --version` |

---

## 🎯 PART 2: Day 1 Official Study Checklist (22 Items)

- [ ] 01. HPC concept and purpose
- [ ] 02. HPC system overview
- [ ] 03. HPC versus ordinary computing
- [ ] 04. Intel Xeon Scalable Processors
- [ ] 05. Intel Data Center GPUs
- [ ] 06. Habana Gaudi AI Accelerators
- [ ] 07. Silicon hardware roles in HPC
- [ ] 08. Linux filesystem hierarchy & paths (absolute vs relative)
- [ ] 09. Core Linux navigation & file commands
- [ ] 10. Linux environment variables & `$PATH`
- [ ] 11. Shell script creation & execution permissions
- [ ] 12. Shell variables and command execution
- [ ] 13. Shell task automation workflows
- [ ] 14. SSH remote access purpose
- [ ] 15. SSH connection syntax & ports
- [ ] 16. Password vs Key-based authentication (`ed25519`)
- [ ] 17. Intel oneAPI Toolkit purpose
- [ ] 18. oneAPI components overview (DPC++/SYCL, oneMKL, oneDNN)
- [ ] 19. oneAPI environment access (`setvars.sh`)
- [ ] 20. Intel HPC Toolkit introduction
- [ ] 21. HPC compilation workflow (`icx`, `icpx`, `ifx`)
- [ ] 22. Intel HPC Toolkit tools (Intel MPI, Inspector, ITAC)

---

## 📝 PART 3: 50 Official Evaluated Pre-Assessment Questions (With Answers & Explanations)

> **Official 50-Question Diagnostic Bank for Day 1 Pre-Assessment (GLA University BCSG701)**  
> **Track:** Intel & NEC Supercomputing Alliance × Edulateral Foundation  
> **Gradation:** Easy (14) | Medium (21) | Hard (15) — Strictly structured across Day 1 Syllabus Modules 1 to 7.

---

### 🔷 Module 1: Introduction to HPC

#### Q01. [Easy] Which performance metric is the primary benchmark utilized to evaluate and rank the world's most powerful supercomputers on the official TOP500 list?
- A) Clock frequency measured in Gigahertz (GHz)
- B) Floating-point Operations Per Second (FLOPS) achieved on High Performance LINPACK (HPL)
- C) Input/Output Operations Per Second (IOPS) on NVMe storage
- D) Instructions Per Cycle (IPC) on integer ALU workloads
**Answer: B** | *Explanation: The TOP500 supercomputing ranking measures the maximum sustained floating-point execution rate (Rmax in FLOPS), benchmarked using High Performance LINPACK (HPL) solving a dense system of linear equations.*

#### Q02. [Easy] Under Flynn's classical taxonomy of computer architectures, modern High Performance Computing clusters comprising multi-core CPUs and distributed compute nodes are predominantly categorized as:
- A) Single Instruction, Single Data (SISD)
- B) Single Instruction, Multiple Data (SIMD)
- C) Multiple Instruction, Single Data (MISD)
- D) Multiple Instruction, Multiple Data (MIMD)
**Answer: D** | *Explanation: Modern HPC clusters consist of autonomous compute nodes executing independent instruction streams on independent datasets, making them MIMD systems (which may internally leverage SIMD vectorization at the core level).*

#### Q03. [Medium] In modern computer architecture and high-performance system design, what fundamental architectural bottleneck is termed the 'Memory Wall'?
- A) The physical DRAM capacity limit imposed by 64-bit operating systems
- B) The growing performance disparity where CPU processing speed grows far faster than main memory (DRAM) bandwidth and access latency
- C) The maximum number of DIMM slots physically permitted on an ATX motherboard
- D) The file size limit imposed by 32-bit legacy file systems
**Answer: B** | *Explanation: The Memory Wall refers to the widening divergence between processor compute throughput (which has scaled rapidly via multi-core and vectorization) and DRAM access latency/bandwidth, causing cores to spend significant cycles stalled waiting for data.*

#### Q04. [Medium] In a production HPC cluster environment, what is the crucial operational distinction between a Login (Head) Node and Compute Nodes?
- A) Login nodes run heavy distributed deep learning training, while Compute nodes only manage user home directories
- B) Login nodes are dedicated to user authentication, code compilation, and job submission, while Compute nodes are reserved exclusively for parallel workload execution managed by a scheduler
- C) Login nodes contain all cluster GPUs, whereas Compute nodes feature only single-core CPUs
- D) Compute nodes allow direct interactive shell access to all users, whereas Login nodes refuse SSH connections
**Answer: B** | *Explanation: Login nodes provide access for code editing, compiling, and submitting batch jobs to Slurm, while Compute nodes are isolated worker resources where heavy parallel simulations execute without interactive contention.*

#### Q05. [Medium] According to Amdahl's Law, if an algorithm contains 20% strictly sequential (non-parallelizable) operations and 80% perfectly parallelizable operations, what is the theoretical maximum speedup limit on an infinite number of processor cores?
- A) 4x speedup
- B) 5x speedup
- C) 10x speedup
- D) Infinite speedup
**Answer: B** | *Explanation: Amdahl's Law defines Speedup S(N) = 1 / (s + p/N). As N approaches infinity, S_max = 1 / s = 1 / 0.20 = 5x maximum achievable speedup.*

#### Q06. [Hard] While Amdahl's Law evaluates 'Strong Scaling' by holding the total workload size fixed, what scaling model does Gustafson's Law introduce to more accurately evaluate real-world supercomputing applications?
- A) Weak Scaling: The problem size scales proportionally with the number of processors, maintaining a constant execution time
- B) Strong Scaling: The total problem size is halved each time processor count doubles
- C) Static Scaling: The execution time increases exponentially as nodes are added
- D) Negative Scaling: The communication overhead always exceeds computational gains
**Answer: A** | *Explanation: Gustafson's Law formalizes 'Weak Scaling,' recognizing that researchers exploit larger supercomputers not to solve the same tiny problem faster, but to solve massively larger grid resolutions and physical datasets within a practical, constant time window.*

#### Q07. [Hard] Why was the High Performance Conjugate Gradients (HPCG) benchmark established as a companion to the traditional High Performance LINPACK (HPL) on the TOP500 list?
- A) HPL measures dense linear algebra compute throughput (high compute-to-memory ratio), whereas HPCG stresses memory bandwidth, latency, and sparse, irregular memory access patterns common in modern scientific simulations
- B) HPL evaluates only CPU clock frequency, while HPCG evaluates GPU video memory display outputs
- C) HPCG is designed strictly for consumer laptops, while HPL is designed only for quantum computers
- D) HPL tests single-threaded Python scripts, while HPCG tests compiled C++ assembly
**Answer: A** | *Explanation: HPL achieves 80-90% of theoretical peak FLOPS on dense matrix math. In contrast, HPCG exercises sparse matrix-vector multiplication, unstructured grids, and low compute-to-memory traffic, typically achieving under 5% peak FLOPS, accurately reflecting real-world simulation performance.*

### 🔷 Module 2: Intel HPC Architecture

#### Q08. [Easy] What dedicated hardware matrix acceleration engine introduced in 4th Gen Intel Xeon Scalable processors (Sapphire Rapids) delivers accelerated deep learning tensor computation directly on CPU cores?
- A) Intel Software Guard Extensions (Intel SGX)
- B) Intel QuickAssist Technology (Intel QAT)
- C) Intel Advanced Matrix Extensions (Intel AMX)
- D) Intel Dynamic Execution Engine (IDEE)
**Answer: C** | *Explanation: Intel AMX (Advanced Matrix Extensions) is a built-in silicon accelerator on 4th and 5th Gen Xeon Scalable CPUs that accelerates matrix multiplication operations for INT8 and BF16 deep learning training and inference.*

#### Q09. [Easy] The Intel Data Center GPU Max Series (formerly codenamed Ponte Vecchio) engineered for exascale supercomputing and deep learning is built upon which GPU microarchitecture?
- A) Intel Xe-LP (Low Power)
- B) Intel Xe-HPG (High Performance Gaming)
- C) Intel Gen9 Graphics
- D) Intel Xe-HPC (High Performance Computing)
**Answer: D** | *Explanation: The Intel Data Center GPU Max Series is designed specifically for extreme supercomputing, HPC simulation, and AI training workloads using the Intel Xe-HPC microarchitecture.*

#### Q10. [Medium] How do Habana Gaudi 2/3 AI accelerators optimize inter-node scale-out communications for massive distributed LLM training clusters compared to typical PCIe accelerators?
- A) By integrating multiple 100 Gigabit Ethernet (RoCE v2) ports directly onto the accelerator silicon, bypassing external host PCIe NIC bottlenecks
- B) By routing all inter-chip communications through legacy SATA storage controllers
- C) By relying exclusively on external USB-C hub adapters
- D) By requiring all network packets to be inspected synchronously by the CPU BIOS
**Answer: A** | *Explanation: Habana Gaudi processors integrate RDMA over Converged Ethernet (RoCE v2) directly on-die (24x 100GbE on Gaudi 2), enabling all-to-all accelerator scaling over standard Ethernet without costly external host NIC bottlenecks.*

#### Q11. [Medium] In a dual-socket Intel Xeon Scalable server node, which high-speed, low-latency point-to-point coherent interconnect bus links the two CPU sockets together for cross-socket cache coherence and memory access?
- A) Universal Serial Bus (USB 3.2)
- B) Intel Ultra Path Interconnect (Intel UPI)
- C) Front Side Bus (FSB 400MHz)
- D) Peripheral Component Interconnect (PCI 33MHz)
**Answer: B** | *Explanation: Intel UPI (Ultra Path Interconnect) provides point-to-point coherent links between processor sockets in multi-socket Intel Xeon systems, replacing the legacy QPI.*

#### Q12. [Medium] What architectural hardware registers does Intel AMX (Advanced Matrix Extensions) introduce to hold 2D sub-matrix tiles in the core execution units?
- A) 8 two-dimensional tile registers named tmm0 through tmm7 (each up to 1KB in capacity)
- B) 32 vector registers named zmm0 through zmm31 (each 512 bits)
- C) 16 general-purpose 64-bit registers rax through r15
- D) 8 floating-point stack registers st(0) through st(7)
**Answer: A** | *Explanation: AMX introduces a 2D tile architecture consisting of 8 tile registers (tmm0 to tmm7), each capable of holding up to 1024 bytes (1KB) in a 2D matrix configuration (up to 16 rows of 64 bytes).*

#### Q13. [Hard] The Intel Xeon CPU Max Series (Sapphire Rapids with HBM2e) integrates up to 64GB of High Bandwidth Memory directly on-package. Which three memory operating modes can be configured via system BIOS?
- A) Striped Mode, Mirror Mode, and Parity Mode
- B) HBM-only Mode, Flat Mode (1LM), and Cache Mode (2LM)
- C) Dynamic Mode, Static Mode, and Swap Mode
- D) Synchronous Mode, Asynchronous Mode, and Dual-Channel Mode
**Answer: B** | *Explanation: Xeon Max supports three memory modes: (1) HBM-only (runs with zero external DDR5), (2) Flat mode / 1LM (HBM and DDR5 exposed as distinct NUMA nodes), and (3) Cache mode / 2LM (HBM acts as a transparent hardware-managed L4 cache for standard DDR5 capacity).*

#### Q14. [Hard] When comparing Intel AVX-512 with Intel AMX on 4th Gen Xeon CPUs for INT8 matrix multiplication, why does AMX achieve up to an 8x throughput boost per clock cycle?
- A) AMX features the Tile Matrix Multiply (TMUL) unit which computes up to 2048 INT8 operations per cycle on 2D tiles, whereas AVX-512 operates on 1D 512-bit vector registers
- B) AMX quadruples the operating clock frequency of the CPU to over 15 GHz
- C) AMX executes instructions exclusively inside the GPU framebuffer
- D) AVX-512 cannot process integer operations, while AMX only processes integers
**Answer: A** | *Explanation: While AVX-512 operates on 1D vectors computing up to 256 INT8 MACs/cycle via VNNI, AMX's dedicated TMUL matrix engine operates on 2D tiles computing up to 2048 INT8 operations (or 1024 BF16 operations) per clock cycle per core.*

### 🔷 Module 3: Linux Basics & VFS

#### Q15. [Easy] In the Linux Virtual File System (VFS) hierarchy, what character designates the single root directory from which all directories, files, and mounted file systems originate?
- A) Backslash (`\`)
- B) Tilde (`~`)
- C) Forward slash (`/`)
- D) Hash symbol (`#`)
**Answer: C** | *Explanation: In Unix/Linux, the single forward slash `/` represents the top-level root directory of the single hierarchical filesystem tree.*

#### Q16. [Easy] Which standard Linux shell command outputs the absolute canonical pathname of the current active working directory?
- A) `cd`
- B) `pwd`
- C) `whoami`
- D) `path`
**Answer: B** | *Explanation: `pwd` stands for 'Print Working Directory' and writes the full absolute pathname from root to the current directory.*

#### Q17. [Medium] In the Linux octal permission model, what access rights does the command `chmod 750 dataset_dir/` grant to the file's owner, group members, and others respectively?
- A) Owner: Read/Write/Execute (7), Group: Read/Execute (5), Others: No access (0)
- B) Owner: Read/Write (6), Group: Read/Write (6), Others: Execute (1)
- C) Owner: Read/Execute (5), Group: Read/Write (6), Others: Read (4)
- D) Owner: Full access (7), Group: Full access (7), Others: Read/Write (6)
**Answer: A** | *Explanation: Octal permissions: 7 = 4(r) + 2(w) + 1(x) = rwx; 5 = 4(r) + 1(x) = r-x; 0 = no permissions. Hence 750 gives owner rwx, group r-x, and others no access.*

#### Q18. [Medium] If a user's active shell environment has an active `umask` setting of `022`, what will be the default octal file permissions assigned to a newly created regular text file?
- A) 755 (`-rwxr-xr-x`)
- B) 666 (`-rw-rw-rw-`)
- C) 644 (`-rw-r--r--`)
- D) 700 (`-rwx------`)
**Answer: C** | *Explanation: For regular files, the standard base permissions are 666 (`rw-rw-rw-`). Applying umask 022 gives 666 - 022 = 644 (`rw-r--r--`), stripping write permissions from group and others.*

#### Q19. [Medium] Why are HPC cluster users strictly instructed not to write massive, high-throughput simulation output checkpoints into their `$HOME` directory?
- A) `$HOME` is typically mounted over a shared, quota-limited network filesystem (NFS) that experiences high latency under heavy I/O, whereas parallel filesystems like `/scratch` (Lustre/GPFS) are optimized for high-bandwidth parallel I/O
- B) `$HOME` is deleted automatically every time a user logs out of the cluster
- C) `$HOME` does not allow binary executable files to be created or executed
- D) `$HOME` cannot store files larger than 1 Megabyte due to kernel locks
**Answer: A** | *Explanation: In HPC architectures, `$HOME` is an NFS share meant for scripts and configuration. High-throughput parallel checkpoints must target high-speed parallel storage (such as Lustre, GPFS, or local NVMe `/scratch`) to prevent degrading cluster metadata servers.*

#### Q20. [Hard] What is the fundamental architectural distinction between the virtual filesystems `/proc` and `/sys` in the Linux kernel?
- A) `/proc` provides a view of process execution state and kernel runtime statistics (procfs), while `/sys` exposes the kernel's unified device model, hardware buses, and driver topology (sysfs)
- B) `/proc` is stored permanently on an NVMe SSD, while `/sys` exists only in CPU cache
- C) `/proc` is read-only for root, while `/sys` can be modified by any unprivileged user
- D) `/proc` manages network routing tables, while `/sys` handles user password hashing
**Answer: A** | *Explanation: `/proc` (procfs) exposes active process metadata and runtime kernel state (`/proc/cpuinfo`, `/proc/meminfo`), while `/sys` (sysfs) represents the structural hierarchy of physical devices, kernel objects, PCIe busses, and device drivers.*

#### Q21. [Hard] When a user executes `rm -f large_dataset.bin` on a Linux filesystem, what happens to the underlying storage data blocks if another running application still holds an open file descriptor to that file?
- A) The data blocks are immediately overwritten with zeros, causing the running application to crash with a segmentation fault
- B) The directory entry is unlinked immediately, but the inode and data blocks remain allocated and accessible to the running application until its file descriptor is closed
- C) The command fails with an 'I/O Resource Busy' error and terminates
- D) The file is automatically relocated to the `/tmp/swap` directory
**Answer: B** | *Explanation: In Linux VFS semantics, `rm` unlinks the directory pointer (reducing the inode's hard-link count). However, disk blocks are only marked free for reuse when the link count reaches zero AND all open file descriptors referencing that inode are closed.*

### 🔷 Module 4: Shell Scripting

#### Q22. [Easy] In a Linux Bash automation script, what is the exact function of the initial line `#!/bin/bash` (commonly termed the Shebang)?
- A) It elevates the script's execution privileges to root automatically
- B) It instructs the kernel's `execve` system call which interpreter binary to launch to parse and execute the script
- C) It compiles the script into an ELF binary executable before running
- D) It marks the entire script file as read-only
**Answer: B** | *Explanation: The shebang `#!` is a 2-byte magic number (`0x23 0x21`) recognized by the Linux kernel loader to invoke the specified interpreter binary (`/bin/bash`) with the script file path as an argument.*

#### Q23. [Easy] Which shell redirection operator appends the Standard Output (stdout) of a command to the end of a specified destination file without overwriting its existing contents?
- A) `>`
- B) `<`
- C) `|`
- D) `>>`
**Answer: D** | *Explanation: `>>` opens the destination file in append mode (`O_APPEND`), adding output to the end of the file. `>` truncates and overwrites existing contents.*

#### Q24. [Medium] What does the special parameter `$?` represent in a Bash shell session immediately following the completion of a program?
- A) The Process ID (PID) of the currently running shell process
- B) The numeric exit status code of the most recently executed foreground pipeline (where 0 indicates success)
- C) The total count of command-line arguments passed to the script
- D) The total wall-clock runtime of the previous command in milliseconds
**Answer: B** | *Explanation: `$?` holds the decimal return status of the last executed foreground command. In standard POSIX conventions, 0 signals success, while any non-zero value (1–255) indicates an error.*

#### Q25. [Medium] In production HPC automation scripts, what is the effect of placing the directive `set -e` at the beginning of the script?
- A) The shell will immediately exit if any command or pipeline returns a non-zero exit status, preventing cascading errors
- B) The shell prints every command to the terminal before executing it
- C) The shell ignores all syntax errors and proceeds execution
- D) The shell allocates maximum GPU memory to all child processes
**Answer: A** | *Explanation: `set -e` (or `set -o errexit`) ensures defensive execution by causing the shell script to abort immediately when a command fails, preventing silent cascading failures in automated batch workflows.*

#### Q26. [Medium] In Bash shell scripting, which syntax correctly redirects both Standard Output (stdout, file descriptor 1) and Standard Error (stderr, file descriptor 2) to a log file named `simulation.log`?
- A) `./sim_engine 2> simulation.log 1>&2`
- B) `./sim_engine | simulation.log`
- C) `./sim_engine > simulation.log 2>&1`
- D) `./sim_engine 1>&2 >> simulation.log`
**Answer: C** | *Explanation: `./sim_engine > simulation.log 2>&1` first redirects stdout (FD 1) to `simulation.log`, then redirects stderr (FD 2) to whatever FD 1 currently points to (`simulation.log`). (Modern bash also supports `./sim_engine &> simulation.log`).*

#### Q27. [Hard] In a piped command sequence such as `cat simulation.dat | grep 'CONVERGED' | wc -l`, why is the defensive flag `set -o pipefail` critical when `set -e` is already active?
- A) By default, the exit status of a pipeline is determined solely by the LAST command (`wc -l`); `pipefail` ensures the pipeline returns the exit code of the last failing command if any step fails
- B) `set -e` crashes if any pipe is used, so `pipefail` is required to enable pipes
- C) `pipefail` increases the buffer size of the Unix pipe from 64KB to 1GB
- D) `pipefail` converts pipe operations into synchronous disk writes
**Answer: A** | *Explanation: Without `pipefail`, if `grep` crashes or errors out, the pipeline still returns the exit status of `wc -l` (which is 0 / success), causing `set -e` to mistakenly treat the whole pipeline as successful. `set -o pipefail` fixes this critical silent bug.*

#### Q28. [Hard] What is an important technical advantage of using the modern Bash compound conditional construct `[[ ... ]]` over the traditional POSIX test operator `[ ... ]`?
- A) `[ ... ]` is executed by the kernel, whereas `[[ ... ]]` runs in user space
- B) `[[ ... ]]` requires compiling the script with GCC before execution
- C) `[ ... ]` only supports floating-point comparisons, while `[[ ... ]]` supports integers
- D) `[[ ... ]]` is a shell keyword that prevents word splitting and pathname expansion on unquoted variable expansions and supports pattern matching with the `=~` regex operator
**Answer: D** | *Explanation: `[[ ... ]]` is built into Bash syntax (a keyword, not a built-in executable like `[`/`test`). It does not perform word splitting or glob expansion on unquoted variables, preventing syntax errors when variables are empty or contain spaces, and supports advanced regex matching (`=~`).*

### 🔷 Module 5: Secured Shell (SSH)

#### Q29. [Easy] What is the standard IANA default network TCP port number on which the OpenSSH daemon (`sshd`) listens for incoming secure remote shell connections?
- A) Port 80
- B) Port 443
- C) Port 22
- D) Port 8080
**Answer: C** | *Explanation: Standard IANA port assignment for the Secure Shell (SSH) protocol is TCP port 22.*

#### Q30. [Easy] When setting up passwordless public-key authentication to an HPC cluster login node, where must the user's PUBLIC key be appended on the remote server?
- A) `~/.ssh/authorized_keys`
- B) `~/.ssh/known_hosts`
- C) `/etc/ssh/ssh_config`
- D) `~/.bashrc`
**Answer: A** | *Explanation: The OpenSSH server verifies incoming client key signatures against the public keys stored in the user's `~/.ssh/authorized_keys` file on the remote machine.*

#### Q31. [Medium] Which modern elliptic-curve public-key algorithm is widely recommended for SSH keys due to its high computational efficiency, compact 256-bit key length, and strong resistance to timing and side-channel attacks?
- A) DES (Data Encryption Standard)
- B) Ed25519 (Edwards-curve Digital Signature Algorithm)
- C) MD5 (Message Digest 5)
- D) RC4 (Rivest Cipher 4)
**Answer: B** | *Explanation: Ed25519 uses the Twisted Edwards curve Curve25519. It provides ~128 bits of security with a 256-bit key length, faster signature verification, and immunity to cache-timing attacks compared to legacy RSA.*

#### Q32. [Medium] If a user accidentally executes `chmod 777 ~/.ssh/id_ed25519` on their private SSH key, what will happen when they attempt to connect to a remote server?
- A) The SSH client will immediately abort the connection with an error warning that the private key permissions are too open
- B) The remote server will automatically format the user's home directory
- C) The SSH client will silently convert the key to a public key
- D) The connection will succeed with enhanced administrative speed
**Answer: A** | *Explanation: OpenSSH enforces strict permission checks. If a private key file is readable by group or others (anything more permissive than `600` or `400`), it prints 'WARNING: UNPROTECTED PRIVATE KEY FILE!' and ignores the key.*

#### Q33. [Medium] Which command transfers a local dataset `hpc_input.tar.gz` to a remote cluster user account at `login.gla.ac.in` under the directory `/scratch/data/`?
- A) `ssh hpc_input.tar.gz user@login.gla.ac.in:/scratch/data/`
- B) `cp -remote hpc_input.tar.gz user@login.gla.ac.in:/scratch/data/`
- C) `sftp-push hpc_input.tar.gz login.gla.ac.in`
- D) `scp hpc_input.tar.gz user@login.gla.ac.in:/scratch/data/`
**Answer: D** | *Explanation: `scp` (Secure Copy Protocol) uses SSH data transfer syntax: `scp [source] [user@host:destination_path]`.*

#### Q34. [Hard] What critical security vulnerability is introduced when an administrator or user enables SSH Agent Forwarding (`ssh -A`) when connecting to an untrusted intermediate bastion host?
- A) Any user with root privileges on the intermediate host can access the forwarded SSH agent's Unix domain socket and authenticate to other remote servers as you without knowing your passphrase
- B) The intermediate host steals your raw private key file and saves it in `/etc/shadow`
- C) Agent forwarding permanently decrypts all data on your local laptop hard drive
- D) It exposes the client machine to denial-of-service via ICMP flood
**Answer: A** | *Explanation: SSH Agent Forwarding passes a Unix domain socket (`$SSH_AUTH_SOCK`) to the remote host. Anyone with root access on that machine can hijack this socket to request signatures from your local key agent, authenticating as you to other machines. `ProxyJump` (`-J`) is the secure alternative.*

#### Q35. [Hard] In high-frequency automated HPC scripting environments, what is the architectural benefit of configuring SSH Connection Multiplexing using `ControlMaster` and `ControlPath`?
- A) It automatically distributes a single SSH session across multiple physical Ethernet switches
- B) It encrypts SSH traffic twice with independent AES-256 ciphers
- C) It maintains a persistent master TCP socket connection, allowing subsequent SSH/SCP sessions to bypass public-key handshakes and authentication overhead
- D) It prevents compute nodes from communicating with each other
**Answer: C** | *Explanation: SSH multiplexing (`ControlMaster auto`) keeps an initial master connection open. Subsequent `ssh` or `scp` invocations communicate through a local control socket (`ControlPath`), reusing the established connection and reducing connection establishment time from ~500ms to ~5ms.*

### 🔷 Module 6: Intel oneAPI Toolkit

#### Q36. [Easy] What is the primary industry objective of the Intel oneAPI programming model?
- A) To replace the Linux operating system kernel with an Intel-proprietary microkernel
- B) To provide an open, cross-architecture, standards-based unified programming framework that abstracts software development across diverse CPUs, GPUs, FPGAs, and AI accelerators
- C) To restrict high-performance software development exclusively to Intel Core desktop processors
- D) To serve as a commercial subscription-only cloud database engine
**Answer: B** | *Explanation: oneAPI is an open, cross-industry programming model designed to provide a unified development environment across heterogeneous compute architectures (CPUs, GPUs, FPGAs, and specialized AI hardware) without proprietary vendor lock-in.*

#### Q37. [Easy] Which shell script must be sourced in an HPC Linux environment to set up the necessary PATH, LD_LIBRARY_PATH, and compiler variables for the Intel oneAPI toolkits?
- A) `source /opt/intel/oneapi/setvars.sh`
- B) `bash /opt/intel/oneapi/init.sh`
- C) `exec start_oneapi`
- D) `python /opt/intel/run_toolkit.py`
**Answer: A** | *Explanation: Sourcing `/opt/intel/oneapi/setvars.sh` initializes all environment variables (compiler paths, library search paths, man pages) required to run oneAPI compilers and libraries in the current shell session.*

#### Q38. [Medium] Intel oneAPI DPC++ (Data Parallel C++) is based upon and actively contributes to which open industry standard maintained by the Khronos Group?
- A) CUDA
- B) OpenMP
- C) SYCL (Single-source C++ heterogeneous programming standard)
- D) Vulkan GLSL
**Answer: C** | *Explanation: Intel DPC++ is built upon the open Khronos SYCL standard, enabling single-source modern C++ code to execute across diverse accelerators from multiple hardware vendors.*

#### Q39. [Medium] In the Intel oneAPI software stack, what is the role of Intel Level Zero?
- A) A high-level visual graph designer for web applications
- B) A low-level, direct-to-metal hardware abstraction interface providing fine-grained control over accelerator memory, device discovery, kernel submission, and telemetry
- C) An audio processing subsystem for desktop sound cards
- D) A database query optimization engine
**Answer: B** | *Explanation: Intel Level Zero provides direct, low-latency, bare-metal hardware access to Intel GPUs and accelerators, serving as the foundational driver interface beneath high-level runtimes like SYCL and oneMKL.*

#### Q40. [Medium] In SYCL Unified Shared Memory (USM), what is the key functional difference between `malloc_device` and `malloc_host` memory allocations?
- A) `malloc_device` allocates memory strictly in accelerator high-bandwidth memory (inaccessible directly by CPU pointers), whereas `malloc_host` allocates pinned host memory accessible by both CPU and GPU
- B) `malloc_device` allocates memory on hard disks, while `malloc_host` allocates memory on tape drives
- C) `malloc_device` is limited to 1 Megabyte, while `malloc_host` is unlimited
- D) `malloc_host` cannot be read by accelerator GPUs
**Answer: A** | *Explanation: `malloc_device` allocates memory resident on the target accelerator device (offering maximum GPU bandwidth, but CPU cannot dereference device pointers). `malloc_host` allocates pinned host memory accessible by both CPU and device across PCIe.*

#### Q41. [Hard] In SYCL Unified Shared Memory (USM), how does `malloc_shared` simplify heterogeneous programming compared to explicit buffer/accessor memory management?
- A) It broadcasts memory across all nodes in a cluster using InfiniBand
- B) It converts all double-precision floating-point numbers into 8-bit integers
- C) It provides a unified pointer accessible by both CPU and GPU, with the SYCL runtime automatically managing page migration on demand between host and device memory
- D) It disables data caching to enforce synchronous disk access
**Answer: C** | *Explanation: `sycl::malloc_shared` allocates memory accessible from both the host CPU and the target device using the same pointer address. The underlying driver/OS automatically migrates data pages across the interconnect on demand, removing the need for manual buffer copies.*

#### Q42. [Hard] When creating a SYCL command queue, what operational difference exists between an in-order queue (`sycl::property::queue::in_order`) and the default out-of-order queue?
- A) An in-order queue can only run on single-core CPUs and cannot target GPUs
- B) Out-of-order queues automatically discard failed execution tasks without notification
- C) In-order queues disable all asynchronous memory transfers
- D) An in-order queue executes submitted command groups strictly in the sequential order they are submitted, whereas default out-of-order queues can execute commands concurrently unless explicit SYCL events/dependencies are declared
**Answer: D** | *Explanation: By default, SYCL queues are out-of-order, allowing kernels to run concurrently or out of sequence unless directed by event dependencies (`depends_on`). Passing `sycl::property::queue::in_order` enforces FIFO sequential execution, simplifying debugging.*

### 🔷 Module 7: Intel HPC Toolkit

#### Q43. [Easy] Which modern LLVM-based C++ compiler provided in the Intel HPC Toolkit is used to compile high-performance SYCL and modern C++ parallel applications?
- A) `gcc`
- B) `icpx`
- C) `javac`
- D) `cl.exe`
**Answer: B** | *Explanation: In the Intel oneAPI HPC Toolkit, `icpx` is the Intel oneAPI DPC++/C++ compiler, built upon LLVM and providing advanced vectorization and SYCL heterogeneous compilation.*

#### Q44. [Easy] Which high-performance Fortran compiler in the Intel HPC Toolkit is the modern LLVM-based replacement for the classic `ifort` compiler?
- A) `ifx`
- B) `gfortran`
- C) `f90`
- D) `flang`
**Answer: A** | *Explanation: `ifx` is Intel's modern LLVM-based Fortran compiler, delivering modern Fortran standard support and OpenMP offloading to Intel GPUs.*

#### Q45. [Medium] When compiling computational physics or machine learning C/C++ codes with `icpx`, what optimization does the flag `-xHost` instruct the compiler to perform?
- A) It binds the compiled binary to execute exclusively on a specific network IP address
- B) It runs the code inside an isolated Docker container
- C) It instructs the compiler to generate SIMD vector instructions targeting the highest instruction set supported by the compilation host CPU (e.g., AVX-512)
- D) It disables all loop unrolling and optimization to prioritize compilation speed
**Answer: C** | *Explanation: `-xHost` queries the CPU where compilation is occurring and instructs the compiler to generate the most advanced SIMD code available (such as AVX-512 or AVX2), maximizing vector arithmetic throughput.*

#### Q46. [Medium] In a multi-node distributed HPC cluster, which component in the Intel HPC Toolkit provides the optimized implementation of the MPI-3 / MPI-4 standard for inter-node communication?
- A) Intel Integrated Performance Primitives (IPP)
- B) Intel Distribution for Python
- C) Intel VTune Profiler
- D) Intel MPI Library
**Answer: D** | *Explanation: The Intel MPI Library is an enterprise multi-fabric message-passing library implementing the MPI standard, optimized for low-latency point-to-point and collective communications across Intel Xeon clusters.*

#### Q47. [Medium] Which diagnostic analysis tool included in the Intel HPC Toolkit is designed to detect dynamic memory corruption, memory leaks, uninitialized memory accesses, and threading data races without needing specialized recompilation?
- A) Intel Inspector
- B) Intel Advisor
- C) Intel Trace Analyzer and Collector (ITAC)
- D) Intel oneDNN
**Answer: A** | *Explanation: Intel Inspector is a dynamic memory and thread checking tool that identifies subtle memory leaks, dangling pointers, deadlocks, and race conditions in multi-threaded C/C++/Fortran programs.*

#### Q48. [Hard] On a multi-socket Intel Xeon server featuring Non-Uniform Memory Access (NUMA), why does unconstrained OS thread migration across NUMA sockets severely degrade HPC application performance?
- A) Remote NUMA access causes immediate hardware watchdog reboot
- B) Accessing memory attached to a remote CPU socket over the UPI interconnect incurs significantly higher latency and lower bandwidth than accessing local NUMA memory; thread affinity pinning (`numactl` / `I_MPI_PIN`) prevents this penalty
- C) Thread migration deletes variables stored in L1 cache permanently
- D) Remote NUMA sockets only support 16-bit calculations
**Answer: B** | *Explanation: In NUMA systems, each socket has its own local memory controller and DDR channels. When a core accesses RAM on a remote socket, requests must traverse the interconnect (Intel UPI), which doubles memory access latency and congests the bus. Process/thread binding prevents cross-socket migrations.*

#### Q49. [Hard] When compiling numerical linear algebra algorithms with `icx` / `icpx`, what is the consequence of specifying the floating-point optimization flag `-fp-model=fast=2` compared to `-fp-model=precise`?
- A) `-fp-model=fast=2` converts all double-precision numbers to 8-bit integers
- B) `-fp-model=precise` disables all CPU vector registers and forces scalar emulation
- C) `-fp-model=fast=2` enables aggressive floating-point algebraic reordering and fused multiply-adds (FMA) that maximize compute throughput at the expense of strict IEEE 754 numerical bitwise reproducibility
- D) `-fp-model=fast=2` only functions on ARM processors
**Answer: C** | *Explanation: `-fp-model=precise` enforces strict IEEE 754 adherence and disables value-unsafe reordering. `-fp-model=fast=2` allows aggressive reassociation, reciprocal approximations, and contracted operations (FMA) that maximize execution speed on scientific workloads while permitting minor rounding variations.*

#### Q50. [Hard] What is the architectural role of the Open Fabrics Interfaces (OFI / Libfabric) provider layer underneath the Intel MPI Library in high-performance computing clusters?
- A) It acts as a modular, hardware-independent network abstraction framework allowing Intel MPI to interface directly with high-speed kernel-bypass fabrics (InfiniBand verbs, RoCE, Omni-Path, TCP) with minimal overhead
- B) It converts MPI communication messages into HTTP REST API queries
- C) It encrypts cluster network packets using software RSA-4096 keys
- D) It assigns dynamic IP addresses to compute nodes using DHCP
**Answer: A** | *Explanation: Libfabric (OFI) is the core fabric interface in Intel MPI. It provides a standard, low-latency API directly above user-space network drivers (like InfiniBand verbs, Cisco usNIC, Intel PSM3, or sockets), enabling kernel-bypass zero-copy communication across HPC fabrics.*
