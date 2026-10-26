# 🎓 DAY 3: MASTER PRESENTATION & SPEAKER NOTES
## Deep Learning on HPC: TensorFlow-MKL, Slurm Batch Scheduling & Habana Gaudi
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Target Audience:** B.Tech / M.Tech Computer Science (60 Students)  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 🏛️ 1. Syllabus Boundary & Scope (Day 3)

```
+─────────────────────────────────────────────────────────────────────────────────────────+
|                                DAY 3 SYLLABUS BOUNDARY                                  |
+─────────────────────────────────────────────────────────────────────────────────────────+
|  [DAY 3: IN-SCOPE]                                                                      |
|  1. The Deep Learning HPC Stack (Frameworks, oneDNN Middleware, Slurm, Silicon)         |
|  2. Hardware-Aware Deep Learning (Memory Wall, Cache Alignment, Fused Operations)       |
|  3. Intel-Optimized TensorFlow (oneDNN Primitive Acceleration, AMX INT8/BF16)           |
|  4. Silicon Selection: Intel Xeon Scalable CPUs vs Habana Gaudi AI Accelerators         |
|  5. HPC Multi-Tenancy & Slurm Workload Manager (Login Nodes vs Compute Partitions)      |
|  6. Writing Slurm Batch Scripts (#SBATCH Directives, Resource Requests, sbatch/squeue)  |
|  7. Introduction to Distributed Deep Learning (Parameter Server vs Ring-Allreduce)     |
+─────────────────────────────────────────────────────────────────────────────────────────+
|  [DAY 4-5: FUTURE SCOPE - DO NOT PRE-EMPT ON DAY 3]                                     |
|  Horovod Advanced Ring-Allreduce & Multi-Node Cluster Scaling (Day 4)                   |
|  Intel VTune Deep Microarchitecture Profiling (Day 4)                                   |
|  Generative AI, Large Language Models, OpenVINO IR Export & INT4 Quantization (Day 5)   |
+─────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 📋 2. Complete Topic & Subtopic Breakdown (Day 3)

### Topic 1: The Deep Learning HPC Stack
- **Layer 1: Applications & Frameworks:** High-level Python DL frameworks (TensorFlow, PyTorch, Keras).
- **Layer 2: Middleware & Acceleration Libraries:** Intel oneAPI, oneDNN (Deep Neural Network Library), oneMKL.
- **Layer 3: Orchestration & Workload Scheduling:** Linux kernel, Slurm (Simple Linux Utility for Resource Management).
- **Layer 4: Silicon & Interconnects:** Intel Xeon Scalable Processors, Intel Data Center GPU Max, Habana Gaudi 2/3 accelerators.

### Topic 2: Why Hardware-Aware Optimization Matters
- **The Memory Wall in Deep Learning:** Neural networks spend 70%+ of runtime moving weights between DRAM and cache registers, not doing pure math.
- **Cache-Conscious Tiling & Operator Fusion:** Fusing Convolution + BiasAdd + ReLU into a single pass through L1/L2 cache lines to eradicate off-chip DRAM memory trips.
- **Vector Registers & Mixed Precision:** Leveraging AVX-512 VNNI (Vector Neural Network Instructions) and AMX (Advanced Matrix Extensions) for BF16 and INT8 tensor arithmetic.

### Topic 3: Intel-Optimized TensorFlow & oneDNN
- **The Stock TensorFlow Problem:** Upstream PyPI TensorFlow is built for generic x86_64 CPUs, leaving vector and matrix silicon engines completely idle.
- **Intel oneDNN Acceleration:** Seamless runtime replacement of core convolution, GEMM, and pooling operations with hand-tuned assembly kernels.
- **Enabling oneDNN:** Setting environment variables:
  ```bash
  export TF_ENABLE_ONEDNN_OPTS=1
  ```

### Topic 4: Hardware Matrix: Intel Xeon vs Habana Gaudi
- **Intel Xeon Scalable Processors:** Versatile compute, large system memory (up to 4TB DDR5 per socket), master data preprocessing, agile mixed ML/DL inference.
- **Habana Gaudi Accelerators:** Dedicated Deep Learning matrix accelerator featuring 24 Tensor Processor Cores (TPCs), Matrix Multiplication Engines (MME), 96GB HBM2e (2.45 TB/s bandwidth), and 24 integrated 100GbE RoCE RDMA network interfaces.

### Topic 5: Slurm Workload Manager & Cluster Scheduling
- **The Golden Rule of Supercomputing:** *Never run heavy workloads on the login/head node!*
- **Head Node vs Compute Node Topology:** The login node is shared by 50+ users for code editing, compiling small scripts, and queuing jobs. Heavy training runs on worker nodes managed by Slurm.
- **Slurm Architecture:** `slurmctld` (controller daemon on head node) and `slurmd` (worker daemon on compute nodes).
- **Essential Slurm Commands:**
  - `sbatch <job_script.sh>` (Submit non-interactive batch job)
  - `squeue -u $USER` (Inspect status: PENDING, RUNNING, COMPLETED)
  - `scancel <job_id>` (Terminate hung or errant job)
  - `sinfo` (Inspect available nodes and partition health)
  - `srun` (Launch parallel interactive tasks across allocated nodes)

### Topic 6: Writing Industrial `#SBATCH` Scripts
- Anatomy of a cluster batch script:
  ```bash
  #!/bin/bash
  #SBATCH --job-name=gla_dl_train
  #SBATCH --output=logs/%x_%j.out
  #SBATCH --error=logs/%x_%j.err
  #SBATCH --nodes=2
  #SBATCH --ntasks-per-node=4
  #SBATCH --cpus-per-task=8
  #SBATCH --time=02:00:00
  #SBATCH --partition=compute

  # Load environment modules
  source /opt/intel/oneapi/setvars.sh
  export TF_ENABLE_ONEDNN_OPTS=1

  # Launch training across allocated cores
  python3 train_model.py --epochs 50 --batch_size 128
  ```

---

## 🖥️ 3. Slide-by-Slide Speaker Notes

*Mapped to the 15 Slides of `Day_03_NotebookLM_Master_Deck.pptx`*

- **Slide 1: Day 3: Deep Learning on HPC**  
  *Speaker Point:* "Welcome to Day 3! Today, we leave toy datasets behind. We enter the world of enterprise Deep Learning: hardware acceleration with oneDNN, cluster scheduling with Slurm, and modern AI silicon architectures."
- **Slide 2: Day 3 Pedagogical Blueprint**  
  *Speaker Point:* "Our 3 pillars: HPC Principles (memory wall, tensor math), Industrial Tools (oneDNN, Slurm, Gaudi), and Practical Cluster Execution (writing and deploying `#SBATCH` jobs)."
- **Slide 3: The Deep Learning HPC Stack**  
  *Speaker Point:* "Walk students from bottom to top: Physical Silicon -> Slurm OS -> oneAPI Middleware -> High-level TensorFlow."
- **Slide 4: Why Hardware-Aware Optimization Matters**  
  *Speaker Point:* "Contrast the two diagrams: Hardware-Agnostic ML leaves cores idle and starves on memory bandwidth; Hardware-Aware ML fills vector registers and keeps caches saturated."
- **Slide 5: Injecting Performance with oneDNN & MKL**  
  *Speaker Point:* "Show students that by enabling oneDNN in TensorFlow, they get massive acceleration without changing a single line of Keras model architecture code."
- **Slide 6: Hardware Selection: Xeon vs. Gaudi Comparison Matrix**  
  *Speaker Point:* "Analyze the matrix: Use Xeon for preprocessing, pipeline orchestration, and general inference; use Gaudi for massive multi-node training and LLM scaling."
- **Slide 7: Managing Multi-Tenant HPC Resources**  
  *Speaker Point:* "Explain what happens if 60 students run deep neural networks on the login node at the same time: the server crashes! Slurm exists to fairly queue and allocate hardware."
- **Slide 8: System & Hands-On: Slurm Job Scheduling**  
  *Speaker Point:* "Deconstruct the `#SBATCH` directives: `--nodes=4`, `--partition=compute`, `--time=02:00:00`, and `srun`."
- **Slide 9: The Distributed Training Challenge**  
  *Speaker Point:* "Explain why doubling nodes doesn't double training speed: the Communication Bottleneck. As nodes increase, time spent synchronizing gradients overtakes computation."
- **Slide 10: Solving the Bottleneck with Horovod Ring-Allreduce**  
  *Speaker Point:* "Compare Centralized Parameter Server (bottlenecked central bandwidth) vs Ring-Allreduce (decentralized, peer-to-peer ring synchronization)."
- **Slide 11: Implementing Horovod in TensorFlow**  
  *Speaker Point:* "Show the simple wrapper: `hvd.init()`, `hvd.DistributedOptimizer()`, and scaling learning rate by `hvd.size()`."
- **Slide 12: Launching Distributed TF with Slurm**  
  *Speaker Point:* "Show how `srun` launches the distributed processes mapped directly across the Slurm-allocated hardware tasks."
- **Slide 13: Lab Objective: End-to-End AI Workflow**  
  *Speaker Point:* "Review the 4-step lab progression: Prepare Baseline -> Optimize with oneDNN -> Distribute with Horovod -> Execute via Slurm."
- **Slide 14: The Complete Deep Learning HPC Workflow**  
  *Speaker Point:* "Synthesize the full architecture: Code -> Middleware -> Scheduler -> Network -> Silicon."
- **Slide 15: Day 3 Achieved & Next Up (Day 4)**  
  *Speaker Point:* "Celebrate Day 3 accomplishments! Preview Day 4: Opening the black box to profile cache misses and thread contention using Intel VTune."

---

## 🔬 4. Lab Hands-On Synchronization

- **Lab 1:** Benchmarking stock TensorFlow vs Intel oneDNN-accelerated TensorFlow on a Convolutional Neural Network (measure 3x-6x throughput gain).
- **Lab 2:** Writing a complete, error-free `#SBATCH` script with output logging and time limits.
- **Lab 3:** Inspecting cluster status via `sinfo`, submitting with `sbatch`, and monitoring job progression via `squeue`.
