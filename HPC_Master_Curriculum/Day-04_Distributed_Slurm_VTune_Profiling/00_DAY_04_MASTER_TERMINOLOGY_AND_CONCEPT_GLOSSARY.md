# 📚 DAY 4: MASTER TERMINOLOGY & CONCEPT GLOSSARY
## Distributed AI Training & Profiling Optimization with Intel VTune
**Course Code:** `GLA-HPC-BCSG701` | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Session:** Day 4 (Strictly 3 Hours / 180 Minutes)  
**Primary Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 📌 Master Vocabulary & Performance Engineering Mechanics (Terms #1 – #36)

### 1. Performance Profiling vs. Benchmarking
* **Benchmarking**: Measures the gross wall-clock runtime of an entire application (e.g., "The model took 45 minutes to train"). It tells you *that* a program is slow, but not *why*.
* **Profiling**: Introspects execution at the function, loop, and microarchitectural level to identify specific hardware bottlenecks (e.g., "Function `gemm_kernel` consumes 68% of CPU cycles, and 45% of pipeline slots are stalled on L3 cache misses").

### 2. Sampling vs. Instrumentation
* **Instrumentation**: Modifying source code or binary instructions to insert timing probes. High accuracy, but introduces observer effect (measurement overhead can alter application behavior).
* **Statistical Sampling**: The profiler queries hardware Performance Monitoring Unit (PMU) counters at periodic intervals (e.g., every 1 ms). Negligible overhead (< 2%), ideal for production HPC clusters.

### 3. Performance Monitoring Unit (PMU)
* **Definition**: Dedicated silicon registers inside modern Intel Xeon CPUs that count low-level hardware events: CPU clock cycles, retired instructions, branch mispredictions, cache misses (L1, L2, L3), and bus transactions.

### 4. Intel VTune Profiler
* **Definition**: An industry-leading performance analysis tool from the Intel oneAPI HPC Toolkit that collects PMU hardware events to analyze application performance across CPUs, GPUs, and cluster nodes.

### 5. Top-Down Microarchitecture Analysis Method (TMAM)
* **Definition**: A systematic, hierarchical methodology created by Intel to categorize CPU pipeline inefficiencies into four primary quadrants:
  1. **Frontend Bound**
  2. **Bad Speculation**
  3. **Backend Bound**
  4. **Retiring (Useful Work)**

### 6. Retiring (Useful Pipeline Slots)
* **Definition**: The percentage of CPU pipeline slots devoted to processing instructions that actually finish and commit their architectural results (e.g., a pure compute loop).
* **Target**: Production compute-bound HPC applications aim for $\ge 60\%$ Retiring slots.

### 7. Frontend Bound
* **Definition**: The CPU execution pipeline is starved of instructions because the instruction fetch and decode units cannot deliver micro-operations (uOps) fast enough.
* **Causes**: Instruction Cache (ICache) misses, Instruction Translation Lookaside Buffer (ITLB) misses, complex macro-instruction decoding delays.

### 8. Bad Speculation
* **Definition**: The CPU spent clock cycles speculatively executing instructions along branch paths that were ultimately not taken due to branch mispredictions.
* **HPC Fix**: Replace unpredictable dynamic `if/else` conditions inside hot computational loops with branchless conditional moves (`CMOV`) or mathematical lookup masks.

### 9. Backend Bound (Core Bound vs. Memory Bound)
* **Definition**: The execution pipeline has instructions ready to execute, but cannot issue them because execution resources are stalled. Divided into:
  * **Core Bound**: Execution divider/multiplier units are fully saturated, or execution port contention occurs.
  * **Memory Bound**: Pipeline is stalled waiting for data to arrive from L1, L2, L3 caches or DDR5 main memory.

### 10. Memory Access Analysis (VTune)
* **Definition**: A specialized VTune analysis mode that measures memory bandwidth saturation, Average Latency per Access, and cache hit/miss ratios across L1d, L2, and L3 caches.

### 11. Memory Wall
* **Definition**: The physical performance disparity between fast CPU computation (~0.3 ns clock cycles) and slow main memory retrieval (~65–80 ns DRAM latency).
* **HPC Solution**: Cache blocking, data alignment, hardware vectorization, and prefetching.

### 12. Non-Uniform Memory Access (NUMA)
* **Definition**: A multi-socket server architecture where each CPU socket has physical RAM directly attached to its local memory controller.
* **Local Access**: Core accessing its local socket RAM (~65 ns).
* **Remote Access**: Core accessing the other socket's RAM over Intel UPI (~140 ns).
* **NUMA Node Optimization**: Use `numactl --cpunodebind=0 --membind=0` to ensure memory allocations reside on the same socket executing the threads.

### 13. Intel Advisor & The Roofline Model
* **The Roofline Model**: A 2D performance chart that plots:
  * **X-Axis**: **Arithmetic Intensity** (FLOPs / Byte of memory transferred).
  * **Y-Axis**: **Attained Performance** (GFLOPs / Second).
  * **The Ceiling**: Two physical limits—the flat **Peak Computational Ceiling** and the slanted **Memory Bandwidth Ceiling**.
* **Diagnostic**: Instantly reveals whether an algorithm is **Memory Bound** (sitting on the slanted roof) or **Compute Bound** (sitting on the flat roof).

### 14. Arithmetic Intensity (Operational Intensity)
* **Formula**: $\text{Arithmetic Intensity} = \frac{\text{Total Floating Point Operations (FLOPs)}}{\text{Total Bytes Transferred from Memory (Bytes)}}$.
* **Example**:
  * Vector Addition ($C[i] = A[i] + B[i]$): 1 addition for 3 floats (12 bytes) = $\frac{1}{12} \approx 0.083$ FLOPs/byte (Heavily Memory Bound!).
  * Matrix Multiply ($N \times N$ GEMM): $2N^3$ FLOPs for $O(N^2)$ memory footprint = $O(N)$ FLOPs/byte (Compute Bound!).

### 15. Vectorization Advisor
* **Definition**: An Intel Advisor component that identifies scalar loops, explains compiler vectorization failures (e.g., pointer aliasing, non-contiguous strides), and recommends `#pragma omp simd` hints.

### 16. Intel Inspector
* **Definition**: A dynamic memory and threading error debugger that detects non-deterministic race conditions, deadlocks, and memory corruption bugs.

### 17. ITAC (Intel Trace Analyzer and Collector)
* **Definition**: A graphical MPI profiling tool that records message passing communication timelines across cluster nodes, identifying synchronization wait states.

### 18. Straggler Problem (Late Sender / Late Receiver)
* **Definition**: In distributed MPI / Horovod training, when 63 worker nodes finish their mini-batch in 100 ms, but 1 worker node experiences thermal throttling or network latency and takes 500 ms.
* **Impact**: Under synchronous Ring-AllReduce, all 63 fast nodes sit idle at the barrier for 400 ms, destroying cluster scaling efficiency!

### 19. Distributed Slurm Multi-Node Coordination
* **Definition**: Slurm launching multi-node distributed AI jobs using `sbatch`, assigning a node hostfile, and executing across InfiniBand network interfaces.

### 20. Hostfile (`--hostfile` / `SLURM_JOB_NODELIST`)
* **Definition**: A list of cluster hostnames assigned by Slurm to an MPI job, instructing the process manager where to spawn ranks.

### 21. `vtune -collect hotspots`
* **Definition**: Command-line invocation of VTune to identify the top time-consuming functions and call stacks in an application:
  ```bash
  vtune -collect hotspots -result-dir=vtune_hotspots ./my_program
  ```

### 22. `vtune -collect uarch-exploration`
* **Definition**: Command-line invocation of VTune to perform full Top-Down Microarchitecture Analysis (TMAM).

### 23. `vtune -report summary`
* **Definition**: Generates a clean text or HTML summary from a collected VTune performance result directory.

### 24. Instructions Per Cycle (IPC)
* **Formula**: $\text{IPC} = \frac{\text{Total Retired Instructions}}{\text{Total Clock Cycles}}$.
* **Interpretation**: High-performance vectorized compute code reaches $\text{IPC} \ge 2.0$. Memory-stalled code drops to $\text{IPC} < 0.5$.

### 25. Cache Miss Ratio
* **Definition**: The fraction of memory references that miss a specific cache level:
  $$\text{Miss Ratio}_{\text{L1}} = \frac{\text{L1 Misses}}{\text{L1 References}}$$

### 26. Memory Bandwidth Saturation
* **Definition**: When memory traffic exceeds the physical transfer capability of the DDR5 memory bus (e.g., reaching 300 GB/s on an 8-channel Xeon system). Extra memory read requests are queued, stalling execution.

### 27. Vector Length & Register Occupancy
* **Definition**: The percentage of vector register lanes utilized during computation. For AVX-512, all 16 float elements (512 bits) must be active for 100% vector efficiency.

### 28. Loop Unrolling
* **Definition**: A compiler optimization where loop iterations are replicated in code to reduce branch overhead and increase instruction-level parallelism (ILP).

### 29. Profile-Guided Optimization (PGO)
* **Definition**: Compiling an application with instrumentation, executing it on representative data to generate a profile (`.profdata`), and recompiling so the compiler optimizes hot execution paths.

### 30. Inter-Procedural Optimization (IPO / `-ipo`)
* **Definition**: Multi-file compilation optimization where functions are inlined across separate source translation units, eliminating function call overhead.

### 31. CPI (Clock Cycles Per Instruction)
* **Formula**: $\text{CPI} = \frac{1}{\text{IPC}}$. Measures the average clock ticks needed to complete an instruction.

### 32. Flop Counting (GFLOPS / TFLOPS)
* **Definition**: GigaFLOPs ($10^9$) or TeraFLOPs ($10^{12}$) floating-point operations executed per second.

### 33. AllReduce Communication Wait Time
* **Definition**: The time worker nodes spend stalled waiting for gradient reduction over the network instead of executing forward/backward compute passes.

### 34. Flame Graph
* **Definition**: A visual representation of profiled software, where the x-axis represents population percentage of CPU time and the y-axis represents call-stack depth.

### 35. Cache Line Bouncing
* **Definition**: Repeated invalidation and transfer of a shared cache line between multiple CPU sockets due to concurrent writes, leading to interconnect bus saturation.

### 36. Optimization Feedback Loop
* **Rule**: Profile $\to$ Identify Bottleneck $\to$ Formulate Hypothesis $\to$ Apply Minimal Code/Compiler Change $\to$ Profile Again $\to$ Verify Bit-Exact Correctness.

---
**Glossary Status:** 100% Complete & Verified | GLA University HPC Masterclass Day 4
