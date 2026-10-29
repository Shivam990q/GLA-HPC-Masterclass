# 🏢 GLA UNIVERSITY — DAY 1 PRE-ASSESSMENT QUESTION PAPER
## High Performance Computing & Heterogeneous AI Systems (GLA-HPC-BCSG701)
**Target Batch:** 7th-Semester B.Tech Computer Science & IT | **Total Questions:** 50
**Time Allowed:** 60 Minutes | **Maximum Marks:** 50 | **Negative Marking:** None
**Instructions:** Read each question carefully. Select the most appropriate option (A, B, C, or D).

---

## 🔷 Module 1: Introduction to HPC

#### Q01. Which performance metric is the primary benchmark utilized to evaluate and rank the world's most powerful supercomputers on the official TOP500 list?

- (A) Clock frequency measured in Gigahertz (GHz)
- (B) Floating-point Operations Per Second (FLOPS) achieved on High Performance LINPACK (HPL)
- (C) Input/Output Operations Per Second (IOPS) on NVMe storage
- (D) Instructions Per Cycle (IPC) on integer ALU workloads

#### Q02. Under Flynn's classical taxonomy of computer architectures, modern High Performance Computing clusters comprising multi-core CPUs and distributed compute nodes are predominantly categorized as:

- (A) Single Instruction, Single Data (SISD)
- (B) Single Instruction, Multiple Data (SIMD)
- (C) Multiple Instruction, Single Data (MISD)
- (D) Multiple Instruction, Multiple Data (MIMD)

#### Q03. In modern computer architecture and high-performance system design, what fundamental architectural bottleneck is termed the 'Memory Wall'?

- (A) The physical DRAM capacity limit imposed by 64-bit operating systems
- (B) The growing performance disparity where CPU processing speed grows far faster than main memory (DRAM) bandwidth and access latency
- (C) The maximum number of DIMM slots physically permitted on an ATX motherboard
- (D) The file size limit imposed by 32-bit legacy file systems

#### Q04. In a production HPC cluster environment, what is the crucial operational distinction between a Login (Head) Node and Compute Nodes?

- (A) Login nodes run heavy distributed deep learning training, while Compute nodes only manage user home directories
- (B) Login nodes are dedicated to user authentication, code compilation, and job submission, while Compute nodes are reserved exclusively for parallel workload execution managed by a scheduler
- (C) Login nodes contain all cluster GPUs, whereas Compute nodes feature only single-core CPUs
- (D) Compute nodes allow direct interactive shell access to all users, whereas Login nodes refuse SSH connections

#### Q05. According to Amdahl's Law, if an algorithm contains 20% strictly sequential (non-parallelizable) operations and 80% perfectly parallelizable operations, what is the theoretical maximum speedup limit on an infinite number of processor cores?

- (A) 4x speedup
- (B) 5x speedup
- (C) 10x speedup
- (D) Infinite speedup

#### Q06. While Amdahl's Law evaluates 'Strong Scaling' by holding the total workload size fixed, what scaling model does Gustafson's Law introduce to more accurately evaluate real-world supercomputing applications?

- (A) Weak Scaling: The problem size scales proportionally with the number of processors, maintaining a constant execution time
- (B) Strong Scaling: The total problem size is halved each time processor count doubles
- (C) Static Scaling: The execution time increases exponentially as nodes are added
- (D) Negative Scaling: The communication overhead always exceeds computational gains

#### Q07. Why was the High Performance Conjugate Gradients (HPCG) benchmark established as a companion to the traditional High Performance LINPACK (HPL) on the TOP500 list?

- (A) HPL measures dense linear algebra compute throughput (high compute-to-memory ratio), whereas HPCG stresses memory bandwidth, latency, and sparse, irregular memory access patterns common in modern scientific simulations
- (B) HPL evaluates only CPU clock frequency, while HPCG evaluates GPU video memory display outputs
- (C) HPCG is designed strictly for consumer laptops, while HPL is designed only for quantum computers
- (D) HPL tests single-threaded Python scripts, while HPCG tests compiled C++ assembly

## 🔷 Module 2: Intel HPC Architecture

#### Q08. What dedicated hardware matrix acceleration engine introduced in 4th Gen Intel Xeon Scalable processors (Sapphire Rapids) delivers accelerated deep learning tensor computation directly on CPU cores?

- (A) Intel Software Guard Extensions (Intel SGX)
- (B) Intel QuickAssist Technology (Intel QAT)
- (C) Intel Advanced Matrix Extensions (Intel AMX)
- (D) Intel Dynamic Execution Engine (IDEE)

#### Q09. The Intel Data Center GPU Max Series (formerly codenamed Ponte Vecchio) engineered for exascale supercomputing and deep learning is built upon which GPU microarchitecture?

- (A) Intel Xe-LP (Low Power)
- (B) Intel Xe-HPG (High Performance Gaming)
- (C) Intel Gen9 Graphics
- (D) Intel Xe-HPC (High Performance Computing)

#### Q10. How do Habana Gaudi 2/3 AI accelerators optimize inter-node scale-out communications for massive distributed LLM training clusters compared to typical PCIe accelerators?

- (A) By integrating multiple 100 Gigabit Ethernet (RoCE v2) ports directly onto the accelerator silicon, bypassing external host PCIe NIC bottlenecks
- (B) By routing all inter-chip communications through legacy SATA storage controllers
- (C) By relying exclusively on external USB-C hub adapters
- (D) By requiring all network packets to be inspected synchronously by the CPU BIOS

#### Q11. In a dual-socket Intel Xeon Scalable server node, which high-speed, low-latency point-to-point coherent interconnect bus links the two CPU sockets together for cross-socket cache coherence and memory access?

- (A) Universal Serial Bus (USB 3.2)
- (B) Intel Ultra Path Interconnect (Intel UPI)
- (C) Front Side Bus (FSB 400MHz)
- (D) Peripheral Component Interconnect (PCI 33MHz)

#### Q12. What architectural hardware registers does Intel AMX (Advanced Matrix Extensions) introduce to hold 2D sub-matrix tiles in the core execution units?

- (A) 8 two-dimensional tile registers named tmm0 through tmm7 (each up to 1KB in capacity)
- (B) 32 vector registers named zmm0 through zmm31 (each 512 bits)
- (C) 16 general-purpose 64-bit registers rax through r15
- (D) 8 floating-point stack registers st(0) through st(7)

#### Q13. The Intel Xeon CPU Max Series (Sapphire Rapids with HBM2e) integrates up to 64GB of High Bandwidth Memory directly on-package. Which three memory operating modes can be configured via system BIOS?

- (A) Striped Mode, Mirror Mode, and Parity Mode
- (B) HBM-only Mode, Flat Mode (1LM), and Cache Mode (2LM)
- (C) Dynamic Mode, Static Mode, and Swap Mode
- (D) Synchronous Mode, Asynchronous Mode, and Dual-Channel Mode

#### Q14. When comparing Intel AVX-512 with Intel AMX on 4th Gen Xeon CPUs for INT8 matrix multiplication, why does AMX achieve up to an 8x throughput boost per clock cycle?

- (A) AMX features the Tile Matrix Multiply (TMUL) unit which computes up to 2048 INT8 operations per cycle on 2D tiles, whereas AVX-512 operates on 1D 512-bit vector registers
- (B) AMX quadruples the operating clock frequency of the CPU to over 15 GHz
- (C) AMX executes instructions exclusively inside the GPU framebuffer
- (D) AVX-512 cannot process integer operations, while AMX only processes integers

## 🔷 Module 3: Linux Basics & VFS

#### Q15. In the Linux Virtual File System (VFS) hierarchy, what character designates the single root directory from which all directories, files, and mounted file systems originate?

- (A) Backslash (`\`)
- (B) Tilde (`~`)
- (C) Forward slash (`/`)
- (D) Hash symbol (`#`)

#### Q16. Which standard Linux shell command outputs the absolute canonical pathname of the current active working directory?

- (A) `cd`
- (B) `pwd`
- (C) `whoami`
- (D) `path`

#### Q17. In the Linux octal permission model, what access rights does the command `chmod 750 dataset_dir/` grant to the file's owner, group members, and others respectively?

- (A) Owner: Read/Write/Execute (7), Group: Read/Execute (5), Others: No access (0)
- (B) Owner: Read/Write (6), Group: Read/Write (6), Others: Execute (1)
- (C) Owner: Read/Execute (5), Group: Read/Write (6), Others: Read (4)
- (D) Owner: Full access (7), Group: Full access (7), Others: Read/Write (6)

#### Q18. If a user's active shell environment has an active `umask` setting of `022`, what will be the default octal file permissions assigned to a newly created regular text file?

- (A) 755 (`-rwxr-xr-x`)
- (B) 666 (`-rw-rw-rw-`)
- (C) 644 (`-rw-r--r--`)
- (D) 700 (`-rwx------`)

#### Q19. Why are HPC cluster users strictly instructed not to write massive, high-throughput simulation output checkpoints into their `$HOME` directory?

- (A) `$HOME` is typically mounted over a shared, quota-limited network filesystem (NFS) that experiences high latency under heavy I/O, whereas parallel filesystems like `/scratch` (Lustre/GPFS) are optimized for high-bandwidth parallel I/O
- (B) `$HOME` is deleted automatically every time a user logs out of the cluster
- (C) `$HOME` does not allow binary executable files to be created or executed
- (D) `$HOME` cannot store files larger than 1 Megabyte due to kernel locks

#### Q20. What is the fundamental architectural distinction between the virtual filesystems `/proc` and `/sys` in the Linux kernel?

- (A) `/proc` provides a view of process execution state and kernel runtime statistics (procfs), while `/sys` exposes the kernel's unified device model, hardware buses, and driver topology (sysfs)
- (B) `/proc` is stored permanently on an NVMe SSD, while `/sys` exists only in CPU cache
- (C) `/proc` is read-only for root, while `/sys` can be modified by any unprivileged user
- (D) `/proc` manages network routing tables, while `/sys` handles user password hashing

#### Q21. When a user executes `rm -f large_dataset.bin` on a Linux filesystem, what happens to the underlying storage data blocks if another running application still holds an open file descriptor to that file?

- (A) The data blocks are immediately overwritten with zeros, causing the running application to crash with a segmentation fault
- (B) The directory entry is unlinked immediately, but the inode and data blocks remain allocated and accessible to the running application until its file descriptor is closed
- (C) The command fails with an 'I/O Resource Busy' error and terminates
- (D) The file is automatically relocated to the `/tmp/swap` directory

## 🔷 Module 4: Shell Scripting

#### Q22. In a Linux Bash automation script, what is the exact function of the initial line `#!/bin/bash` (commonly termed the Shebang)?

- (A) It elevates the script's execution privileges to root automatically
- (B) It instructs the kernel's `execve` system call which interpreter binary to launch to parse and execute the script
- (C) It compiles the script into an ELF binary executable before running
- (D) It marks the entire script file as read-only

#### Q23. Which shell redirection operator appends the Standard Output (stdout) of a command to the end of a specified destination file without overwriting its existing contents?

- (A) `>`
- (B) `<`
- (C) `|`
- (D) `>>`

#### Q24. What does the special parameter `$?` represent in a Bash shell session immediately following the completion of a program?

- (A) The Process ID (PID) of the currently running shell process
- (B) The numeric exit status code of the most recently executed foreground pipeline (where 0 indicates success)
- (C) The total count of command-line arguments passed to the script
- (D) The total wall-clock runtime of the previous command in milliseconds

#### Q25. In production HPC automation scripts, what is the effect of placing the directive `set -e` at the beginning of the script?

- (A) The shell will immediately exit if any command or pipeline returns a non-zero exit status, preventing cascading errors
- (B) The shell prints every command to the terminal before executing it
- (C) The shell ignores all syntax errors and proceeds execution
- (D) The shell allocates maximum GPU memory to all child processes

#### Q26. In Bash shell scripting, which syntax correctly redirects both Standard Output (stdout, file descriptor 1) and Standard Error (stderr, file descriptor 2) to a log file named `simulation.log`?

- (A) `./sim_engine 2> simulation.log 1>&2`
- (B) `./sim_engine | simulation.log`
- (C) `./sim_engine > simulation.log 2>&1`
- (D) `./sim_engine 1>&2 >> simulation.log`

#### Q27. In a piped command sequence such as `cat simulation.dat | grep 'CONVERGED' | wc -l`, why is the defensive flag `set -o pipefail` critical when `set -e` is already active?

- (A) By default, the exit status of a pipeline is determined solely by the LAST command (`wc -l`); `pipefail` ensures the pipeline returns the exit code of the last failing command if any step fails
- (B) `set -e` crashes if any pipe is used, so `pipefail` is required to enable pipes
- (C) `pipefail` increases the buffer size of the Unix pipe from 64KB to 1GB
- (D) `pipefail` converts pipe operations into synchronous disk writes

#### Q28. What is an important technical advantage of using the modern Bash compound conditional construct `[[ ... ]]` over the traditional POSIX test operator `[ ... ]`?

- (A) `[ ... ]` is executed by the kernel, whereas `[[ ... ]]` runs in user space
- (B) `[[ ... ]]` requires compiling the script with GCC before execution
- (C) `[ ... ]` only supports floating-point comparisons, while `[[ ... ]]` supports integers
- (D) `[[ ... ]]` is a shell keyword that prevents word splitting and pathname expansion on unquoted variable expansions and supports pattern matching with the `=~` regex operator

## 🔷 Module 5: Secured Shell (SSH)

#### Q29. What is the standard IANA default network TCP port number on which the OpenSSH daemon (`sshd`) listens for incoming secure remote shell connections?

- (A) Port 80
- (B) Port 443
- (C) Port 22
- (D) Port 8080

#### Q30. When setting up passwordless public-key authentication to an HPC cluster login node, where must the user's PUBLIC key be appended on the remote server?

- (A) `~/.ssh/authorized_keys`
- (B) `~/.ssh/known_hosts`
- (C) `/etc/ssh/ssh_config`
- (D) `~/.bashrc`

#### Q31. Which modern elliptic-curve public-key algorithm is widely recommended for SSH keys due to its high computational efficiency, compact 256-bit key length, and strong resistance to timing and side-channel attacks?

- (A) DES (Data Encryption Standard)
- (B) Ed25519 (Edwards-curve Digital Signature Algorithm)
- (C) MD5 (Message Digest 5)
- (D) RC4 (Rivest Cipher 4)

#### Q32. If a user accidentally executes `chmod 777 ~/.ssh/id_ed25519` on their private SSH key, what will happen when they attempt to connect to a remote server?

- (A) The SSH client will immediately abort the connection with an error warning that the private key permissions are too open
- (B) The remote server will automatically format the user's home directory
- (C) The SSH client will silently convert the key to a public key
- (D) The connection will succeed with enhanced administrative speed

#### Q33. Which command transfers a local dataset `hpc_input.tar.gz` to a remote cluster user account at `login.gla.ac.in` under the directory `/scratch/data/`?

- (A) `ssh hpc_input.tar.gz user@login.gla.ac.in:/scratch/data/`
- (B) `cp -remote hpc_input.tar.gz user@login.gla.ac.in:/scratch/data/`
- (C) `sftp-push hpc_input.tar.gz login.gla.ac.in`
- (D) `scp hpc_input.tar.gz user@login.gla.ac.in:/scratch/data/`

#### Q34. What critical security vulnerability is introduced when an administrator or user enables SSH Agent Forwarding (`ssh -A`) when connecting to an untrusted intermediate bastion host?

- (A) Any user with root privileges on the intermediate host can access the forwarded SSH agent's Unix domain socket and authenticate to other remote servers as you without knowing your passphrase
- (B) The intermediate host steals your raw private key file and saves it in `/etc/shadow`
- (C) Agent forwarding permanently decrypts all data on your local laptop hard drive
- (D) It exposes the client machine to denial-of-service via ICMP flood

#### Q35. In high-frequency automated HPC scripting environments, what is the architectural benefit of configuring SSH Connection Multiplexing using `ControlMaster` and `ControlPath`?

- (A) It automatically distributes a single SSH session across multiple physical Ethernet switches
- (B) It encrypts SSH traffic twice with independent AES-256 ciphers
- (C) It maintains a persistent master TCP socket connection, allowing subsequent SSH/SCP sessions to bypass public-key handshakes and authentication overhead
- (D) It prevents compute nodes from communicating with each other

## 🔷 Module 6: Intel oneAPI Toolkit

#### Q36. What is the primary industry objective of the Intel oneAPI programming model?

- (A) To replace the Linux operating system kernel with an Intel-proprietary microkernel
- (B) To provide an open, cross-architecture, standards-based unified programming framework that abstracts software development across diverse CPUs, GPUs, FPGAs, and AI accelerators
- (C) To restrict high-performance software development exclusively to Intel Core desktop processors
- (D) To serve as a commercial subscription-only cloud database engine

#### Q37. Which shell script must be sourced in an HPC Linux environment to set up the necessary PATH, LD_LIBRARY_PATH, and compiler variables for the Intel oneAPI toolkits?

- (A) `source /opt/intel/oneapi/setvars.sh`
- (B) `bash /opt/intel/oneapi/init.sh`
- (C) `exec start_oneapi`
- (D) `python /opt/intel/run_toolkit.py`

#### Q38. Intel oneAPI DPC++ (Data Parallel C++) is based upon and actively contributes to which open industry standard maintained by the Khronos Group?

- (A) CUDA
- (B) OpenMP
- (C) SYCL (Single-source C++ heterogeneous programming standard)
- (D) Vulkan GLSL

#### Q39. In the Intel oneAPI software stack, what is the role of Intel Level Zero?

- (A) A high-level visual graph designer for web applications
- (B) A low-level, direct-to-metal hardware abstraction interface providing fine-grained control over accelerator memory, device discovery, kernel submission, and telemetry
- (C) An audio processing subsystem for desktop sound cards
- (D) A database query optimization engine

#### Q40. In SYCL Unified Shared Memory (USM), what is the key functional difference between `malloc_device` and `malloc_host` memory allocations?

- (A) `malloc_device` allocates memory strictly in accelerator high-bandwidth memory (inaccessible directly by CPU pointers), whereas `malloc_host` allocates pinned host memory accessible by both CPU and GPU
- (B) `malloc_device` allocates memory on hard disks, while `malloc_host` allocates memory on tape drives
- (C) `malloc_device` is limited to 1 Megabyte, while `malloc_host` is unlimited
- (D) `malloc_host` cannot be read by accelerator GPUs

#### Q41. In SYCL Unified Shared Memory (USM), how does `malloc_shared` simplify heterogeneous programming compared to explicit buffer/accessor memory management?

- (A) It broadcasts memory across all nodes in a cluster using InfiniBand
- (B) It converts all double-precision floating-point numbers into 8-bit integers
- (C) It provides a unified pointer accessible by both CPU and GPU, with the SYCL runtime automatically managing page migration on demand between host and device memory
- (D) It disables data caching to enforce synchronous disk access

#### Q42. When creating a SYCL command queue, what operational difference exists between an in-order queue (`sycl::property::queue::in_order`) and the default out-of-order queue?

- (A) An in-order queue can only run on single-core CPUs and cannot target GPUs
- (B) Out-of-order queues automatically discard failed execution tasks without notification
- (C) In-order queues disable all asynchronous memory transfers
- (D) An in-order queue executes submitted command groups strictly in the sequential order they are submitted, whereas default out-of-order queues can execute commands concurrently unless explicit SYCL events/dependencies are declared

## 🔷 Module 7: Intel HPC Toolkit

#### Q43. Which modern LLVM-based C++ compiler provided in the Intel HPC Toolkit is used to compile high-performance SYCL and modern C++ parallel applications?

- (A) `gcc`
- (B) `icpx`
- (C) `javac`
- (D) `cl.exe`

#### Q44. Which high-performance Fortran compiler in the Intel HPC Toolkit is the modern LLVM-based replacement for the classic `ifort` compiler?

- (A) `ifx`
- (B) `gfortran`
- (C) `f90`
- (D) `flang`

#### Q45. When compiling computational physics or machine learning C/C++ codes with `icpx`, what optimization does the flag `-xHost` instruct the compiler to perform?

- (A) It binds the compiled binary to execute exclusively on a specific network IP address
- (B) It runs the code inside an isolated Docker container
- (C) It instructs the compiler to generate SIMD vector instructions targeting the highest instruction set supported by the compilation host CPU (e.g., AVX-512)
- (D) It disables all loop unrolling and optimization to prioritize compilation speed

#### Q46. In a multi-node distributed HPC cluster, which component in the Intel HPC Toolkit provides the optimized implementation of the MPI-3 / MPI-4 standard for inter-node communication?

- (A) Intel Integrated Performance Primitives (IPP)
- (B) Intel Distribution for Python
- (C) Intel VTune Profiler
- (D) Intel MPI Library

#### Q47. Which diagnostic analysis tool included in the Intel HPC Toolkit is designed to detect dynamic memory corruption, memory leaks, uninitialized memory accesses, and threading data races without needing specialized recompilation?

- (A) Intel Inspector
- (B) Intel Advisor
- (C) Intel Trace Analyzer and Collector (ITAC)
- (D) Intel oneDNN

#### Q48. On a multi-socket Intel Xeon server featuring Non-Uniform Memory Access (NUMA), why does unconstrained OS thread migration across NUMA sockets severely degrade HPC application performance?

- (A) Remote NUMA access causes immediate hardware watchdog reboot
- (B) Accessing memory attached to a remote CPU socket over the UPI interconnect incurs significantly higher latency and lower bandwidth than accessing local NUMA memory; thread affinity pinning (`numactl` / `I_MPI_PIN`) prevents this penalty
- (C) Thread migration deletes variables stored in L1 cache permanently
- (D) Remote NUMA sockets only support 16-bit calculations

#### Q49. When compiling numerical linear algebra algorithms with `icx` / `icpx`, what is the consequence of specifying the floating-point optimization flag `-fp-model=fast=2` compared to `-fp-model=precise`?

- (A) `-fp-model=fast=2` converts all double-precision numbers to 8-bit integers
- (B) `-fp-model=precise` disables all CPU vector registers and forces scalar emulation
- (C) `-fp-model=fast=2` enables aggressive floating-point algebraic reordering and fused multiply-adds (FMA) that maximize compute throughput at the expense of strict IEEE 754 numerical bitwise reproducibility
- (D) `-fp-model=fast=2` only functions on ARM processors

#### Q50. What is the architectural role of the Open Fabrics Interfaces (OFI / Libfabric) provider layer underneath the Intel MPI Library in high-performance computing clusters?

- (A) It acts as a modular, hardware-independent network abstraction framework allowing Intel MPI to interface directly with high-speed kernel-bypass fabrics (InfiniBand verbs, RoCE, Omni-Path, TCP) with minimal overhead
- (B) It converts MPI communication messages into HTTP REST API queries
- (C) It encrypts cluster network packets using software RSA-4096 keys
- (D) It assigns dynamic IP addresses to compute nodes using DHCP
