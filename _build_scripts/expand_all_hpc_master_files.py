"""
expand_all_hpc_master_files.py
Part 1: Upgrades Day 1 and Day 2 files in HPC_Master_Curriculum
"""

import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# DAY 1 EXPANSIONS
# ==============================================================================

write_f("Day-01_HPC_Linux_Shell_oneAPI/theory_notes/day01_hpc_architecture.md", """# Day 1 Master Theory: HPC Silicon, Supercomputing Topologies & Linux Foundations
**Program**: GLA University Block Teaching | High Performance Computing (Intel & NEC Edition)  
**Lead Trainer**: Shivam Gupta | **Partner Organizations**: Edulateral Foundation, Intel & NEC Corporation  

---

## 1. The Physics and Economics of Supercomputing

### 1.1 The Breakdown of Dennard Scaling & The Power Wall
For three decades (1974–2005), microprocessor development was governed by Robert Dennard's scaling law:
$$\\text{Power Density} = \\frac{P}{A} \\propto \\frac{V^2 \\times f \\times C}{\\text{Area}} \\approx \\text{Constant}$$
As transistor dimensions shrank by a factor of $k \\approx 1.4$, capacitance $C$ decreased by $k$, allowing operating voltage $V$ and clock period to scale down simultaneously while total power per square millimeter remained constant.

**The Breakdown (c. 2005)**:
- At sub-90nm physical gate lengths, quantum mechanical tunneling through gate oxides caused sub-threshold leakage current to explode exponentially.
- Operating voltage could no longer scale below ~0.8V to 1.0V without rendering transistor switching unstable.
- Consequently, power density soared, creating the **Power Wall**. Increasing clock frequencies beyond 4.0–5.0 GHz caused thermal dissipation to exceed ~300 Watts per socket—risking silicon melting.
- **The Paradigm Shift**: Processor architects ceased pursuing higher clock speeds and transitioned to chip-multiprocessing (CMP), heterogeneous accelerators, and ultra-wide SIMD vectorization.

```
Transistor Scaling & The Power Wall (1970 - Present)
Log Scale
  ^
  │                           Transistors (Moore's Law continues)
  │                     /═════════════════════════════════════════
  │                   /
  │                 /    [2005: Dennard Scaling Collapses]
  │               /           Single-Thread Performance Plateaus
  │             /       - - - - - - - - - - - - - - - - - - - - -
  │           /               Clock Frequency (Power Wall ~4 GHz)
  │         /           ═════════════════════════════════════════
  │       /
  └─────────────────────────────────────────────────────────────> Year
```

---

### 1.2 Mathematical Scaling Limits: Amdahl vs Gustafson

#### Amdahl's Law (Strong Scaling / Fixed Workload)
Gene Amdahl (1967) demonstrated that speedup for a fixed problem size executed across $N$ parallel execution units is fundamentally bounded by the strictly sequential fraction of the algorithm $(1 - p)$:
$$S_{\\text{latency}}(N) = \\frac{1}{(1 - p) + \\frac{p}{N}}$$
As $N \\to \\infty$, the parallel term $\\frac{p}{N} \\to 0$, yielding the theoretical asymptote:
$$S_{\\max} = \\lim_{N \\to \\infty} S(N) = \\frac{1}{1 - p}$$

*Forensic Analysis Table*:
| Parallel Fraction ($p$) | Sequential Bottleneck ($1 - p$) | Theoretical Max Speedup ($N \\to \\infty$) | Speedup on 64 Cores | Speedup on 1024 Cores |
| :---: | :---: | :---: | :---: | :---: |
| 50.0% | 50.0% | **2.00x** | 1.97x | 1.99x |
| 80.0% | 20.0% | **5.00x** | 4.71x | 4.98x |
| 90.0% | 10.0% | **10.00x** | 8.77x | 9.90x |
| 95.0% | 5.0% | **20.00x** | 15.42x | 19.63x |
| 99.0% | 1.0% | **100.00x** | 39.26x | 91.18x |

#### Gustafson's Law (Weak Scaling / Scaled Workload)
John Gustafson (1988) observed that supercomputers are rarely used to run fixed, small problems faster. Instead, scientists use larger supercomputers to run dramatically larger, higher-resolution models.
$$S_{\\text{scaled}}(P) = P - \\alpha(P - 1)$$
Where $P$ is processor count and $\\alpha = 1 - p$ is the sequential fraction. When problem volume scales proportionally with core count, parallel computation expands while sequential setup overhead remains constant.

---

## 2. Silicon Microarchitecture: Intel Xeon Scalable (Sapphire Rapids)

```
┌────────────────────────────────────────────────────────────────────────┐
│           Intel Xeon Scalable (Sapphire Rapids) Dual-Socket            │
├───────────────────────────────────┬────────────────────────────────────┤
│           SOCKET 0 (NUMA 0)       │          SOCKET 1 (NUMA 1)         │
│  ┌─────────────────────────────┐  │  ┌─────────────────────────────┐   │
│  │ Up to 60 Golden Cove Cores  │  │  │ Up to 60 Golden Cove Cores  │   │
│  │ ├─ L1d Cache: 48 KB / core  │  │  │ ├─ L1d Cache: 48 KB / core  │   │
│  │ ├─ L2 Cache: 2 MB / core    │  │  │ ├─ L2 Cache: 2 MB / core    │   │
│  │ ├─ AVX-512 Vector Engine    │  │  │ ├─ AVX-512 Vector Engine    │   │
│  │ └─ AMX 2D Tile Engine (TMUL)│  │  │ └─ AMX 2D Tile Engine (TMUL)│   │
│  ├─────────────────────────────┤  │  ├─────────────────────────────┤   │
│  │ Shared L3 Cache: 112.5 MB   │  │  │ Shared L3 Cache: 112.5 MB   │   │
│  │ 8-Channel DDR5 @ 4800 MT/s  │  │  │ 8-Channel DDR5 @ 4800 MT/s  │   │
│  └──────────────┬──────────────┘  │  └──────────────┬──────────────┘   │
└─────────────────┼─────────────────┴─────────────────┼──────────────────┘
                  │  Intel Ultra Path Interconnect    │
                  └────────◄═══ UPI Links ═══►────────┘
                       (Cross-Socket: ~140ns Latency)
```

### 2.1 NUMA Architecture & UPI Interconnect
Modern enterprise HPC servers feature multi-socket Non-Uniform Memory Access (NUMA) topologies:
1. **Local Access**: CPU cores on Socket 0 access memory channels directly attached to Socket 0 with ~80ns latency and full DDR5 bus bandwidth (~307 GB/s aggregate).
2. **Remote Access**: When a thread running on Socket 0 accesses physical memory attached to Socket 1, the memory transaction must traverse the **Intel Ultra Path Interconnect (UPI)** coherent fabric. This introduces an additional ~60–80ns latency penalty (~140–160ns total) and saturates UPI inter-socket bandwidth.
3. **Engineering Directive**: High-performance applications must enforce NUMA thread pinning via `numactl` or `KMP_AFFINITY` to prevent cross-socket thrashing.

### 2.2 SIMD Vectorization: AVX-512
- **Vector Registers**: Thirty-two 512-bit registers (`ZMM0` through `ZMM31`).
- **Instruction Throughput**: In a single clock cycle, an AVX-512 FMA instruction computes sixteen 32-bit single-precision floats:
$$\\text{Throughput} = \\frac{512\\text{ bits}}{32\\text{ bits/float}} = 16\\text{ operations per cycle per FMA unit}$$
- Dual FMA units per core deliver 32 FP32 operations per cycle per core.

### 2.3 Intel Advanced Matrix Extensions (AMX)
Sapphire Rapids introduced hardware matrix acceleration:
- **TMM Architecture**: Eight 2-dimensional tile registers (`TMM0` through `TMM7`), each holding up to 1 Kilobyte of matrix data ($16 \\times 64$ bytes).
- **TMUL Execution Engine**: Systolic matrix multiplier executing matrix multiply-accumulate operations ($C += A \\times B$) in a single cycle:
  - 2048 INT8 operations per cycle per core.
  - 1024 Bfloat16 operations per cycle per core.

---

## 3. Supercomputing Cluster Interconnect Topologies

```
Fat-Tree Non-Blocking Interconnect Topology
                  [ Core Switches / Spine ]
                  ┌─────────┴─────────┐
             ┌────┴────┐         ┌────┴────┐
             │ Switch  │         │ Switch  │
             └────┬────┘         └────┬────┘
        ┌─────────┴─────────┐         └─────────┐
   ┌────┴────┐         ┌────┴────┐         ┌────┴────┐
   │ Leaf SW │         │ Leaf SW │         │ Leaf SW │  [ Leaf Switches ]
   └──┬───┬──┘         └──┬───┬──┘         └──┬───┬──┘
      │   │               │   │               │   │
    [Compute Nodes]     [Compute Nodes]     [Compute Nodes]
```

### 3.1 Network Fabric Comparison
1. **InfiniBand (HDR / NDR)**:
   - **HDR (High Data Rate)**: 200 Gbps per port, sub-600ns switch latency.
   - **NDR (Next Data Rate)**: 400 Gbps per port using 4x 100G PAM4 signaling.
   - **Zero-Copy RDMA (Remote Direct Memory Access)**: Transfers data directly from user application memory on Node A to Node B bypassing the operating system kernel and CPU cache.
2. **RoCE v2 (RDMA over Converged Ethernet)**:
   - Encapsulates InfiniBand transport packets inside standard UDP/IP Ethernet frames.
   - Enables RDMA on enterprise Ethernet switches supporting Priority Flow Control (PFC) and Explicit Congestion Notification (ECN).
3. **Fat-Tree Topology**:
   - Ensures full bisection non-blocking bandwidth across all racks. Uplinks from leaf to spine switches scale proportionally to node count, eliminating network oversubscription.

---

## 4. HPC Linux Storage Hierarchy & Parallel File Systems

| Tier | Mount Path | Storage Technology | Latency | Bandwidth | Typical Allocation |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L1 / L2 / L3** | On-Die CPU | Static RAM (SRAM) | 1ns – 15ns | 1 – 4 TB/s | Registers & Caches |
| **Local DRAM** | `/dev/shm` | 8-Channel DDR5 | ~80ns | ~300 GB/s | Active Process Memory |
| **Node NVMe** | `/tmp` | PCIe Gen 5 NVMe SSD | ~10μs | ~7 – 14 GB/s | Fast Local Temp Spilling |
| **Parallel Scratch**| `/scratch` | Lustre / GPFS (IBM) | ~100μs | 100 – 1000 GB/s| Checkpoints, Large Datasets |
| **NFS Home** | `/home` | Network File System | ~1ms – 5ms | ~1 – 10 GB/s | Code, Scripts, Dotfiles |

### 4.1 Lustre File System Mechanics
- **Management Server (MGS)**: Cluster storage configuration registry.
- **Metadata Server & Target (MDS/MDT)**: Stores file names, permissions, and directory trees.
- **Object Storage Server & Target (OSS/OST)**: High-speed disk arrays storing raw striped file data chunks.
- **File Striping**: Large multi-gigabyte files are partitioned across multiple OSTs, allowing hundreds of nodes to read and write parallel streams simultaneously.
""")

write_f("Day-01_HPC_Linux_Shell_oneAPI/theory_notes/intel_nec_architecture_spec.md", """# Intel & NEC HPC Synergy: Vector Host & Vector Engine Architecture
**Technical Specification & Comparative Analysis**  
**Lead Trainer**: Shivam Gupta | Edulateral Foundation Master Curriculum  

---

## 1. Architectural Philosophy: Scalar Engine vs Ultra-Wide Vector Pipeline

High-Performance Computing systems are broadly bifurcated into two computational archetypes:
1. **General-Purpose Scalar/Multi-Core (Intel Xeon)**: Optimized for branchy code, operating system services, complex file system I/O, database coordination, and moderate SIMD vectorization.
2. **Dedicated Pure Vector Supercomputing (NEC SX-Aurora TSUBASA)**: Optimized for extremely wide vector pipelining and massive memory bandwidth where execution speed is strictly bounded by the rate at which floating-point numbers can be streamed from memory.

```
┌───────────────────────────────────────────────────────────────────────────────┐
│                      NEC SX-Aurora TSUBASA Supercomputer                      │
├───────────────────────────────────────┬───────────────────────────────────────┤
│          VECTOR HOST (VH)             │          VECTOR ENGINE (VE)           │
│     [ Intel Xeon Scalable CPU ]       │     [ NEC SX-Aurora PCIe Engine ]     │
├───────────────────────────────────────┼───────────────────────────────────────┤
│ • Architecture: x86_64 CISC           │ • Architecture: NEC Vector Engine     │
│ • Runs Standard Linux OS (RHEL/Ubuntu)│ • Dedicated PCIe Gen 4/5 accelerator  │
│ • Manages Lustre, Slurm, InfiniBand   │ • 8 to 10 Ultra-Wide Vector Cores     │
│ • 8-Channel DDR5 (250-300 GB/s BW)    │ • Dedicated HBM2 (1.2 to 1.53 TB/s BW)│
│ • Handles Scalar I/O & Preprocessing  │ • 64 Vector Regs of 256 Elements/core │
└───────────────────────────────────────┴───────────────────────────────────────┘
```

---

## 2. Deep Dive: NEC Vector Engine (VE) Microarchitecture

### 2.1 The Vector Register File
Unlike Intel AVX-512 (which provides thirty-two 512-bit registers holding 16 single-precision floats), each core of the NEC Vector Engine contains:
- **64 Vector Registers**: Each register holds **256 elements of 64-bit floating-point numbers** (or 512 elements of 32-bit floats).
- **Register Width**: $256 \\times 64 = \\mathbf{16,384\\text{ bits}}$ per vector register!
- **Vector Pipeline**: Three parallel vector execution units (Fused Multiply-Add, Logical, Divide) operating concurrently per core.

### 2.2 Memory Bandwidth: Conquering the Memory Wall
The NEC Vector Engine Type 20B/30 integrates 3D-stacked High Bandwidth Memory (HBM2):
- **Aggregate Bandwidth**: **1.53 Terabytes per second (TB/s)**.
- **Byte-to-Flop Ratio ($B/F$)**: ~0.5 to 0.6 Bytes/FLOP. (Standard x86 CPUs typically offer $<0.1$ B/F).
- **Application Advantage**: Scientific codes with low operational intensity (sparse matrix-vector products, Poisson solvers, weather simulation stencils) run near peak hardware speed on NEC VE without hitting the memory wall.

---

## 3. The VH + VE Offloading & Hybrid Execution Models

NEC SX-Aurora supports two distinct deployment execution paradigms:

### 3.1 Model A: Native VE Execution (VE Offloading / VH Standby)
- The user application compiles directly for the VE target using the NEC compiler toolchain (`ncc`, `nc++`, `nfort`).
- The program runs natively on the Vector Engine. System calls (e.g. `open`, `read`, `printf`) are transparently forwarded across the PCIe bus to the Vector Host (Intel Xeon) via the VEOS (Vector Engine Operating System) kernel module.

### 3.2 Model B: Hybrid Heterogeneous Co-Processing
- The main control flow, data ingestion, and orchestration execute on the Intel Xeon (Vector Host).
- Heavy computational loops are offloaded to the NEC Vector Engine using **OpenMP Target Directives** (`#pragma omp target`) or **oneAPI SYCL offload**.
- The Intel oneAPI ecosystem bridges x86_64 and accelerator platforms through open standards.

---

## 4. NEC Toolchain Reference & Compilation Guide

| Tool / Command | Functionality | Equivalent Intel oneAPI Tool |
| :--- | :--- | :--- |
| `ncc -O3 -fpic` | NEC C Vector Compiler | `icx -O3 -xSapphireRapids` |
| `nc++ -O3` | NEC C++ Vector Compiler | `icpx -O3` |
| `nfort -O3` | NEC Fortran Vector Compiler | `ifx -O3` |
| `mpisx_ncc` | NEC MPI Vector Compiler | `mpiicx` |
| `veoffload` | Offload Runtime API | Intel Level Zero / OpenMP Target |

### Optimization Flag Best Practices:
```bash
# Compile vector C++ program for NEC Vector Engine
nc++ -O3 -ftrace -report-all -o simulation_ve simulation.cpp

# Inspect automatic vectorization report
# Output indicates vector loop length (VLEN: up to 256) and vectorization ratio
```
""")

write_f("Day-01_HPC_Linux_Shell_oneAPI/presentation_scripts/trainer_speaking_script.md", """# 🎙️ Day 1 Lead Trainer Speaking Script (Shivam Gupta)
### GLA University Block Teaching: High Performance Computing
**Morning Delivery (09:00 AM – 12:45 PM) & Afternoon Lab (01:45 PM – 05:00 PM)**  
**Audience**: 7th Semester B.Tech Computer Science & Engineering  

---

## ⏰ 09:00 AM – 09:30 AM: Opening Hook & Establishing Authority

### 🎬 The Hook (Stand at the Whiteboard, Do NOT Click Slides Yet):
> *"Good morning, engineers. Welcome to High Performance Computing.  
> Let me ask you a straight question: Right now, every one of you writes code in Python, C++, or Java. You write a loop, you run it, and it works. But have you ever stopped to think about what is happening on the physical silicon?  
> When you buy a 4.0 GHz processor, do you know why it is not 10.0 GHz? Do you know why in the year 2005, the entire computer architecture industry hit a brick wall that changed software engineering forever?  
> Over the next five days, we are going to tear down the abstractions. We are not here to read slides. We are here to talk about what happens when you have to process 50 Terabytes of data across 1,000 servers connected by InfiniBand fibers, where a 10-nanosecond cache stall costs a bank $500,000 or causes a deep learning training run to waste 50,000 kilowatt-hours of power.  
> My name is Shivam Gupta, and representing the Edulateral Foundation in technical alignment with Intel and NEC Supercomputing, we are going to build, benchmark, profile, and optimize real high-performance systems."*

---

## ⏰ 09:30 AM – 10:30 AM: Dennard Scaling & Amdahl's Law (Whiteboard Derivation)

### 🖊️ Whiteboard Diagram: Dennard Scaling Breakdown
*Draw the Power Density equation on the physical board:*
> *"Look at this equation: Power = Voltage squared times frequency times capacitance.  
> Between 1974 and 2005, Dennard scaling was magic. Every time transistors got smaller, power density stayed constant. We could double clock speed without burning the chip.  
> Then we hit 90 nanometers. Transistor gates got so thin that electrons started quantum-tunneling right through the insulator. Static leakage current exploded. If Intel or AMD tried to push a desktop chip to 8 GHz on air cooling, the silicon would literally desolder itself from the motherboard.  
> That is the Power Wall. That is why single-thread performance flatlined, and that is why you cannot get a high-paying systems engineering job today without understanding multi-core parallelism and vectorization."*

### 💡 Interactive Challenge: Amdahl's Law Trap
*Turn to the class:*
> *"Let's test your systems intuition. Suppose your team writes an AI training algorithm. 95% of your code is perfectly parallelized across 1,000 Xeon CPU cores. Only 5% is sequential—just reading the dataset config file.  
> How fast will your code run? Will it run 500 times faster? 100 times faster?"*  
*(Wait for 2-3 student answers)*  
> *"The answer is: It can NEVER run more than 20 times faster. Even if you buy 1,000,000 cores.  
> S = 1 / (1 - 0.95) = 1 / 0.05 = 20x.  
> That 5% serial bottleneck strangles your million-dollar cluster. That is Amdahl's Law. And that is why systems engineers get paid top dollar: to hunt down and eliminate that 5%."*

---

## ⏰ 10:45 AM – 12:45 PM: Linux HPC Terminal & Intel oneAPI Setup

### 🖥️ Live Terminal Demonstration (Projector):
> *"Open your terminals. Do not use generic graphical monitors. In an HPC cluster, you have no desktop GUI. You have a terminal prompt over SSH.  
> Run `lscpu -C`. Look at that table. Look at L1 data cache: 48 KB. L2 cache: 2 MB. L3 cache: 112 MB.  
> If your data fits in L1 cache, the CPU reads it in 1 nanosecond. If your code accesses memory badly and hops to remote DRAM, it takes 140 nanoseconds. That is a 140x slowdown before you even write a single line of machine learning code!  
> Now run: `grep -o 'avx512[^ ]*' /proc/cpuinfo | sort -u`.  
> What does AVX-512 mean? It means 512-bit vector registers. One clock cycle, sixteen 32-bit floating point calculations. If you compile your code without vector flags, you are throwing away 93% of your CPU's hardware capacity."*

---

## ⏰ 01:45 PM – 05:00 PM: Hands-On Laboratory & Co-Trainer Coordination

### 🛠️ Floor Protocol:
* Shivam leads the challenges from the podium; co-trainer Nikhil moves up and down the aisles resolving terminal permission issues, conda paths, and SSH syntax.
* Run the live benchmark scripts in `live_demo/`.
* Administer the Day 1 Official MCQ Quiz (25 questions) at 04:15 PM.
* Close session by previewing Day 2: OpenMP multithreading and the 30x Intel Scikit-Learn speedup showdown!
""")

write_f("Day-01_HPC_Linux_Shell_oneAPI/student_cheatsheets/quick_reference_card.md", """# 🚀 Day 1 Student Quick Reference Card: HPC Linux & oneAPI
**Edulateral Foundation | High Performance Computing @ GLA University**  
*Keep this reference card open during all laboratory sessions.*

---

## 1. Silicon & Hardware Topology Inspection
```bash
# Detailed CPU architecture and core topology
lscpu

# Inspect CPU cache sizes, associativity, and mappings
lscpu -C

# Query NUMA nodes, socket memory capacities, and distance matrix
numactl --hardware

# Verify AVX-512 and SIMD vector support flags
grep -o 'avx[^ ]*' /proc/cpuinfo | sort -u

# Inspect physical PCIe devices, accelerators, and link width
lspci -vvv | grep -i -E "vga|3d|accelerator|intel|nec"
```

---

## 2. Robust HPC Bash Scripting (`set -euo pipefail`)
```bash
#!/usr/bin/env bash
# ==============================================================================
# Fail-Safe HPC Script Header
# ==============================================================================
set -euo pipefail

# Trap signals and purge scratch on exit
SCRATCH_DIR=$(mktemp -d /tmp/hpc_job_XXXXXX)
cleanup() {
    echo "[CLEANUP] Removing temporary scratch directory: ${SCRATCH_DIR}"
    rm -rf "${SCRATCH_DIR}"
}
trap cleanup EXIT SIGINT SIGTERM

echo "[INFO] Running on host: $(hostname) with $(nproc) threads"
```

---

## 3. OpenSSH HPC Cluster Configuration
```bash
# Generate modern Ed25519 elliptic-curve keypair
ssh-keygen -t ed25519 -C "student@gla.ac.in" -f ~/.ssh/id_ed25519 -N ""

# Set mandatory OpenSSH directory and key permissions
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub

# Append public key to authorized keys
cat ~/.ssh/id_ed25519.pub >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
```

### High-Performance `~/.ssh/config` Template:
```text
Host node*
    User student
    IdentityFile ~/.ssh/id_ed25519
    StrictHostKeyChecking no
    ControlMaster auto
    ControlPath ~/.ssh/sockets/%r@%h:%p
    ControlPersist 10m
    ServerAliveInterval 60
```

---

## 4. Intel oneAPI Environment Variables
```bash
# Initialize complete oneAPI toolchain
source /opt/intel/oneapi/setvars.sh --force

# Hardware thread binding and affinity
export OMP_NUM_THREADS=$(nproc)
export KMP_AFFINITY=granularity=fine,compact,1,0
export KMP_BLOCKTIME=1

# TensorFlow oneDNN hardware acceleration
export TF_ENABLE_ONEDNN_OPTS=1
```
""")

print("[SUCCESS] Day 1 Master Upgrades applied successfully!")
