# 🏛️ GLA UNIVERSITY, MATHURA
## DEPARTMENT OF COMPUTER ENGINEERING & TECHNOLOGY
### High Performance Computing & Heterogeneous AI Systems (GLA-HPC-BCSG701)
#### DAY 1 WORKSHOP ENTRANCE & DIAGNOSTIC PRE-ASSESSMENT

**Student Name:** ____________________________________ | **Roll Number:** ____________________
**Section / Group:** _________________________________ | **Date:** __________________________
**Time Allowed:** 60 Minutes | **Total Marks:** 50 Marks (1 Mark per Question | No Negative Marking)

---

> **Instructions to Candidates:**
> 1. This pre-assessment contains exactly 50 multiple-choice questions covering High Performance Computing, Intel Silicon Architecture, Linux Systems, Shell Automation, SSH Security, and the oneAPI Ecosystem.
> 2. Choose the single best answer for each question and mark the corresponding option (A, B, C, or D).
> 3. This test establishes your diagnostic entry baseline for the 5-day masterclass certification.

---

## 🔷 SECTION A: HPC Foundations, Linux VFS, Shell & SSH (Questions 01 – 25)

**Q01. What does HPC stand for?**
- (A) High Performance Computing
- (B) Heavy Processing Cluster
- (C) Hardware Parallel Control
- (D) Heterogeneous Processor Core

**Q02. Which architectural limitation primarily prevents standard consumer laptops from training 70-Billion parameter LLMs?**
- (A) Operating system GUI overhead
- (B) Memory Wall (limited DDR channels, capacity & bandwidth)
- (C) Slower SSD read speeds only
- (D) Absence of Python 3.12

**Q03. In an HPC cluster topology, what is the role of the Head / Login Node?**
- (A) Running heavy 50-hour model training jobs directly
- (B) Providing a secure access gateway for editing code, compiling, and submitting batch jobs
- (C) Acting as a high-voltage power transformer
- (D) Storing long-term tape archives only

**Q04. Which Intel silicon engine is purpose-built with integrated 24x 100GbE RoCE networking for large-scale Deep Learning training?**
- (A) Intel Core i9-14900K
- (B) Intel Xeon Platinum 8480+
- (C) Habana Gaudi 2 / Gaudi 3
- (D) Intel Arc A770

**Q05. What hardware feature in 4th/5th Gen Intel Xeon Scalable processors provides on-die matrix multiplication acceleration?**
- (A) Hyper-Threading
- (B) Intel AMX (Advanced Matrix Extensions)
- (C) QuickPath Interconnect
- (D) Turbo Boost 2.0

**Q06. What does an absolute path in Linux always start with?**
- (A) `~` (Tilde)
- (B) `.` (Dot)
- (C) `/` (Forward slash / Root)
- (D) `C:\`

**Q07. Which command lists all files including hidden dotfiles with detailed permissions and human-readable file sizes?**
- (A) `dir /a`
- (B) `ls -la`
- (C) `show -all`
- (D) `list -files`

**Q08. What happens when a user deletes a file with `rm file.txt` on a remote Linux server?**
- (A) It moves to the Windows Recycle Bin
- (B) It is moved to `/tmp/recycle` and can be restored for 30 days
- (C) It is permanently unlinked immediately without confirmation
- (D) The server prompts the administrator for an OTP

**Q09. How do you correctly assign a string to a variable in Bash?**
- (A) `CLUSTER = "GLA_HPC"`
- (B) `set CLUSTER = "GLA_HPC"`
- (C) `CLUSTER="GLA_HPC"`
- (D) `var CLUSTER := "GLA_HPC"`

**Q10. What is line 1 of an automated Bash script called (`#!/bin/bash`)?**
- (A) Hashpipe
- (B) Shebang
- (C) Preprocessor Directive
- (D) Interpreter Header

**Q11. Which permission command must be run before executing a newly created script via `./automate.sh`?**
- (A) `chmod +x automate.sh`
- (B) `chown root automate.sh`
- (C) `chmod 444 automate.sh`
- (D) `attrib +r automate.sh`

**Q12. In shell scripting, what does `command >> output.log` do?**
- (A) Overwrites `output.log` with the command output
- (B) Appends command output to the end of `output.log`
- (C) Deletes `output.log` if an error occurs
- (D) Redirects standard input from `output.log`

**Q13. What is the default network port used by the Secure Shell (SSH) protocol?**
- (A) 21
- (B) 22
- (C) 80
- (D) 443

**Q14. Which asymmetric algorithm is modern industry best-practice for SSH key generation?**
- (A) DES
- (B) MD5
- (C) Ed25519
- (D) SHA-1

**Q15. Where must a student's public SSH key be placed on a remote Linux server to allow passwordless login?**
- (A) `/etc/ssh/ssh_config`
- (B) `~/.ssh/authorized_keys`
- (C) `/var/log/secure`
- (D) `~/public_keys.txt`

**Q16. What is the fundamental vision behind the Intel oneAPI programming model?**
- (A) Rewriting all software in Python
- (B) Single-source cross-architecture programming (CPU, GPU, FPGA) without proprietary lock-in
- (C) Restricting software to run exclusively on Intel Core i5 laptops
- (D) Eliminating the C++ language

**Q17. What standard language extension is used by oneAPI for heterogeneous parallel computing?**
- (A) CUDA C
- (B) SYCL (Standard C++)
- (C) Visual Basic
- (D) JavaScript

**Q18. Which script initializes the Intel oneAPI environment variables (`$PATH`, `$LD_LIBRARY_PATH`)?**
- (A) `source /etc/profile`
- (B) `source /opt/intel/oneapi/setvars.sh`
- (C) `bash install_oneapi.sh`
- (D) `init_intel.cmd`

**Q19. What is the name of the LLVM-based Intel oneAPI C++ Compiler?**
- (A) `gcc`
- (B) `clang++`
- (C) `icpx`
- (D) `msvc`

**Q20. What is the primary role of the Intel oneMKL library in the oneAPI Base Toolkit?**
- (A) Parsing HTML web pages
- (B) High-performance math kernels (BLAS, LAPACK, FFT) optimized for AVX-512 and AMX
- (C) Managing network firewalls
- (D) Rendering 3D video game animations

**Q21. Which tool in the Intel HPC Toolkit is used to detect memory leaks and thread race conditions in parallel applications?**
- (A) Intel Inspector
- (B) GDB
- (C) Valgrind only
- (D) Wireshark

**Q22. Which library in the Intel HPC Toolkit enables multi-node message passing across cluster networks?**
- (A) Intel oneDNN
- (B) Intel MPI Library
- (C) Intel oneDAL
- (D) Intel DPC++

**Q23. What command displays the exit status code of the immediately preceding command in Bash?**
- (A) `echo $STATUS`
- (B) `echo $?`
- (C) `return`
- (D) `check`

**Q24. In Linux, what does the `$PATH` environment variable represent?**
- (A) The filepath of the current text document
- (B) A colon-separated list of directories searched by the shell to find executable binaries
- (C) The user's home folder location
- (D) The network IP route to the internet

**Q25. Which of the following topics belongs STRICTLY to Day 2 and should NOT be executed on Day 1?**
- (A) Linux Filesystem Navigation
- (B) Shell Scripting Automation
- (C) OpenMP multithreading & MPI distributed computing
- (D) Intel oneAPI environment sourcing


---

## 🔷 SECTION B: Supercomputer Architecture, NUMA, Fabrics & oneAPI (Questions 26 – 50)

**Q26. Why did Dennard scaling breakdown around 2005, forcing processor manufacturers to transition from increasing single-core clock frequencies to multi-core and heterogeneous architectures?**
- (A) Sub-threshold leakage current and static power dissipation grew exponentially at sub-90nm process nodes, causing thermal runaway.
- (B) Amdahl's law proved that clock frequencies above 4 GHz mathematically reduce instruction-level parallelism.
- (C) InfiniBand fabric became mandatory for motherboard bus routing, capping CPU clock oscillators.
- (D) Operating system schedulers could not allocate virtual memory addresses faster than 3.8 GHz.

**Q27. According to Amdahl's Law, if 90% of an HPC application's execution time is parallelizable and 10% is strictly sequential, what is the theoretical maximum speedup limit as the number of parallel processor cores approaches infinity?**
- (A) 90x
- (B) 10x
- (C) 100x
- (D) Infinity

**Q28. How does Gustafson's Law fundamentally differ from Amdahl's Law in evaluating the scalability of high-performance computing clusters?**
- (A) Gustafson's Law assumes a fixed problem size, whereas Amdahl's Law scales the problem size with core count.
- (B) Gustafson's Law models scaled speedup where problem size increases proportionally to compute resources, demonstrating that the parallel fraction dominates large-scale workloads.
- (C) Gustafson's Law only applies to shared-memory NUMA nodes, while Amdahl's Law applies to InfiniBand networks.
- (D) Gustafson's Law models GPU matrix multiplication while Amdahl's Law models CPU scalar execution.

**Q29. In a dual-socket 4th Gen Intel Xeon Scalable (Sapphire Rapids) server, what interconnect fabric facilitates cache-coherent inter-socket communication, and what is its typical latency penalty relative to local DRAM access?**
- (A) PCIe Gen 3 bus; ~20ns penalty.
- (B) Intel Ultra Path Interconnect (UPI); approximately 60ns to 80ns latency penalty compared to local NUMA memory.
- (C) InfiniBand HDR switch; ~500ns penalty.
- (D) SATA Express controller; 10x slower bandwidth.

**Q30. What is the register width and single-precision IEEE 754 floating-point capacity of Intel AVX-512 vector units?**
- (A) 256 bits, processing 8 FP32 values per instruction.
- (B) 512 bits (ZMM registers), processing 16 FP32 values per instruction.
- (C) 128 bits (XMM registers), processing 4 FP32 values per instruction.
- (D) 1024 bits, processing 32 FP32 values per instruction.

**Q31. What architectural engine was introduced in 4th Gen Intel Xeon Scalable (Sapphire Rapids) to accelerate deep learning tensor matrix multiplications in hardware?**
- (A) Intel AMX (Advanced Matrix Extensions) with 2D tile registers (TMM) and TMUL matrix multiplication units.
- (B) Intel Iris Xe Integrated Graphics Core.
- (C) Intel QuickPath Interconnect (QPI).
- (D) Intel Hyper-Threading Technology v2.

**Q32. In the NEC SX-Aurora TSUBASA supercomputing architecture, what role does the Intel Xeon processor play relative to the NEC Vector Engine (VE)?**
- (A) The Intel Xeon acts as the Vector Host (VH), running the Linux OS, managing storage/Lustre I/O, and job dispatching, while the NEC VE PCIe card executes ultra-wide vector computations.
- (B) The Intel Xeon is an idle standby CPU used only if the NEC Vector Engine burns out.
- (C) The Intel Xeon is embedded inside the NEC PCIe card as an L1 cache controller.
- (D) The NEC VE runs the Linux kernel while the Intel Xeon acts as a graphical display adapter.

**Q33. What is the peak memory bandwidth of the NEC SX-Aurora TSUBASA Type 20B Vector Engine, and what memory technology enables it?**
- (A) 128 GB/s using standard DDR4 memory.
- (B) 1.53 TB/s using stacked High Bandwidth Memory (HBM2).
- (C) 25.6 GB/s using PCIe Gen 3 lanes.
- (D) 500 GB/s using GDDR6 graphic memory.

**Q34. In an HPC Linux cluster, what is the functional difference between `/home` and `/scratch` parallel file systems?**
- (A) `/home` is backed by high-throughput parallel Lustre storage for high IOPS, while `/scratch` is a slow USB stick.
- (B) `/home` is typically an NFS share for source code and config files, while `/scratch` is a high-bandwidth parallel file system (Lustre/GPFS) striped across Object Storage Targets (OSTs) for temporary simulation data.
- (C) `/scratch` is volatile RAM that gets erased every second.
- (D) `/home` is only accessible by root, while `/scratch` is for normal users.

**Q35. Why is the bash directive `set -euo pipefail` considered mandatory for professional HPC job automation scripts?**
- (A) It automatically compiles Python scripts into C++ binaries before execution.
- (B) It halts execution immediately if any command fails (-e), if an unset variable is referenced (-u), or if any command in a pipeline fails (-o pipefail), preventing silent corrupted calculations.
- (C) It allocates 100% of GPU memory to the current shell.
- (D) It disables password prompts across the entire university network.

**Q36. Which elliptic-curve algorithm is the modern enterprise standard for HPC passwordless SSH keys, replacing legacy RSA 2048/4096-bit keys due to superior security and cryptographic handshake speed?**
- (A) DES
- (B) Ed25519
- (C) MD5
- (D) SHA-1

**Q37. In OpenSSH configuration (`~/.ssh/config`), what does the directive `ControlMaster auto` combined with `ControlPath` achieve in an HPC cluster environment?**
- (A) It allows normal users to gain root privileges on compute nodes.
- (B) It enables SSH connection multiplexing, reusing a single master TCP connection for subsequent sessions and eliminating the latency of repeated TLS/cryptographic handshakes.
- (C) It controls the CPU fan speed of remote servers.
- (D) It automatically formats hard drives on remote nodes.

**Q38. What is the primary role of Lmod / Environment Modules (`module load`, `module purge`) on production HPC clusters?**
- (A) It installs Linux kernel drivers directly into motherboard BIOS.
- (B) It dynamically modifies shell environment variables (`PATH`, `LD_LIBRARY_PATH`, `CPATH`) to switch between conflicting compiler toolchains and MPI versions without system-wide collisions.
- (C) It acts as an anti-virus scanner for student home directories.
- (D) It provides a web interface for playing video games on supercomputers.

**Q39. What is the core distinction between the Intel oneAPI Base Toolkit and the Intel oneAPI HPC Toolkit?**
- (A) Base Toolkit is for Microsoft Office; HPC Toolkit is for Linux kernels.
- (B) Base Toolkit provides core SYCL/DPC++ compilers, oneMKL, oneDAL, and profiling tools; HPC Toolkit extends this with production C/C++/Fortran compilers (`icx`, `ifx`), Intel MPI Library, and cluster analysis tools (ITAC, Inspector).
- (C) Base Toolkit is paid; HPC Toolkit is open-source.
- (D) Base Toolkit only runs on laptops; HPC Toolkit only runs on quantum computers.

**Q40. What command-line tool is used in modern Linux kernels to inspect NUMA node assignments, socket CPU affinity, and distance matrices between CPU sockets and memory controllers?**
- (A) numactl --hardware
- (B) ipconfig /all
- (C) systemctl restart numa
- (D) cat /etc/hosts

**Q41. What does a NUMA distance value of '21' relative to a local distance of '10' indicate in `numactl -H` output?**
- (A) The remote memory has 21 GB of capacity.
- (B) Accessing memory located on the remote socket takes approximately 2.1x more latency than accessing memory attached to the local socket.
- (C) The memory controller is operating at 21 MHz clock speed.
- (D) The network connection is 21 Gbps Ethernet.

**Q42. What flag must be passed to the Intel oneAPI C/C++ compiler (`icx`) to instruct it to generate optimized AVX-512 vector instructions targeting Intel 4th Gen Xeon Scalable processors?**
- (A) -O0 -mno-simd
- (B) -O3 -xSapphireRapids (or -mavx512f -mavx512dq -mavx512bw)
- (C) -cuda-arch=sm_80
- (D) -march=armv8-a

**Q43. In Linux cluster administration, what virtual filesystem exposes real-time hardware status such as CPU temperature, frequency scaling governors, and memory sub-timings?**
- (A) /sys and /proc
- (B) /bin and /sbin
- (C) /opt and /usr
- (D) /var/log only

**Q44. What does the Linux command `lscpu -C` display?**
- (A) Computer cost breakdown.
- (B) Detailed CPU cache hierarchy, including L1 Data, L1 Instruction, L2, and L3 cache sizes, types, and core sharing mappings.
- (C) List of compiled C programs.
- (D) PCIe bus clock frequencies.

**Q45. In modern heterogeneous HPC clusters, what is the role of Intel Level Zero API?**
- (A) A low-level direct-to-metal hardware abstraction interface for Intel GPUs and AI accelerators, providing fine-grained device control below the SYCL layer.
- (B) A basic video game design framework.
- (C) An entry-level Linux terminal shell.
- (D) A tool to delete user passwords.

**Q46. What is the key technological feature of InfiniBand NDR networking in top-tier HPC clusters?**
- (A) 400 Gbps per-port throughput with sub-microsecond latency and hardware-offloaded RDMA (Remote Direct Memory Access).
- (B) 10 Mbps dial-up protocol for legacy terminals.
- (C) Wireless Wi-Fi 6 transmission over antennas.
- (D) Bluetooth 5.0 mesh for keyboard connectivity.

**Q47. What is a Fat-Tree network topology in supercomputer cluster design?**
- (A) A tree topology where tree branches grow thicker (more aggregated bandwidth) toward the root, guaranteeing full bisection non-blocking bandwidth across all compute racks.
- (B) A circular ring where all computers share a single cable.
- (C) A wireless network configured in an outdoor park.
- (D) A random daisy chain of ethernet switches.

**Q48. What Linux tool allows an engineer to pin a process to a specific NUMA node and enforce that memory allocations only occur from that node's local memory controllers?**
- (A) numactl --cpunodebind=0 --membind=0 ./app
- (B) kill -9 ./app
- (C) chmod +x ./app
- (D) grep -r numa ./app

**Q49. What does SYCL represent within the Intel oneAPI programming ecosystem?**
- (A) An open standard, single-source C++ programming model governed by Khronos Group for heterogeneous computing across CPUs, GPUs, FPGAs, and AI accelerators.
- (B) A proprietary Nvidia compiler for CUDA graphics cards.
- (C) A replacement for HTML and CSS websites.
- (D) A database query language similar to SQL.

**Q50. When configuring passwordless SSH keys for an HPC cluster, why must the permissions of `~/.ssh` and `~/.ssh/authorized_keys` strictly be set to `700` and `600` respectively?**
- (A) Because SSH daemons enforce strict permission checks and will refuse authentication if the directory or keys are writable by group or other users for security.
- (B) Because Linux hard drives cannot store files larger than 600 bytes.
- (C) Because the Slurm scheduler requires executable bits on authorized_keys.
- (D) Because the files are automatically encrypted with AES-700.
