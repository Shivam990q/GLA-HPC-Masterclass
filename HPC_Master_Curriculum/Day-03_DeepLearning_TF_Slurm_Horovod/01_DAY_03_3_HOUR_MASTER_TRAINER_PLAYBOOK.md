# ⏱️ DAY 3: 3-HOUR COMPLETE MASTER TRAINER PLAYBOOK
## Deep Learning on HPC: TensorFlow-MKL, Slurm Batch Scheduling & Habana Gaudi
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Session Duration:** Exactly 3 Hours (180 Minutes)  
**Official Syllabus Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 🎯 1. Official Syllabus Scope (Day 3 — Strictly Preserved)

The official curriculum specifies **strictly 7 topics for Day 3**:
1. **ML workflows on HPC systems, Optimized libraries**
2. **Introduction to hardware-aware ML optimization**
3. **Intel-optimized TensorFlow (tensorflow-mkl, oneDNN)**
4. **Running DL models on Intel GPUs (Xeon, Habana Gaudi)**
5. **Slurm job scheduling for Deep Learning (batch jobs, resource allocation)**
6. **Training TensorFlow with Horovod**
7. **Distributed training using Horovod**

---

## ⏰ 2. Realistic 180-Minute (3-Hour) Delivery Timeline

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                        DAY 3 TIMELINE (TOTAL: 180 MINUTES)                               |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  00:00 - 00:35 (35m) │ PART 1: The Deep Learning HPC Stack & Hardware-Aware ML           |
|                      │        (Vector Registers, Fused Operators, oneDNN Primitives)     |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  00:35 - 01:10 (35m) │ PART 2: Intel-Optimized TensorFlow & Silicon Mapping              |
|                      │        (TF_ENABLE_ONEDNN_OPTS, Xeon AMX vs Gaudi Accelerators)   |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:10 - 01:20 (10m) │ ☕ REJUVENATION BREAK (10 Minutes)                                |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:20 - 02:00 (40m) │ PART 3: Slurm Workload Manager & Cluster Batch Scheduling        |
|                      │        (Login Node Rule, #SBATCH Directives, sbatch, squeue)      |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:00 - 02:45 (45m) │ PART 4: Distributed Training with Horovod Ring-Allreduce          |
|                      │        (Parameter Server vs Ring-Allreduce, Horovod Wrappers)     |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:45 - 03:00 (15m) │ PART 5: Assessment, 25 MCQs & Wrap-Up                             |
|                      │        (5 Evaluated MCQs + Review & Day 4 Preview)                |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 🎙️ 3. Line-by-Line Minute-by-Minute Trainer Delivery Script

### PART 1 & 2: Hardware-Aware Deep Learning & oneDNN (00:00 - 01:10 | 70 Mins)
- **Concept:** Why standard deep learning frameworks leave performance on the table.
- **What Trainer Says:**
  > "Standard PyPI TensorFlow is compiled for generic x86 CPUs without AVX-512 or AMX optimizations.
  > In HPC, we activate **Intel oneDNN (Deep Neural Network Library)**.
  > oneDNN fuses operations: Convolution + BiasAdd + ReLU into a single pass through CPU L1/L2 cache, eliminating redundant round-trips to main DRAM memory.
  > To enable oneDNN in standard TensorFlow, set:
  > `export TF_ENABLE_ONEDNN_OPTS=1`
  > This immediately accelerates matrix convolutions by 3x to 5x with zero model changes!"

---

### ☕ BREAK (01:10 - 01:20 | 10 Minutes)

---

### PART 3: Slurm Workload Manager & Batch Jobs (01:20 - 02:00 | 40 Mins)
- **Concept:** Multi-tenant cluster scheduling.
- **What Trainer Says:**
  > "The golden rule of supercomputing: *NEVER run heavy workloads directly on the login node!*
  > The login node is shared by dozens of users. If you train a model there, you crash the server.
  > Instead, we write a **Slurm batch script (`#SBATCH`)** and submit it to the scheduler using `sbatch`.
  > Slurm checks cluster queues, allocates requested compute nodes, runs your job in the background, and writes stdout/stderr to log files."
- **Deconstruct the Script:**
  ```bash
  #!/bin/bash
  #SBATCH --job-name=dl_train
  #SBATCH --nodes=2
  #SBATCH --partition=gpu-intel
  #SBATCH --time=02:00:00
  srun python3 train_model.py
  ```

---

### PART 4: Distributed Training with Horovod (02:00 - 02:45 | 45 Mins)
- **Concept:** Scaling across multiple nodes with Ring-Allreduce.
- **What Trainer Says:**
  > "Why does training on 8 nodes sometimes run slower than 1 node? The Communication Bottleneck!
  > In a traditional Parameter Server architecture, one central server gets choked with gradient updates from all workers.
  > **Horovod uses the Ring-Allreduce algorithm**.
  > Workers pass gradient chunks in a logical ring to their neighbors. Bandwidth is perfectly balanced, enabling near-linear scaling across cluster nodes!"
- **Code Wrapper:**
  ```python
  import horovod.tensorflow as hvd
  hvd.init()
  opt = hvd.DistributedOptimizer(opt)
  ```

---

### PART 5: Assessment & Wrap-Up (02:45 - 03:00 | 15 Mins)
- Review 5 core MCQs and connect to Day 4 (Distributed Optimization & VTune Profiling).
