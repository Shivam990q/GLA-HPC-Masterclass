# 🏛️ GLA UNIVERSITY, MATHURA — DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
## HPC Masterclass | Day 4 In-Class Assessment: Distributed AI Training & Intel VTune Profiling
**Target Audience**: 7th Semester B.Tech CSE (HPC Elective) | **Total Questions**: 25 | **Duration**: 30 Minutes

---

### 📋 Answer Key & Forensic Solution Guide (Instructor Copy)

| Q# | Correct Answer | Cognitive Bloom Level | Core Concept Focus |
|:--:|:--------------:|:---------------------:|:-------------------|
| **01** | **B** | `Understand` | In Intel VTune Profiler, what is the fundamental t... |
| **02** | **B** | `Knowledge` | What is the primary role of the CPU Performance Mo... |
| **03** | **C** | `Knowledge` | Which top-level metric in the Top-Down Microarchit... |
| **04** | **B** | `Understand` | What does a high 'Bad Speculation' metric (> 15%) ... |
| **05** | **B** | `Understand` | In TMAM, what hardware execution bottlenecks cause... |
| **06** | **B** | `Knowledge` | Into which two major categories is the 'Back-End B... |
| **07** | **B** | `Understand` | In VTune Hotspots analysis, what is the crucial di... |
| **08** | **B** | `Application` | Which VTune CLI command collects a basic performan... |
| **09** | **B** | `Knowledge` | Which VTune analysis type should an HPC engineer s... |
| **10** | **B** | `Analyze` | How does loop tiling (cache blocking) in matrix mu... |
| **11** | **B** | `Analyze` | What is 'False Sharing' in multi-threaded HPC appl... |
| **12** | **A** | `Understand` | On a multi-socket Intel Xeon server, what performa... |
| **13** | **B** | `Application` | When submitting a multi-node distributed TensorFlo... |
| **14** | **B** | `Application` | In a Slurm distributed training script, how can an... |
| **15** | **B** | `Understand` | What is the primary function of setting 'export HO... |
| **16** | **B** | `Analyze` | In distributed deep learning, what does an enginee... |
| **17** | **B** | `Analyze` | How does tuning 'HOROVOD_FUSION_THRESHOLD' (e.g., ... |
| **18** | **B** | `Knowledge` | What is the mathematical definition of 'Arithmetic... |
| **19** | **B** | `Understand` | In a Roofline Model chart, what does the 'Machine ... |
| **20** | **B** | `Apply` | If an algorithm has an arithmetic intensity of 0.2... |
| **21** | **A** | `Knowledge` | Which Intel oneAPI tool is specifically designed t... |
| **22** | **B** | `Understand` | Why is InfiniBand preferred over standard 1GbE/10G... |
| **23** | **B** | `Understand` | In OpenMP applications running on Intel Xeon proce... |
| **24** | **B** | `Analyze` | What is the primary diagnostic takeaway when an In... |
| **25** | **B** | `Evaluate` | How does combining Slurm job accounting with Intel... |

---

### 🔬 Complete Questions with Detailed Technical Rationale

#### Question 01
In Intel VTune Profiler, what is the fundamental technical difference between 'Software Sampling' and 'Hardware Event-Based Sampling (EBS)'?

- **(a)** Software sampling runs on Windows; EBS only runs on Android.
- **(b)** **[CORRECT]** Software sampling uses operating system timer interrupts to sample call stacks, while EBS utilizes on-chip CPU Performance Monitoring Unit (PMU) hardware counters with near-zero overhead.
- **(c)** Software sampling can only profile Python code; EBS can only profile HTML.
- **(d)** EBS requires recompiling the Linux kernel with debug flags.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Architectural Rationale**: Software sampling relies on OS timer ticks (~1-10 ms resolution), incurring noticeable overhead. Hardware Event-Based Sampling (EBS) programs physical CPU PMU registers (e.g., precise event-based sampling - PEBS) to trigger interrupts after precise counter overflows (e.g., every 1M cache misses) with <2% runtime overhead.

---

#### Question 02
What is the primary role of the CPU Performance Monitoring Unit (PMU) in modern Intel Xeon processors?

- **(a)** Regulating the physical voltage of the power supply unit.
- **(b)** **[CORRECT]** Tracking low-level microarchitectural hardware events (such as clock cycles, retired instructions, cache misses, and branch mispredictions) in dedicated physical silicon registers.
- **(c)** Managing disk encryption keys for the Linux filesystem.
- **(d)** Providing audio output for server diagnostic beeps.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Architectural Rationale**: The PMU contains dedicated hardware performance counters (e.g., IA32_PMC0-7, fixed-function counters) that track specific silicon micro-events directly inside the CPU pipeline without software instrumentation.

---

#### Question 03
Which top-level metric in the Top-Down Microarchitecture Analysis Method (TMAM) indicates that micro-operations (uOps) successfully executed and produced valid architectural results?

- **(a)** Bad Speculation
- **(b)** Front-End Bound
- **(c)** **[CORRECT]** Retiring
- **(d)** Back-End Bound

> **Correct Answer**: **(C)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Architectural Rationale**: 'Retiring' represents the fraction of pipeline slots devoted to processing uOps that actually retire (successfully complete and commit their architectural state). A high retiring percentage indicates good computational efficiency.

---

#### Question 04
What does a high 'Bad Speculation' metric (> 15%) in an Intel VTune TMAM profile reveal about an application?

- **(a)** The developer made poor financial decisions.
- **(b)** **[CORRECT]** The CPU pipeline is allocating significant execution slots to uOps that are eventually discarded due to branch mispredictions or machine clears.
- **(c)** The operating system runqueue is empty.
- **(d)** The Ethernet network switch is dropping packets.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Architectural Rationale**: Bad Speculation measures pipeline slots wasted on speculative execution down incorrect execution paths caused by branch predictor misses, requiring pipeline flushes and re-fetching.

---

#### Question 05
In TMAM, what hardware execution bottlenecks cause an application to be diagnosed as 'Front-End Bound'?

- **(a)** DRAM memory bus saturation.
- **(b)** **[CORRECT]** Delays in fetching and decoding machine instructions into uOps, caused by instruction cache (i-cache) misses, ITLB misses, or complex instruction decoding overhead.
- **(c)** High floating-point division latency.
- **(d)** Thermal throttling of the GPU fan.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Architectural Rationale**: Front-End Bound indicates the front-end pipeline (fetch, decode, pre-decode, branch target buffer) cannot deliver uOps to the out-of-order execution engine fast enough to keep execution units busy.

---

#### Question 06
Into which two major categories is the 'Back-End Bound' metric subdivided in Intel VTune TMAM?

- **(a)** CPU Bound and GPU Bound
- **(b)** **[CORRECT]** Memory Bound and Core Bound
- **(c)** Network Bound and Storage Bound
- **(d)** Static Bound and Dynamic Bound

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Architectural Rationale**: Back-End Bound is partitioned into Memory Bound (stalls caused by data access latencies across L1/L2/LLC caches, DRAM, and NUMA links) and Core Bound (stalls caused by execution unit contention, port pressure, or divider latency).

---

#### Question 07
In VTune Hotspots analysis, what is the crucial distinction between 'Self Time' and 'Total Time' for a profiled function?

- **(a)** Self time includes compiler optimization time; total time does not.
- **(b)** **[CORRECT]** Self Time measures the time spent strictly executing instructions inside the function itself; Total Time includes Self Time plus the time spent in all callees invoked by that function.
- **(c)** Total time is measured in seconds; self time is measured in microseconds.
- **(d)** Self time only counts idle sleep time.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Architectural Rationale**: Self Time isolates the exact function where CPU cycles are spent executing its own instructions. Total Time sums the function and everything it calls down the call stack, pinpointing where to focus algorithmic refactoring.

---

#### Question 08
Which VTune CLI command collects a basic performance Hotspots profile for an executable named './my_simulation' and saves results in './profile_data'?

- **(a)** vtune -run hotspots ./my_simulation
- **(b)** **[CORRECT]** vtune -collect hotspots -result-dir ./profile_data -- ./my_simulation
- **(c)** vtune -export ./profile_data ./my_simulation
- **(d)** vtune --start-profile=hotspots ./my_simulation

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Application`  
> **Architectural Rationale**: The standard VTune syntax uses `-collect <analysis-type>`, specifies the output folder with `-result-dir <dir>`, and passes target command arguments after `--`.

---

#### Question 09
Which VTune analysis type should an HPC engineer select to measure L1/L2/LLC cache miss rates, memory bandwidth saturation, and NUMA remote access latency?

- **(a)** vtune -collect threading
- **(b)** **[CORRECT]** vtune -collect memory-access
- **(c)** vtune -collect system-overview
- **(d)** vtune -collect gpu-offload

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Architectural Rationale**: `vtune -collect memory-access` measures memory hierarchy efficiency: cache misses per layer, read/write bandwidth saturation, cross-socket NUMA remote memory hops, and store forwarding blocks.

---

#### Question 10
How does loop tiling (cache blocking) in matrix multiplication dramatically reduce 'Memory Bound' stalls in an Intel VTune profile?

- **(a)** By converting floating-point numbers into 8-bit characters.
- **(b)** **[CORRECT]** By partitioning large $N \times N$ arrays into smaller sub-blocks sized to fit within L1/L2 caches, ensuring data elements are reused multiple times while resident in high-speed on-chip SRAM.
- **(c)** By disabling multi-threading so only 1 thread accesses RAM.
- **(d)** By writing matrix products to disk instead of memory.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Architectural Rationale**: Standard naive matrix multiplication streams data through memory, continuously evicting cache lines. Cache blocking partitions computation into tiles that fit in L1/L2 cache, maximizing cache hit rates and eliminating DRAM stall cycles.

---

#### Question 11
What is 'False Sharing' in multi-threaded HPC applications, and how is it detected in Intel VTune Memory Access analysis?

- **(a)** Two users sharing the same SSH password.
- **(b)** **[CORRECT]** Independent threads on different CPU cores modifying distinct variables that happen to share the same 64-byte hardware cache line, triggering constant MESI cache-coherence invalidation traffic.
- **(c)** Sharing corrupted datasets across InfiniBand switches.
- **(d)** A bug where a pointer refers to an unallocated memory address.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Architectural Rationale**: False sharing occurs when variables on the same 64-byte cache line are updated by distinct cores. The MESI hardware protocol constantly invalidates the cache line across cores, causing severe memory-bound stalls visible as high LLC misses and contention in VTune.

---

#### Question 12
On a multi-socket Intel Xeon server, what performance impact occurs when a thread running on Socket 0 frequently accesses DRAM physically wired to Socket 1?

- **(a)** **[CORRECT]** Memory access latency increases by $1.5\times$ to $2.5\times$ due to cross-socket Intel Ultra Path Interconnect (UPI) hops, and inter-socket UPI bandwidth is consumed.
- **(b)** The operating system kernel crashes immediately.
- **(c)** The CPU sockets are permanently damaged by voltage surges.
- **(d)** Data is automatically converted from 32-bit to 64-bit.

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Architectural Rationale**: Remote NUMA accesses must traverse Intel UPI links, adding ~40-60 ns of latency per access and saturating the inter-socket interconnect. VTune flags this as 'Remote DRAM Access' in Memory Access reports.

---

#### Question 13
When submitting a multi-node distributed TensorFlow job to Slurm, what does the directive '#SBATCH --nodes=4' combined with '#SBATCH --ntasks-per-node=4' configure?

- **(a)** A single node running 16 threads in serial.
- **(b)** **[CORRECT]** An allocation of 4 physical compute nodes with exactly 4 MPI/Horovod worker tasks spawned per node, yielding 16 total distributed worker processes.
- **(c)** A job that restarts 4 times every 4 hours.
- **(d)** 4 separate Slurm partitions running simultaneously.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Application`  
> **Architectural Rationale**: `--nodes=4` allocates 4 distinct nodes. `--ntasks-per-node=4` launches 4 distinct task instances per node, resulting in $4 \times 4 = 16$ total distributed ranks.

---

#### Question 14
In a Slurm distributed training script, how can an engineer reliably generate an MPI/Horovod hostfile dynamically from the allocated node list?

- **(a)** By hardcoding localhost 16 times in a static text file.
- **(b)** **[CORRECT]** By running 'scontrol show hostnames $SLURM_JOB_NODELIST | awk '{print $1":4"}' > hostfile'.
- **(c)** By querying Google DNS servers.
- **(d)** By reading the /etc/fstab file on the head node.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Application`  
> **Architectural Rationale**: Slurm sets `$SLURM_JOB_NODELIST` to a compressed node expression (e.g., `node[01-04]`). Running `scontrol show hostnames` expands this into individual node hostnames, formatting them with slot counts for MPI/Horovod.

---

#### Question 15
What is the primary function of setting 'export HOROVOD_TIMELINE=./timeline.json' during distributed deep learning runs?

- **(a)** It sets the system clock on the compute nodes.
- **(b)** **[CORRECT]** It exports microsecond-level Chrome tracing JSON logs detailing when each rank computes gradients, enters negotiation, waits for AllReduce, and transfers tensors.
- **(c)** It records audio from the cluster room.
- **(d)** It deletes model checkpoints after 5 minutes.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Architectural Rationale**: Horovod Timeline writes execution timestamps for tensor allreduces in Chrome tracing format (`about://tracing`), enabling visual inspection of communication bubbles, rank desynchronization, and stragglers.

---

#### Question 16
In distributed deep learning, what does an engineer look for on a Horovod Timeline to diagnose severe network communication overhead?

- **(a)** Zero lines in the JSON file.
- **(b)** **[CORRECT]** Large 'NEGOTIATE_ALLREDUCE' and 'WAIT_ALLREDUCE' phases where compute workers remain idle waiting for straggler ranks or tensor synchronization barriers.
- **(c)** CPU core temperatures exceeding 90 degrees.
- **(d)** Text strings written in uppercase letters.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Architectural Rationale**: Long `WAIT_ALLREDUCE` bars indicate that fast workers have finished computing gradients and are stalled waiting for slower worker ranks (stragglers) or delayed network barriers before AllReduce can begin.

---

#### Question 17
How does tuning 'HOROVOD_FUSION_THRESHOLD' (e.g., setting it to 64MB) improve distributed scaling on high-bandwidth cluster fabrics?

- **(a)** It deletes gradients smaller than 64MB.
- **(b)** **[CORRECT]** It coalesces multiple small layer gradients into contiguous 64MB communication buffers before launching Ring-AllReduce, amortizing message initiation latency over high-speed networks.
- **(c)** It forces all tensor operations into 8-bit integers.
- **(d)** It increases the physical RAM on the compute nodes.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Architectural Rationale**: Transferring thousands of small gradient tensors incurs high per-message latency overhead. Tensor fusion buffers small tensors into larger contiguous blocks (e.g., 64MB) to saturate network bandwidth.

---

#### Question 18
What is the mathematical definition of 'Arithmetic Intensity' in the Roofline Model?

- **(a)** Total Wall Clock Time / Number of CPU Sockets
- **(b)** **[CORRECT]** Total Floating-Point Operations (FLOPs) divided by Total Bytes accessed from DRAM memory (FLOPs/Byte)
- **(c)** Clock Frequency (GHz) x Number of Cores
- **(d)** Dataset Size in Megabytes / Batch Size

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Architectural Rationale**: Arithmetic Intensity ($I = \text{FLOPs} / \text{Byte}$) quantifies how many computational operations are performed for each byte of data transferred across the memory bus.

---

#### Question 19
In a Roofline Model chart, what does the 'Machine Ridge Point' ($I_{ridge}$) represent?

- **(a)** The maximum temperature of the server chassis.
- **(b)** **[CORRECT]** The minimum arithmetic intensity required for an algorithm to theoretically achieve the machine's peak theoretical compute performance (Peak FLOP/s / Peak Memory Bandwidth GB/s).
- **(c)** The point where the operating system runs out of swap space.
- **(d)** The physical elevation of the supercomputer datacenter.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Architectural Rationale**: The ridge point is defined as $I_{ridge} = \frac{\text{Peak Compute Performance (GFLOP/s)}}{\text{Peak Memory Bandwidth (GB/s)}}$. If an algorithm's arithmetic intensity is below $I_{ridge}$, its performance is fundamentally limited by memory bandwidth.

---

#### Question 20
If an algorithm has an arithmetic intensity of 0.25 FLOPs/Byte on a system with 1000 GFLOP/s peak compute and 100 GB/s memory bandwidth, what is its maximum attainable performance?

- **(a)** 1000 GFLOP/s
- **(b)** **[CORRECT]** 25 GFLOP/s
- **(c)** 250 GFLOP/s
- **(d)** 4 GFLOP/s

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Apply`  
> **Architectural Rationale**: In the memory-bound regime: $\text{Performance} = \text{Memory Bandwidth} \times \text{Arithmetic Intensity} = 100 \text{ GB/s} \times 0.25 \text{ FLOPs/Byte} = 25 \text{ GFLOP/s}$.

---

#### Question 21
Which Intel oneAPI tool is specifically designed to automatically generate Roofline Model charts and evaluate vectorization efficiency for HPC code?

- **(a)** **[CORRECT]** Intel Advisor
- **(b)** Intel Distribution for Python
- **(c)** Intel Data Analytics Acceleration Library
- **(d)** Intel Quantum Simulator

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Architectural Rationale**: Intel Advisor analyzes memory traffic, counts floating-point operations, and generates interactive Roofline charts showing whether loops are memory-bandwidth or compute-bound relative to hardware ceilings.

---

#### Question 22
Why is InfiniBand preferred over standard 1GbE/10GbE TCP/IP Ethernet for multi-node distributed deep learning training?

- **(a)** InfiniBand cables are made of gold rather than copper.
- **(b)** **[CORRECT]** InfiniBand provides Remote Direct Memory Access (RDMA) that bypasses the host operating system kernel and CPU, achieving sub-microsecond latency and line rates up to 200-400 Gbps.
- **(c)** InfiniBand cannot run Python programs.
- **(d)** Ethernet switches do not support floating-point data.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Architectural Rationale**: InfiniBand with RDMA (e.g., RoCE or native IB) transfers data directly between application memories across cluster nodes without OS kernel context switches or CPU memory copies, dramatically slashing collective AllReduce communication latency.

---

#### Question 23
In OpenMP applications running on Intel Xeon processors, what does setting 'OMP_PROC_BIND=close' accomplish?

- **(a)** It closes all open files on disk when a thread completes.
- **(b)** **[CORRECT]** It binds worker threads to contiguous physical CPU cores located close to each other on the same socket, maximizing shared L3 cache locality.
- **(c)** It forces threads to shut down after 10 seconds.
- **(d)** It prevents threads from executing math operations.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Architectural Rationale**: `OMP_PROC_BIND=close` places OpenMP threads on adjacent physical cores in the same processor socket, allowing threads working on cooperative data chunks to share L3 cache lines without incurring inter-socket communication.

---

#### Question 24
What is the primary diagnostic takeaway when an Intel VTune profile shows high 'Core Bound -> Port Contention'?

- **(a)** The network switch ports are unplugged.
- **(b)** **[CORRECT]** Execution units inside the CPU core (e.g., FMA vector units or branch units) are over-subscribed, causing ready uOps to wait in the reservation station for an available execution port.
- **(c)** The CPU needs more thermal paste.
- **(d)** The hard drive read head is misaligned.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Architectural Rationale**: Port Contention occurs when multiple uOps compete for the same execution ports (such as Ports 0 and 1 for FMA operations) while other execution ports sit underutilized, indicating a need for instruction-level parallelization or loop unrolling.

---

#### Question 25
How does combining Slurm job accounting with Intel VTune profiling empower HPC facility directors and lead researchers?

- **(a)** It allows them to trade supercomputer time on stock exchanges.
- **(b)** **[CORRECT]** It provides quantitative proof of hardware efficiency, isolating whether multi-node scaling bottlenecks stem from cluster network fabric latency, CPU memory saturation, or inefficient algorithmic implementations.
- **(c)** It automatically generates research papers without human authorship.
- **(d)** It replaces all system administrators with machine learning models.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Evaluate`  
> **Architectural Rationale**: Combining Slurm resource allocation metrics (job elapsed time, CPU/memory efficiency via `sacct`) with VTune microarchitectural profiling (TMAM, memory bandwidth, Roofline) provides empirical proof of whether applications are utilizing supercomputing hardware optimally.

---

