"""
generate_official_mcqs.py
Edulateral Foundation — Official MCQ Question Bank Generator.
Generates 125 rigorous, university-grade MCQs (25 per day) for GLA University
Block Teaching on High Performance Computing (Intel & NEC Edition).
Each question includes 4 plausible engineering distractors, correct key, and an in-depth
technical explanation citing hardware counters, silicon architecture, or runtime mechanics.
"""

import os
import json

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\EDULATERAL_OFFICIAL_MCQ_BANK"
os.makedirs(base_dir, exist_ok=True)

mcqs_day1 = [
    {
        "id": "D1-Q01",
        "question": "Why did Dennard scaling breakdown around 2005, forcing processor manufacturers to transition from increasing single-core clock frequencies to multi-core and heterogeneous architectures?",
        "options": {
            "A": "Sub-threshold leakage current and static power dissipation grew exponentially at sub-90nm process nodes, causing thermal runaway.",
            "B": "Amdahl's law proved that clock frequencies above 4 GHz mathematically reduce instruction-level parallelism.",
            "C": "InfiniBand fabric became mandatory for motherboard bus routing, capping CPU clock oscillators.",
            "D": "Operating system schedulers could not allocate virtual memory addresses faster than 3.8 GHz."
        },
        "answer": "A",
        "explanation": "Dennard scaling stated that as transistors shrink, their power density stays constant because voltage and current scale downward proportionally. Below ~90nm, quantum tunneling and gate oxide leakage currents escalated exponentially. Operating voltages could no longer scale down without causing gate instability, leading to the 'Power Wall' where increasing clock speed resulted in uncontrollable thermal dissipation."
    },
    {
        "id": "D1-Q02",
        "question": "According to Amdahl's Law, if 90% of an HPC application's execution time is parallelizable and 10% is strictly sequential, what is the theoretical maximum speedup limit as the number of parallel processor cores approaches infinity?",
        "options": {
            "A": "90x",
            "B": "10x",
            "C": "100x",
            "D": "Infinity"
        },
        "answer": "B",
        "explanation": "Amdahl's law states that maximum speedup S = 1 / ((1 - p) + (p / N)). As N -> infinity, p / N -> 0, leaving S_max = 1 / (1 - p). Here, p = 0.90, so S_max = 1 / (1 - 0.90) = 1 / 0.10 = 10x. Regardless of having 10,000 cores, the 10% serial bottleneck caps speedup at 10x."
    },
    {
        "id": "D1-Q03",
        "question": "How does Gustafson's Law fundamentally differ from Amdahl's Law in evaluating the scalability of high-performance computing clusters?",
        "options": {
            "A": "Gustafson's Law assumes a fixed problem size, whereas Amdahl's Law scales the problem size with core count.",
            "B": "Gustafson's Law models scaled speedup where problem size increases proportionally to compute resources, demonstrating that the parallel fraction dominates large-scale workloads.",
            "C": "Gustafson's Law only applies to shared-memory NUMA nodes, while Amdahl's Law applies to InfiniBand networks.",
            "D": "Gustafson's Law models GPU matrix multiplication while Amdahl's Law models CPU scalar execution."
        },
        "answer": "B",
        "explanation": "Amdahl's law assumes strong scaling (fixed problem size run on more cores). Gustafson's law assumes weak scaling (scaled speedup S(P) = P - alpha*(P - 1)), where as compute resources expand, scientists enlarge the problem grid (e.g. higher resolution simulation), causing the time spent in parallel execution to dwarf the constant sequential setup phase."
    },
    {
        "id": "D1-Q04",
        "question": "In a dual-socket 4th Gen Intel Xeon Scalable (Sapphire Rapids) server, what interconnect fabric facilitates cache-coherent inter-socket communication, and what is its typical latency penalty relative to local DRAM access?",
        "options": {
            "A": "PCIe Gen 3 bus; ~20ns penalty.",
            "B": "Intel Ultra Path Interconnect (UPI); approximately 60ns to 80ns latency penalty compared to local NUMA memory.",
            "C": "InfiniBand HDR switch; ~500ns penalty.",
            "D": "SATA Express controller; 10x slower bandwidth."
        },
        "answer": "B",
        "explanation": "Intel Xeon multi-socket systems use UPI (Ultra Path Interconnect) links to maintain hardware cache coherency across sockets. Accessing memory attached to a local socket takes ~80ns, whereas a remote NUMA access crossing UPI links incurs an additional ~60-80ns (~140-160ns total), emphasizing the critical need for thread pinning and NUMA-aware allocation."
    },
    {
        "id": "D1-Q05",
        "question": "What is the register width and single-precision IEEE 754 floating-point capacity of Intel AVX-512 vector units?",
        "options": {
            "A": "256 bits, processing 8 FP32 values per instruction.",
            "B": "512 bits (ZMM registers), processing 16 FP32 values per instruction.",
            "C": "128 bits (XMM registers), processing 4 FP32 values per instruction.",
            "D": "1024 bits, processing 32 FP32 values per instruction."
        },
        "answer": "B",
        "explanation": "AVX-512 defines thirty-two 512-bit wide vector registers (ZMM0 through ZMM31). In a single clock cycle, an AVX-512 Fused Multiply-Add (FMA) unit computes sixteen 32-bit single-precision floats simultaneously (512 / 32 = 16)."
    },
    {
        "id": "D1-Q06",
        "question": "What architectural engine was introduced in 4th Gen Intel Xeon Scalable (Sapphire Rapids) to accelerate deep learning tensor matrix multiplications in hardware?",
        "options": {
            "A": "Intel AMX (Advanced Matrix Extensions) with 2D tile registers (TMM) and TMUL matrix multiplication units.",
            "B": "Intel Iris Xe Integrated Graphics Core.",
            "C": "Intel QuickPath Interconnect (QPI).",
            "D": "Intel Hyper-Threading Technology v2."
        },
        "answer": "A",
        "explanation": "Intel AMX (Advanced Matrix Extensions) is a dedicated accelerator block embedded directly in Sapphire Rapids cores. It features 8 two-dimensional tile registers (TMM0-TMM7, 1KB each) and a TMUL (Tile Matrix Multiply) systolic execution unit capable of executing 2048 INT8 or 1024 BF16 operations per cycle."
    },
    {
        "id": "D1-Q07",
        "question": "In the NEC SX-Aurora TSUBASA supercomputing architecture, what role does the Intel Xeon processor play relative to the NEC Vector Engine (VE)?",
        "options": {
            "A": "The Intel Xeon acts as the Vector Host (VH), running the Linux OS, managing storage/Lustre I/O, and job dispatching, while the NEC VE PCIe card executes ultra-wide vector computations.",
            "B": "The Intel Xeon is an idle standby CPU used only if the NEC Vector Engine burns out.",
            "C": "The Intel Xeon is embedded inside the NEC PCIe card as an L1 cache controller.",
            "D": "The NEC VE runs the Linux kernel while the Intel Xeon acts as a graphical display adapter."
        },
        "answer": "A",
        "explanation": "NEC SX-Aurora TSUBASA employs a decoupled hybrid model: the standard x86_64 CPU (Intel Xeon) is the Vector Host (VH), handling standard Linux OS services, network drivers, Slurm scheduling, and Lustre file I/O. The NEC Vector Engine (VE) is a dedicated PCIe processor with dedicated HBM2 memory delivering massive vector throughput."
    },
    {
        "id": "D1-Q08",
        "question": "What is the peak memory bandwidth of the NEC SX-Aurora TSUBASA Type 20B Vector Engine, and what memory technology enables it?",
        "options": {
            "A": "128 GB/s using standard DDR4 memory.",
            "B": "1.53 TB/s using stacked High Bandwidth Memory (HBM2).",
            "C": "25.6 GB/s using PCIe Gen 3 lanes.",
            "D": "500 GB/s using GDDR6 graphic memory."
        },
        "answer": "B",
        "explanation": "The NEC SX-Aurora TSUBASA VE20B features integrated 3D-stacked HBM2 memory directly on the silicon interposer, delivering up to 1.53 Terabytes per second (TB/s) of memory bandwidth—essential for memory-bound sparse scientific HPC codes."
    },
    {
        "id": "D1-Q09",
        "question": "In an HPC Linux cluster, what is the functional difference between `/home` and `/scratch` parallel file systems?",
        "options": {
            "A": "`/home` is backed by high-throughput parallel Lustre storage for high IOPS, while `/scratch` is a slow USB stick.",
            "B": "`/home` is typically an NFS share for source code and config files, while `/scratch` is a high-bandwidth parallel file system (Lustre/GPFS) striped across Object Storage Targets (OSTs) for temporary simulation data.",
            "C": "`/scratch` is volatile RAM that gets erased every second.",
            "D": "`/home` is only accessible by root, while `/scratch` is for normal users."
        },
        "answer": "B",
        "explanation": "In production HPC clusters, user home directories are hosted on standard NFS with strict storage quotas and backup snapshots. The high-performance parallel file systems (such as Lustre or IBM Spectrum Scale / GPFS) are mounted at `/scratch`, striping multi-terabyte datasets across dozens of parallel OSTs for hundreds of gigabytes per second of aggregated sequential I/O."
    },
    {
        "id": "D1-Q10",
        "question": "Why is the bash directive `set -euo pipefail` considered mandatory for professional HPC job automation scripts?",
        "options": {
            "A": "It automatically compiles Python scripts into C++ binaries before execution.",
            "B": "It halts execution immediately if any command fails (-e), if an unset variable is referenced (-u), or if any command in a pipeline fails (-o pipefail), preventing silent corrupted calculations.",
            "C": "It allocates 100% of GPU memory to the current shell.",
            "D": "It disables password prompts across the entire university network."
        },
        "answer": "B",
        "explanation": "`set -e` ensures the script exits on non-zero command return; `set -u` treats uninitialized variables as fatal errors; and `set -o pipefail` ensures that a pipeline (e.g. `cmd1 | cmd2`) fails if `cmd1` fails, rather than masking errors with `cmd2`'s exit code. This prevents runaway corrupted jobs on expensive supercomputer allocations."
    },
    {
        "id": "D1-Q11",
        "question": "Which elliptic-curve algorithm is the modern enterprise standard for HPC passwordless SSH keys, replacing legacy RSA 2048/4096-bit keys due to superior security and cryptographic handshake speed?",
        "options": {
            "A": "DES",
            "B": "Ed25519",
            "C": "MD5",
            "D": "SHA-1"
        },
        "answer": "B",
        "explanation": "Ed25519 (Edwards-curve Digital Signature Algorithm over Curve25519) provides 128-bit security level equivalent to ~3000-bit RSA, but with significantly smaller keys (68 characters), immune to side-channel timing attacks, and orders of magnitude faster signature generation."
    },
    {
        "id": "D1-Q12",
        "question": "In OpenSSH configuration (`~/.ssh/config`), what does the directive `ControlMaster auto` combined with `ControlPath` achieve in an HPC cluster environment?",
        "options": {
            "A": "It allows normal users to gain root privileges on compute nodes.",
            "B": "It enables SSH connection multiplexing, reusing a single master TCP connection for subsequent sessions and eliminating the latency of repeated TLS/cryptographic handshakes.",
            "C": "It controls the CPU fan speed of remote servers.",
            "D": "It automatically formats hard drives on remote nodes."
        },
        "answer": "B",
        "explanation": "SSH connection multiplexing (`ControlMaster auto`, `ControlPath ~/.ssh/sockets/%r@%h:%p`, `ControlPersist 10m`) creates a local Unix domain socket on the first SSH handshake. Subsequent commands (e.g., Slurm remote copies, `scp`, `rsync`, automated cluster health checks) instantly route over the existing authenticated TCP socket, reducing connection latency from ~400ms to <2ms."
    },
    {
        "id": "D1-Q13",
        "question": "What is the primary role of Lmod / Environment Modules (`module load`, `module purge`) on production HPC clusters?",
        "options": {
            "A": "It installs Linux kernel drivers directly into motherboard BIOS.",
            "B": "It dynamically modifies shell environment variables (`PATH`, `LD_LIBRARY_PATH`, `CPATH`) to switch between conflicting compiler toolchains and MPI versions without system-wide collisions.",
            "C": "It acts as an anti-virus scanner for student home directories.",
            "D": "It provides a web interface for playing video games on supercomputers."
        },
        "answer": "B",
        "explanation": "HPC clusters host multiple conflicting versions of compilers (GCC 11, GCC 13, Intel oneAPI ICX) and MPI libraries (OpenMPI, Intel MPI, MPICH). Environment Modules modify `PATH`, `LD_LIBRARY_PATH`, and include directories dynamically per-user session without overwriting base system libraries."
    },
    {
        "id": "D1-Q14",
        "question": "What is the core distinction between the Intel oneAPI Base Toolkit and the Intel oneAPI HPC Toolkit?",
        "options": {
            "A": "Base Toolkit is for Microsoft Office; HPC Toolkit is for Linux kernels.",
            "B": "Base Toolkit provides core SYCL/DPC++ compilers, oneMKL, oneDAL, and profiling tools; HPC Toolkit extends this with production C/C++/Fortran compilers (`icx`, `ifx`), Intel MPI Library, and cluster analysis tools (ITAC, Inspector).",
            "C": "Base Toolkit is paid; HPC Toolkit is open-source.",
            "D": "Base Toolkit only runs on laptops; HPC Toolkit only runs on quantum computers."
        },
        "answer": "B",
        "explanation": "The Intel oneAPI Base Toolkit includes foundational cross-architecture developer tools (Intel DPC++/C++ Compiler, oneMKL, oneDNN, oneDAL, Intel VTune Profiler). The Intel HPC Toolkit builds upon the Base Toolkit to provide dedicated distributed HPC libraries: Intel Fortran Compiler (`ifx`), Intel MPI Library, Intel Trace Analyzer & Collector (ITAC), and Intel Cluster Checker."
    },
    {
        "id": "D1-Q15",
        "question": "What command-line tool is used in modern Linux kernels to inspect NUMA node assignments, socket CPU affinity, and distance matrices between CPU sockets and memory controllers?",
        "options": {
            "A": "numactl --hardware",
            "B": "ipconfig /all",
            "C": "systemctl restart numa",
            "D": "cat /etc/hosts"
        },
        "answer": "A",
        "explanation": "`numactl --hardware` (or `numactl -H`) queries the Linux kernel NUMA subsystem, outputting available NUMA nodes, the exact CPU core IDs mapped to each node, the amount of physical RAM attached per node, and the NUMA distance matrix (relative latency of cross-node access)."
    },
    {
        "id": "D1-Q16",
        "question": "What does a NUMA distance value of '21' relative to a local distance of '10' indicate in `numactl -H` output?",
        "options": {
            "A": "The remote memory has 21 GB of capacity.",
            "B": "Accessing memory located on the remote socket takes approximately 2.1x more latency than accessing memory attached to the local socket.",
            "C": "The memory controller is operating at 21 MHz clock speed.",
            "D": "The network connection is 21 Gbps Ethernet."
        },
        "answer": "B",
        "explanation": "In ACPI SLIT (System Locality Information Table) tables displayed by `numactl -H`, local node memory access is normalized to a baseline distance of 10. A distance of 21 signifies that memory transactions must cross inter-socket UPI interconnects, incurring ~2.1 times the latency of local node DRAM."
    },
    {
        "id": "D1-Q17",
        "question": "What flag must be passed to the Intel oneAPI C/C++ compiler (`icx`) to instruct it to generate optimized AVX-512 vector instructions targeting Intel 4th Gen Xeon Scalable processors?",
        "options": {
            "A": "-O0 -mno-simd",
            "B": "-O3 -xSapphireRapids (or -mavx512f -mavx512dq -mavx512bw)",
            "C": "-cuda-arch=sm_80",
            "D": "-march=armv8-a"
        },
        "answer": "B",
        "explanation": "The Intel compiler (`icx`) uses `-x<target>` flags (e.g. `-xSapphireRapids` or `-xCORE-AVX512`) along with aggressive optimization level `-O3` to vectorize loops into 512-bit ZMM register instructions, enabling AVX-512 FMA, VNNI, and mask register optimizations."
    },
    {
        "id": "D1-Q18",
        "question": "In Linux cluster administration, what virtual filesystem exposes real-time hardware status such as CPU temperature, frequency scaling governors, and memory sub-timings?",
        "options": {
            "A": "/sys and /proc",
            "B": "/bin and /sbin",
            "C": "/opt and /usr",
            "D": "/var/log only"
        },
        "answer": "A",
        "explanation": "`/proc` provides a window into kernel process state and hardware definitions (`/proc/cpuinfo`, `/proc/meminfo`), while `/sys` (sysfs) exposes structured device tree hierarchies including CPU power management (`/sys/devices/system/cpu/cpu*/cpufreq/`) and cache geometry."
    },
    {
        "id": "D1-Q19",
        "question": "What does the Linux command `lscpu -C` display?",
        "options": {
            "A": "Computer cost breakdown.",
            "B": "Detailed CPU cache hierarchy, including L1 Data, L1 Instruction, L2, and L3 cache sizes, types, and core sharing mappings.",
            "C": "List of compiled C programs.",
            "D": "PCIe bus clock frequencies."
        },
        "answer": "B",
        "explanation": "`lscpu -C` formats a complete table of the processor cache subsystem, listing NAME (L1d, L1i, L2, L3), ONE-SIZE, ALL-SIZE, WAYS of associativity, TYPE, and the CPU allocation mapping."
    },
    {
        "id": "D1-Q20",
        "question": "In modern heterogeneous HPC clusters, what is the role of Intel Level Zero API?",
        "options": {
            "A": "A low-level direct-to-metal hardware abstraction interface for Intel GPUs and AI accelerators, providing fine-grained device control below the SYCL layer.",
            "B": "A basic video game design framework.",
            "C": "An entry-level Linux terminal shell.",
            "D": "A tool to delete user passwords."
        },
        "answer": "A",
        "explanation": "Intel oneAPI Level Zero provides direct, low-overhead access to hardware capabilities of Intel discrete GPUs (like Data Center GPU Max) and accelerators, controlling device initialization, memory allocations, peer-to-peer copies, kernel launches, and hardware telemetry."
    },
    {
        "id": "D1-Q21",
        "question": "What is the key technological feature of InfiniBand NDR networking in top-tier HPC clusters?",
        "options": {
            "A": "400 Gbps per-port throughput with sub-microsecond latency and hardware-offloaded RDMA (Remote Direct Memory Access).",
            "B": "10 Mbps dial-up protocol for legacy terminals.",
            "C": "Wireless Wi-Fi 6 transmission over antennas.",
            "D": "Bluetooth 5.0 mesh for keyboard connectivity."
        },
        "answer": "A",
        "explanation": "InfiniBand NDR (Next Data Rate) delivers 400 Gbps per port using 4 lanes of 100 Gbps PAM4 signaling. With hardware-level RDMA, compute nodes transfer data directly between application memories across cluster nodes without involving the operating system kernel or CPU copy overhead."
    },
    {
        "id": "D1-Q22",
        "question": "What is a Fat-Tree network topology in supercomputer cluster design?",
        "options": {
            "A": "A tree topology where tree branches grow thicker (more aggregated bandwidth) toward the root, guaranteeing full bisection non-blocking bandwidth across all compute racks.",
            "B": "A circular ring where all computers share a single cable.",
            "C": "A wireless network configured in an outdoor park.",
            "D": "A random daisy chain of ethernet switches."
        },
        "answer": "A",
        "explanation": "In a Fat-Tree topology, switches closer to the root have more aggregated uplink bandwidth than leaf switches. A 2-tier or 3-tier non-blocking fat-tree guarantees that any arbitrary half of the cluster can communicate simultaneously with the other half at wire speed without network oversubscription."
    },
    {
        "id": "D1-Q23",
        "question": "What Linux tool allows an engineer to pin a process to a specific NUMA node and enforce that memory allocations only occur from that node's local memory controllers?",
        "options": {
            "A": "numactl --cpunodebind=0 --membind=0 ./app",
            "B": "kill -9 ./app",
            "C": "chmod +x ./app",
            "D": "grep -r numa ./app"
        },
        "answer": "A",
        "explanation": "`numactl --cpunodebind=0 --membind=0 ./app` binds the process's CPU execution threads strictly to the cores of NUMA node 0 and strictly enforces memory allocations from node 0's local DRAM channels, eliminating remote cross-socket UPI traffic."
    },
    {
        "id": "D1-Q24",
        "question": "What does SYCL represent within the Intel oneAPI programming ecosystem?",
        "options": {
            "A": "An open standard, single-source C++ programming model governed by Khronos Group for heterogeneous computing across CPUs, GPUs, FPGAs, and AI accelerators.",
            "B": "A proprietary Nvidia compiler for CUDA graphics cards.",
            "C": "A replacement for HTML and CSS websites.",
            "D": "A database query language similar to SQL."
        },
        "answer": "A",
        "explanation": "SYCL is a royalty-free, open standard C++ programming model managed by the Khronos Group. Intel oneAPI's DPC++ is built upon SYCL, allowing developers to write standards-compliant modern C++ that compiles seamlessly for Intel CPUs, Intel Data Center GPUs, and accelerators without vendor lock-in."
    },
    {
        "id": "D1-Q25",
        "question": "When configuring passwordless SSH keys for an HPC cluster, why must the permissions of `~/.ssh` and `~/.ssh/authorized_keys` strictly be set to `700` and `600` respectively?",
        "options": {
            "A": "Because SSH daemons enforce strict permission checks and will refuse authentication if the directory or keys are writable by group or other users for security.",
            "B": "Because Linux hard drives cannot store files larger than 600 bytes.",
            "C": "Because the Slurm scheduler requires executable bits on authorized_keys.",
            "D": "Because the files are automatically encrypted with AES-700."
        },
        "answer": "A",
        "explanation": "The OpenSSH daemon enforces `StrictModes yes` by default. If `~/.ssh` has permissions looser than `700` (`rwx------`) or `authorized_keys` has permissions looser than `600` (`rw-------`), other local users could potentially tamper with the key files, causing OpenSSH to silently reject the key."
    }
]

# We will compile Day 2, Day 3, Day 4, and Day 5 MCQs similarly
print(f"[*] Day 1 MCQ Bank prepared: {len(mcqs_day1)} questions.")
