# ⏱️ DAY 3: 3-HOUR COMPLETE MASTER TRAINER PLAYBOOK
## Deep Learning on HPC with TensorFlow, Slurm & GPUs
**Course Code:** `GLA-HPC-BCSG701` | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Session:** Day 3 (Strictly 3 Hours / 180 Minutes)  
**Official Syllabus Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 🎯 1. Official Syllabus Scope (Day 3 Topics)
1. **ML workflows on HPC systems, Optimized libraries**
2. **Introduction to hardware-aware ML optimization**
3. **Intel-optimized TensorFlow (tensorflow-mkl, oneDNN)**
4. **Running DL models on Intel GPUs (Xeon, Habana Gaudi)**
5. **Slurm job scheduling for Deep Learning (batch jobs, resource allocation)**
6. **Training TensorFlow with Horovod & Distributed training**

---

## ⏰ 2. Realistic 180-Minute (3-Hour) Delivery Timeline

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                        DAY 3 TIMELINE (TOTAL: 180 MINUTES)                               |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  00:00 - 00:30 (30m) │ PART 1: Hardware-Aware DL & Intel oneDNN Primitives               |
|                      │        (Operator Fusion, AMX Matrix Engines, tensorflow-mkl)     |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  00:30 - 01:05 (35m) │ PART 2: Accelerators in HPC: Intel GPU Max & Habana Gaudi 2/3     |
|                      │        (MME Systolic Arrays, TPCs, Integrated 24x 100GbE RoCE)    |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:05 - 01:15 (10m) │ ☕ REJUVENATION BREAK (10 Minutes)                                |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:15 - 01:50 (35m) │ PART 3: Supercomputer Orchestration with Slurm Workload Manager   |
|                      │        (sbatch, squeue, slurmd, Resource Allocations, GPU binding)|
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:50 - 02:40 (50m) │ PART 4: Distributed Deep Learning with Horovod                   |
|                      │        (Ring-AllReduce, hvd.init(), Gradient Sync, Scaling Math)  |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:40 - 03:00 (20m) │ PART 5: Live Distributed Training Benchmark & 25 MCQs Review      |
|                      │        (Multi-worker scaling throughput images/sec, Day 4 preview)|
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 🎙️ 3. Line-by-Line Minute-by-Minute Trainer Delivery Script

### PART 1: Hardware-Aware DL & Intel oneDNN (00:00 - 00:30 | 30 Mins)
* **Slide Alignment:** Day 3 Slide Deck (Slides 1–5: Deep Learning on HPC & oneDNN).
* **Concept:** Moving from traditional ML to Deep Learning; hardware operator fusion.
* **Trainer Script:**
  > "Welcome to Day 3 of the HPC Masterclass!
  > Yesterday we saw how Scikit-learn accelerates traditional machine learning. Today, we step into the massive scale of **Deep Learning on HPC clusters**.
  > When training a deep convolutional neural network or a Transformer, millions of matrix multiplications occur every second.
  > If you run generic TensorFlow, every layer writes its output back to DRAM, and the next layer reads it back over the memory bus. This creates a massive **Memory Wall bottleneck**.
  > Intel created **oneDNN (oneAPI Deep Neural Network Library)** to eliminate this!
  > Look at **Operator Fusion**: instead of doing Convolution $\to$ Write to RAM $\to$ Read from RAM $\to$ ReLU, oneDNN combines them into a single fused hardware kernel! The ReLU activation executes while the intermediate activations are still hot in CPU L1 cache.
  > On modern 4th/5th Gen Intel Xeon CPUs, oneDNN activates **Intel AMX (Advanced Matrix Extensions)**—specialized silicon tile registers (`tmm0`–`tmm7`) that compute 1024 BF16 operations in a single clock cycle!"

---

### PART 2: DL Accelerators: Intel GPU Max & Habana Gaudi (00:30 - 01:05 | 35 Mins)
* **Slide Alignment:** Day 3 Slide Deck (Slides 6–10: The Accelerator Continuum).
* **Concept:** Intel Data Center GPU Max 1550 vs. Habana Gaudi 2/3.
* **Trainer Script:**
  > "Now let's compare our accelerator options for deep learning:
  > 1. **Intel Xeon CPU**: Perfect for data loaders, preprocessing, inference on INT8/BF16 via AMX, and medium-sized neural networks.
  > 2. **Intel Data Center GPU Max (Ponte Vecchio)**: Features up to 128 Xe-cores and 128 GB of ultra-fast HBM2e memory delivering over 3.2 Terabytes/sec of bandwidth.
  > 3. **Habana Gaudi (Gaudi 2 & Gaudi 3)**: Purpose-built for massive AI training and large models.
  > Why is Gaudi unique? In traditional GPU clusters, you must purchase expensive external Mellanox InfiniBand network cards.
  > **Habana Gaudi integrates 24 ports of 100/200 Gigabit RoCE (RDMA over Converged Ethernet) DIRECTLY ON THE SILICON DIE!**
  > That means Gaudi accelerators communicate directly in an all-to-all cluster fabric with zero external network cards!"

---

### ☕ BREAK (01:05 - 01:15 | 10 Minutes)

---

### PART 3: Supercomputer Orchestration with Slurm (01:15 - 01:50 | 35 Mins)
* **Slide Alignment:** Day 3 Slide Deck (Slides 11–15: Slurm Architecture & Batch Jobs).
* **Concept:** Resource managers, non-interactive execution, `#SBATCH` directives.
* **Trainer Script:**
  > "Class, in an enterprise HPC cluster or national supercomputer, you NEVER run deep learning by typing `python train.py` directly into the login terminal!
  > If 60 researchers do that, the login node crashes.
  > Instead, supercomputers use **Slurm (Simple Linux Utility for Resource Management)**.
  > Slurm has two main engines:
  > - `slurmctld`: The master controller that manages the job queue.
  > - `slurmd`: The worker daemon running on each compute node.
  > You write a **Slurm batch script** (`job.slurm`) with resource requests:
  > `#SBATCH --nodes=4` (give me 4 physical servers)
  > `#SBATCH --ntasks-per-node=8` (launch 8 processes per server)
  > `#SBATCH --cpus-per-task=4` (give each process 4 CPU cores)
  > `#SBATCH --time=02:00:00` (time limit 2 hours)
  > You submit it using `sbatch job.slurm`. Slurm queues the job, allocates the physical servers when available, executes your workload, and writes logs to `/scratch`!"

---

### PART 4: Distributed Deep Learning with Horovod (01:50 - 02:40 | 50 Mins)
* **Slide Alignment:** Day 3 Slide Deck (Slides 16–22: Ring-AllReduce & Horovod).
* **Concept:** Overcoming parameter-server bottlenecks via Ring-AllReduce.
* **Trainer Script:**
  > "Now, how do we scale a neural network across 64 GPUs?
  > In old parameter-server architectures, 64 workers all send their gradients to one master server, causing a massive network choke.
  > **Horovod** solves this using the **Ring-AllReduce algorithm**!
  > Workers are arranged in a logical ring. In step 1, each worker sends a fraction of its gradients to its neighbor and receives a fraction. After $2(N - 1)$ transfers, ALL workers have the exact sum of gradients!
  > Look at how simple Horovod makes your TensorFlow code:
  > 1. `import horovod.tensorflow as hvd; hvd.init()`
  > 2. Pin GPU to local rank: `gpus = tf.config.experimental.set_visible_devices(..., gpus[hvd.local_rank()])`
  > 3. Wrap optimizer: `opt = hvd.DistributedOptimizer(opt)`
  > 4. Broadcast weights from Rank 0: `hvd.broadcast_variables(model.variables, root_rank=0)`
  > 5. Scale learning rate: `base_lr * hvd.size()`!
  > With Horovod, you get near-linear 90%+ scaling efficiency across nodes!"

---

### PART 5: Live Benchmark & MCQ Assessment (02:40 - 03:00 | 20 Mins)
* **Activities:**
  1. Have students run the Slurm + Horovod simulation notebook cells.
  2. Measure training throughput in **Images / Second**.
  3. Review the 5 core MCQs from [`03_DAY_03_STUDENT_CHEATSHEET_AND_MCQS.md`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-03_DeepLearning_TF_Slurm_Horovod/03_DAY_03_STUDENT_CHEATSHEET_AND_MCQS.md).
  4. **Day 4 Teaser:** *"Tomorrow on Day 4, we perform multi-node distributed training and master Intel VTune Profiler to hunt down hardware bottlenecks, cache misses, and communication stragglers!"*

---
**Playbook Status:** 100% Complete & Verified | GLA University HPC Masterclass Day 3
