"""
build_all_edulateral_pptx.py
Edulateral Foundation — Official PowerPoint Presentation Generator.
Generates 5 comprehensive, professionally designed .pptx presentation decks:
- Day-01_HPC_Foundations_Linux_oneAPI.pptx
- Day-02_Parallel_OpenMP_MPI_oneDAL.pptx
- Day-03_DeepLearning_TensorFlow_Slurm_Horovod.pptx
- Day-04_Distributed_AI_Slurm_VTune.pptx
- Day-05_GenAI_LLMs_OpenVINO_Gaudi.pptx

Target: GLA University Block Teaching (Nov 16-20, 2026)
Lead Trainer: Shivam Gupta | Edulateral Foundation Corporate Design System
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

output_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\Edulateral_Official_Presentations"
os.makedirs(output_dir, exist_ok=True)

# Color Palette: Corporate High-Tech
COLOR_BG = RGBColor(15, 23, 42)        # Slate 900
COLOR_SURFACE = RGBColor(30, 41, 59)   # Slate 800
COLOR_NAVY = RGBColor(14, 116, 144)    # Cyan 700 / Edulateral Blue
COLOR_ACCENT = RGBColor(56, 189, 248)  # Cyan 400
COLOR_TEXT = RGBColor(248, 250, 252)   # Slate 50
COLOR_MUTED = RGBColor(148, 163, 184)  # Slate 400
COLOR_GOLD = RGBColor(251, 191, 36)    # Amber 400

def create_deck(day_num, day_title, subtitle, slides_data):
    prs = Presentation()
    prs.slide_width = Inches(13.333) # 16:9 Widescreen
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # Blank layout

    # 1. TITLE SLIDE
    slide = prs.slides.add_slide(blank_layout)
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg.fill.solid()
    bg.fill.fore_color.rgb = COLOR_BG
    bg.line.fill.background()

    # Edulateral Top Banner
    banner = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
    banner.fill.solid()
    banner.fill.fore_color.rgb = COLOR_NAVY
    banner.line.fill.background()
    
    tf_b = banner.text_frame
    tf_b.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_b = tf_b.paragraphs[0]
    p_b.text = "🏢 EDULATERAL FOUNDATION | OFFICIAL TECHNICAL WORKSHOP"
    p_b.font.size = Pt(20)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_TEXT
    p_b.alignment = PP_ALIGN.CENTER

    # Main Title Card
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.2), Inches(1.8), Inches(10.933), Inches(4.8))
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_SURFACE
    card.line.color.rgb = COLOR_ACCENT

    tf_c = card.text_frame
    tf_c.word_wrap = True
    tf_c.vertical_anchor = MSO_ANCHOR.MIDDLE

    p1 = tf_c.paragraphs[0]
    p1.text = f"GLA UNIVERSITY BLOCK TEACHING — DAY {day_num}"
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_ACCENT
    p1.alignment = PP_ALIGN.CENTER

    p2 = tf_c.add_paragraph()
    p2.text = day_title
    p2.font.size = Pt(36)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_TEXT
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf_c.add_paragraph()
    p3.text = subtitle
    p3.font.size = Pt(20)
    p3.font.color.rgb = COLOR_GOLD
    p3.alignment = PP_ALIGN.CENTER

    p4 = tf_c.add_paragraph()
    p4.text = "\nLead Trainer: Shivam Gupta | Partner Organizations: Intel & NEC Supercomputing"
    p4.font.size = Pt(16)
    p4.font.color.rgb = COLOR_MUTED
    p4.alignment = PP_ALIGN.CENTER

    # Add presenter note to Title slide
    notes = slide.notes_slide.notes_text_frame
    notes.text = f"Welcome to Day {day_num} of the GLA University Block Teaching on High Performance Computing. Introduce yourself as Lead Trainer representing Edulateral Foundation. Set an authoritative, energetic, and professional tone."

    # 2. CONTENT SLIDES
    for s_idx, s in enumerate(slides_data, 1):
        slide = prs.slides.add_slide(blank_layout)
        
        # Background
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()

        # Header Bar
        header = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(1.1))
        header.fill.solid()
        header.fill.fore_color.rgb = COLOR_SURFACE
        header.line.color.rgb = COLOR_NAVY
        
        tf_h = header.text_frame
        tf_h.vertical_anchor = MSO_ANCHOR.MIDDLE
        p_h = tf_h.paragraphs[0]
        p_h.text = f"EDULATERAL FOUNDATION  •  DAY {day_num}  •  SLIDE {s_idx + 1}"
        p_h.font.size = Pt(13)
        p_h.font.bold = True
        p_h.font.color.rgb = COLOR_ACCENT
        
        p_ht = tf_h.add_paragraph()
        p_ht.text = s["title"]
        p_ht.font.size = Pt(24)
        p_ht.font.bold = True
        p_ht.font.color.rgb = COLOR_TEXT

        # Content Card
        c_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.4), Inches(11.733), Inches(5.6))
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = COLOR_SURFACE
        c_box.line.color.rgb = COLOR_NAVY

        tf = c_box.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.TOP

        for bullet_idx, bullet in enumerate(s["bullets"]):
            p = tf.paragraphs[0] if bullet_idx == 0 else tf.add_paragraph()
            p.text = bullet
            p.font.size = Pt(17)
            p.font.color.rgb = COLOR_TEXT
            p.space_after = Pt(12)
            p.level = 0

        if "code" in s and s["code"]:
            code_p = tf.add_paragraph()
            code_p.text = "\n[TERMINAL / CODE IMPLEMENTATION]:"
            code_p.font.size = Pt(15)
            code_p.font.bold = True
            code_p.font.color.rgb = COLOR_ACCENT

            code_body = tf.add_paragraph()
            code_body.text = s["code"]
            code_body.font.size = Pt(14)
            code_body.font.name = "Consolas"
            code_body.font.color.rgb = COLOR_GOLD

        # Speaker notes for Shivam
        notes = slide.notes_slide.notes_text_frame
        notes.text = s.get("notes", "Drive discussion with whiteboard diagram and live terminal execution.")

    # Save Deck
    out_filename = f"Day-{day_num:02d}_{day_title.replace(' ', '_').replace(',', '').replace('&', 'and')[:40]}.pptx"
    out_path = os.path.join(output_dir, out_filename)
    prs.save(out_path)
    print(f"[OK] Generated Presentation: {out_filename} ({len(slides_data) + 1} slides)")
    return out_path

# ==============================================================================
# SLIDE DECKS CONTENT DATA
# ==============================================================================

# DAY 1 SLIDES
day1_slides = [
    {
        "title": "Pedagogy & 5-Day Curriculum Roadmap",
        "bullets": [
            "• Concept → System Understanding → Hands-On: Core theory followed immediately by live Linux execution.",
            "• Industry-Grade Toolchains: Intel oneAPI Base & HPC Toolkits, Slurm Workload Manager, Intel VTune, OpenVINO.",
            "• Silicon Ecosystem: Intel Xeon Scalable (Sapphire Rapids), NEC SX-Aurora TSUBASA, Habana Gaudi 2/3.",
            "• Placement & Capstone Orientation: Translating HPC systems engineering into Tier-1 tech competencies."
        ],
        "notes": "Walk through the pedagogy. Emphasize that 7th semester students will work on real industrial cluster tools, not toy classroom examples."
    },
    {
        "title": "The Physics & Economics of Supercomputing",
        "bullets": [
            "• The Collapse of Dennard Scaling (2005): Sub-threshold gate leakage destroyed constant power density.",
            "• The Power Wall: Clock speeds plateaued at 4-5 GHz; cooling beyond that requires liquid nitrogen or burns silicon.",
            "• The Transition: High-Performance Computing transitioned to massive multi-core parallelism and vector accelerators.",
            "• Flops & The TOP500: Petaflops (10^15) to Exaflops (10^18) supercomputing benchmarks."
        ],
        "notes": "Draw the Dennard Scaling graph on the whiteboard. Show how clock speed flatlined in 2005 while transistor counts kept climbing, necessitating parallelism."
    },
    {
        "title": "Amdahl's Law vs Gustafson's Law: Mathematical Limits",
        "bullets": [
            "• Amdahl's Law (Strong Scaling): S = 1 / ((1 - p) + (p / N)). Serial fraction (1-p) strictly caps maximum speedup.",
            "• The Bottleneck: If 10% of code is serial, speedup CANNOT exceed 10x, even with 100,000 Xeon cores!",
            "• Gustafson's Law (Weak Scaling): S(P) = P - alpha * (P - 1). Parallel fraction expands as problem size scales.",
            "• Industrial Reality: HPC clusters conquer Amdahl's Law by computing massively larger simulation grids."
        ],
        "notes": "Ask students: 'If your program is 95% parallel, what is the max speedup on an infinite cluster?' Answer: 20x. Show Gustafson's weak scaling."
    },
    {
        "title": "Intel Xeon Scalable Architecture: Sapphire Rapids",
        "bullets": [
            "• Non-Uniform Memory Access (NUMA): Multi-socket topology with dedicated DDR5 memory controllers per socket.",
            "• Inter-Socket Interconnect: Intel Ultra Path Interconnect (UPI) links providing cache coherency across sockets.",
            "• NUMA Latency Penalty: Local DRAM access takes ~80ns; remote socket cross-UPI access incurs 140-160ns latency.",
            "• Thread Pinning Mandate: Applications must pin execution threads to avoid catastrophic cross-socket hops."
        ],
        "code": "numactl --hardware\n# Inspect distance matrix: Local = 10, Remote = 21",
        "notes": "Show the output of numactl -H. Explain why cross-socket remote DRAM access cuts bandwidth in half."
    },
    {
        "title": "SIMD Vectorization & AVX-512 Microarchitecture",
        "bullets": [
            "• Single Instruction Multiple Data: Computing an entire vector array in a single clock cycle.",
            "• 512-Bit Vector Registers: Thirty-two 512-bit registers (ZMM0 to ZMM31).",
            "• Single-Precision Throughput: 512 bits / 32 bits = 16 float32 operations per instruction cycle.",
            "• FMA (Fused Multiply-Add): Computes (A * B + C) in a single instruction with zero intermediate rounding."
        ],
        "code": "grep -o 'avx512[^ ]*' /proc/cpuinfo | sort -u",
        "notes": "Demonstrate the vector registers on the board: 512 bits divided into 16 slices of 32-bit floats. One instruction, 16 results."
    },
    {
        "title": "Intel Advanced Matrix Extensions (AMX)",
        "bullets": [
            "• Next-Generation Silicon Accelerator: Embedded directly into Sapphire Rapids Xeon processor cores.",
            "• 2D Tile Architecture: Eight 1-Kilobyte 2D tile registers (TMM0 to TMM7).",
            "• TMUL (Tile Matrix Multiply): Systolic hardware execution engine computing matrix products in a single operation.",
            "• Deep Learning Throughput: Computes 2048 INT8 or 1024 Bfloat16 matrix operations per core per cycle."
        ],
        "notes": "Contrast traditional 1D vector registers (AVX-512) with 2D matrix tiles (AMX). Explain how AMX turns Xeon CPUs into deep learning inference beasts."
    },
    {
        "title": "NEC SX-Aurora TSUBASA Vector Architecture",
        "bullets": [
            "• Vector Host (VH) + Vector Engine (VE): Decoupled hybrid supercomputing paradigm.",
            "• Intel Xeon (Vector Host): Executes standard Linux OS, system daemons, Lustre I/O, and Slurm scheduling.",
            "• NEC Vector Engine (PCIe Card): Dedicated vector processor card containing 8-10 ultra-wide vector cores.",
            "• Ultra-Wide Registers: 64 vector registers of 256 elements (16,384 bits per register) per core!"
        ],
        "notes": "Cover the NEC SX-Aurora TSUBASA model. Highlight that the Intel Xeon handles scalar I/O and OS, while the NEC VE handles dense vector computation."
    },
    {
        "title": "NEC SX-Aurora: Conquering the Memory Wall",
        "bullets": [
            "• The Memory Wall: CPU compute speeds have grown 100x faster than DRAM memory bandwidth.",
            "• NEC VE HBM2 Memory: High-Bandwidth Memory stacked directly on silicon interposer.",
            "• Memory Bandwidth: Up to 1.53 Terabytes/second (TB/s) dedicated memory throughput per card.",
            "• Ideal Workloads: Sparse matrix solvers, computational fluid dynamics, climate modeling, and weather forecasting."
        ],
        "notes": "Explain why standard DDR5 (~250 GB/s) starves vector units, and how NEC's 1.53 TB/s HBM2 eliminates the memory bottleneck."
    },
    {
        "title": "HPC Linux File Systems: Lustre vs NFS",
        "bullets": [
            "• Home Directory (`/home`): Hosted on standard NFS; intended for source code, dotfiles, and scripts with quotas.",
            "• Parallel Scratch (`/scratch`): Production high-performance parallel file system (Lustre / IBM Spectrum Scale).",
            "• Lustre Architecture: Management Server (MGS), Metadata Targets (MDT), and parallel Object Storage Targets (OSTs).",
            "• Striping Mechanics: Files are sliced into stripes and written across dozens of parallel OSTs simultaneously."
        ],
        "code": "lfs getstripe /scratch/simulation_data.h5\n# Shows parallel file striping across storage targets",
        "notes": "Warn students: NEVER run large HPC dataset I/O inside /home! Always execute heavy simulations on /scratch."
    },
    {
        "title": "Production Shell Scripting for HPC Automation",
        "bullets": [
            "• The Mandatory Directive: `set -euo pipefail` halts execution immediately upon any error or unset variable.",
            "• Signal Trapping: Use `trap cleanup EXIT SIGINT SIGTERM` to purge temporary scratch directories reliably.",
            "• Process Substitution: Stream command outputs without writing slow temporary files to disk.",
            "• Cluster Logging: Redirect stdout and stderr cleanly (`cmd > job.log 2>&1`) for post-mortem Slurm auditing."
        ],
        "code": "#!/usr/bin/env bash\nset -euo pipefail\ntrap 'echo Cleaned scratch; rm -rf /tmp/hpc_$$' EXIT",
        "notes": "Show why without pipefail, a failed command in a pipe silently passes exit code 0 and corrupts supercomputing jobs."
    },
    {
        "title": "Secured Shell (SSH) & HPC Cluster Access",
        "bullets": [
            "• Cryptographic Standards: Ed25519 elliptic-curve keys replace legacy RSA 2048/4096-bit keys.",
            "• File Permissions: OpenSSH enforces strict security (`~/.ssh` = 700, `authorized_keys` = 600).",
            "• Connection Multiplexing: `ControlMaster auto` reuses authenticated TCP sockets for instant command execution.",
            "• Cluster Host Aliases: Configuring `~/.ssh/config` for passwordless traversal across cluster login & compute nodes."
        ],
        "code": "ssh-keygen -t ed25519 -N '' -f ~/.ssh/id_ed25519\nchmod 700 ~/.ssh && chmod 600 ~/.ssh/authorized_keys",
        "notes": "Demonstrate generating Ed25519 keys live. Explain how ControlMaster cuts cluster SSH connection latency from 400ms to 2ms."
    },
    {
        "title": "Environment Modules & Dynamic Toolchain Swapping",
        "bullets": [
            "• The Problem: Conflicting compiler toolchains (GCC vs Intel ICX) and MPI libraries (OpenMPI vs Intel MPI).",
            "• The Lmod Solution: Dynamically updates `PATH`, `LD_LIBRARY_PATH`, `CPATH`, and `MANPATH` per user session.",
            "• Core Commands: `module avail` (list packages), `module load <tool>` (activate), `module purge` (reset environment).",
            "• Automation: Embedding `module load intel/oneapi/latest` inside Slurm batch submission scripts."
        ],
        "code": "module purge\nmodule load compiler/latest mpi/latest mkl/latest\necho $LD_LIBRARY_PATH",
        "notes": "Show how modules prevent DLL hell on shared supercomputing clusters."
    },
    {
        "title": "Intel oneAPI Ecosystem & Unified Architecture",
        "bullets": [
            "• The Vision: A single, open, standards-based programming model across CPUs, GPUs, FPGAs, and AI accelerators.",
            "• DPC++ / SYCL: Modern C++ abstraction allowing heterogeneous execution without proprietary vendor lock-in.",
            "• Level Zero API: Bare-metal direct-to-hardware interface for fine-grained device control and performance.",
            "• Enterprise Reality: 70% of enterprise servers already run Intel Xeon; oneAPI unleashes existing hardware."
        ],
        "notes": "Address the CUDA vs oneAPI question. Explain open standard SYCL vs proprietary vendor lock-in."
    },
    {
        "title": "Intel oneAPI Base vs HPC Toolkit Breakdown",
        "bullets": [
            "• Intel oneAPI Base Toolkit: Intel oneDPC++/C++ Compiler, oneMKL, oneDNN, oneDAL, and Intel VTune Profiler.",
            "• Intel oneAPI HPC Toolkit: Intel C/C++ Compiler Classic & Next-Gen (`icx`), Intel Fortran (`ifx`), Intel MPI.",
            "• Cluster Analysis: Intel Trace Analyzer and Collector (ITAC) and Intel Cluster Checker.",
            "• Activation: Initialized via `source /opt/intel/oneapi/setvars.sh`."
        ],
        "code": "source /opt/intel/oneapi/setvars.sh --force\nicx --version && mpirun --version",
        "notes": "Demonstrate sourcing setvars.sh and inspecting compiler versions."
    },
    {
        "title": "Day 1 Hands-On Lab & Student Milestones",
        "bullets": [
            "• Lab Challenge 1: CPU microarchitecture audit (`lscpu -C`, cache sizes, socket mappings).",
            "• Lab Challenge 2: AVX-512 vector flag inspection and compilation targeting Sapphire Rapids.",
            "• Lab Challenge 3: Automated passwordless Ed25519 SSH setup with ControlMaster multiplexing.",
            "• Lab Challenge 4: Bash automation script with `set -euo pipefail` and signal trap cleanup.",
            "• Milestone Evaluation: Complete Day 1 Official MCQ Evaluation Quiz (25 questions)."
        ],
        "notes": "Co-trainer Nikhil roams the room to fix terminal path issues. Shivam coordinates lab challenge execution and grading."
    }
]

# DAY 2 SLIDES
day2_slides = [
    {
        "title": "Day 2 Agenda: Parallel Computing & oneDAL",
        "bullets": [
            "• Shared Memory (OpenMP) vs Distributed Memory (MPI) Computing Paradigms.",
            "• Flynn's Taxonomy: MIMD Systems & Memory Topologies.",
            "• OpenMP Pragmas, Thread Teams, Scheduling Overheads & Thread Pinning.",
            "• Race Conditions, False Sharing & Cache Line Bouncing.",
            "• MPI Communicators, Collective Communications & Non-Blocking Requests.",
            "• Intel oneDAL & `scikit-learn-intelex`: Unleashing 30x ML Speedups on Xeon."
        ],
        "notes": "Set the stage for Day 2. Transition from hardware architectures to software parallelization models."
    },
    {
        "title": "Flynn's Taxonomy & Memory Architecture Paradigms",
        "bullets": [
            "• SISD: Single Instruction, Single Data (Classical single-core scalar processor).",
            "• SIMD: Single Instruction, Multiple Data (Vector registers: AVX-512, GPU streaming multiprocessors).",
            "• MISD: Multiple Instruction, Single Data (Fault-tolerant aerospace computing, systolic arrays).",
            "• MIMD: Multiple Instruction, Multiple Data (Modern multi-core clusters running OpenMP and MPI).",
            "• Memory Paradigms: Shared Memory (SMP/NUMA) vs Distributed Memory (Clusters with network interconnects)."
        ],
        "notes": "Draw Flynn's 2x2 matrix on the whiteboard. Explain why modern HPC clusters are hybrid: MIMD across nodes, MIMD across cores, SIMD inside each core."
    },
    {
        "title": "OpenMP: Shared-Memory Multithreading",
        "bullets": [
            "• The Fork-Join Execution Model: Master thread spawns a team of worker threads for parallel regions.",
            "• Core Directive: `#pragma omp parallel for` automatically distributes loop iterations across available cores.",
            "• Data Scoping: `shared(x)` (single variable accessed by all threads) vs `private(y)` (independent local copy per thread).",
            "• Reduction Clause: `reduction(+:sum)` eliminates race conditions with zero lock contention."
        ],
        "code": "#pragma omp parallel for reduction(+:pi_sum)\nfor (long i = 0; i < N; i++) {\n    pi_sum += compute_term(i);\n}",
        "notes": "Explain how reduction gives each thread its own accumulator, summing them into the master variable upon exit."
    },
    {
        "title": "OpenMP Loop Scheduling & Load Balancing",
        "bullets": [
            "• Static Scheduling: `schedule(static, chunk)` partitions loop iterations evenly at compile/launch time. Zero runtime overhead.",
            "• Dynamic Scheduling: `schedule(dynamic, chunk)` pulls work from a centralized queue. Ideal for non-uniform workloads.",
            "• Guided Scheduling: `schedule(guided, chunk)` starts with large chunks to minimize overhead, exponentially shrinking chunks.",
            "• The Trade-off: Static minimizes scheduling overhead; dynamic maximizes core utilization for irregular tasks."
        ],
        "notes": "Contrast static vs dynamic scheduling using a Mandelbrot set or ray tracing example."
    },
    {
        "title": "Synchronization: Critical, Atomic & Barriers",
        "bullets": [
            "• Data Race: Two concurrent threads access the same memory location, at least one write, with no synchronization.",
            "• `#pragma omp critical`: Instantiates a global software mutex. High overhead, serializes execution.",
            "• `#pragma omp atomic`: Maps directly to single hardware atomic assembly instructions (e.g. `LOCK XADD`). Minimal overhead.",
            "• `#pragma omp barrier`: Explicit synchronization point where all threads wait until the entire team arrives."
        ],
        "notes": "Show assembly difference between atomic (1 lock instruction) and critical (pthread mutex lock/unlock calls)."
    },
    {
        "title": "The Silent Killer: False Sharing & Cache Bouncing",
        "bullets": [
            "• The Hardware Reality: Modern CPUs do not fetch individual bytes; they fetch 64-byte Cache Lines.",
            "• False Sharing Defined: Two threads modify distinct variables that reside within the same 64-byte cache line.",
            "• The Pathology: Cache coherency protocols (MESI) repeatedly invalidate the cache line across cores.",
            "• The Result: Severe performance degradation (10x-50x slower) despite zero logical algorithmic data races!",
            "• The Solution: Pad variables or align to cache lines (`alignas(64)`)."
        ],
        "code": "struct PaddedCounter {\n    long value;\n    char padding[56]; // 64 bytes total\n};",
        "notes": "This is a favorite interview question. Draw two cores and a shared 64-byte cache line invalidating back and forth."
    },
    {
        "title": "Thread Affinity & NUMA Core Pinning",
        "bullets": [
            "• OS Thread Migration: Linux kernel scheduler moves threads across cores, destroying L1/L2 cache locality.",
            "• OpenMP Thread Pinning: `export OMP_PROC_BIND=close` keeps threads on contiguous cores to share L3 cache.",
            "• Intel KMP Affinity: `export KMP_AFFINITY=granularity=fine,compact,1,0` binds threads to physical cores.",
            "• Benchmark Impact: Proper pinning yields 15% to 35% performance boosts on multi-socket Xeon servers."
        ],
        "code": "export OMP_NUM_THREADS=$(nproc)\nexport OMP_PROC_BIND=close\nexport OMP_PLACES=cores",
        "notes": "Show how without affinity, threads hop between sockets, triggering remote UPI DRAM transactions."
    },
    {
        "title": "MPI: The Distributed Memory Programming Model",
        "bullets": [
            "• Distributed Memory Architecture: Each process possesses completely private virtual address space and memory.",
            "• Message Passing: Processes coordinate exclusively by sending and receiving discrete messages over the network.",
            "• Communicators: `MPI_COMM_WORLD` encompasses all active processes in the cluster allocation.",
            "• Process Identity: `MPI_Comm_rank` (unique ID from 0 to N-1) and `MPI_Comm_size` (total process count)."
        ],
        "code": "from mpi4py import MPI\ncomm = MPI.COMM_WORLD\nrank = comm.Get_rank()\nsize = comm.Get_size()",
        "notes": "Contrast OpenMP (threads sharing address space) with MPI (processes with isolated address spaces)."
    },
    {
        "title": "MPI Point-to-Point Communication & Deadlocks",
        "bullets": [
            "• Blocking Communication: `MPI_Send` and `MPI_Recv` block execution until buffer can be safely reused.",
            "• The Classic Deadlock: Rank 0 waits to receive from Rank 1; Rank 1 simultaneously waits to receive from Rank 0.",
            "• Deadlock Prevention: Pair Sends and Recvs in alternate order (even ranks send first, odd ranks receive first).",
            "• Non-Blocking Primitives: `MPI_Isend` and `MPI_Irecv` return immediately, verified later via `MPI_Wait`."
        ],
        "notes": "Draw the circular wait deadlock on the whiteboard. Explain why non-blocking MPI eliminates this risk."
    },
    {
        "title": "Overlapping Computation with Communication",
        "bullets": [
            "• The Latency Problem: Network transit across InfiniBand takes microseconds where CPU cycles sit completely wasted.",
            "• Asynchronous Execution: Launch non-blocking `MPI_Isend` / `MPI_Irecv` using zero-copy RDMA network hardware.",
            "• Simultaneous Compute: Execute intensive internal domain computations while network transfers proceed in background.",
            "• Synchronization: Call `MPI_Wait` only when boundary data is strictly required, hiding network latency completely."
        ],
        "code": "req = comm.Isend(sendbuf, dest=next_rank)\ncompute_local_domain() # Overlap\nreq.Wait() # Sync",
        "notes": "Show the timeline of computation overlapping communication. This is master-level HPC systems engineering."
    },
    {
        "title": "MPI Collective Communications: Broadcast & Allreduce",
        "bullets": [
            "• Broadcast (`MPI_Bcast`): Root process transmits an identical data buffer to all participating ranks.",
            "• Scatter (`MPI_Scatter`): Root splits a master array into disjoint slices, distributing one slice per rank.",
            "• Gather (`MPI_Gather`): Root collects individual slices from each rank and reconstructs the composite array.",
            "• Allreduce (`MPI_Allreduce`): Computes global reduction (SUM, MAX, MIN) and returns final result to every rank."
        ],
        "notes": "Explain why MPI collectives use optimized tree algorithms (O(log N)) rather than naive linear loops (O(N))."
    },
    {
        "title": "Intel oneDAL & Intel AI Analytics Toolkit",
        "bullets": [
            "• The Bottleneck: Standard Python machine learning packages (NumPy, Scikit-learn) rely on unvectorized Cython loops.",
            "• Intel oneDAL: High-performance C++ algorithmic library optimized for Xeon AVX-512 and AMX instructions.",
            "• Seamless Integration: Intel Extension for Scikit-learn (`scikit-learn-intelex`) accelerates stock Scikit-learn.",
            "• The Speedup Secret: Requires zero code refactoring; patching dynamically intercepts estimator instantiations."
        ],
        "code": "from sklearnex import patch_sklearn\npatch_sklearn()\nfrom sklearn.ensemble import RandomForestClassifier",
        "notes": "Show the 2-line patch. Emphasize that it works with existing student code with zero changes to model hyperparameters."
    },
    {
        "title": "Live Showdown: Stock Scikit-Learn vs Intel oneDAL",
        "bullets": [
            "• Support Vector Machines (SVM): 30x to 100x speedup via AVX-512 kernel evaluations and cache-blocked SMO.",
            "• Random Forest: 15x to 40x speedup via multi-threaded histogram-based split finding and vectorized binning.",
            "• k-Means Clustering: 20x to 50x speedup via vectorized Euclidean distance matrix calculations.",
            "• Principal Component Analysis (PCA): 10x to 25x speedup using oneMKL LAPACK eigensolvers."
        ],
        "notes": "Run the live benchmark in class. Show the terminal execution time dropping from 12 seconds to 0.4 seconds."
    },
    {
        "title": "Day 2 Hands-On Lab & Student Milestones",
        "bullets": [
            "• Lab Challenge 1: OpenMP multi-threaded parallel matrix multiplication with thread scaling benchmark.",
            "• Lab Challenge 2: False sharing diagnosis and padding elimination in C++.",
            "• Lab Challenge 3: MPI Ring communication pipeline using `mpi4py`.",
            "• Lab Challenge 4: Intel `sklearnex` speedup benchmark showdown on 500k-sample dataset.",
            "• Milestone Evaluation: Complete Day 2 Official MCQ Evaluation Quiz (25 questions)."
        ],
        "notes": "Floor trainer assists with mpi4py execution and OpenMP compiler flags (-fopenmp)."
    }
]

# DAY 3 SLIDES
day3_slides = [
    {
        "title": "Day 3 Agenda: Deep Learning on Clusters",
        "bullets": [
            "• Deep Learning Compute Anatomy: GEMM Arithmetic Intensity & The Memory Wall.",
            "• Precision Formats: FP32 vs FP16 vs Bfloat16 vs INT8.",
            "• Intel oneDNN: JIT Operator Fusion & Cache-Resident Neural Primitives.",
            "• TensorFlow-MKL: Tuning `intra_op` and `inter_op` Parallelism.",
            "• Slurm Workload Manager: Architecture, Daemons & `#SBATCH` Scripts.",
            "• Horovod & Ring-AllReduce: Bandwidth-Optimal Multi-Node Training."
        ],
        "notes": "Transition from traditional ML to modern deep neural networks on supercomputing clusters."
    },
    {
        "title": "Deep Learning Compute Anatomy: The GEMM Matrix",
        "bullets": [
            "• General Matrix Multiply (GEMM): Over 85% of deep learning FLOPs reside in matrix multiplications and convolutions.",
            "• Arithmetic Intensity: Ratio of floating-point operations performed per byte of DRAM memory transferred (FLOPs/Byte).",
            "• Compute-Bound Operations: Large matrix multiplications with high arithmetic intensity, saturating vector execution units.",
            "• Memory-Bound Operations: Activations, LayerNorm, and Softmax with low arithmetic intensity, saturating DRAM bandwidth."
        ],
        "notes": "Explain why deep learning is fundamentally an exercise in linear algebra acceleration."
    },
    {
        "title": "Numerical Precision: Why Bfloat16 Rules AI",
        "bullets": [
            "• FP32 (Single Precision): 1 sign bit, 8 exponent bits, 23 mantissa bits (Standard IEEE scientific precision).",
            "• FP16 (Half Precision): 1 sign bit, 5 exponent bits, 10 mantissa bits (Narrow dynamic range, prone to underflow).",
            "• Bfloat16 (Brain Floating Point): 1 sign bit, 8 exponent bits, 7 mantissa bits (Matches FP32 dynamic range in 16 bits!).",
            "• Bandwidth & Memory Savings: Bfloat16 cuts memory bandwidth traffic by 50% without requiring loss scaling."
        ],
        "notes": "Draw the bit allocations of FP32 vs FP16 vs BF16 on the board. Show why BF16 never underflows during backprop."
    },
    {
        "title": "Intel oneDNN: Operator Fusion & JIT Primitives",
        "bullets": [
            "• Unoptimized Execution: Convolution writes to DRAM -> BiasAdd reads from DRAM -> ReLU writes to DRAM.",
            "• The DRAM Latency Penalty: Repeatedly round-tripping intermediate tensors wastes 80% of execution time.",
            "• oneDNN Operator Fusion: Fuses Conv + Bias + Activation into a single continuous kernel loop.",
            "• Cache Residency: Intermediate activations remain in ultra-fast L1/L2 cache, eliminating DRAM traffic."
        ],
        "code": "export TF_ENABLE_ONEDNN_OPTS=1\n# Activates oneDNN graph rewrite passes automatically",
        "notes": "Show the visual diagram of fused operators vs separate operators."
    },
    {
        "title": "Tuning TensorFlow Thread Pools on Xeon",
        "bullets": [
            "• `intra_op_parallelism_threads`: Threads collaborating on a single tensor operation (Set equal to physical cores per socket).",
            "• `inter_op_parallelism_threads`: Independent operations executed concurrently in computation graph (Typically set to 2).",
            "• OpenMP Affinity: `KMP_AFFINITY=granularity=fine,compact,1,0` binds threads to adjacent cores.",
            "• Memory Allocators: Utilizing Google `tcmalloc` or `jemalloc` to eliminate multi-threaded glibc heap locks."
        ],
        "code": "import tensorflow as tf\ntf.config.threading.set_intra_op_parallelism_threads(16)\ntf.config.threading.set_inter_op_parallelism_threads(2)",
        "notes": "Demonstrate the dramatic performance jump when setting intra_op threads properly."
    },
    {
        "title": "Intel Hardware Accelerators: Ponte Vecchio & Gaudi",
        "bullets": [
            "• Intel Data Center GPU Max (Ponte Vecchio): 128 GB HBM2e memory delivering 3.2 TB/s bandwidth with Xe Matrix Extensions (XMX).",
            "• Habana Gaudi 2 / Gaudi 3: Specialized deep learning ASICs engineered for massive transformer workloads.",
            "• Gaudi Silicon Architecture: Matrix Multiplication Engines (MME) paired with programmable Tensor Processing Cores (TPC).",
            "• On-Chip Networking: 24 integrated 100-Gigabit Ethernet (RoCE v2) ports directly on-die for seamless all-to-all scale-out."
        ],
        "notes": "Highlight Gaudi's unique on-chip 100GbE networking. No PCIe bottleneck for cluster scaling."
    },
    {
        "title": "Why HPC Clusters Require Slurm Workload Manager",
        "bullets": [
            "• Multi-User Cluster Challenges: 200 researchers competing for 64 compute nodes cannot just SSH and run `python train.py`.",
            "• Slurm (Simple Linux Utility for Resource Management): The gold-standard workload manager across 60%+ of TOP500 clusters.",
            "• Core Functions: Arbitrates resource access, queues competing jobs, enforces fair-share policies, and monitors execution health.",
            "• Daemons: `slurmctld` (Central manager daemon), `slurmd` (Node compute daemon), `slurmdbd` (Database accounting daemon)."
        ],
        "notes": "Explain why running workloads directly on login nodes gets student accounts suspended by sysadmins."
    },
    {
        "title": "Anatomy of a Production Slurm Batch Script",
        "bullets": [
            "• `#SBATCH --job-name`: Unique descriptive identifier for the scheduled job.",
            "• `#SBATCH --nodes=4`: Number of discrete physical server nodes reserved.",
            "• `#SBATCH --ntasks-per-node=2`: Number of tasks (MPI ranks) spawned per node.",
            "• `#SBATCH --cpus-per-task=16`: Number of CPU hardware threads allocated per task.",
            "• `#SBATCH --time=02:00:00`: Hard wall-clock limit; job killed if exceeded."
        ],
        "code": "#!/bin/bash\n#SBATCH --job-name=tf_hpc\n#SBATCH --nodes=2\n#SBATCH --ntasks-per-node=1\n#SBATCH --cpus-per-task=16\n#SBATCH --output=logs_%j.out\nsrun python train.py",
        "notes": "Walk through every line of the Slurm batch script. Explain what %j means (Job ID substitution)."
    },
    {
        "title": "Slurm CLI Commands Mastery",
        "bullets": [
            "• `sbatch script.slurm`: Submits batch job to queue and returns Job ID immediately.",
            "• `squeue`: Displays active, queued, running, and completing jobs across partitions.",
            "• `sinfo`: Queries node availability, partition limits, and idle vs allocated sockets.",
            "• `scancel <job_id>`: Aborts running job and releases hardware resources.",
            "• `salloc --nodes=1 --pty bash`: Spawns interactive shell on a compute node for real-time debugging."
        ],
        "notes": "Demonstrate submitting, inspecting, and cancelling jobs live on the terminal."
    },
    {
        "title": "Distributed DL Bottleneck: Parameter Server vs Ring-AllReduce",
        "bullets": [
            "• Parameter Server Bottleneck: All workers transmit gradients to central servers; network bandwidth scales as O(N).",
            "• Ring-AllReduce Architecture: Workers arranged in a logical ring; each node communicates only with immediate neighbors.",
            "• Constant Communication Volume: Total data transferred per node is 2 * (N - 1) / N * M, asymptotically approaching 2M.",
            "• Scalability: Bandwidth per node remains CONSTANT regardless of whether scaling across 4 nodes or 4,000 nodes!"
        ],
        "notes": "Draw the Ring-AllReduce diagram on the board: Scatter-Reduce phase followed by AllGather phase."
    },
    {
        "title": "Horovod: Bandwidth-Optimal Distributed Training",
        "bullets": [
            "• Origins: Developed by Uber to eliminate distributed TensorFlow parameter server bottlenecks.",
            "• Network Backends: Built on top of MPI (OpenMPI / Intel MPI) and NCCL / Intel oneCCL.",
            "• Tensor Fusion: Batches thousands of small gradient tensors into a single ring buffer to maximize network saturation.",
            "• Minimal Code Overhead: Requires fewer than 6 lines of code modification to convert single-GPU code to multi-node."
        ],
        "code": "import horovod.tensorflow as hvd\nhvd.init()\nopt = hvd.DistributedOptimizer(tf.keras.optimizers.Adam(lr * hvd.size()))",
        "notes": "Highlight how clean Horovod's API is compared to manual distributed orchestrators."
    },
    {
        "title": "Horovod Code Integration Best Practices",
        "bullets": [
            "• Linear Scaling Rule: Scale base learning rate by `hvd.size()` to compensate for larger effective global batch size.",
            "• Weight Synchronization: `hvd.callbacks.BroadcastGlobalVariablesCallback(0)` broadcasts initial weights from Rank 0.",
            "• Dataset Sharding: `dataset.shard(num_shards=hvd.size(), index=hvd.rank())` prevents duplicate data processing.",
            "• Checkpoint Isolation: Guard disk writes with `if hvd.rank() == 0:` to prevent multi-worker file corruption."
        ],
        "notes": "Warn students: If all ranks try to save checkpoints to the same file, the file will be corrupted."
    },
    {
        "title": "Day 3 Hands-On Lab & Student Milestones",
        "bullets": [
            "• Lab Challenge 1: TensorFlow-MKL operator benchmarking with `TF_ENABLE_ONEDNN_OPTS=1`.",
            "• Lab Challenge 2: Authoring a multi-node Slurm batch submission script with `#SBATCH` directives.",
            "• Lab Challenge 3: Horovod distributed training script with dataset sharding and Rank 0 checkpointing.",
            "• Lab Challenge 4: Slurm queue monitoring and log file inspection.",
            "• Milestone Evaluation: Complete Day 3 Official MCQ Evaluation Quiz (25 questions)."
        ],
        "notes": "Floor trainer monitors student Slurm scripts for syntax errors. Shivam guides Horovod distributed scaling."
    }
]

# DAY 4 SLIDES
day4_slides = [
    {
        "title": "Day 4 Agenda: Distributed Scaling & VTune Profiling",
        "bullets": [
            "• Multi-Node Slurm Cluster Workflows & Interconnect Scaling.",
            "• Scaling Metrics: Strong Scaling, Weak Scaling & Parallel Efficiency.",
            "• Hardware Performance Monitoring Units (PMU) & Event Counters.",
            "• Intel VTune Profiler Architecture & Top-Down Microarchitecture Analysis (TMAM).",
            "• Front-End Bound, Bad Speculation, Back-End Bound & Retiring.",
            "• Memory Access Analysis, NUMA Remote Traffic & False Sharing Profiling.",
            "• The Roofline Model: Calculating Operational Intensity (FLOPs/Byte)."
        ],
        "notes": "Transition from building distributed models to engineering extreme performance and profiling."
    },
    {
        "title": "Measuring Parallel Scaling Efficiency",
        "bullets": [
            "• Speedup Formula: S(N) = T_1 / T_N (Execution time on 1 node divided by execution time on N nodes).",
            "• Parallel Efficiency Formula: E = S(N) / N * 100% (Percentage of ideal linear scaling achieved).",
            "• Ideal Linear Scaling: E = 100% (Doubling nodes halves execution time).",
            "• The Scaling Cliff: As node count grows, communication overhead and AllReduce barriers erode efficiency."
        ],
        "notes": "Give a quick math problem: 'If 1 node takes 100s, and 4 nodes take 30s, what is efficiency?' S=3.33, E=83.3%."
    },
    {
        "title": "The Straggler Effect in Distributed Clusters",
        "bullets": [
            "• Synchronous AllReduce: Every worker must reach the synchronization barrier before the next training step can start.",
            "• The Straggler: A single throttled node (due to thermal throttling, bad memory channel, or OS jitter) delays the entire cluster.",
            "• Cluster Degradation: On a 128-node cluster, 1 straggler forces 127 healthy nodes to sit 100% idle at the barrier.",
            "• Mitigation Strategies: System monitoring via IPMI, node draining, and gradient compression."
        ],
        "notes": "Explain why cluster health is dictated by the slowest link. Draw the barrier timeline on the whiteboard."
    },
    {
        "title": "Performance Engineering: The Profiling Philosophy",
        "bullets": [
            "• The Golden Rule of Optimization: 'Never optimize without profiling first.' Intuition about bottlenecks is usually wrong.",
            "• Coarse vs Fine Profiling: High-level timers (`time`, `chrono`) identify slow functions; PMU profilers identify WHY.",
            "• Overhead Constraints: Profilers must sample with minimal intrusion (<2% overhead) to avoid distorting real behavior.",
            "• Enterprise Tool: Intel VTune Profiler is the industry standard across aerospace, AI, and algorithmic trading."
        ],
        "notes": "Quote Donald Knuth: 'Premature optimization is the root of all evil.' Teach students to measure with precision."
    },
    {
        "title": "Hardware Performance Monitoring Units (PMU)",
        "bullets": [
            "• On-Chip Hardware Counters: Dedicated registers in CPU silicon that count microarchitectural events in real time.",
            "• Core PMU Events: `CPU_CLK_UNHALTED` (core cycles), `INST_RETIRED` (instructions executed), `L3_CACHE_MISS`.",
            "• Event-Based Sampling (EBS): VTune programs PMU to trigger a hardware interrupt every N events, capturing instruction pointers.",
            "• Zero Code Intrusion: Profiles un-instrumented C, C++, Fortran, and Python binaries directly in assembly."
        ],
        "notes": "Explain how PMU registers work in silicon without slowing down the application."
    },
    {
        "title": "Top-Down Microarchitecture Analysis (TMAM)",
        "bullets": [
            "• The TMAM Methodology: Developed by Ahmad Yasin at Intel to diagnose CPU pipeline slot utilization.",
            "• Pipeline Slots: Every cycle, an out-of-order execution pipeline can issue a fixed number of micro-operations (uOps).",
            "• The 4 Top-Level Categories:",
            "  1. Retiring: uOps that successfully completed and committed their results (Useful work!).",
            "  2. Bad Speculation: uOps wasted on incorrectly predicted branches.",
            "  3. Front-End Bound: Pipeline starved because instructions could not be fetched/decoded fast enough.",
            "  4. Back-End Bound: Pipeline stalled waiting for data from memory or overloaded execution ports."
        ],
        "notes": "Draw the 4 TMAM quadrants on the whiteboard. Explain that Retiring > 50% is the goal of optimization."
    },
    {
        "title": "Diagnosing Back-End Bound: Memory vs Core",
        "bullets": [
            "• Memory Bound: Execution units sit idle waiting for data to arrive from L1, L2, L3 cache, or main DRAM.",
            "• DRAM Latency: Accessing main memory takes ~200-300 cycles where core pipelines sit completely stalled.",
            "• Core Bound: Execution units are stalled due to port contention, long latency dividers, or un-vectorized scalar math.",
            "• Remedy for Memory Bound: Loop tiling (cache blocking), data alignment, and converting AoS to SoA."
        ],
        "notes": "Show how memory latency creates the 'Memory Wall' inside individual CPU cores."
    },
    {
        "title": "Bad Speculation & Front-End Bottlenecks",
        "bullets": [
            "• Branch Mispredictions: When CPU branch predictor guesses wrong, all speculative in-flight instructions are flushed.",
            "• The Flush Penalty: Flushing an out-of-order execution pipeline costs 15 to 20 cycles per misprediction.",
            "• Front-End Latency: Instruction cache (ICache) misses and instruction TLB (iTLB) misses stall the fetch engine.",
            "• Remedy: Eliminate unpredictable conditional branches inside hot loops; use branchless arithmetic or lookup tables."
        ],
        "notes": "Demonstrate branchless code: replacing `if (val > 0) sum += val;` with branchless bit manipulation."
    },
    {
        "title": "Intel VTune CLI Command Mastery",
        "bullets": [
            "• Collecting Hotspots: `vtune -collect hotspots -result-dir ./vtune_out -- python train.py`",
            "• Collecting Microarchitecture Exploration: `vtune -collect uarch-exploration -result-dir ./vtune_uarch -- ./app`",
            "• Collecting Memory Access: `vtune -collect memory-access -result-dir ./vtune_mem -- ./app`",
            "• Generating Terminal Reports: `vtune -report summary -result-dir ./vtune_out`"
        ],
        "code": "vtune -collect hotspots -result-dir ./hotspots_out -- python compute.py\nvtune -report summary -result-dir ./hotspots_out",
        "notes": "Show VTune running from the command line without needing a heavy GUI window."
    },
    {
        "title": "Interpreting Flame Graphs & Hotspot Call Stacks",
        "bullets": [
            "• Flame Graphs: Hierarchical visualization of sampled function call stacks.",
            "• X-Axis: Represents proportion of total CPU time spent in each function (wider box = bigger bottleneck).",
            "• Y-Axis: Stack depth (top boxes are child functions called by parent functions below).",
            "• Instant Diagnosis: Look for the widest 'flat plateaus' on the graph; that is where your CPU cycles are burning!"
        ],
        "notes": "Show how to read a Flame Graph in 5 seconds to pinpoint the exact bottleneck function."
    },
    {
        "title": "Memory Access Profiling: Remote NUMA Hops",
        "bullets": [
            "• VTune Memory Access Analysis: Tracks DRAM bandwidth saturation and cross-socket UPI interconnect traffic.",
            "• Remote DRAM Access Metric: High percentages indicate threads are accessing memory attached to remote NUMA nodes.",
            "• Cache Line Contention: Pinpoints false sharing down to the exact line of C++/Python code.",
            "• Optimization Proof: Re-running VTune after applying `numactl` shows remote memory traffic dropping to 0%."
        ],
        "notes": "Demonstrate the 'before and after' VTune report proving remote DRAM hops dropped to zero."
    },
    {
        "title": "The Roofline Model: Calculating Operational Intensity",
        "bullets": [
            "• 2D Visual Performance Boundary: Plots Performance (GFLOP/s) vs Operational Intensity (FLOPs/Byte).",
            "• The Ceiling: Peak floating-point throughput of the processor hardware.",
            "• The Sloped Boundary: Peak memory bandwidth (GB/s) of the hardware.",
            "• Knee Point: The threshold intensity where an application transitions from memory-bound to compute-bound.",
            "• Diagnostic Power: Reveals whether rewriting code with SIMD vs optimizing cache reuse will yield speedups."
        ],
        "notes": "Draw the Roofline chart on the whiteboard. Plot matrix multiplication vs vector addition on the curve."
    },
    {
        "title": "Data Layout Transformation: AoS vs SoA",
        "bullets": [
            "• Array of Structures (AoS): `struct Point { float x, y, z; } points[N];`",
            "  - Memory Layout: `x0 y0 z0 x1 y1 z1 x2 y2 z2...` (Strided memory access, impossible to load aligned SIMD).",
            "• Structure of Arrays (SoA): `struct Points { float x[N]; float y[N]; float z[N]; };`",
            "  - Memory Layout: `x0 x1 x2 x3...` (Contiguous unit-stride memory access).",
            "• Vector Advantage: SoA allows single-instruction aligned 512-bit vector loads (`_mm512_load_ps`), yielding 4x speedups."
        ],
        "notes": "This is a classic systems interview question at Intel, AMD, and Nvidia. Draw the memory layouts side-by-side."
    },
    {
        "title": "Day 4 Hands-On Lab & Student Milestones",
        "bullets": [
            "• Lab Challenge 1: Profiling an intentional CPU bottleneck script with VTune Hotspots.",
            "• Lab Challenge 2: Extracting TMAM metrics (Front-End Bound vs Back-End Bound) via VTune CLI.",
            "• Lab Challenge 3: Profiling memory access and diagnosing false sharing with VTune.",
            "• Lab Challenge 4: Refactoring AoS data structures to SoA and verifying speedup.",
            "• Milestone Evaluation: Complete Day 4 Official MCQ Evaluation Quiz (25 questions)."
        ],
        "notes": "Guide students through VTune summary reports. Reinforce how to explain VTune findings in technical interviews."
    }
]

# DAY 5 SLIDES
day5_slides = [
    {
        "title": "Day 5 Agenda: Generative AI & LLMs on Intel HPC",
        "bullets": [
            "• Large Language Model (LLM) Computational Anatomy & Transformer Attention.",
            "• The Two Phases: Prefill Phase (Compute-Bound) vs Decode Phase (Memory-Bound).",
            "• The Memory Bandwidth Bottleneck: Why TB/s Caps Token Generation Speed.",
            "• Intel Hardware for LLMs: 4th/5th Gen Xeon with AMX & Habana Gaudi 2/3.",
            "• Intel OpenVINO Toolkit: Model Optimization, INT4 NNCF Quantization & KV-Caching.",
            "• Parameter-Efficient Fine-Tuning (PEFT): Mathematical Derivation of LoRA & QLoRA.",
            "• Distributed Fine-Tuning with DeepSpeed ZeRO & Serving with FastAPI."
        ],
        "notes": "The Grand Finale! Bring together hardware, parallelism, distributed scaling, and modern Generative AI."
    },
    {
        "title": "Transformer Anatomy: The Computational Engine",
        "bullets": [
            "• Self-Attention Formula: Attention(Q, K, V) = softmax((Q * K^T) / sqrt(d_k)) * V.",
            "• Computational Complexity: Naive self-attention scales as O(N^2) in sequence length N.",
            "• Projection GEMMs: Query, Key, Value, and Output projection matrices dominate FLOP count.",
            "• Multi-Layer Stacking: 32 to 80 transformer layers sequentially propagating contextual embeddings."
        ],
        "notes": "Walk through the Attention equation on the board. Explain Q, K, and V projections as matrix multiplications."
    },
    {
        "title": "The Two Phases of LLM Inference",
        "bullets": [
            "• Phase 1: Prefill Phase (Prompt Processing)",
            "  - Computes all input prompt tokens in parallel in a single forward pass.",
            "  - Compute-Bound: Matrix multiplications with high arithmetic intensity; saturates AMX/GPU systolic engines.",
            "• Phase 2: Decode Phase (Autoregressive Token Generation)",
            "  - Generates tokens one-by-one sequentially; each token requires a full forward pass.",
            "  - Memory-Bandwidth Bound: Arithmetic intensity ~1 FLOP/Byte; throughput strictly capped by memory bandwidth (TB/s)!"
        ],
        "notes": "This distinction is essential. Draw the timeline: big initial compute spike (Prefill), followed by memory-bound token stream (Decode)."
    },
    {
        "title": "The Memory Bandwidth Wall in Token Generation",
        "bullets": [
            "• The Physics: To generate 1 token from an 8-Billion parameter FP16 model (16 GB weights), the CPU must stream all 16 GB from DRAM!",
            "• Arithmetic Intensity: 2 FLOPs per parameter / 2 Bytes per parameter = 1 FLOP / Byte.",
            "• The Speed Cap: If server memory bandwidth is 100 GB/s, maximum theoretical speed is 100 GB/s / 16 GB = 6.25 tokens/second!",
            "• The Implication: Faster compute cores do NOT speed up generation; only HIGHER MEMORY BANDWIDTH or WEIGHT QUANTIZATION can!"
        ],
        "notes": "Derive this formula live on the board. Students will have an 'aha!' moment seeing why memory bandwidth rules AI."
    },
    {
        "title": "The KV-Cache Bottleneck & Memory Footprint",
        "bullets": [
            "• Redundant Computation: Without caching, generating token t requires recomputing Key and Value projections for all past tokens.",
            "• KV-Cache: Stores computed Key and Value projection tensors in memory, reducing per-token computation from O(T^2) to O(T).",
            "• Memory Footprint: Memory = 2 * layers * kv_heads * head_dim * context_length * precision * batch_size.",
            "• The Consequence: At 32k or 128k context lengths, KV-cache easily consumes tens of gigabytes, exceeding base model weights!"
        ],
        "notes": "Explain why KV-cache causes Out-Of-Memory errors during long document processing or high concurrent user loads."
    },
    {
        "title": "Architectural Solutions: GQA & FlashAttention",
        "bullets": [
            "• Multi-Head Attention (MHA): 32 Query heads paired with 32 distinct Key/Value heads (Massive KV-cache).",
            "• Grouped-Query Attention (GQA): 32 Query heads share 8 Key/Value heads (4x reduction in KV-cache size!).",
            "• Used by Modern LLMs: Llama 3, Mistral, and Qwen adopt GQA to maximize decode throughput.",
            "• FlashAttention: Uses online softmax tiling in SRAM to compute exact attention without materializing N x N matrix in DRAM."
        ],
        "notes": "Show how GQA cuts memory bandwidth by 4x without sacrificing model conversational quality."
    },
    {
        "title": "Intel Hardware for LLMs: Xeon AMX & Gaudi",
        "bullets": [
            "• 4th/5th Gen Intel Xeon Scalable: Intel AMX accelerates Bfloat16 matrix multiplication in Prefill and LoRA fine-tuning.",
            "• Intel Xeon Max Series: Integrates 64 GB on-package HBM2e memory delivering 1 TB/s bandwidth for memory-bound decoding.",
            "• Habana Gaudi 2 / Gaudi 3: 128 GB HBM2e (2.45 to 3.7 TB/s bandwidth) tailored for massive LLM training and serving.",
            "• Cost Advantage: Fine-tuning and serving on enterprise Xeon CPUs eliminates dependency on scarce, costly GPU cloud instances."
        ],
        "notes": "Show how enterprises leverage existing Xeon servers to run local LLMs securely behind corporate firewalls."
    },
    {
        "title": "Intel OpenVINO Toolkit for LLM Optimization",
        "bullets": [
            "• Open Visual Inference and Neural Network Optimization: Intel's premier cross-platform AI deployment runtime.",
            "• Architecture: Model Optimizer converts PyTorch/ONNX models into OpenVINO Intermediate Representation (.xml + .bin).",
            "• C++ Runtime Engine: Highly optimized execution pipelines targeting AVX-512, AMX, Intel GPUs, and NPUs.",
            "• Hugging Face Integration: `optimum-intel` allows loading OpenVINO models with native `transformers` pipelines in 1 line."
        ],
        "code": "from optimum.intel.openvino import OVModelForCausalLM\nmodel = OVModelForCausalLM.from_pretrained('model_dir', export=True)",
        "notes": "Show how optimum-intel makes OpenVINO transparent to anyone familiar with Hugging Face."
    },
    {
        "title": "INT4 Weight-Only Quantization (WOQ) with NNCF",
        "bullets": [
            "• Neural Network Compression Framework (NNCF): Intel's framework for state-of-the-art model quantization.",
            "• Weight-Only Quantization: Quantizes model weights from 16-bit floats to 4-bit integers while activations remain in float.",
            "• Memory Traffic Reduction: Reduces model footprint by 75% (8B model drops from 16 GB to 4.5 GB!).",
            "• The Direct Speedup: 4x reduction in DRAM memory traffic yields 2.5x to 3.8x faster token generation with near-zero perplexity loss."
        ],
        "code": "from nncf import compress_weights\ncompressed_model = compress_weights(model, mode=CompressWeightsMode.INT4_SYM)",
        "notes": "Show the math: 16 GB streamed -> 4.5 GB streamed. Speed increases almost 4x because decoding is memory-bandwidth bound."
    },
    {
        "title": "Benchmarking LLM Inference Performance",
        "bullets": [
            "• Time-To-First-Token (TTFT): Time elapsed between submitting prompt and receiving first output token (Prefill latency).",
            "• Inter-Token Latency (ITL): Time elapsed between consecutive generated tokens (Human reading fluency requires >15 TPS).",
            "• Tokens-Per-Second (TPS): Throughput metric = Total generated tokens / Total generation time.",
            "• First-Token vs Streamed: Streaming tokens over Server-Sent Events (SSE) masks perceived latency completely."
        ],
        "notes": "Explain why streaming tokens makes user interfaces feel instantaneous even on CPU inference."
    },
    {
        "title": "Parameter-Efficient Fine-Tuning: LoRA Mathematics",
        "bullets": [
            "• The Problem: Full fine-tuning of an 8B model requires 80+ GB VRAM to store optimizer states and gradients.",
            "• Low-Rank Adaptation (LoRA): Freezes pre-trained weight matrix W_0 and injects trainable low-rank decomposition matrices.",
            "• Mathematical Formulation: W = W_0 + B * A, where B in R^(d x r) and A in R^(r x k) with rank r << min(d, k).",
            "• Parameter Reduction: Reduces trainable parameters by over 99% (e.g. from 16.7M weights down to 131k weights for d=4096, r=16)."
        ],
        "notes": "Derive LoRA on the whiteboard. Show how rank r=16 captures the task-specific subspace."
    },
    {
        "title": "QLoRA & Distributed Fine-Tuning with DeepSpeed",
        "bullets": [
            "• QLoRA: Quantizes frozen base model to 4-bit NormalFloat (NF4), backpropagates gradients into 16-bit LoRA adapter matrices.",
            "• Double Quantization: Quantizes the quantization constants, saving an additional 0.37 bits per parameter.",
            "• DeepSpeed ZeRO: Partitions optimizer states (Stage 1), gradients (Stage 2), and parameters (Stage 3) across cluster nodes.",
            "• Scaling: Enables fine-tuning 70B parameter models on modest multi-node cluster allocations."
        ],
        "notes": "Explain how QLoRA democratized LLM fine-tuning across academia and enterprise."
    },
    {
        "title": "Building a Production LLM REST Microservice",
        "bullets": [
            "• FastAPI + Uvicorn: Asynchronous, high-throughput ASGI web framework built on Python asyncio.",
            "• Streaming Token Generation: Using `StreamingResponse` with Server-Sent Events (SSE) to stream tokens in real time.",
            "• Pydantic Schema Validation: Enforcing strict JSON request validation (prompt, temperature, top_p, max_tokens).",
            "• Capstone Project Architecture: High-performance, self-contained local AI assistant ready for B.Tech project defense."
        ],
        "code": "@app.post('/generate')\nasync def generate(req: PromptRequest):\n    return StreamingResponse(stream_llm(req.prompt), media_type='text/event-stream')",
        "notes": "Walk through the FastAPI server code. Show how it powers their final-year capstone projects."
    },
    {
        "title": "Final Capstone Blueprint & Course Graduation",
        "bullets": [
            "• Capstone Architecture: End-to-end HPC pipeline combining data loading, Slurm scheduling, Intel optimization, and API serving.",
            "• Placement Interview Playbook: How to articulate NUMA, AVX-512, AMX, Slurm, and OpenVINO in technical interview rounds.",
            "• Career Pathways: High Performance Computing Systems Engineer, AI Performance Architect, Distributed Infrastructure Engineer.",
            "• Course Conclusion: Congratulations GLA University B.Tech Engineers! Formal course completion & evaluation."
        ],
        "notes": "Inspire the students. Connect everything they learned to real-world job roles and capstone project success."
    }
]

# Build all 5 decks
create_deck(1, "Fundamentals of HPC, Linux & oneAPI", "Intel Xeon, NEC SX-Aurora TSUBASA, Shell Automation & oneAPI Toolkits", day1_slides)
create_deck(2, "Traditional ML & Parallel Computing", "OpenMP Multithreading, MPI Distributed Clusters & Intel oneDAL Acceleration", day2_slides)
create_deck(3, "Deep Learning on HPC & Slurm", "Intel oneDNN, Slurm Cluster Scheduling, Habana Gaudi & Horovod Scaling", day3_slides)
create_deck(4, "Distributed AI & VTune Profiling", "Multi-Node Slurm, Hardware PMU Counters & Top-Down Microarchitecture Profiling", day4_slides)
create_deck(5, "Generative AI & LLMs on Intel HPC", "Transformer Compute, Memory Bandwidth Bottlenecks, OpenVINO & Distributed Fine-Tuning", day5_slides)

print("\n[SUCCESS] All 5 Official Edulateral PowerPoint Presentations generated successfully!")
