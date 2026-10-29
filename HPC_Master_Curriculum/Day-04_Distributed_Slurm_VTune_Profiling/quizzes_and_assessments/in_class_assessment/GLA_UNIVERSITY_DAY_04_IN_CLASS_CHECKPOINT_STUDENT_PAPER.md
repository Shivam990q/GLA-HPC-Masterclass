# 🏛️ GLA UNIVERSITY, MATHURA — DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
## HPC Masterclass | Day 4 In-Class Checkpoint Assessment
**Course**: B.Tech CSE 7th Sem — High Performance Computing Masterclass  
**Module**: Day 4 — Distributed AI Training, Slurm Scheduling & Intel VTune Profiling Optimization  
**Duration**: 30 Minutes | **Total Questions**: 25 MCQs | **Maximum Marks**: 25  

**Student Name**: ___________________________ **Roll Number**: __________________ **Section**: ______

---

### 📝 Instructions for Candidates
1. All questions are compulsory. Each question carries exactly 1 mark.
2. Select the single best answer for each question.
3. No negative marking.

---

#### Q01. In Intel VTune Profiler, what is the fundamental technical difference between 'Software Sampling' and 'Hardware Event-Based Sampling (EBS)'?
- [ ] **(a)** Software sampling runs on Windows; EBS only runs on Android.
- [ ] **(b)** Software sampling uses operating system timer interrupts to sample call stacks, while EBS utilizes on-chip CPU Performance Monitoring Unit (PMU) hardware counters with near-zero overhead.
- [ ] **(c)** Software sampling can only profile Python code; EBS can only profile HTML.
- [ ] **(d)** EBS requires recompiling the Linux kernel with debug flags.

#### Q02. What is the primary role of the CPU Performance Monitoring Unit (PMU) in modern Intel Xeon processors?
- [ ] **(a)** Regulating the physical voltage of the power supply unit.
- [ ] **(b)** Tracking low-level microarchitectural hardware events (such as clock cycles, retired instructions, cache misses, and branch mispredictions) in dedicated physical silicon registers.
- [ ] **(c)** Managing disk encryption keys for the Linux filesystem.
- [ ] **(d)** Providing audio output for server diagnostic beeps.

#### Q03. Which top-level metric in the Top-Down Microarchitecture Analysis Method (TMAM) indicates that micro-operations (uOps) successfully executed and produced valid architectural results?
- [ ] **(a)** Bad Speculation
- [ ] **(b)** Front-End Bound
- [ ] **(c)** Retiring
- [ ] **(d)** Back-End Bound

#### Q04. What does a high 'Bad Speculation' metric (> 15%) in an Intel VTune TMAM profile reveal about an application?
- [ ] **(a)** The developer made poor financial decisions.
- [ ] **(b)** The CPU pipeline is allocating significant execution slots to uOps that are eventually discarded due to branch mispredictions or machine clears.
- [ ] **(c)** The operating system runqueue is empty.
- [ ] **(d)** The Ethernet network switch is dropping packets.

#### Q05. In TMAM, what hardware execution bottlenecks cause an application to be diagnosed as 'Front-End Bound'?
- [ ] **(a)** DRAM memory bus saturation.
- [ ] **(b)** Delays in fetching and decoding machine instructions into uOps, caused by instruction cache (i-cache) misses, ITLB misses, or complex instruction decoding overhead.
- [ ] **(c)** High floating-point division latency.
- [ ] **(d)** Thermal throttling of the GPU fan.

#### Q06. Into which two major categories is the 'Back-End Bound' metric subdivided in Intel VTune TMAM?
- [ ] **(a)** CPU Bound and GPU Bound
- [ ] **(b)** Memory Bound and Core Bound
- [ ] **(c)** Network Bound and Storage Bound
- [ ] **(d)** Static Bound and Dynamic Bound

#### Q07. In VTune Hotspots analysis, what is the crucial distinction between 'Self Time' and 'Total Time' for a profiled function?
- [ ] **(a)** Self time includes compiler optimization time; total time does not.
- [ ] **(b)** Self Time measures the time spent strictly executing instructions inside the function itself; Total Time includes Self Time plus the time spent in all callees invoked by that function.
- [ ] **(c)** Total time is measured in seconds; self time is measured in microseconds.
- [ ] **(d)** Self time only counts idle sleep time.

#### Q08. Which VTune CLI command collects a basic performance Hotspots profile for an executable named './my_simulation' and saves results in './profile_data'?
- [ ] **(a)** vtune -run hotspots ./my_simulation
- [ ] **(b)** vtune -collect hotspots -result-dir ./profile_data -- ./my_simulation
- [ ] **(c)** vtune -export ./profile_data ./my_simulation
- [ ] **(d)** vtune --start-profile=hotspots ./my_simulation

#### Q09. Which VTune analysis type should an HPC engineer select to measure L1/L2/LLC cache miss rates, memory bandwidth saturation, and NUMA remote access latency?
- [ ] **(a)** vtune -collect threading
- [ ] **(b)** vtune -collect memory-access
- [ ] **(c)** vtune -collect system-overview
- [ ] **(d)** vtune -collect gpu-offload

#### Q10. How does loop tiling (cache blocking) in matrix multiplication dramatically reduce 'Memory Bound' stalls in an Intel VTune profile?
- [ ] **(a)** By converting floating-point numbers into 8-bit characters.
- [ ] **(b)** By partitioning large $N \times N$ arrays into smaller sub-blocks sized to fit within L1/L2 caches, ensuring data elements are reused multiple times while resident in high-speed on-chip SRAM.
- [ ] **(c)** By disabling multi-threading so only 1 thread accesses RAM.
- [ ] **(d)** By writing matrix products to disk instead of memory.

#### Q11. What is 'False Sharing' in multi-threaded HPC applications, and how is it detected in Intel VTune Memory Access analysis?
- [ ] **(a)** Two users sharing the same SSH password.
- [ ] **(b)** Independent threads on different CPU cores modifying distinct variables that happen to share the same 64-byte hardware cache line, triggering constant MESI cache-coherence invalidation traffic.
- [ ] **(c)** Sharing corrupted datasets across InfiniBand switches.
- [ ] **(d)** A bug where a pointer refers to an unallocated memory address.

#### Q12. On a multi-socket Intel Xeon server, what performance impact occurs when a thread running on Socket 0 frequently accesses DRAM physically wired to Socket 1?
- [ ] **(a)** Memory access latency increases by $1.5\times$ to $2.5\times$ due to cross-socket Intel Ultra Path Interconnect (UPI) hops, and inter-socket UPI bandwidth is consumed.
- [ ] **(b)** The operating system kernel crashes immediately.
- [ ] **(c)** The CPU sockets are permanently damaged by voltage surges.
- [ ] **(d)** Data is automatically converted from 32-bit to 64-bit.

#### Q13. When submitting a multi-node distributed TensorFlow job to Slurm, what does the directive '#SBATCH --nodes=4' combined with '#SBATCH --ntasks-per-node=4' configure?
- [ ] **(a)** A single node running 16 threads in serial.
- [ ] **(b)** An allocation of 4 physical compute nodes with exactly 4 MPI/Horovod worker tasks spawned per node, yielding 16 total distributed worker processes.
- [ ] **(c)** A job that restarts 4 times every 4 hours.
- [ ] **(d)** 4 separate Slurm partitions running simultaneously.

#### Q14. In a Slurm distributed training script, how can an engineer reliably generate an MPI/Horovod hostfile dynamically from the allocated node list?
- [ ] **(a)** By hardcoding localhost 16 times in a static text file.
- [ ] **(b)** By running 'scontrol show hostnames $SLURM_JOB_NODELIST | awk '{print $1":4"}' > hostfile'.
- [ ] **(c)** By querying Google DNS servers.
- [ ] **(d)** By reading the /etc/fstab file on the head node.

#### Q15. What is the primary function of setting 'export HOROVOD_TIMELINE=./timeline.json' during distributed deep learning runs?
- [ ] **(a)** It sets the system clock on the compute nodes.
- [ ] **(b)** It exports microsecond-level Chrome tracing JSON logs detailing when each rank computes gradients, enters negotiation, waits for AllReduce, and transfers tensors.
- [ ] **(c)** It records audio from the cluster room.
- [ ] **(d)** It deletes model checkpoints after 5 minutes.

#### Q16. In distributed deep learning, what does an engineer look for on a Horovod Timeline to diagnose severe network communication overhead?
- [ ] **(a)** Zero lines in the JSON file.
- [ ] **(b)** Large 'NEGOTIATE_ALLREDUCE' and 'WAIT_ALLREDUCE' phases where compute workers remain idle waiting for straggler ranks or tensor synchronization barriers.
- [ ] **(c)** CPU core temperatures exceeding 90 degrees.
- [ ] **(d)** Text strings written in uppercase letters.

#### Q17. How does tuning 'HOROVOD_FUSION_THRESHOLD' (e.g., setting it to 64MB) improve distributed scaling on high-bandwidth cluster fabrics?
- [ ] **(a)** It deletes gradients smaller than 64MB.
- [ ] **(b)** It coalesces multiple small layer gradients into contiguous 64MB communication buffers before launching Ring-AllReduce, amortizing message initiation latency over high-speed networks.
- [ ] **(c)** It forces all tensor operations into 8-bit integers.
- [ ] **(d)** It increases the physical RAM on the compute nodes.

#### Q18. What is the mathematical definition of 'Arithmetic Intensity' in the Roofline Model?
- [ ] **(a)** Total Wall Clock Time / Number of CPU Sockets
- [ ] **(b)** Total Floating-Point Operations (FLOPs) divided by Total Bytes accessed from DRAM memory (FLOPs/Byte)
- [ ] **(c)** Clock Frequency (GHz) x Number of Cores
- [ ] **(d)** Dataset Size in Megabytes / Batch Size

#### Q19. In a Roofline Model chart, what does the 'Machine Ridge Point' ($I_{ridge}$) represent?
- [ ] **(a)** The maximum temperature of the server chassis.
- [ ] **(b)** The minimum arithmetic intensity required for an algorithm to theoretically achieve the machine's peak theoretical compute performance (Peak FLOP/s / Peak Memory Bandwidth GB/s).
- [ ] **(c)** The point where the operating system runs out of swap space.
- [ ] **(d)** The physical elevation of the supercomputer datacenter.

#### Q20. If an algorithm has an arithmetic intensity of 0.25 FLOPs/Byte on a system with 1000 GFLOP/s peak compute and 100 GB/s memory bandwidth, what is its maximum attainable performance?
- [ ] **(a)** 1000 GFLOP/s
- [ ] **(b)** 25 GFLOP/s
- [ ] **(c)** 250 GFLOP/s
- [ ] **(d)** 4 GFLOP/s

#### Q21. Which Intel oneAPI tool is specifically designed to automatically generate Roofline Model charts and evaluate vectorization efficiency for HPC code?
- [ ] **(a)** Intel Advisor
- [ ] **(b)** Intel Distribution for Python
- [ ] **(c)** Intel Data Analytics Acceleration Library
- [ ] **(d)** Intel Quantum Simulator

#### Q22. Why is InfiniBand preferred over standard 1GbE/10GbE TCP/IP Ethernet for multi-node distributed deep learning training?
- [ ] **(a)** InfiniBand cables are made of gold rather than copper.
- [ ] **(b)** InfiniBand provides Remote Direct Memory Access (RDMA) that bypasses the host operating system kernel and CPU, achieving sub-microsecond latency and line rates up to 200-400 Gbps.
- [ ] **(c)** InfiniBand cannot run Python programs.
- [ ] **(d)** Ethernet switches do not support floating-point data.

#### Q23. In OpenMP applications running on Intel Xeon processors, what does setting 'OMP_PROC_BIND=close' accomplish?
- [ ] **(a)** It closes all open files on disk when a thread completes.
- [ ] **(b)** It binds worker threads to contiguous physical CPU cores located close to each other on the same socket, maximizing shared L3 cache locality.
- [ ] **(c)** It forces threads to shut down after 10 seconds.
- [ ] **(d)** It prevents threads from executing math operations.

#### Q24. What is the primary diagnostic takeaway when an Intel VTune profile shows high 'Core Bound -> Port Contention'?
- [ ] **(a)** The network switch ports are unplugged.
- [ ] **(b)** Execution units inside the CPU core (e.g., FMA vector units or branch units) are over-subscribed, causing ready uOps to wait in the reservation station for an available execution port.
- [ ] **(c)** The CPU needs more thermal paste.
- [ ] **(d)** The hard drive read head is misaligned.

#### Q25. How does combining Slurm job accounting with Intel VTune profiling empower HPC facility directors and lead researchers?
- [ ] **(a)** It allows them to trade supercomputer time on stock exchanges.
- [ ] **(b)** It provides quantitative proof of hardware efficiency, isolating whether multi-node scaling bottlenecks stem from cluster network fabric latency, CPU memory saturation, or inefficient algorithmic implementations.
- [ ] **(c)** It automatically generates research papers without human authorship.
- [ ] **(d)** It replaces all system administrators with machine learning models.

