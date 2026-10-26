# 🎓 DAY 4: MASTER PRESENTATION & SPEAKER NOTES
## Distributed AI Training & Performance Profiling with Intel VTune
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Target Audience:** B.Tech / M.Tech Computer Science (60 Students)  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 🏛️ 1. Syllabus Boundary & Scope (Day 4)

```
+─────────────────────────────────────────────────────────────────────────────────────────+
|                                DAY 4 SYLLABUS BOUNDARY                                  |
+─────────────────────────────────────────────────────────────────────────────────────────+
|  [DAY 4: IN-SCOPE]                                                                      |
|  1. Horizontal vs Vertical Scaling (The Memory Wall, Network Friction, Multi-Node DL)   |
|  2. Horovod Ring-Allreduce Distributed Scaling (Tensor Fusion, Learning Rate Warmup)   |
|  3. Multi-Node Slurm Resource Mapping (--ntasks-per-node, Core Pinning, MPI Binding)    |
|  4. The Optimization Gap (Why unprofiled code fails to scale linearly across nodes)    |
|  5. Intel VTune Profiler Architecture (Hotspots, Microarchitecture Exploration)        |
|  6. Threading & Memory Profiling (Lock Contention, False Sharing, DRAM Bandwidth)      |
|  7. Performance Diagnostic Matrix & Iterative Optimization Pipeline                     |
+─────────────────────────────────────────────────────────────────────────────────────────+
|  [DAY 5: FUTURE SCOPE - DO NOT PRE-EMPT ON DAY 4]                                       |
|  Generative AI & Transformer Architecture (Day 5)                                       |
|  OpenVINO IR Conversion & INT4 Weight-Only Quantization (Day 5)                         |
|  Habana Gaudi SynapseAI & Distributed LLM Fine-Tuning (Day 5)                           |
+─────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 📋 2. Complete Topic & Subtopic Breakdown (Day 4)

### Topic 1: The Horizontal Scaling Imperative
- **The Limits of Vertical Scaling:** Upgrading to a single machine with 2TB RAM and 8 GPUs hits severe physical cost, thermal density, and PCIe bus limitations.
- **Horizontal Scaling:** Pooling discrete compute nodes connected via high-speed low-latency fabrics (InfiniBand HDR/NDR or 100GbE RoCE).
- **The Communication Friction:** Network serialization, packet drops, tail latency, and gradient synchronization bottlenecks.

### Topic 2: Scaling Distributed Training with Horovod
- **Ring-Allreduce Deep Dive:** Each worker communicates only with its left and right neighbors. Time to synchronize gradients is independent of the number of nodes!
  $$\text{Transfer Time} = 2 \cdot \frac{N - 1}{N} \cdot \frac{M}{B}$$
  *(where $N$ is number of nodes, $M$ is model size in bytes, $B$ is network bandwidth).*
- **Tensor Fusion:** Combining thousands of tiny gradient buffers into a single contiguous ring buffer (e.g. 64MB) to minimize network packet overhead.
- **Learning Rate Warmup & Scaling:** Linear scaling rule: when batch size increases by factor of $K$ (across $K$ workers), learning rate must scale by $K$, backed by a gradual 5-epoch warmup to prevent divergent initial gradients.

### Topic 3: Multi-Node Slurm Orchestration
- Coordinating multi-node tasks:
  ```bash
  #SBATCH --nodes=4
  #SBATCH --ntasks-per-node=2
  #SBATCH --cpus-per-task=16
  #SBATCH --partition=gpu-intel

  mpirun -np 8 --bind-to socket python3 train_horovod.py
  ```
- **CPU Binding & Core Pinning:** Ensuring MPI/Horovod processes stay pinned to physical CPU sockets rather than bouncing between cores, preventing destructive L1/L2 cache invalidations.

### Topic 4: The Optimization Gap & Why Profiling Matters
- **The Fallacy of "Just Add More Nodes":** Doubling nodes on an unoptimized model often yields 10% speedup or even slowdown due to communication overhead, I/O blocking, and thread contention.
- **Closing the Gap:** Profiling hardware telemetry to achieve near-linear 90%+ parallel efficiency.

### Topic 5: Inside Intel VTune Profiler
- **What is Intel VTune?** The industry-standard microarchitectural analysis tool designed to inspect execution bottlenecks on x86 silicon.
- **Core Analysis Modes:**
  1. *Hotspots Analysis:* Identifies the exact functions and source code lines consuming the greatest percentage of CPU time.
  2. *Microarchitecture Exploration:* Deconstructs CPU pipeline execution according to the Top-Down Characterization Methodology:
     - Frontend Bound (Instruction cache misses, branch decode latency)
     - Bad Speculation (Branch mispredictions)
     - Backend Bound (Core execution stall, Memory stall)
     - Retiring (Instructions successfully completing)
  3. *Memory Access Profiling:* Measures DRAM bandwidth saturation, NUMA cross-node traffic, and L1/L2/L3 cache miss ratios.
  4. *Threading & Concurrency Analysis:* Visualizes OpenMP and POSIX thread utilization, lock wait times, and thread synchronization overhead.

### Topic 6: The Performance Diagnostic Matrix
| Observed Symptom | VTune Telemetry Indicator | Root Cause | Hardware-Aware Solution |
| :--- | :--- | :--- | :--- |
| High wait time between training epochs | Elevated I/O Wait / Storage Latency | CPU waiting for disk reads | Implement PyTorch `DataLoader(pin_memory=True, num_workers=8)` and prefetching |
| Low CPU/GPU utilization during active compute | High Thread Lock Wait / Spin Time | Thread contention or poor batch sizing | Tune OpenMP thread pool (`OMP_NUM_THREADS`), increase batch size to fill matrix units |
| Scaling efficiency drops sharply at 4+ nodes | Horovod Ring-Allreduce Wait latency | Network packet overhead on small tensors | Increase Horovod Tensor Fusion buffer (`HOROVOD_AUTOTUNE=1`), tune RoCE MTU |

### Topic 7: The Iterative Hardware-Aware Optimization Loop
```
[ 01. EXECUTE ] ──► [ 02. PROFILE ] ──► [ 03. ANALYZE ] ──► [ 04. OPTIMIZE ] ──► (Repeat)
Submit job via      Capture raw hardware   Inspect hotspots &    Tune parameters &
Slurm batch script  telemetry with VTune   microarchitecture     refactor hot loops
```

---

## 🖥️ 3. Slide-by-Slide Speaker Notes

*Mapped to the 13 Slides of `Day_04_NotebookLM_Master_Deck.pptx`*

- **Slide 1: High Performance Computing: Day 4**  
  *Speaker Point:* "Welcome to Day 4! Today we tackle the greatest challenge in supercomputing: Scaling distributed models across an entire cluster and profiling silicon bottlenecks with Intel VTune."
- **Slide 2: Cluster-Based Reality**  
  *Speaker Point:* "Remind students: We are not guessing or running toys. We are profiling real hardware metrics on multi-core nodes."
- **Slide 3: Day 4 Focus Area**  
  *Speaker Point:* "Break down the stack: VTune Profiler on top, TensorFlow-MKL and Horovod in the framework layer, Slurm and Linux in the infrastructure layer."
- **Slide 4: Workflow Optimization Process**  
  *Speaker Point:* "Walk through the 4 steps: Orchestrate with Slurm -> Scale with Horovod -> Profile with VTune -> Optimize and re-run."
- **Slide 5: The Wall: Vertical vs Horizontal Scaling**  
  *Speaker Point:* "Explain what happens when an AI model hits 100GB. No single server can hold it. We must scale horizontally, but horizontal scaling introduces network latency and synchronization friction."
- **Slide 6: Cluster Workflow & Resource Allocation**  
  *Speaker Point:* "Explain how Slurm inspects hardware attributes (AVX-512, AMX, GPU memory) to assign jobs to the optimal compute nodes."
- **Slide 7: Multi-Node Slurm Directives**  
  *Speaker Point:* "Deconstruct `#SBATCH --nodes=4`, `#SBATCH --ntasks-per-node=2`, and `mpirun -np 8 python3 train_horovod.py`."
- **Slide 8: The Optimization Gap: Why Profiling Matters**  
  *Speaker Point:* "Point to the curve: Ideal linear scaling vs Reality curve. Show that without VTune profiling, scaling degrades rapidly after 4 nodes due to communication overhead."
- **Slide 9: Inside Intel VTune Profiler**  
  *Speaker Point:* "Explain the 4 key views: Hotspot analysis, Microarchitecture exploration, Threading efficiency, and Memory access profiling."
- **Slide 10: Performance Diagnostic Matrix**  
  *Speaker Point:* "Walk through the diagnostic table: How to translate a slow training loop into exact hardware metrics and concrete engineering fixes."
- **Slide 11: Iterative Optimization Pipeline**  
  *Speaker Point:* "Emphasize the scientific method in HPC: Never guess. Measure baseline, profile with VTune, change ONE parameter, and measure again."
- **Slide 12: Distributed AI Workflow: The Complete Loop**  
  *Speaker Point:* "Review the unified diagram: Python Code + Slurm Config -> Cluster Execution -> VTune Performance Report -> Hardware-Aware Optimization."
- **Slide 13: The Path Forward to Day 5**  
  *Speaker Point:* "Preview the grand capstone: Tomorrow on Day 5, we combine everything to deploy, fine-tune, and optimize massive Large Language Models using Habana Gaudi and OpenVINO!"

---

## 🔬 4. Lab Hands-On Synchronization

- **Lab 1:** Setting up a multi-process distributed training job with Horovod Ring-Allreduce on synthetic gradient data.
- **Lab 2:** Running Intel VTune CLI (`vtune -collect hotspots`) on an unoptimized loop to generate a hotspot report.
- **Lab 3:** Identifying thread lock overhead, fixing core pinning with `OMP_PROC_BIND=spread`, and re-profiling to verify 2x throughput gain.
