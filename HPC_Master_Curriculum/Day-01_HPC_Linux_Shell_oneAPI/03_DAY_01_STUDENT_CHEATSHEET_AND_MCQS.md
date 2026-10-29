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

> Official 50-Question Diagnostic Bank for Day 1 Pre-Assessment (GLA University BCSG701)

### 🔷 Section A: Foundational Concepts & Operational Linux (Q01 – Q25)

#### Q1. What does HPC stand for?
- A) High Performance Computing
- B) Heavy Processing Cluster
- C) Hardware Parallel Control
- D) Heterogeneous Processor Core  
**Answer: A** | *Explanation: High Performance Computing refers to aggregating computing power to solve complex engineering and scientific problems.*

#### Q2. Which architectural limitation primarily prevents standard consumer laptops from training 70-Billion parameter LLMs?
- A) Operating system GUI overhead
- B) Memory Wall (limited DDR channels, capacity & bandwidth)
- C) Slower SSD read speeds only
- D) Absence of Python 3.12  
**Answer: B** | *Explanation: Consumer laptops typically have 2 memory channels (~60-80 GB/s bandwidth), whereas enterprise Xeon nodes have 8 to 16 channels exceeding 600 GB/s bandwidth.*

#### Q3. In an HPC cluster topology, what is the role of the Head / Login Node?
- A) Running heavy 50-hour model training jobs directly
- B) Providing a secure access gateway for editing code, compiling, and submitting batch jobs
- C) Acting as a high-voltage power transformer
- D) Storing long-term tape archives only  
**Answer: B** | *Explanation: The login node is shared by all users to prepare scripts and interact with the batch scheduler; heavy jobs must run on worker nodes.*

#### Q4. Which Intel silicon engine is purpose-built with integrated 24x 100GbE RoCE networking for large-scale Deep Learning training?
- A) Intel Core i9-14900K
- B) Intel Xeon Platinum 8480+
- C) Habana Gaudi 2 / Gaudi 3
- D) Intel Arc A770  
**Answer: C** | *Explanation: Habana Gaudi accelerators feature integrated RoCE RDMA network ports directly on-die to eliminate external networking bottlenecks during distributed training.*

#### Q5. What hardware feature in 4th/5th Gen Intel Xeon Scalable processors provides on-die matrix multiplication acceleration?
- A) Hyper-Threading
- B) Intel AMX (Advanced Matrix Extensions)
- C) QuickPath Interconnect
- D) Turbo Boost 2.0  
**Answer: B** | *Explanation: Intel AMX introduces dedicated hardware tile registers (TMUL) for accelerating BF16 and INT8 matrix math directly on the CPU.*

#### Q6. What does an absolute path in Linux always start with?
- A) `~` (Tilde)
- B) `.` (Dot)
- C) `/` (Forward slash / Root)
- D) `C:\`  
**Answer: C** | *Explanation: An absolute path begins at the root of the filesystem hierarchy (`/`).*

#### Q7. Which command lists all files including hidden dotfiles with detailed permissions and human-readable file sizes?
- A) `dir /a`
- B) `ls -la`
- C) `show -all`
- D) `list -files`  
**Answer: B** | *Explanation: In `ls -la`, `-l` enables long listing, `-a` includes all hidden files, and `-h` makes file sizes human-readable.*

#### Q8. What happens when a user deletes a file with `rm file.txt` on a remote Linux server?
- A) It moves to the Windows Recycle Bin
- B) It is moved to `/tmp/recycle` and can be restored for 30 days
- C) It is permanently unlinked immediately without confirmation
- D) The server prompts the administrator for an OTP  
**Answer: C** | *Explanation: Standard Linux `rm` unlinks the inode immediately; there is no default recycle bin on terminal sessions.*

#### Q9. How do you correctly assign a string to a variable in Bash?
- A) `CLUSTER = "GLA_HPC"`
- B) `set CLUSTER = "GLA_HPC"`
- C) `CLUSTER="GLA_HPC"`
- D) `var CLUSTER := "GLA_HPC"`  
**Answer: C** | *Explanation: Bash does not allow spaces around the `=` assignment operator.*

#### Q10. What is line 1 of an automated Bash script called (`#!/bin/bash`)?
- A) Hashpipe
- B) Shebang
- C) Preprocessor Directive
- D) Interpreter Header  
**Answer: B** | *Explanation: `#!` is called the Shebang, instructing the OS loader which interpreter binary to invoke.*

#### Q11. Which permission command must be run before executing a newly created script via `./automate.sh`?
- A) `chmod +x automate.sh`
- B) `chown root automate.sh`
- C) `chmod 444 automate.sh`
- D) `attrib +r automate.sh`  
**Answer: A** | *Explanation: Newly created files lack execute permission by default; `chmod +x` enables the executable bit.*

#### Q12. In shell scripting, what does `command >> output.log` do?
- A) Overwrites `output.log` with the command output
- B) Appends command output to the end of `output.log`
- C) Deletes `output.log` if an error occurs
- D) Redirects standard input from `output.log`  
**Answer: B** | *Explanation: `>` overwrites a file, while `>>` appends to the existing file.*

#### Q13. What is the default network port used by the Secure Shell (SSH) protocol?
- A) 21
- B) 22
- C) 80
- D) 443  
**Answer: B** | *Explanation: SSH runs on standard TCP port 22.*

#### Q14. Which asymmetric algorithm is modern industry best-practice for SSH key generation?
- A) DES
- B) MD5
- C) Ed25519
- D) SHA-1  
**Answer: C** | *Explanation: Ed25519 (Edwards-curve Digital Signature Algorithm) offers superior security and performance over legacy RSA and DSA.*

#### Q15. Where must a student's public SSH key be placed on a remote Linux server to allow passwordless login?
- A) `/etc/ssh/ssh_config`
- B) `~/.ssh/authorized_keys`
- C) `/var/log/secure`
- D) `~/public_keys.txt`  
**Answer: B** | *Explanation: The OpenSSH daemon checks `~/.ssh/authorized_keys` for recognized client public keys.*

#### Q16. What is the fundamental vision behind the Intel oneAPI programming model?
- A) Rewriting all software in Python
- B) Single-source cross-architecture programming (CPU, GPU, FPGA) without proprietary lock-in
- C) Restricting software to run exclusively on Intel Core i5 laptops
- D) Eliminating the C++ language  
**Answer: B** | *Explanation: oneAPI is an open, standards-based unified programming model built on SYCL to target heterogeneous architectures.*

#### Q17. What standard language extension is used by oneAPI for heterogeneous parallel computing?
- A) CUDA C
- B) SYCL (Standard C++)
- C) Visual Basic
- D) JavaScript  
**Answer: B** | *Explanation: SYCL is the Khronos open standard for heterogeneous computing in standard ISO C++.*

#### Q18. Which script initializes the Intel oneAPI environment variables (`$PATH`, `$LD_LIBRARY_PATH`)?
- A) `source /etc/profile`
- B) `source /opt/intel/oneapi/setvars.sh`
- C) `bash install_oneapi.sh`
- D) `init_intel.cmd`  
**Answer: B** | *Explanation: `setvars.sh` sets all necessary compiler, library, and tool paths for the active shell session.*

#### Q19. What is the name of the LLVM-based Intel oneAPI C++ Compiler?
- A) `gcc`
- B) `clang++`
- C) `icpx`
- D) `msvc`  
**Answer: C** | *Explanation: `icpx` is the modern LLVM-based Intel C++ Compiler supporting DPC++, SYCL, and OpenMP.*

#### Q20. What is the primary role of the Intel oneMKL library in the oneAPI Base Toolkit?
- A) Parsing HTML web pages
- B) High-performance math kernels (BLAS, LAPACK, FFT) optimized for AVX-512 and AMX
- C) Managing network firewalls
- D) Rendering 3D video game animations  
**Answer: B** | *Explanation: Intel oneMKL (Math Kernel Library) provides heavily optimized linear algebra, FFT, and vector math routines.*

#### Q21. Which tool in the Intel HPC Toolkit is used to detect memory leaks and thread race conditions in parallel applications?
- A) Intel Inspector
- B) GDB
- C) Valgrind only
- D) Wireshark  
**Answer: A** | *Explanation: Intel Inspector is a memory and thread error debugger for C, C++, and Fortran applications.*

#### Q22. Which library in the Intel HPC Toolkit enables multi-node message passing across cluster networks?
- A) Intel oneDNN
- B) Intel MPI Library
- C) Intel oneDAL
- D) Intel DPC++  
**Answer: B** | *Explanation: Intel MPI implements the MPI-3.1 standard optimized for low-latency cluster interconnects.*

#### Q23. What command displays the exit status code of the immediately preceding command in Bash?
- A) `echo $STATUS`
- B) `echo $?`
- C) `return`
- D) `check`  
**Answer: B** | *Explanation: `$?` stores the exit code of the last executed command (0 = Success, non-zero = Failure).*

#### Q24. In Linux, what does the `$PATH` environment variable represent?
- A) The filepath of the current text document
- B) A colon-separated list of directories searched by the shell to find executable binaries
- C) The user's home folder location
- D) The network IP route to the internet  
**Answer: B** | *Explanation: When a command name is typed, the shell searches directories listed in `$PATH` in order.*

#### Q25. Which of the following topics belongs STRICTLY to Day 2 and should NOT be executed on Day 1?
- A) Linux Filesystem Navigation
- B) Shell Scripting Automation
- C) OpenMP multithreading & MPI distributed computing
- D) Intel oneAPI environment sourcing  
**Answer: C** | *Explanation: OpenMP, MPI, and oneDAL Machine Learning are scheduled for Day 2 as per the official curriculum.*

---

### 🔷 Section B: Advanced Supercomputer & Silicon Architecture (Q26 – Q50)

### Question 26 (D1-Q26)
**Why did Dennard scaling breakdown around 2005, forcing processor manufacturers to transition from increasing single-core clock frequencies to multi-core and heterogeneous architectures?**

- **(A)** Sub-threshold leakage current and static power dissipation grew exponentially at sub-90nm process nodes, causing thermal runaway.
- **(B)** Amdahl's law proved that clock frequencies above 4 GHz mathematically reduce instruction-level parallelism.
- **(C)** InfiniBand fabric became mandatory for motherboard bus routing, capping CPU clock oscillators.
- **(D)** Operating system schedulers could not allocate virtual memory addresses faster than 3.8 GHz.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: Dennard scaling stated that as transistors shrink, power density stays constant because voltage and current scale downward proportionally. Below ~90nm, quantum tunneling and gate oxide leakage currents escalated exponentially. Operating voltages could no longer scale down without causing gate instability, leading to the 'Power Wall' where increasing clock speed resulted in uncontrollable thermal dissipation.

---

### Question 27 (D1-Q27)
**According to Amdahl's Law, if 90% of an HPC application's execution time is parallelizable and 10% is strictly sequential, what is the theoretical maximum speedup limit as the number of parallel processor cores approaches infinity?**

- **(A)** 90x
- **(B)** 10x
- **(C)** 100x
- **(D)** Infinity

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Amdahl's law states that maximum speedup S = 1 / ((1 - p) + (p / N)). As N -> infinity, p / N -> 0, leaving S_max = 1 / (1 - p). Here, p = 0.90, so S_max = 1 / (1 - 0.90) = 1 / 0.10 = 10x. Regardless of having 10,000 cores, the 10% serial bottleneck caps speedup at 10x.

---

### Question 28 (D1-Q28)
**How does Gustafson's Law fundamentally differ from Amdahl's Law in evaluating the scalability of high-performance computing clusters?**

- **(A)** Gustafson's Law assumes a fixed problem size, whereas Amdahl's Law scales the problem size with core count.
- **(B)** Gustafson's Law models scaled speedup where problem size increases proportionally to compute resources, demonstrating that the parallel fraction dominates large-scale workloads.
- **(C)** Gustafson's Law only applies to shared-memory NUMA nodes, while Amdahl's Law applies to InfiniBand networks.
- **(D)** Gustafson's Law models GPU matrix multiplication while Amdahl's Law models CPU scalar execution.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Amdahl's law assumes strong scaling (fixed problem size run on more cores). Gustafson's law assumes weak scaling (scaled speedup S(P) = P - alpha*(P - 1)), where as compute resources expand, scientists enlarge the problem grid, causing the time spent in parallel execution to dwarf the constant sequential setup phase.

---

### Question 29 (D1-Q29)
**In a dual-socket 4th Gen Intel Xeon Scalable (Sapphire Rapids) server, what interconnect fabric facilitates cache-coherent inter-socket communication, and what is its typical latency penalty relative to local DRAM access?**

- **(A)** PCIe Gen 3 bus; ~20ns penalty.
- **(B)** Intel Ultra Path Interconnect (UPI); approximately 60ns to 80ns latency penalty compared to local NUMA memory.
- **(C)** InfiniBand HDR switch; ~500ns penalty.
- **(D)** SATA Express controller; 10x slower bandwidth.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Intel Xeon multi-socket systems use UPI (Ultra Path Interconnect) links to maintain hardware cache coherency across sockets. Accessing memory attached to a local socket takes ~80ns, whereas a remote NUMA access crossing UPI links incurs an additional ~60-80ns (~140-160ns total), emphasizing the critical need for thread pinning and NUMA-aware allocation.

---

### Question 30 (D1-Q30)
**What is the register width and single-precision IEEE 754 floating-point capacity of Intel AVX-512 vector units?**

- **(A)** 256 bits, processing 8 FP32 values per instruction.
- **(B)** 512 bits (ZMM registers), processing 16 FP32 values per instruction.
- **(C)** 128 bits (XMM registers), processing 4 FP32 values per instruction.
- **(D)** 1024 bits, processing 32 FP32 values per instruction.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: AVX-512 defines thirty-two 512-bit wide vector registers (ZMM0 through ZMM31). In a single clock cycle, an AVX-512 Fused Multiply-Add (FMA) unit computes sixteen 32-bit single-precision floats simultaneously (512 / 32 = 16).

---

### Question 31 (D1-Q31)
**What architectural engine was introduced in 4th Gen Intel Xeon Scalable (Sapphire Rapids) to accelerate deep learning tensor matrix multiplications in hardware?**

- **(A)** Intel AMX (Advanced Matrix Extensions) with 2D tile registers (TMM) and TMUL matrix multiplication units.
- **(B)** Intel Iris Xe Integrated Graphics Core.
- **(C)** Intel QuickPath Interconnect (QPI).
- **(D)** Intel Hyper-Threading Technology v2.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: Intel AMX (Advanced Matrix Extensions) is a dedicated accelerator block embedded directly in Sapphire Rapids cores. It features 8 two-dimensional tile registers (TMM0-TMM7, 1KB each) and a TMUL (Tile Matrix Multiply) systolic execution unit capable of executing 2048 INT8 or 1024 BF16 operations per cycle.

---

### Question 32 (D1-Q32)
**In the NEC SX-Aurora TSUBASA supercomputing architecture, what role does the Intel Xeon processor play relative to the NEC Vector Engine (VE)?**

- **(A)** The Intel Xeon acts as the Vector Host (VH), running the Linux OS, managing storage/Lustre I/O, and job dispatching, while the NEC VE PCIe card executes ultra-wide vector computations.
- **(B)** The Intel Xeon is an idle standby CPU used only if the NEC Vector Engine burns out.
- **(C)** The Intel Xeon is embedded inside the NEC PCIe card as an L1 cache controller.
- **(D)** The NEC VE runs the Linux kernel while the Intel Xeon acts as a graphical display adapter.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: NEC SX-Aurora TSUBASA employs a decoupled hybrid model: the standard x86_64 CPU (Intel Xeon) is the Vector Host (VH), handling standard Linux OS services, network drivers, Slurm scheduling, and Lustre file I/O. The NEC Vector Engine (VE) is a dedicated PCIe processor with dedicated HBM2 memory delivering massive vector throughput.

---

### Question 33 (D1-Q33)
**What is the peak memory bandwidth of the NEC SX-Aurora TSUBASA Type 20B Vector Engine, and what memory technology enables it?**

- **(A)** 128 GB/s using standard DDR4 memory.
- **(B)** 1.53 TB/s using stacked High Bandwidth Memory (HBM2).
- **(C)** 25.6 GB/s using PCIe Gen 3 lanes.
- **(D)** 500 GB/s using GDDR6 graphic memory.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: The NEC SX-Aurora TSUBASA VE20B features integrated 3D-stacked HBM2 memory directly on the silicon interposer, delivering up to 1.53 Terabytes per second (TB/s) of memory bandwidth—essential for memory-bound sparse scientific HPC codes.

---

### Question 34 (D1-Q34)
**In an HPC Linux cluster, what is the functional difference between `/home` and `/scratch` parallel file systems?**

- **(A)** `/home` is backed by high-throughput parallel Lustre storage for high IOPS, while `/scratch` is a slow USB stick.
- **(B)** `/home` is typically an NFS share for source code and config files, while `/scratch` is a high-bandwidth parallel file system (Lustre/GPFS) striped across Object Storage Targets (OSTs) for temporary simulation data.
- **(C)** `/scratch` is volatile RAM that gets erased every second.
- **(D)** `/home` is only accessible by root, while `/scratch` is for normal users.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: In production HPC clusters, user home directories are hosted on standard NFS with strict storage quotas and backup snapshots. The high-performance parallel file systems (such as Lustre or IBM Spectrum Scale / GPFS) are mounted at `/scratch`, striping multi-terabyte datasets across dozens of parallel OSTs for hundreds of gigabytes per second of aggregated sequential I/O.

---

### Question 35 (D1-Q35)
**Why is the bash directive `set -euo pipefail` considered mandatory for professional HPC job automation scripts?**

- **(A)** It automatically compiles Python scripts into C++ binaries before execution.
- **(B)** It halts execution immediately if any command fails (-e), if an unset variable is referenced (-u), or if any command in a pipeline fails (-o pipefail), preventing silent corrupted calculations.
- **(C)** It allocates 100% of GPU memory to the current shell.
- **(D)** It disables password prompts across the entire university network.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: `set -e` ensures the script exits on non-zero command return; `set -u` treats uninitialized variables as fatal errors; and `set -o pipefail` ensures that a pipeline fails if any upstream command fails, rather than masking errors with the downstream command's exit code.

---

### Question 36 (D1-Q36)
**Which elliptic-curve algorithm is the modern enterprise standard for HPC passwordless SSH keys, replacing legacy RSA 2048/4096-bit keys due to superior security and cryptographic handshake speed?**

- **(A)** DES
- **(B)** Ed25519
- **(C)** MD5
- **(D)** SHA-1

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Ed25519 provides 128-bit security level equivalent to ~3000-bit RSA, but with significantly smaller keys (68 characters), immune to side-channel timing attacks, and orders of magnitude faster signature generation.

---

### Question 37 (D1-Q37)
**In OpenSSH configuration (`~/.ssh/config`), what does the directive `ControlMaster auto` combined with `ControlPath` achieve in an HPC cluster environment?**

- **(A)** It allows normal users to gain root privileges on compute nodes.
- **(B)** It enables SSH connection multiplexing, reusing a single master TCP connection for subsequent sessions and eliminating the latency of repeated TLS/cryptographic handshakes.
- **(C)** It controls the CPU fan speed of remote servers.
- **(D)** It automatically formats hard drives on remote nodes.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: SSH connection multiplexing (`ControlMaster auto`, `ControlPath ~/.ssh/sockets/%r@%h:%p`) creates a local Unix domain socket on the first SSH handshake. Subsequent commands reuse the existing authenticated TCP socket, reducing connection latency from ~400ms to <2ms.

---

### Question 38 (D1-Q38)
**What is the primary role of Lmod / Environment Modules (`module load`, `module purge`) on production HPC clusters?**

- **(A)** It installs Linux kernel drivers directly into motherboard BIOS.
- **(B)** It dynamically modifies shell environment variables (`PATH`, `LD_LIBRARY_PATH`, `CPATH`) to switch between conflicting compiler toolchains and MPI versions without system-wide collisions.
- **(C)** It acts as an anti-virus scanner for student home directories.
- **(D)** It provides a web interface for playing video games on supercomputers.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: HPC clusters host multiple conflicting versions of compilers and MPI libraries. Environment Modules modify `PATH`, `LD_LIBRARY_PATH`, and include directories dynamically per-user session without overwriting base system libraries.

---

### Question 39 (D1-Q39)
**What is the core distinction between the Intel oneAPI Base Toolkit and the Intel oneAPI HPC Toolkit?**

- **(A)** Base Toolkit is for Microsoft Office; HPC Toolkit is for Linux kernels.
- **(B)** Base Toolkit provides core SYCL/DPC++ compilers, oneMKL, oneDAL, and profiling tools; HPC Toolkit extends this with production C/C++/Fortran compilers (`icx`, `ifx`), Intel MPI Library, and cluster analysis tools (ITAC, Inspector).
- **(C)** Base Toolkit is paid; HPC Toolkit is open-source.
- **(D)** Base Toolkit only runs on laptops; HPC Toolkit only runs on quantum computers.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: The Base Toolkit includes cross-architecture developer tools (Intel DPC++/C++ Compiler, oneMKL, oneDNN, oneDAL, VTune). The HPC Toolkit provides dedicated distributed HPC libraries: Intel Fortran (`ifx`), Intel MPI Library, and Intel Trace Analyzer & Collector (ITAC).

---

### Question 40 (D1-Q40)
**What command-line tool is used in modern Linux kernels to inspect NUMA node assignments, socket CPU affinity, and distance matrices between CPU sockets and memory controllers?**

- **(A)** numactl --hardware
- **(B)** ipconfig /all
- **(C)** systemctl restart numa
- **(D)** cat /etc/hosts

> **Correct Answer**: **(A)**  
> **Technical Explanation**: `numactl --hardware` (or `numactl -H`) queries the Linux kernel NUMA subsystem, outputting available NUMA nodes, CPU core IDs mapped to each node, physical RAM per node, and the relative distance matrix.

---

### Question 41 (D1-Q41)
**What does a NUMA distance value of '21' relative to a local distance of '10' indicate in `numactl -H` output?**

- **(A)** The remote memory has 21 GB of capacity.
- **(B)** Accessing memory located on the remote socket takes approximately 2.1x more latency than accessing memory attached to the local socket.
- **(C)** The memory controller is operating at 21 MHz clock speed.
- **(D)** The network connection is 21 Gbps Ethernet.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Local node memory access is normalized to a baseline distance of 10. A distance of 21 signifies that memory transactions must cross inter-socket UPI interconnects, incurring ~2.1 times the latency of local node DRAM.

---

### Question 42 (D1-Q42)
**What flag must be passed to the Intel oneAPI C/C++ compiler (`icx`) to instruct it to generate optimized AVX-512 vector instructions targeting Intel 4th Gen Xeon Scalable processors?**

- **(A)** -O0 -mno-simd
- **(B)** -O3 -xSapphireRapids (or -mavx512f -mavx512dq -mavx512bw)
- **(C)** -cuda-arch=sm_80
- **(D)** -march=armv8-a

> **Correct Answer**: **(B)**  
> **Technical Explanation**: The Intel compiler (`icx`) uses `-x<target>` flags (e.g. `-xSapphireRapids`) along with optimization level `-O3` to vectorize loops into 512-bit ZMM register instructions, enabling AVX-512 FMA, VNNI, and mask register optimizations.

---

### Question 43 (D1-Q43)
**In Linux cluster administration, what virtual filesystem exposes real-time hardware status such as CPU temperature, frequency scaling governors, and memory sub-timings?**

- **(A)** /sys and /proc
- **(B)** /bin and /sbin
- **(C)** /opt and /usr
- **(D)** /var/log only

> **Correct Answer**: **(A)**  
> **Technical Explanation**: `/proc` provides kernel process state and hardware definitions (`/proc/cpuinfo`, `/proc/meminfo`), while `/sys` (sysfs) exposes structured device tree hierarchies including CPU power management and cache geometry.

---

### Question 44 (D1-Q44)
**What does the Linux command `lscpu -C` display?**

- **(A)** Computer cost breakdown.
- **(B)** Detailed CPU cache hierarchy, including L1 Data, L1 Instruction, L2, and L3 cache sizes, types, and core sharing mappings.
- **(C)** List of compiled C programs.
- **(D)** PCIe bus clock frequencies.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: `lscpu -C` formats a complete table of the processor cache subsystem, listing NAME (L1d, L1i, L2, L3), ONE-SIZE, ALL-SIZE, WAYS of associativity, TYPE, and the CPU allocation mapping.

---

### Question 45 (D1-Q45)
**In modern heterogeneous HPC clusters, what is the role of Intel Level Zero API?**

- **(A)** A low-level direct-to-metal hardware abstraction interface for Intel GPUs and AI accelerators, providing fine-grained device control below the SYCL layer.
- **(B)** A basic video game design framework.
- **(C)** An entry-level Linux terminal shell.
- **(D)** A tool to delete user passwords.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: Intel oneAPI Level Zero provides direct, low-overhead access to hardware capabilities of Intel discrete GPUs (like Data Center GPU Max) and accelerators, controlling device initialization, memory allocations, peer-to-peer copies, and kernel launches.

---

### Question 46 (D1-Q46)
**What is the key technological feature of InfiniBand NDR networking in top-tier HPC clusters?**

- **(A)** 400 Gbps per-port throughput with sub-microsecond latency and hardware-offloaded RDMA (Remote Direct Memory Access).
- **(B)** 10 Mbps dial-up protocol for legacy terminals.
- **(C)** Wireless Wi-Fi 6 transmission over antennas.
- **(D)** Bluetooth 5.0 mesh for keyboard connectivity.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: InfiniBand NDR delivers 400 Gbps per port using 4 lanes of 100 Gbps PAM4 signaling. With hardware-level RDMA, compute nodes transfer data directly between application memories without involving OS kernel copy overhead.

---

### Question 47 (D1-Q47)
**What is a Fat-Tree network topology in supercomputer cluster design?**

- **(A)** A tree topology where tree branches grow thicker (more aggregated bandwidth) toward the root, guaranteeing full bisection non-blocking bandwidth across all compute racks.
- **(B)** A circular ring where all computers share a single cable.
- **(C)** A wireless network configured in an outdoor park.
- **(D)** A random daisy chain of ethernet switches.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: In a Fat-Tree topology, switches closer to the root have more aggregated uplink bandwidth than leaf switches. A non-blocking fat-tree guarantees that any arbitrary half of the cluster can communicate simultaneously with the other half at wire speed.

---

### Question 48 (D1-Q48)
**What Linux tool allows an engineer to pin a process to a specific NUMA node and enforce that memory allocations only occur from that node's local memory controllers?**

- **(A)** numactl --cpunodebind=0 --membind=0 ./app
- **(B)** kill -9 ./app
- **(C)** chmod +x ./app
- **(D)** grep -r numa ./app

> **Correct Answer**: **(A)**  
> **Technical Explanation**: `numactl --cpunodebind=0 --membind=0 ./app` binds the process's CPU execution threads strictly to the cores of NUMA node 0 and strictly enforces memory allocations from node 0's local DRAM channels, eliminating remote cross-socket UPI traffic.

---

### Question 49 (D1-Q49)
**What does SYCL represent within the Intel oneAPI programming ecosystem?**

- **(A)** An open standard, single-source C++ programming model governed by Khronos Group for heterogeneous computing across CPUs, GPUs, FPGAs, and AI accelerators.
- **(B)** A proprietary Nvidia compiler for CUDA graphics cards.
- **(C)** A replacement for HTML and CSS websites.
- **(D)** A database query language similar to SQL.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: SYCL is a royalty-free, open standard C++ programming model managed by the Khronos Group. Intel oneAPI's DPC++ is built upon SYCL, allowing developers to write standards-compliant modern C++ that compiles across Intel CPUs, GPUs, and accelerators.

---

### Question 50 (D1-Q50)
**When configuring passwordless SSH keys for an HPC cluster, why must the permissions of `~/.ssh` and `~/.ssh/authorized_keys` strictly be set to `700` and `600` respectively?**

- **(A)** Because SSH daemons enforce strict permission checks and will refuse authentication if the directory or keys are writable by group or other users for security.
- **(B)** Because Linux hard drives cannot store files larger than 600 bytes.
- **(C)** Because the Slurm scheduler requires executable bits on authorized_keys.
- **(D)** Because the files are automatically encrypted with AES-700.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: The OpenSSH daemon enforces `StrictModes yes` by default. If `~/.ssh` has permissions looser than `700` or `authorized_keys` looser than `600`, other local users could tamper with the keys, causing OpenSSH to silently reject authentication.

---
