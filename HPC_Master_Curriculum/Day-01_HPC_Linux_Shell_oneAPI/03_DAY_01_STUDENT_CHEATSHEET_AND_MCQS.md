# 📝 DAY 1: STUDENT QUICK REFERENCE & OFFICIAL MCQ BANK
## 1-Page Cheat Sheet + 25 Evaluated Assessment Questions
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

## 📝 PART 3: 25 Official Multiple-Choice Questions (With Answers & Explanations)

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
