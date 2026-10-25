# 🏢 Edulateral Foundation — Official Evaluative Assessment Bank
### Day 1: Fundamentals of HPC, Linux, Shell Scripting & Hardware Architectures
**Target Audience**: GLA University 7th Semester B.Tech Computer Science & Engineering  
**Lead Trainer**: Shivam Gupta | **Evaluation Mode**: Objective Technical MCQ Assessment  
**Total Questions**: 25 Questions | **Time Limit**: 45 Minutes  

---

### Question 01: D1-Q01
**Why did Dennard scaling breakdown around 2005, forcing processor manufacturers to transition from increasing single-core clock frequencies to multi-core and heterogeneous architectures?**

- **(A)** Sub-threshold leakage current and static power dissipation grew exponentially at sub-90nm process nodes, causing thermal runaway.
- **(B)** Amdahl's law proved that clock frequencies above 4 GHz mathematically reduce instruction-level parallelism.
- **(C)** InfiniBand fabric became mandatory for motherboard bus routing, capping CPU clock oscillators.
- **(D)** Operating system schedulers could not allocate virtual memory addresses faster than 3.8 GHz.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: Dennard scaling stated that as transistors shrink, power density stays constant because voltage and current scale downward proportionally. Below ~90nm, quantum tunneling and gate oxide leakage currents escalated exponentially. Operating voltages could no longer scale down without causing gate instability, leading to the 'Power Wall' where increasing clock speed resulted in uncontrollable thermal dissipation.

---

### Question 02: D1-Q02
**According to Amdahl's Law, if 90% of an HPC application's execution time is parallelizable and 10% is strictly sequential, what is the theoretical maximum speedup limit as the number of parallel processor cores approaches infinity?**

- **(A)** 90x
- **(B)** 10x
- **(C)** 100x
- **(D)** Infinity

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Amdahl's law states that maximum speedup S = 1 / ((1 - p) + (p / N)). As N -> infinity, p / N -> 0, leaving S_max = 1 / (1 - p). Here, p = 0.90, so S_max = 1 / (1 - 0.90) = 1 / 0.10 = 10x. Regardless of having 10,000 cores, the 10% serial bottleneck caps speedup at 10x.

---

### Question 03: D1-Q03
**How does Gustafson's Law fundamentally differ from Amdahl's Law in evaluating the scalability of high-performance computing clusters?**

- **(A)** Gustafson's Law assumes a fixed problem size, whereas Amdahl's Law scales the problem size with core count.
- **(B)** Gustafson's Law models scaled speedup where problem size increases proportionally to compute resources, demonstrating that the parallel fraction dominates large-scale workloads.
- **(C)** Gustafson's Law only applies to shared-memory NUMA nodes, while Amdahl's Law applies to InfiniBand networks.
- **(D)** Gustafson's Law models GPU matrix multiplication while Amdahl's Law models CPU scalar execution.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Amdahl's law assumes strong scaling (fixed problem size run on more cores). Gustafson's law assumes weak scaling (scaled speedup S(P) = P - alpha*(P - 1)), where as compute resources expand, scientists enlarge the problem grid, causing the time spent in parallel execution to dwarf the constant sequential setup phase.

---

### Question 04: D1-Q04
**In a dual-socket 4th Gen Intel Xeon Scalable (Sapphire Rapids) server, what interconnect fabric facilitates cache-coherent inter-socket communication, and what is its typical latency penalty relative to local DRAM access?**

- **(A)** PCIe Gen 3 bus; ~20ns penalty.
- **(B)** Intel Ultra Path Interconnect (UPI); approximately 60ns to 80ns latency penalty compared to local NUMA memory.
- **(C)** InfiniBand HDR switch; ~500ns penalty.
- **(D)** SATA Express controller; 10x slower bandwidth.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Intel Xeon multi-socket systems use UPI (Ultra Path Interconnect) links to maintain hardware cache coherency across sockets. Accessing memory attached to a local socket takes ~80ns, whereas a remote NUMA access crossing UPI links incurs an additional ~60-80ns (~140-160ns total), emphasizing the critical need for thread pinning and NUMA-aware allocation.

---

### Question 05: D1-Q05
**What is the register width and single-precision IEEE 754 floating-point capacity of Intel AVX-512 vector units?**

- **(A)** 256 bits, processing 8 FP32 values per instruction.
- **(B)** 512 bits (ZMM registers), processing 16 FP32 values per instruction.
- **(C)** 128 bits (XMM registers), processing 4 FP32 values per instruction.
- **(D)** 1024 bits, processing 32 FP32 values per instruction.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: AVX-512 defines thirty-two 512-bit wide vector registers (ZMM0 through ZMM31). In a single clock cycle, an AVX-512 Fused Multiply-Add (FMA) unit computes sixteen 32-bit single-precision floats simultaneously (512 / 32 = 16).

---

### Question 06: D1-Q06
**What architectural engine was introduced in 4th Gen Intel Xeon Scalable (Sapphire Rapids) to accelerate deep learning tensor matrix multiplications in hardware?**

- **(A)** Intel AMX (Advanced Matrix Extensions) with 2D tile registers (TMM) and TMUL matrix multiplication units.
- **(B)** Intel Iris Xe Integrated Graphics Core.
- **(C)** Intel QuickPath Interconnect (QPI).
- **(D)** Intel Hyper-Threading Technology v2.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: Intel AMX (Advanced Matrix Extensions) is a dedicated accelerator block embedded directly in Sapphire Rapids cores. It features 8 two-dimensional tile registers (TMM0-TMM7, 1KB each) and a TMUL (Tile Matrix Multiply) systolic execution unit capable of executing 2048 INT8 or 1024 BF16 operations per cycle.

---

### Question 07: D1-Q07
**In the NEC SX-Aurora TSUBASA supercomputing architecture, what role does the Intel Xeon processor play relative to the NEC Vector Engine (VE)?**

- **(A)** The Intel Xeon acts as the Vector Host (VH), running the Linux OS, managing storage/Lustre I/O, and job dispatching, while the NEC VE PCIe card executes ultra-wide vector computations.
- **(B)** The Intel Xeon is an idle standby CPU used only if the NEC Vector Engine burns out.
- **(C)** The Intel Xeon is embedded inside the NEC PCIe card as an L1 cache controller.
- **(D)** The NEC VE runs the Linux kernel while the Intel Xeon acts as a graphical display adapter.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: NEC SX-Aurora TSUBASA employs a decoupled hybrid model: the standard x86_64 CPU (Intel Xeon) is the Vector Host (VH), handling standard Linux OS services, network drivers, Slurm scheduling, and Lustre file I/O. The NEC Vector Engine (VE) is a dedicated PCIe processor with dedicated HBM2 memory delivering massive vector throughput.

---

### Question 08: D1-Q08
**What is the peak memory bandwidth of the NEC SX-Aurora TSUBASA Type 20B Vector Engine, and what memory technology enables it?**

- **(A)** 128 GB/s using standard DDR4 memory.
- **(B)** 1.53 TB/s using stacked High Bandwidth Memory (HBM2).
- **(C)** 25.6 GB/s using PCIe Gen 3 lanes.
- **(D)** 500 GB/s using GDDR6 graphic memory.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: The NEC SX-Aurora TSUBASA VE20B features integrated 3D-stacked HBM2 memory directly on the silicon interposer, delivering up to 1.53 Terabytes per second (TB/s) of memory bandwidth—essential for memory-bound sparse scientific HPC codes.

---

### Question 09: D1-Q09
**In an HPC Linux cluster, what is the functional difference between `/home` and `/scratch` parallel file systems?**

- **(A)** `/home` is backed by high-throughput parallel Lustre storage for high IOPS, while `/scratch` is a slow USB stick.
- **(B)** `/home` is typically an NFS share for source code and config files, while `/scratch` is a high-bandwidth parallel file system (Lustre/GPFS) striped across Object Storage Targets (OSTs) for temporary simulation data.
- **(C)** `/scratch` is volatile RAM that gets erased every second.
- **(D)** `/home` is only accessible by root, while `/scratch` is for normal users.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: In production HPC clusters, user home directories are hosted on standard NFS with strict storage quotas and backup snapshots. The high-performance parallel file systems (such as Lustre or IBM Spectrum Scale / GPFS) are mounted at `/scratch`, striping multi-terabyte datasets across dozens of parallel OSTs for hundreds of gigabytes per second of aggregated sequential I/O.

---

### Question 10: D1-Q10
**Why is the bash directive `set -euo pipefail` considered mandatory for professional HPC job automation scripts?**

- **(A)** It automatically compiles Python scripts into C++ binaries before execution.
- **(B)** It halts execution immediately if any command fails (-e), if an unset variable is referenced (-u), or if any command in a pipeline fails (-o pipefail), preventing silent corrupted calculations.
- **(C)** It allocates 100% of GPU memory to the current shell.
- **(D)** It disables password prompts across the entire university network.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: `set -e` ensures the script exits on non-zero command return; `set -u` treats uninitialized variables as fatal errors; and `set -o pipefail` ensures that a pipeline fails if any upstream command fails, rather than masking errors with the downstream command's exit code.

---

### Question 11: D1-Q11
**Which elliptic-curve algorithm is the modern enterprise standard for HPC passwordless SSH keys, replacing legacy RSA 2048/4096-bit keys due to superior security and cryptographic handshake speed?**

- **(A)** DES
- **(B)** Ed25519
- **(C)** MD5
- **(D)** SHA-1

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Ed25519 provides 128-bit security level equivalent to ~3000-bit RSA, but with significantly smaller keys (68 characters), immune to side-channel timing attacks, and orders of magnitude faster signature generation.

---

### Question 12: D1-Q12
**In OpenSSH configuration (`~/.ssh/config`), what does the directive `ControlMaster auto` combined with `ControlPath` achieve in an HPC cluster environment?**

- **(A)** It allows normal users to gain root privileges on compute nodes.
- **(B)** It enables SSH connection multiplexing, reusing a single master TCP connection for subsequent sessions and eliminating the latency of repeated TLS/cryptographic handshakes.
- **(C)** It controls the CPU fan speed of remote servers.
- **(D)** It automatically formats hard drives on remote nodes.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: SSH connection multiplexing (`ControlMaster auto`, `ControlPath ~/.ssh/sockets/%r@%h:%p`) creates a local Unix domain socket on the first SSH handshake. Subsequent commands reuse the existing authenticated TCP socket, reducing connection latency from ~400ms to <2ms.

---

### Question 13: D1-Q13
**What is the primary role of Lmod / Environment Modules (`module load`, `module purge`) on production HPC clusters?**

- **(A)** It installs Linux kernel drivers directly into motherboard BIOS.
- **(B)** It dynamically modifies shell environment variables (`PATH`, `LD_LIBRARY_PATH`, `CPATH`) to switch between conflicting compiler toolchains and MPI versions without system-wide collisions.
- **(C)** It acts as an anti-virus scanner for student home directories.
- **(D)** It provides a web interface for playing video games on supercomputers.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: HPC clusters host multiple conflicting versions of compilers and MPI libraries. Environment Modules modify `PATH`, `LD_LIBRARY_PATH`, and include directories dynamically per-user session without overwriting base system libraries.

---

### Question 14: D1-Q14
**What is the core distinction between the Intel oneAPI Base Toolkit and the Intel oneAPI HPC Toolkit?**

- **(A)** Base Toolkit is for Microsoft Office; HPC Toolkit is for Linux kernels.
- **(B)** Base Toolkit provides core SYCL/DPC++ compilers, oneMKL, oneDAL, and profiling tools; HPC Toolkit extends this with production C/C++/Fortran compilers (`icx`, `ifx`), Intel MPI Library, and cluster analysis tools (ITAC, Inspector).
- **(C)** Base Toolkit is paid; HPC Toolkit is open-source.
- **(D)** Base Toolkit only runs on laptops; HPC Toolkit only runs on quantum computers.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: The Base Toolkit includes cross-architecture developer tools (Intel DPC++/C++ Compiler, oneMKL, oneDNN, oneDAL, VTune). The HPC Toolkit provides dedicated distributed HPC libraries: Intel Fortran (`ifx`), Intel MPI Library, and Intel Trace Analyzer & Collector (ITAC).

---

### Question 15: D1-Q15
**What command-line tool is used in modern Linux kernels to inspect NUMA node assignments, socket CPU affinity, and distance matrices between CPU sockets and memory controllers?**

- **(A)** numactl --hardware
- **(B)** ipconfig /all
- **(C)** systemctl restart numa
- **(D)** cat /etc/hosts

> **Correct Answer**: **(A)**  
> **Technical Explanation**: `numactl --hardware` (or `numactl -H`) queries the Linux kernel NUMA subsystem, outputting available NUMA nodes, CPU core IDs mapped to each node, physical RAM per node, and the relative distance matrix.

---

### Question 16: D1-Q16
**What does a NUMA distance value of '21' relative to a local distance of '10' indicate in `numactl -H` output?**

- **(A)** The remote memory has 21 GB of capacity.
- **(B)** Accessing memory located on the remote socket takes approximately 2.1x more latency than accessing memory attached to the local socket.
- **(C)** The memory controller is operating at 21 MHz clock speed.
- **(D)** The network connection is 21 Gbps Ethernet.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: Local node memory access is normalized to a baseline distance of 10. A distance of 21 signifies that memory transactions must cross inter-socket UPI interconnects, incurring ~2.1 times the latency of local node DRAM.

---

### Question 17: D1-Q17
**What flag must be passed to the Intel oneAPI C/C++ compiler (`icx`) to instruct it to generate optimized AVX-512 vector instructions targeting Intel 4th Gen Xeon Scalable processors?**

- **(A)** -O0 -mno-simd
- **(B)** -O3 -xSapphireRapids (or -mavx512f -mavx512dq -mavx512bw)
- **(C)** -cuda-arch=sm_80
- **(D)** -march=armv8-a

> **Correct Answer**: **(B)**  
> **Technical Explanation**: The Intel compiler (`icx`) uses `-x<target>` flags (e.g. `-xSapphireRapids`) along with optimization level `-O3` to vectorize loops into 512-bit ZMM register instructions, enabling AVX-512 FMA, VNNI, and mask register optimizations.

---

### Question 18: D1-Q18
**In Linux cluster administration, what virtual filesystem exposes real-time hardware status such as CPU temperature, frequency scaling governors, and memory sub-timings?**

- **(A)** /sys and /proc
- **(B)** /bin and /sbin
- **(C)** /opt and /usr
- **(D)** /var/log only

> **Correct Answer**: **(A)**  
> **Technical Explanation**: `/proc` provides kernel process state and hardware definitions (`/proc/cpuinfo`, `/proc/meminfo`), while `/sys` (sysfs) exposes structured device tree hierarchies including CPU power management and cache geometry.

---

### Question 19: D1-Q19
**What does the Linux command `lscpu -C` display?**

- **(A)** Computer cost breakdown.
- **(B)** Detailed CPU cache hierarchy, including L1 Data, L1 Instruction, L2, and L3 cache sizes, types, and core sharing mappings.
- **(C)** List of compiled C programs.
- **(D)** PCIe bus clock frequencies.

> **Correct Answer**: **(B)**  
> **Technical Explanation**: `lscpu -C` formats a complete table of the processor cache subsystem, listing NAME (L1d, L1i, L2, L3), ONE-SIZE, ALL-SIZE, WAYS of associativity, TYPE, and the CPU allocation mapping.

---

### Question 20: D1-Q20
**In modern heterogeneous HPC clusters, what is the role of Intel Level Zero API?**

- **(A)** A low-level direct-to-metal hardware abstraction interface for Intel GPUs and AI accelerators, providing fine-grained device control below the SYCL layer.
- **(B)** A basic video game design framework.
- **(C)** An entry-level Linux terminal shell.
- **(D)** A tool to delete user passwords.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: Intel oneAPI Level Zero provides direct, low-overhead access to hardware capabilities of Intel discrete GPUs (like Data Center GPU Max) and accelerators, controlling device initialization, memory allocations, peer-to-peer copies, and kernel launches.

---

### Question 21: D1-Q21
**What is the key technological feature of InfiniBand NDR networking in top-tier HPC clusters?**

- **(A)** 400 Gbps per-port throughput with sub-microsecond latency and hardware-offloaded RDMA (Remote Direct Memory Access).
- **(B)** 10 Mbps dial-up protocol for legacy terminals.
- **(C)** Wireless Wi-Fi 6 transmission over antennas.
- **(D)** Bluetooth 5.0 mesh for keyboard connectivity.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: InfiniBand NDR delivers 400 Gbps per port using 4 lanes of 100 Gbps PAM4 signaling. With hardware-level RDMA, compute nodes transfer data directly between application memories without involving OS kernel copy overhead.

---

### Question 22: D1-Q22
**What is a Fat-Tree network topology in supercomputer cluster design?**

- **(A)** A tree topology where tree branches grow thicker (more aggregated bandwidth) toward the root, guaranteeing full bisection non-blocking bandwidth across all compute racks.
- **(B)** A circular ring where all computers share a single cable.
- **(C)** A wireless network configured in an outdoor park.
- **(D)** A random daisy chain of ethernet switches.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: In a Fat-Tree topology, switches closer to the root have more aggregated uplink bandwidth than leaf switches. A non-blocking fat-tree guarantees that any arbitrary half of the cluster can communicate simultaneously with the other half at wire speed.

---

### Question 23: D1-Q23
**What Linux tool allows an engineer to pin a process to a specific NUMA node and enforce that memory allocations only occur from that node's local memory controllers?**

- **(A)** numactl --cpunodebind=0 --membind=0 ./app
- **(B)** kill -9 ./app
- **(C)** chmod +x ./app
- **(D)** grep -r numa ./app

> **Correct Answer**: **(A)**  
> **Technical Explanation**: `numactl --cpunodebind=0 --membind=0 ./app` binds the process's CPU execution threads strictly to the cores of NUMA node 0 and strictly enforces memory allocations from node 0's local DRAM channels, eliminating remote cross-socket UPI traffic.

---

### Question 24: D1-Q24
**What does SYCL represent within the Intel oneAPI programming ecosystem?**

- **(A)** An open standard, single-source C++ programming model governed by Khronos Group for heterogeneous computing across CPUs, GPUs, FPGAs, and AI accelerators.
- **(B)** A proprietary Nvidia compiler for CUDA graphics cards.
- **(C)** A replacement for HTML and CSS websites.
- **(D)** A database query language similar to SQL.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: SYCL is a royalty-free, open standard C++ programming model managed by the Khronos Group. Intel oneAPI's DPC++ is built upon SYCL, allowing developers to write standards-compliant modern C++ that compiles across Intel CPUs, GPUs, and accelerators.

---

### Question 25: D1-Q25
**When configuring passwordless SSH keys for an HPC cluster, why must the permissions of `~/.ssh` and `~/.ssh/authorized_keys` strictly be set to `700` and `600` respectively?**

- **(A)** Because SSH daemons enforce strict permission checks and will refuse authentication if the directory or keys are writable by group or other users for security.
- **(B)** Because Linux hard drives cannot store files larger than 600 bytes.
- **(C)** Because the Slurm scheduler requires executable bits on authorized_keys.
- **(D)** Because the files are automatically encrypted with AES-700.

> **Correct Answer**: **(A)**  
> **Technical Explanation**: The OpenSSH daemon enforces `StrictModes yes` by default. If `~/.ssh` has permissions looser than `700` or `authorized_keys` looser than `600`, other local users could tamper with the keys, causing OpenSSH to silently reject authentication.

---
