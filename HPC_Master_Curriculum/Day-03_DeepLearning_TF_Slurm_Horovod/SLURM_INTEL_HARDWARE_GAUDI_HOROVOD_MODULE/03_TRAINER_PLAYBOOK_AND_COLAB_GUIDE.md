# 🎙️ MASTER TRAINER PLAYBOOK & COLAB EXECUTION GUIDE
## Slurm Scheduling, Intel Hardware, Habana Gaudi & Horovod Distributed Training
**Course Code:** `GLA-HPC-BCSG701` | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Session:** Day 3 Dedicated Afternoon Masterclass  
**Module Directory:** [`c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\Day-03_DeepLearning_TF_Slurm_Horovod\SLURM_INTEL_HARDWARE_GAUDI_HOROVOD_MODULE`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-03_DeepLearning_TF_Slurm_Horovod/SLURM_INTEL_HARDWARE_GAUDI_HOROVOD_MODULE)

---

## 🧭 EXECUTIVE OVERVIEW & CLASSROOM PACING

This guide provides the exact section-by-section roadmap for teaching:
1. **Slurm job scheduling, batch jobs, and resource allocation**
2. **Running DL models on Intel hardware (Xeon, Intel GPU Max 1550) and Habana Gaudi (Gaudi 2/3)**
3. **Training TensorFlow with Horovod & Distributed training using Horovod**

### ⏱️ Recommended Lecture Schedule (3 Hours Total)
- **Hour 1 (01:30 PM - 02:30 PM):** Slurm Cluster Architecture, `#SBATCH` Scripts & Queue Management.
- **Hour 2 (02:30 PM - 03:30 PM):** Intel Hardware Acceleration (AMX/VNNI, oneDNN Fusion, GPU Max 1550 & Habana Gaudi 2/3).
- **Hour 3 (03:30 PM - 04:30 PM):** Horovod Distributed Data-Parallelism (Ring-AllReduce Math, 4-Rank Multi-Process Colab Lab & 15-Q Quiz).

---

## 💻 PART 1: EXACT COLAB NOTEBOOK MAPPING (WHICH SECTION TO COVER)

You can run these sections either in the **Master Day 3 Notebook** (`Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb`) or in the **Dedicated Module Notebook** (`Dedicated_Slurm_Intel_Gaudi_Horovod_HandsOn.ipynb`):

```
+─────────────────────────────────────────────────────────────────────────────────────────────────────────+
|                                    COLAB NOTEBOOK EXECUTION MATRIX                                      |
+──────────────────────────┬────────────────────────────┬─────────────────────────────────────────────────+
| Required Syllabus Topic  | Master Notebook Section    | Dedicated Module Notebook Section               |
+──────────────────────────┼────────────────────────────┼─────────────────────────────────────────────────+
| 1. Slurm Job Scheduling  | SECTION 8 (Cells 21–24)    | PART 1: Slurm Workload Scheduling & #SBATCH     |
| 2. Intel Xeon & oneDNN   | SECTION 4 & 6 (Cells 9–16) | PART 2: Intel oneDNN Operator Fusion Benchmark  |
| 3. Intel GPU & Gaudi     | SECTION 7 (Cells 17–20)    | PART 3: Intel GPU Max 1550 & Habana Gaudi Probe |
| 4. Horovod Distributed DL| SECTION 9 (Cells 25–28)    | PART 4: 4-Rank Horovod Ring-AllReduce Training  |
+──────────────────────────┴────────────────────────────┴─────────────────────────────────────────────────+
```

---

## 📌 MODULE 1: SLURM JOB SCHEDULING, BATCH JOBS & RESOURCE ALLOCATION

### 1. Colab Section to Cover:
- Open **Section 8** in Colab (`SECTION 8: Slurm Job Scheduling for Deep Learning`).
- **Run Cell 21:** Starts the `munge` authentication daemon and initializes `slurmctld` and `slurmd`.
- **Run Cell 22:** Generates `train_resnet_hpc.slurm`.
- **Run Cell 23:** Submits batch job via `sbatch`, inspects queue with `squeue`, and shows log output.

### 2. Trainer Speaking Script:
> **Say this:**  
> *"Students, on your personal laptop you simply run `python train.py`. But in an enterprise HPC center with 1,000 servers and 200 users, running jobs directly on the login node is strictly forbidden—it exhausts shared RAM and crashes the server for the entire university! Slurm is the central traffic controller that arbitrates resource allocation, schedules queued jobs, and guarantees fair access across all compute nodes."*

### 3. Key Concepts to Draw on the Whiteboard / Project:
1. **Head/Login Node vs Compute Nodes:**
   - Login Node runs `slurmctld` (the controller).
   - Compute Nodes run `slurmd` (the worker agent).
2. **Deconstructing `#SBATCH` Directives:**
   - `--nodes=2`: Requests 2 physical discrete servers.
   - `--ntasks-per-node=4`: 4 MPI process ranks per node (Total 8 ranks across cluster).
   - `--cpus-per-task=8`: 8 CPU hardware threads allocated per task for high-speed data loading.
   - `--time=02:00:00`: Hard walltime limit. Prevents runaway processes from blocking queues.
   - `--output=logs/%x_%j.out`: `%j` dynamically substitutes the unique numeric Job ID allocated by Slurm.
3. **The 4 Essential Slurm Commands:**
   - `sbatch script.slurm` $\to$ Submit batch script.
   - `squeue -u $USER` $\to$ Check running (`R`) vs pending (`PD`) status.
   - `sinfo` $\to$ View node partition availability (allocated, idle, drained).
   - `scancel <job_id>` $\to$ Abort a runaway or deadlocked job.

### 4. Interactive Visual Demo:
- Switch to [**`01_interactive_animations.html`**](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-03_DeepLearning_TF_Slurm_Horovod/SLURM_INTEL_HARDWARE_GAUDI_HOROVOD_MODULE/01_interactive_animations.html), click **Tab 1: Slurm Job Scheduling**.
- Press **`Z`** for Projector Zoom. Click **"Step Slurm Batch Job Lifecycle"** to demonstrate state transitions: `sbatch` $\to$ `PENDING (PD)` $\to$ `RUNNING (R)` $\to$ `COMPLETED (CD)`.

---

## 📌 MODULE 2: RUNNING DL MODELS ON INTEL HARDWARE & HABANA GAUDI

### 1. Colab Section to Cover:
- Open **Section 6 & 7** in Colab (`SECTION 6: Intel-Optimized TensorFlow (oneDNN)` & `SECTION 7: Running Deep Learning Models on Intel GPUs & Habana Gaudi`).
- **Run Cell 14:** Executes `benchmark_onednn_fusion.py` measuring `Conv2D + BatchNorm + ReLU` latency and memory traffic.
- **Run Cell 18:** Runs `intel_gpu_xpu_check.py` (Xe-HPC Ponte Vecchio architecture probe).
- **Run Cell 20:** Runs `habana_gaudi_synapse_check.py` (SynapseAI & MME compute probe, computing 340.8 BF16 TFLOPS peak).

### 2. Trainer Speaking Script:
> **Say this:**  
> *"In modern supercomputing, deep learning is heterogeneous. You must master three physical silicon platforms:  
> 1. **Intel 4th/5th Gen Xeon Scalable CPUs:** Powered by **AMX (Advanced Matrix Extensions)**, achieving **2,048 INT8 ops per clock cycle** directly on the host CPU!  
> 2. **Intel oneDNN Operator Fusion:** Fuses Conv2D, BatchNorm, and ReLU in L1/L2 cache, crushing the DRAM memory wall and cutting bus traffic by 75%!  
> 3. **Habana Gaudi 2 & 3:** Purpose-built for massive LLM training. Its secret weapon is **24 integrated 100GbE RoCEv2 RDMA ports directly on the silicon substrate**, eliminating external PCIe network cards and cluster switches!"*

### 3. Core Architecture Points:
- **DRAM Memory Wall (Show Visual Tab 3):**
  - Unfused Conv2D flushes intermediate feature maps out to slow DRAM (12.8 MB traversed).
  - oneDNN Fused kernel keeps intermediate tensors hot in L1/L2 cache lines (64 bytes). DRAM traffic reduced to 3.2 MB (75% savings).
- **Intel Data Center GPU Max 1550 (Show Visual Tab 4):**
  - 128 Xe Cores with 1,024 XMX systolic engines.
  - 128 GB of HBM2e memory delivering 3.2 TB/s bandwidth.
  - Programmed via open-standard SYCL / DPC++ through Intel oneAPI.
- **Habana Gaudi 2/3 (Show Visual Tab 4):**
  - Dual Matrix Multiplication Engines (MMEs) + 8 Tensor Processor Cores (TPCs).
  - 24 on-die 100GbE RoCEv2 ports forming an All-to-All direct scale-out mesh.

---

## 📌 MODULE 3 & 4: TRAINING TENSORFLOW WITH HOROVOD & DISTRIBUTED TRAINING

### 1. Colab Section to Cover:
- Open **Section 9** in Colab (`SECTION 9: Distributed Deep Learning: Training TensorFlow with Horovod`).
- **Run Cell 25:** Writes `distributed_tf_horovod.py`.
- **Run Cell 26:** Launches the real multi-process distributed training job:
  ```bash
  mpirun -n 4 --allow-run-as-root python3 distributed_tf_horovod.py
  ```
- **Show Students the Verified Live Output:**
  ```text
  [Rank 0] Epoch 1/3 Complete | Loss: 0.7052 | Throughput: 894.2 samples/sec
  [Rank 0] Epoch 2/3 Complete | Loss: 0.6733 | Throughput: 902.1 samples/sec
  [Rank 0] Epoch 3/3 Complete | Loss: 0.6587 | Throughput: 906.4 samples/sec
  [+] 4-Worker Cluster Throughput : 900.9 samples / sec
  [+] Scaling Efficiency         : 98.5 %
  ```

### 2. Trainer Speaking Script:
> **Say this:**  
> *"Why did parameter servers fail at scale? Because in parameter server mode, every worker sends gradients to one central server. At 32 nodes, the central server's network cable saturates with $2(N-1)S$ bytes of traffic!  
> Horovod uses **Baidu's Ring-AllReduce algorithm**. Nodes pass chunks in a circle ($0 \to 1 \to 2 \to 3 \to 0$). In two phases—Scatter-Reduce and All-Gather—every node sends exactly $2 \frac{N-1}{N} S$ bytes. **The bandwidth required per worker is completely independent of the number of nodes in the cluster!**"*

### 3. The 6 Invariant Rules of Horovod Code (Walk Through Line-by-Line):
```python
import tensorflow as tf
import horovod.tensorflow as hvd

# 1. Initialize Horovod Communicator
hvd.init()

# 2. Pin Hardware Device to Local Rank
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    tf.config.set_visible_devices(gpus[hvd.local_rank()], 'GPU')

# 3. Linear Learning Rate Scaling Rule (Goyal et al.)
# Effective batch size is multiplied by N, so scale learning rate proportionally!
base_lr = 0.001
scaled_lr = base_lr * hvd.size()
opt = tf.optimizers.Adam(scaled_lr)

# 4. Wrap Optimizer for Ring-AllReduce Interception
opt = hvd.DistributedOptimizer(opt)

# 5. Broadcast Initial Weights from Rank 0
hvd.broadcast_variables(model.variables, root_rank=0)

# 6. Rank-0 Disk Isolation
# ONLY Rank 0 writes logs and saves checkpoints to prevent disk write collisions!
if hvd.rank() == 0:
    model.save("checkpoints/model.keras")
```

### 4. Interactive Visual Demo:
- Switch to [**`01_interactive_animations.html`**](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-03_DeepLearning_TF_Slurm_Horovod/SLURM_INTEL_HARDWARE_GAUDI_HOROVOD_MODULE/01_interactive_animations.html), click **Tab 5: Ring-AllReduce Scaling**.
- Click **"Step Ring-AllReduce Phase"** to watch the circular token rotation across Rank 0, 1, 2, and 3 through Phase 1 (Scatter-Reduce) and Phase 2 (All-Gather).

---

## 🏆 PART 5: LIVE CLASSROOM ASSESSMENT

1. Open [**`02_interactive_quiz.html`**](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-03_DeepLearning_TF_Slurm_Horovod/SLURM_INTEL_HARDWARE_GAUDI_HOROVOD_MODULE/02_interactive_quiz.html) in your browser.
2. Toggle **Projector Zoom (`Z` key)**.
3. Conduct the 15-question quiz interactively with the classroom:
   - Ask students for their answer before clicking.
   - Click the chosen option to reveal immediate Green/Red feedback.
   - Read the `.why` architectural rationale box aloud to reinforce physical hardware and scheduler mechanisms.

