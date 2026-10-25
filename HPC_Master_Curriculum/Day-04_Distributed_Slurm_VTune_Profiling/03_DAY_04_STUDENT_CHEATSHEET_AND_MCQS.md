# 📝 DAY 4: STUDENT QUICK REFERENCE & OFFICIAL MCQ BANK
## 1-Page Cheat Sheet + 25 Evaluated Assessment Questions
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 📌 PART 1: 1-Page Student Command & VTune Cheat Sheet

### 1. Intel VTune Profiler CLI Quick Reference
| Command | Analysis Type | Primary Target |
| :--- | :--- | :--- |
| `vtune -collect hotspots -r <dir> -- <cmd>` | Hotspots Analysis | Identify top time-consuming functions |
| `vtune -collect uarch-exploration -r <dir> -- <cmd>` | Microarchitecture (TMAM) | Identify Frontend/Backend memory stalls |
| `vtune -collect memory-access -r <dir> -- <cmd>` | Memory Access Profiling | Measure DRAM bandwidth and cache misses |
| `vtune -collect threading -r <dir> -- <cmd>` | Threading Efficiency | Measure lock wait time and thread imbalance |
| `vtune -report summary -r <dir>` | Summary Report | View overall CPI (Cycles per Instruction) |
| `vtune -report hotspots -r <dir>` | Hotspots Breakdown | Sort functions by CPU execution time |

### 2. The TMAM (Top-Down) Classification Hierarchy
```
                   +------------------------------------+
                   |          TOTAL CPU SLOTS           |
                   +-----------------+------------------+
                                     |
         +------------------+--------+--------+------------------+
         |                  |                 |                  |
+--------v-------+  +-------v-------+  +------v-------+  +-------v-------+
|    RETIRING    |  |BAD SPECULATION|  |FRONTEND BOUND|  | BACKEND BOUND |
| (Good Work!)   |  | (Branch Miss) |  | (Fetch/Decode|  | (Memory Stall |
| 30-50% Target  |  | < 10% Target  |  | < 15% Target |  | & Execution)  |
+----------------+  +---------------+  +--------------+  +---------------+
```

---

## 🎯 PART 2: Day 4 Official Syllabus Checklist

- [ ] 01. Distributed TensorFlow training with Slurm
- [ ] 02. Multi-node task mapping (`--nodes`, `--ntasks-per-node`)
- [ ] 03. Socket binding and core pinning (`mpirun --bind-to socket`)
- [ ] 04. The Optimization Gap in cluster scaling
- [ ] 05. Intel VTune Profiler architecture and GUI/CLI modes
- [ ] 06. Top-Down Microarchitecture Analysis Method (TMAM)
- [ ] 07. Retiring vs Bad Speculation vs Frontend vs Backend Bound
- [ ] 08. Diagnosing CPU Memory Stalls vs Core Execution Stalls
- [ ] 09. Thread synchronization overhead & lock wait time
- [ ] 10. Memory access profiling & LLC cache miss analysis
- [ ] 11. Performance diagnostic matrix & hardware-aware fixes
- [ ] 12. Iterative optimization loop (Execute -> Profile -> Analyze -> Optimize)

---

## 📝 PART 3: 25 Official Multiple-Choice Questions (With Answers & Explanations)

#### Q1. What is the primary purpose of Intel VTune Profiler?
- A) Writing unit tests in Python
- B) Microarchitecture performance analysis, hotspot isolation, and bottleneck debugging on x86 hardware
- C) Managing git repositories
- D) Formatting Linux hard drives  
**Answer: B** | *Explanation: Intel VTune analyzes CPU hardware performance counters to diagnose code inefficiencies.*

#### Q2. What does TMAM stand for in Intel VTune microarchitecture exploration?
- A) Thread Management Allocation Module
- B) Top-Down Microarchitecture Analysis Method
- C) Terminal Multi-Agent Model
- D) Total Memory Access Multiplexer  
**Answer: B** | *Explanation: TMAM is the industry-standard methodology for categorizing CPU pipeline stall cycles.*

#### Q3. In the TMAM hierarchy, what does a high percentage in the "Retiring" category indicate?
- A) The CPU is idle and waiting to shut down
- B) Useful work: instructions are successfully executing and committing results to registers
- C) The program has crashed
- D) Memory bandwidth is exhausted  
**Answer: B** | *Explanation: Retiring represents cycles spent completing instructions that produce true program output.*

#### Q4. What is indicated when VTune reports that a workload is "Backend Bound: Memory Bound"?
- A) The program has a syntax error
- B) The CPU execution pipelines are frequently stalled waiting for data to load from L3 cache or main DRAM memory
- C) The network connection is lost
- D) The monitor display refresh rate is low  
**Answer: B** | *Explanation: Memory-bound stalls mean CPU execution units are starving waiting for memory bus transfers.*

#### Q5. Why is "Core Pinning" (`--bind-to socket` or `OMP_PROC_BIND=close`) important in multi-node HPC jobs?
- A) To prevent physical CPU theft
- B) To keep threads pinned to specific physical CPU cores and sockets, preventing costly L1/L2 cache invalidations caused by OS thread migration
- C) To reduce fan noise
- D) To limit memory usage  
**Answer: B** | *Explanation: Binding threads prevents the OS scheduler from bouncing threads between NUMA domains, maintaining warm caches.*

#### Q6. What does `CPI` stand for in a VTune summary report?
- A) Central Processing Identifier
- B) Clocks per Instruction (Cycles per Instruction)
- C) Cache Packet Ingestion
- D) Core Power Indicator  
**Answer: B** | *Explanation: CPI measures how many CPU clock cycles are required on average to retire one instruction.*

#### Q7. A developer doubles the number of cluster nodes from 4 to 8, but the training time remains identical. What is the most likely cause?
- A) A bad power supply
- B) The Communication Bottleneck (time spent exchanging gradients over the network exceeds compute gains)
- C) Python version mismatch
- D) Incorrect filename  
**Answer: B** | *Explanation: Horizontal scaling delivers diminishing returns if network latency and gradient synchronization dominate.*

#### Q8. Which VTune CLI collection type identifies the exact lines of code that consume the most CPU cycles?
- A) `-collect hotspots`
- B) `-collect memory-leak`
- C) `-collect network`
- D) `-collect disk`  
**Answer: A** | *Explanation: Hotspots analysis samples CPU instruction pointers to identify time-consuming functions and source lines.*

#### Q9. What does a high "Spin Time" or "Wait Time" in a VTune Threading report signify?
- A) The fan is spinning fast
- B) Worker threads are stalled waiting on synchronization primitives (locks, mutexes, barriers) while other threads finish
- C) Disk read speeds are high
- D) The model is overfitting  
**Answer: B** | *Explanation: Elevated wait/spin time indicates thread imbalance or lock contention in OpenMP/pthreads.*

#### Q10. What does the `Bad Speculation` metric in TMAM represent?
- A) Financial loss in stock trading
- B) CPU cycles wasted executing instructions along branch paths that were incorrectly predicted by the branch predictor
- C) Incompatible compiler flags
- D) Unused RAM  
**Answer: B** | *Explanation: When a branch is mispredicted, the processor must flush its pipeline, discarding speculative work.*

#### Q11. Which tool or technique helps solve I/O storage bottlenecks during distributed deep learning training?
- A) Reading files one by one in Python loops
- B) Multi-threaded data pre-fetching and pinned host memory (`DataLoader(pin_memory=True, num_workers=8)`)
- C) Compressing image files during training
- D) Deleting training logs  
**Answer: B** | *Explanation: Asynchronous prefetching hides disk latency by loading the next batch into pinned RAM while the current batch trains.*

#### Q12. In Slurm, what does `#SBATCH --ntasks-per-node=2` specify?
- A) Exactly 2 MPI/process ranks will be spawned per physical node
- B) The job will run twice
- C) Only 2 files can be opened
- D) The job will finish in 2 minutes  
**Answer: A** | *Explanation: `--ntasks-per-node` allocates a specific count of independent process tasks on each node.*

#### Q13. In VTune, what is a "Flame Graph"?
- A) A chart showing CPU temperature
- B) A visual representation of hierarchical call stacks, where the width of each box indicates the proportion of execution time spent
- C) A warning that the server is overheating
- D) A network throughput graph  
**Answer: B** | *Explanation: Flame graphs visualize stack traces to make hot call paths immediately obvious.*

#### Q14. What is the effect of setting `OMP_NUM_THREADS` higher than the number of physical CPU cores on a node?
- A) The program runs 2x faster
- B) Severe performance degradation due to CPU oversubscription and excessive OS context-switching overhead
- C) The CPU permanently locks up
- D) Memory bandwidth increases  
**Answer: B** | *Explanation: Oversubscribing cores forces the OS scheduler to continuously swap thread contexts, incurring high overhead.*

#### Q15. Which hardware feature is inspected during VTune Memory Access profiling to diagnose cache efficiency?
- A) Keyboard latency
- B) LLC (Last Level Cache / L3) Miss Rate and DRAM bandwidth saturation
- C) Wi-Fi signal strength
- D) HDMI cable bandwidth  
**Answer: B** | *Explanation: LLC misses force CPU execution units to fetch data across the memory bus from high-latency DRAM.*

#### Q16. How does Horovod Tensor Fusion reduce network communication overhead?
- A) By converting all numbers to integers
- B) By aggregating multiple small gradient tensors into a single contiguous ring buffer before transmitting over the network
- C) By dropping half of the gradients
- D) By compressing text files  
**Answer: B** | *Explanation: Tensor Fusion reduces packet header overhead and latency by sending fewer, larger network packets.*

#### Q17. What is NUMA in multi-socket enterprise servers?
- A) Non-Uniform Memory Access (memory latency varies depending on whether a core accesses local or remote socket RAM)
- B) Network Uniform Management Architecture
- C) Numerical Units for Matrix Arithmetic
- D) New Universal Memory Array  
**Answer: A** | *Explanation: In multi-socket Xeon servers, accessing memory attached to the remote CPU socket incurs higher latency.*

#### Q18. Which Linux utility allows pinning processes to specific NUMA memory domains?
- A) `numactl`
- B) `ping`
- C) `top`
- D) `free`  
**Answer: A** | *Explanation: `numactl --cpunodebind=0 --membind=0` enforces NUMA socket and memory affinity.*

#### Q19. What does the "Roofline Model" analyze in HPC performance engineering?
- A) Building architectural safety
- B) The relationship between operational arithmetic intensity (FLOPs/Byte) and maximum hardware peak performance (Compute Bound vs Memory Bound)
- C) Server rack height limits
- D) Cooling fan speeds  
**Answer: B** | *Explanation: The roofline model identifies whether an application is constrained by memory bandwidth or peak compute capacity.*

#### Q20. In VTune, what does a "Frontend Bound" bottleneck typically point to?
- A) Inefficient HTML rendering
- B) Instruction cache (ICache) misses or branch target buffer (BTB) latency preventing instructions from reaching execution decoders
- C) Slow network switches
- D) Exhausted hard disk space  
**Answer: B** | *Explanation: Frontend stalls occur when the processor cannot fetch or decode instructions fast enough.*

#### Q21. Which VTune command exports a collected analysis directory into a summary report?
- A) `vtune -report summary -r <result_dir>`
- B) `vtune --export-txt`
- C) `vtune -show all`
- D) `vtune --print`  
**Answer: A** | *Explanation: `vtune -report summary` parses the database and prints text metrics.*

#### Q22. What is the recommended first step in the 4-step Iterative Optimization Pipeline?
- A) Rewrite the entire algorithm from scratch
- B) Measure baseline performance and profile with tools like VTune before changing any code
- C) Buy more hardware
- D) Disable all compiler optimizations  
**Answer: B** | *Explanation: Optimization must be evidence-based: profile first to identify true bottlenecks before modifying code.*

#### Q23. Why do unoptimized distributed deep learning jobs often show low CPU/GPU utilization?
- A) Because the hardware is broken
- B) Because compute units are stalled waiting for I/O disk reads or inter-node network synchronization
- C) Because neural networks don't require compute
- D) Because Python is inherently fast  
**Answer: B** | *Explanation: Low utilization usually indicates processors are starved for data due to I/O or network barriers.*

#### Q24. Which high-speed interconnect technology is standard in modern supercomputing clusters alongside InfiniBand?
- A) USB 2.0
- B) RoCE v2 (RDMA over Converged Ethernet)
- C) Bluetooth 5.0
- D) Dial-up DSL  
**Answer: B** | *Explanation: RoCE v2 enables sub-microsecond remote direct memory access over enterprise Ethernet fabrics.*

#### Q25. What grand capstone topic synthesizes Day 4 distributed scaling and profiling on Day 5?
- A) Generative AI & Large Language Models (LLMs) on Intel Xeon AMX, Habana Gaudi, and OpenVINO
- B) CSS stylesheet design
- C) Word document editing
- D) Spreadsheet pivot tables  
**Answer: A** | *Explanation: Day 5 unites all preceding skills to deploy, fine-tune, and optimize massive Large Language Models.*
