# 🏢 GLA UNIVERSITY — DAY 1 PRE-ASSESSMENT QUESTION PAPER
## High Performance Computing & Heterogeneous AI Systems (GLA-HPC-BCSG701)
**Target Batch:** 7th-Semester B.Tech Computer Science & IT | **Total Questions:** 50
**Time Allowed:** 60 Minutes | **Maximum Marks:** 50 | **Negative Marking:** None
**Instructions:** Read each question carefully. Select the most appropriate option (A, B, C, or D).

---

## 🔷 Module 1: Introduction to HPC

#### Q01. [Foundational] Which performance metric is the primary benchmark utilized to evaluate and rank the world's most powerful supercomputers on the official TOP500 list?

- (A) Clock frequency measured in Gigahertz (GHz)
- (B) Floating-point Operations Per Second (FLOPS) achieved on High Performance LINPACK (HPL)
- (C) Input/Output Operations Per Second (IOPS) on NVMe storage
- (D) Instructions Per Cycle (IPC) on integer ALU workloads

#### Q02. [Numerical] A dual-socket HPC compute node is equipped with two 32-core Intel Xeon processors running at a base clock frequency of 2.0 GHz. If each core can execute 32 double-precision floating-point operations per cycle using AVX-512 vector units, what is the theoretical peak double-precision compute performance (Rpeak) of the node?

- (A) 1.024 TFLOPS
- (B) 2.048 TFLOPS
- (C) 8.192 TFLOPS
- (D) 4.096 TFLOPS

#### Q03. [Conceptual] In modern computer architecture and high-performance system design, what fundamental architectural bottleneck is termed the 'Memory Wall'?

- (A) The physical DRAM capacity limit imposed by 64-bit operating systems
- (B) The growing performance disparity where CPU processing speed grows far faster than main memory (DRAM) bandwidth and access latency
- (C) The maximum number of DIMM slots physically permitted on an ATX motherboard
- (D) The file size limit imposed by 32-bit legacy file systems

#### Q04. [Scenario] In a production HPC cluster environment, what is the crucial operational distinction between a Login (Head) Node and Compute Nodes?

- (A) Login nodes run heavy distributed deep learning training, while Compute nodes only manage user home directories
- (B) Login nodes are dedicated to user authentication, code compilation, and job submission, while Compute nodes are reserved exclusively for parallel workload execution managed by a scheduler
- (C) Login nodes contain all cluster GPUs, whereas Compute nodes feature only single-core CPUs
- (D) Compute nodes allow direct interactive shell access to all users, whereas Login nodes refuse SSH connections

#### Q05. [Numerical] An HPC optimization engineer profiles a simulation algorithm and finds that 20% of the runtime is strictly sequential (s = 0.20), while 80% is parallelizable (p = 0.80). According to Amdahl's Law, what is the theoretical maximum speedup limit achievable by this algorithm even if executed across an infinite number of processor cores?

- (A) 4x speedup
- (B) 5x speedup
- (C) 10x speedup
- (D) Infinite speedup

#### Q06. [Numerical] A researcher scales an atmospheric climate model across a 64-core HPC compute node. If 95% of the scaled execution time is spent in parallel computation (p = 0.95) and 5% is sequential (s = 0.05), what is the scaled speedup achieved according to Gustafson's Law (S(N) = s + p * N)?

- (A) 60.85x speedup
- (B) 20.00x speedup
- (C) 5.00x speedup
- (D) 128.00x speedup

#### Q07. [Conceptual] Why was the High Performance Conjugate Gradients (HPCG) benchmark established as a companion to the traditional High Performance LINPACK (HPL) on the TOP500 list?

- (A) HPL measures dense linear algebra compute throughput (high compute-to-memory ratio), whereas HPCG stresses memory bandwidth, latency, and sparse, irregular memory access patterns common in modern scientific simulations
- (B) HPL evaluates only CPU clock frequency, while HPCG evaluates GPU video memory display outputs
- (C) HPCG is designed strictly for consumer laptops, while HPL is designed only for quantum computers
- (D) HPL tests single-threaded Python scripts, while HPCG tests compiled C++ assembly

## 🔷 Module 2: Intel HPC Architecture

#### Q08. [Foundational] What dedicated hardware matrix acceleration engine introduced in 4th Gen Intel Xeon Scalable processors (Sapphire Rapids) delivers accelerated deep learning tensor computation directly on CPU cores?

- (A) Intel Software Guard Extensions (Intel SGX)
- (B) Intel QuickAssist Technology (Intel QAT)
- (C) Intel Advanced Matrix Extensions (Intel AMX)
- (D) Intel Dynamic Execution Engine (IDEE)

#### Q09. [Foundational] The Intel Data Center GPU Max Series (formerly codenamed Ponte Vecchio) engineered for exascale supercomputing and deep learning is built upon which GPU microarchitecture?

- (A) Intel Xe-LP (Low Power)
- (B) Intel Xe-HPG (High Performance Gaming)
- (C) Intel Gen9 Graphics
- (D) Intel Xe-HPC (High Performance Computing)

#### Q10. [Numerical] A Habana Gaudi 2 AI accelerator card integrates 24 dedicated 100 Gigabit Ethernet (100GbE) RoCE v2 ports directly on the silicon for scale-out inter-chip communication. What is the total aggregate networking throughput provided per accelerator in Gigabytes per second (GB/s)?

- (A) 100 GB/s
- (B) 200 GB/s
- (C) 600 GB/s
- (D) 300 GB/s

#### Q11. [Numerical] A dual-socket 4th Gen Intel Xeon Scalable server (Sapphire Rapids) features 8 DDR5 memory channels per socket operating at DDR5-4800 (4800 MT/s). Given a standard 64-bit (8-byte) bus width per channel, what is the theoretical peak aggregate memory bandwidth of the dual-socket system?

- (A) 153.6 GB/s
- (B) 307.2 GB/s
- (C) 614.4 GB/s
- (D) 1228.8 GB/s

#### Q12. [Numerical] Intel Advanced Matrix Extensions (AMX) architecture provides 8 dedicated 2D tile registers (tmm0 through tmm7). If each tile register can configure up to 16 rows of 64 bytes each, what is the maximum total data capacity stored across all 8 AMX tile registers simultaneously?

- (A) 512 bytes
- (B) 2048 bytes (2 KB)
- (C) 4096 bytes (4 KB)
- (D) 8192 bytes (8 KB)

#### Q13. [Technical] The Intel Xeon CPU Max Series (Sapphire Rapids with HBM2e) integrates up to 64GB of High Bandwidth Memory directly on-package. Which three memory operating modes can be configured via system BIOS?

- (A) Striped Mode, Mirror Mode, and Parity Mode
- (B) HBM-only Mode, Flat Mode (1LM), and Cache Mode (2LM)
- (C) Dynamic Mode, Static Mode, and Swap Mode
- (D) Synchronous Mode, Asynchronous Mode, and Dual-Channel Mode

#### Q14. [Numerical] On a 4th Gen Xeon core, AVX-512 VNNI computes up to 256 INT8 operations per cycle, while the Intel AMX TMUL accelerator computes up to 2048 INT8 operations per cycle. By what factor (speedup ratio) does AMX outperform AVX-512 in raw INT8 matrix multiply throughput per clock cycle?

- (A) 8x throughput boost
- (B) 4x throughput boost
- (C) 2x throughput boost
- (D) 16x throughput boost

## 🔷 Module 3: Linux Basics & VFS

#### Q15. [Foundational] In the Linux Virtual File System (VFS) hierarchy, what character designates the single root directory from which all directories, files, and mounted file systems originate?

- (A) Backslash ('\')
- (B) Tilde ('~')
- (C) Forward slash ('/')
- (D) Hash symbol ('#')

#### Q16. [Foundational] Which standard Linux shell command outputs the absolute canonical pathname of the current active working directory?

- (A) 'cd'
- (B) 'pwd'
- (C) 'whoami'
- (D) 'path'

#### Q17. [Numerical] In Linux octal permission notation, a systems administrator issues the command 'chmod 750 /scratch/project'. What exact read (r), write (w), and execute (x) permissions are assigned to the Owner, Group, and Others?

- (A) Owner: rwx (7), Group: r-x (5), Others: --- (0)
- (B) Owner: rw- (6), Group: rw- (6), Others: --x (1)
- (C) Owner: r-x (5), Group: rwx (7), Others: r-- (4)
- (D) Owner: rwx (7), Group: rwx (7), Others: r-x (5)

#### Q18. [Numerical] If a Linux user's shell session has an active 'umask' setting of 027, what will be the default octal permissions assigned to a newly created directory (base 777) and a newly created regular text file (base 666) respectively?

- (A) Directory: 755 ('rwxr-xr-x'), File: 644 ('rw-r--r--')
- (B) Directory: 700 ('rwx------'), File: 600 ('rw-------')
- (C) Directory: 770 ('rwxrwx---'), File: 660 ('rw-rw----')
- (D) Directory: 750 ('rwxr-x---'), File: 640 ('rw-r-----')

#### Q19. [Numerical] In a Linux ext4 filesystem configured with the standard 4096-byte (4 KB) allocation block size, if a simulation outputs a configuration file of exactly 10,000 bytes, how many filesystem blocks are allocated on disk and how much internal fragmentation (slack space) is unused in the final block?

- (A) 2 blocks allocated, 0 bytes slack space
- (B) 3 blocks allocated, 2288 bytes slack space
- (C) 4 blocks allocated, 6384 bytes slack space
- (D) 1 block allocated, 5904 bytes slack space

#### Q20. [Technical] What is the fundamental architectural distinction between the virtual filesystems '/proc' and '/sys' in the Linux kernel?

- (A) '/proc' provides a view of process execution state and kernel runtime statistics (procfs), while '/sys' exposes the kernel's unified device model, hardware buses, and driver topology (sysfs)
- (B) '/proc' is stored permanently on an NVMe SSD, while '/sys' exists only in CPU cache
- (C) '/proc' is read-only for root, while '/sys' can be modified by any unprivileged user
- (D) '/proc' manages network routing tables, while '/sys' handles user password hashing

#### Q21. [Scenario] When a user executes 'rm -f large_dataset.bin' on a Linux filesystem, what happens to the underlying storage data blocks if another running application still holds an open file descriptor to that file?

- (A) The data blocks are immediately overwritten with zeros, causing the running application to crash with a segmentation fault
- (B) The directory entry is unlinked immediately, but the inode and data blocks remain allocated and accessible to the running application until its file descriptor is closed
- (C) The command fails with an 'I/O Resource Busy' error and terminates
- (D) The file is automatically relocated to the '/tmp/swap' directory

## 🔷 Module 4: Shell Scripting

#### Q22. [Foundational] In a Linux Bash automation script, what is the exact function of the initial line '#!/bin/bash' (commonly termed the Shebang)?

- (A) It elevates the script's execution privileges to root automatically
- (B) It instructs the kernel's 'execve' system call which interpreter binary to launch to parse and execute the script
- (C) It compiles the script into an ELF binary executable before running
- (D) It marks the entire script file as read-only

#### Q23. [Foundational] Which shell redirection operator appends the Standard Output (stdout) of a command to the end of a specified destination file without overwriting its existing contents?

- (A) '>'
- (B) '<'
- (C) '|'
- (D) '>>'

#### Q24. [Numerical] In a Bash automation script, what integer result is printed to the terminal when executing the arithmetic evaluation command: 'echo $(( (15 % 4) + (2 ** 5) - (12 / 3) ))'?

- (A) 27
- (B) 42
- (C) 35
- (D) 31

#### Q25. [Technical] In production HPC automation scripts, what is the effect of placing the directive 'set -e' at the beginning of the script?

- (A) The shell will immediately exit if any command or pipeline returns a non-zero exit status, preventing cascading errors
- (B) The shell prints every command to the terminal before executing it
- (C) The shell ignores all syntax errors and proceeds execution
- (D) The shell allocates maximum GPU memory to all child processes

#### Q26. [Numerical] An HPC batch simulation job terminates unexpectedly. In the shell, checking 'echo $?' yields an exit code of 137. By standard Linux convention, a process killed by an external operating system signal returns '128 + Signal Number'. Which Linux signal terminated the process?

- (A) Signal 1 (SIGHUP)
- (B) Signal 2 (SIGINT)
- (C) Signal 9 (SIGKILL / Out-Of-Memory Killer)
- (D) Signal 15 (SIGTERM)

#### Q27. [Scenario] A student writes an automation pipeline: "cat input.dat | grep 'CRITICAL_METRIC' | awk '{print $2}' > output.txt". The input file 'input.dat' does not exist, yet the bash script continues execution and reports exit status '$? = 0'. Why did this silent failure occur, and how should it be prevented?

- (A) By default, a shell pipeline returns the exit status of the LAST command in the pipeline ('awk'), masking the failure of 'cat'; enabling 'set -o pipefail' ensures the pipeline returns non-zero if ANY stage fails
- (B) 'cat' always returns exit code 0 even if files are missing
- (C) Redirection with '>' forces the shell to ignore all previous errors
- (D) 'awk' elevated the execution privileges to root

#### Q28. [Technical] What is an important technical advantage of using the modern Bash compound conditional construct '[[ ... ]]' over the traditional POSIX test operator '[ ... ]'?

- (A) '[ ... ]' is executed by the kernel, whereas '[[ ... ]]' runs in user space
- (B) '[[ ... ]]' requires compiling the script with GCC before execution
- (C) '[ ... ]' only supports floating-point comparisons, while '[[ ... ]]' supports integers
- (D) '[[ ... ]]' is a shell keyword that prevents word splitting and pathname expansion on unquoted variable expansions and supports pattern matching with the '=~' regex operator

## 🔷 Module 5: Secured Shell (SSH)

#### Q29. [Foundational] What is the standard IANA default network TCP port number on which the OpenSSH daemon ('sshd') listens for incoming secure remote shell connections?

- (A) Port 80
- (B) Port 443
- (C) Port 22
- (D) Port 8080

#### Q30. [Foundational] When setting up passwordless public-key authentication to an HPC cluster login node, where must the user's PUBLIC key be appended on the remote server?

- (A) '~/.ssh/authorized_keys'
- (B) '~/.ssh/known_hosts'
- (C) '/etc/ssh/ssh_config'
- (D) '~/.bashrc'

#### Q31. [Numerical] Modern HPC clusters recommend 256-bit Ed25519 elliptic-curve SSH keys, which offer equivalent cryptographic security strength to classic 3072-bit RSA keys. By what factor (ratio) is the Ed25519 key size smaller than the equivalent RSA key size?

- (A) 4x smaller
- (B) 8x smaller
- (C) 12x smaller
- (D) 24x smaller

#### Q32. [Scenario] A user generates an Ed25519 key pair and copies the private key to a new workstation. When running 'ssh -i ~/.ssh/id_ed25519 user@hpc.gla.ac.in', the connection immediately terminates with: 'Permissions 0777 for id_ed25519 are too open'. Which exact command resolves this error?

- (A) 'chmod 600 ~/.ssh/id_ed25519'
- (B) 'chmod 755 ~/.ssh/id_ed25519'
- (C) 'chown root ~/.ssh/id_ed25519'
- (D) 'rm -f ~/.ssh/known_hosts'

#### Q33. [Numerical] A research student transfers a 45 Gigabyte (GB) raw simulation dataset from a local workstation to the cluster storage over a dedicated 1 Gigabit per second (1 Gbps) Ethernet link using 'scp'. Assuming 100% link utilization without protocol overhead, what is the theoretical minimum transfer time in seconds?

- (A) 45 seconds
- (B) 90 seconds
- (C) 180 seconds
- (D) 360 seconds

#### Q34. [Scenario] What critical security vulnerability is introduced when an administrator or user enables SSH Agent Forwarding ('ssh -A') when connecting to an untrusted intermediate bastion host?

- (A) Any user with root privileges on the intermediate host can access the forwarded SSH agent's Unix domain socket and authenticate to other remote servers as you without knowing your passphrase
- (B) The intermediate host steals your raw private key file and saves it in '/etc/shadow'
- (C) Agent forwarding permanently decrypts all data on your local laptop hard drive
- (D) It exposes the client machine to denial-of-service via ICMP flood

#### Q35. [Technical] In high-frequency automated HPC scripting environments, what is the architectural benefit of configuring SSH Connection Multiplexing using 'ControlMaster' and 'ControlPath'?

- (A) It automatically distributes a single SSH session across multiple physical Ethernet switches
- (B) It encrypts SSH traffic twice with independent AES-256 ciphers
- (C) It maintains a persistent master TCP socket connection, allowing subsequent SSH/SCP sessions to bypass public-key handshakes and authentication overhead
- (D) It prevents compute nodes from communicating with each other

## 🔷 Module 6: Intel oneAPI Toolkit

#### Q36. [Conceptual] What is the primary industry objective of the Intel oneAPI programming model?

- (A) To replace the Linux operating system kernel with an Intel-proprietary microkernel
- (B) To provide an open, cross-architecture, standards-based unified programming framework that abstracts software development across diverse CPUs, GPUs, FPGAs, and AI accelerators
- (C) To restrict high-performance software development exclusively to Intel Core desktop processors
- (D) To serve as a commercial subscription-only cloud database engine

#### Q37. [Foundational] Which shell script must be sourced in an HPC Linux environment to set up the necessary PATH, LD_LIBRARY_PATH, and compiler variables for the Intel oneAPI toolkits?

- (A) 'source /opt/intel/oneapi/setvars.sh'
- (B) 'bash /opt/intel/oneapi/init.sh'
- (C) 'exec start_oneapi'
- (D) 'python /opt/intel/run_toolkit.py'

#### Q38. [Technical] Intel oneAPI DPC++ (Data Parallel C++) is based upon and actively contributes to which open industry standard maintained by the Khronos Group?

- (A) CUDA
- (B) OpenMP
- (C) SYCL (Single-source C++ heterogeneous programming standard)
- (D) Vulkan GLSL

#### Q39. [Numerical] In a SYCL kernel execution, a 1-dimensional computational domain of global size 2048 work-items is launched with a work-group size specified as 'sycl::range<1>(256)'. How many independent work-groups will the SYCL runtime schedule across the hardware compute units?

- (A) 4 work-groups
- (B) 8 work-groups
- (C) 16 work-groups
- (D) 32 work-groups

#### Q40. [Technical] In SYCL Unified Shared Memory (USM), what is the key functional difference between 'malloc_device' and 'malloc_host' memory allocations?

- (A) 'malloc_device' allocates memory strictly in accelerator high-bandwidth memory (inaccessible directly by CPU pointers), whereas 'malloc_host' allocates pinned host memory accessible by both CPU and GPU
- (B) 'malloc_device' allocates memory on hard disks, while 'malloc_host' allocates memory on tape drives
- (C) 'malloc_device' is limited to 1 Megabyte, while 'malloc_host' is unlimited
- (D) 'malloc_host' cannot be read by accelerator GPUs

#### Q41. [Numerical] A developer allocates a 2D square matrix of dimension 2048 x 2048 containing double-precision floating-point numbers ('sizeof(double) = 8 bytes') using 'sycl::malloc_shared'. How many Megabytes (MB) of memory does this single allocation request?

- (A) 8 MB
- (B) 16 MB
- (C) 32 MB
- (D) 64 MB

#### Q42. [Scenario] When creating a SYCL command queue, what operational difference exists between an in-order queue ('sycl::property::queue::in_order') and the default out-of-order queue?

- (A) An in-order queue can only run on single-core CPUs and cannot target GPUs
- (B) Out-of-order queues automatically discard failed execution tasks without notification
- (C) In-order queues disable all asynchronous memory transfers
- (D) An in-order queue executes submitted command groups strictly in the sequential order they are submitted, whereas default out-of-order queues can execute commands concurrently unless explicit SYCL events/dependencies are declared

## 🔷 Module 7: Intel HPC Toolkit

#### Q43. [Foundational] Which modern LLVM-based C++ compiler provided in the Intel HPC Toolkit is used to compile high-performance SYCL and modern C++ parallel applications?

- (A) 'gcc'
- (B) 'icpx'
- (C) 'javac'
- (D) 'cl.exe'

#### Q44. [Foundational] Which high-performance Fortran compiler in the Intel HPC Toolkit is the modern LLVM-based replacement for the classic 'ifort' compiler?

- (A) 'ifx'
- (B) 'gfortran'
- (C) 'f90'
- (D) 'flang'

#### Q45. [Technical] When compiling computational physics or machine learning C/C++ codes with 'icpx', what optimization does the flag '-xHost' instruct the compiler to perform?

- (A) It binds the compiled binary to execute exclusively on a specific network IP address
- (B) It runs the code inside an isolated Docker container
- (C) It instructs the compiler to generate SIMD vector instructions targeting the highest instruction set supported by the compilation host CPU (e.g., AVX-512)
- (D) It disables all loop unrolling and optimization to prioritize compilation speed

#### Q46. [Numerical] An Intel MPI simulation is submitted across 4 cluster compute nodes with the execution command: 'mpirun -n 64 -ppn 16 ./simulation_app'. How many total MPI ranks (processes) are spawned in total, and how many MPI ranks execute per physical node?

- (A) 16 total ranks, 4 ranks per node
- (B) 32 total ranks, 8 ranks per node
- (C) 128 total ranks, 32 ranks per node
- (D) 64 total ranks, 16 ranks per node

#### Q47. [Scenario] Which diagnostic analysis tool included in the Intel HPC Toolkit is designed to detect dynamic memory corruption, memory leaks, uninitialized memory accesses, and threading data races without needing specialized recompilation?

- (A) Intel Inspector
- (B) Intel Advisor
- (C) Intel Trace Analyzer and Collector (ITAC)
- (D) Intel oneDNN

#### Q48. [Scenario] An HPC engineer profiles an OpenMP simulation on a dual-socket 64-core Intel Xeon node and observes severe memory latency spikes due to cross-socket UPI traffic. Which command pins the process to CPU cores on Socket 0 and restricts physical memory allocation exclusively to Socket 0's local NUMA domain?

- (A) Remote NUMA access causes immediate hardware watchdog reboot
- (B) numactl --cpunodebind=0 --membind=0 ./simulation_app
- (C) nice -n -20 ./simulation_app
- (D) nohup ./simulation_app &

#### Q49. [Numerical] Hardware profiling on a dual-socket Intel Xeon server indicates that local NUMA memory read access on Socket 0 takes 75 nanoseconds (ns), while accessing remote memory attached to Socket 1 across the Intel UPI interconnect takes 135 nanoseconds (ns). What is the percentage increase in memory access latency incurred by the remote NUMA access?

- (A) 20% increase
- (B) 45% increase
- (C) 80% increase
- (D) 150% increase

#### Q50. [Technical] What is the architectural role of the Open Fabrics Interfaces (OFI / Libfabric) provider layer underneath the Intel MPI Library in high-performance computing clusters?

- (A) It acts as a modular, hardware-independent network abstraction framework allowing Intel MPI to interface directly with high-speed kernel-bypass fabrics (InfiniBand verbs, RoCE, Omni-Path, TCP) with minimal overhead
- (B) It converts MPI communication messages into HTTP REST API queries
- (C) It encrypts cluster network packets using software RSA-4096 keys
- (D) It assigns dynamic IP addresses to compute nodes using DHCP
