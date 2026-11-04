# 🛠️ HANDS-ON COMMAND RUNBOOK: SLURM, INTEL HARDWARE, GAUDI & HOROVOD
## Terminal Commands, Batch Scripts & Multi-Node Distributed Training
**Course Code:** `GLA-HPC-BCSG701` | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Session:** Day 3 Server Lab  
**Module Directory:** [`c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\Day-03_DeepLearning_TF_Slurm_Horovod\SLURM_INTEL_HARDWARE_GAUDI_HOROVOD_MODULE`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-03_DeepLearning_TF_Slurm_Horovod/SLURM_INTEL_HARDWARE_GAUDI_HOROVOD_MODULE)

---

## 🚀 STAGE 0: ENVIRONMENT PREPARATION & SCRATCH DIRECTORY SETUP

```bash
# 1. Create fast NVMe scratch directories
mkdir -p /scratch/hpc_day03/{scripts,slurm_jobs,logs,checkpoints}
cd /scratch/hpc_day03/scripts

# 2. Enable Intel oneDNN Optimizations globally
export TF_ENABLE_ONEDNN_OPTS=1
echo "export TF_ENABLE_ONEDNN_OPTS=1" >> ~/.bashrc

# 3. Verify Active Python & TensorFlow Environment
python3 -c "
import tensorflow as tf
print('[*] TensorFlow Version:', tf.__version__)
print('[*] Physical Devices Detected:', tf.config.list_physical_devices())
"
```

---

## ⚡ STAGE 1: oneDNN OPERATOR FUSION BENCHMARK

Execute the standalone oneDNN operator fusion benchmark to measure kernel latency and memory bandwidth savings:

```bash
# Run the benchmark
python3 ../scripts/benchmark_onednn_fusion.py
```

**Expected Console Output:**
```text
==========================================================
     INTEL oneDNN OPERATOR FUSION CONVOLUTION BENCHMARK   
     Course: GLA-HPC-BCSG701 | Supercomputing Masterclass 
==========================================================
[*] Input Batch: 32 images, 56x56x32
[*] oneDNN Environment Status: TF_ENABLE_ONEDNN_OPTS = 1
[*] Executing 30 forward inference iterations...
----------------------------------------------------------
[+] Average Fused Kernel Latency : 38.45 ms
[+] Model Inference Throughput   : 832.25 Images / Second
[+] Unfused DRAM Memory Traffic  : 25.17 MB (3 round-trips)
[+] oneDNN Fused Memory Traffic  : 6.29 MB (Cache resident)
[+] Memory Bandwidth Saved       : 75.0 %
[+] Status                       : ✅ 100% HARDWARE ACCELERATED VIA oneDNN
==========================================================
```

---

## 🖥️ STAGE 2: SLURM BATCH SCRIPTING & RESOURCE ALLOCATION

### 1. View the Production `#SBATCH` Script:
```bash
cat << 'EOF' > ../slurm_jobs/train_resnet_hpc.slurm
#!/bin/bash
#SBATCH --job-name=gla_dl_horovod
#SBATCH --output=/scratch/logs/%x_%j.out
#SBATCH --error=/scratch/logs/%x_%j.err
#SBATCH --partition=compute-ai
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --time=02:00:00
#SBATCH --mem=64G

set -eo pipefail

export TF_ENABLE_ONEDNN_OPTS=1
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
export KMP_AFFINITY=granularity=fine,compact,1,0

mpirun -n ${SLURM_NTASKS} \
    -ppn ${SLURM_NTASKS_PER_NODE} \
    -bind-to core \
    python3 ../scripts/distributed_tf_horovod.py
EOF
```

### 2. Submit and Monitor via Slurm Commands:
```bash
# Submit batch job script to the queue
sbatch ../slurm_jobs/train_resnet_hpc.slurm

# Check active and queued jobs for current user
squeue -u $USER

# Inspect cluster partition states
sinfo

# If job deadlocks, cancel immediately:
# scancel <job_id>
```

### 3. Run the Standalone Cluster Simulator:
In environments where Slurm daemons are simulated (e.g. Google Colab without systemd root):
```bash
python3 ../scripts/slurm_cluster_simulator.py
```

---

## 🔬 STAGE 3: INTEL GPU MAX 1550 & HABANA GAUDI HARDWARE PROBES

Audit the heterogeneous deep learning accelerator specifications:

```bash
# 1. Audit Intel Data Center GPU Max 1550 (Ponte Vecchio)
python3 ../scripts/intel_gpu_xpu_check.py

# 2. Audit Habana Gaudi 2 / Gaudi 3 (SynapseAI & 24x 100GbE RoCE)
python3 ../scripts/habana_gaudi_synapse_check.py
```

---

## 🌐 STAGE 4: MULTI-PROCESS HOROVOD DISTRIBUTED TRAINING

Launch real data-parallel training across 4 OpenMPI / Horovod worker ranks with synchronized Ring-AllReduce:

```bash
# Launch 4-worker distributed training
mpirun -n 4 --allow-run-as-root python3 ../scripts/distributed_tf_horovod.py
```

**Expected Console Output:**
```text
[Worker Rank 0/4] Initialized on Local Node Core ID: 0
[Worker Rank 1/4] Initialized on Local Node Core ID: 1
[Worker Rank 2/4] Initialized on Local Node Core ID: 2
[Worker Rank 3/4] Initialized on Local Node Core ID: 3
[Rank 0] Epoch 1/3 Complete | Loss: 0.7052 | Cluster Throughput: 894.2 samples/sec
[Rank 0] Epoch 2/3 Complete | Loss: 0.6733 | Cluster Throughput: 902.1 samples/sec
[Rank 0] Epoch 3/3 Complete | Loss: 0.6587 | Cluster Throughput: 906.4 samples/sec
----------------------------------------------------------
[+] Multi-Worker Training Complete across 4 Ranks.
[+] Total Cluster Throughput   : 900.9 samples / second
[+] Distributed Ring Efficiency : 98.5 %
[+] Status                      : ✅ RING-ALLREDUCE SYNCHRONIZATION VERIFIED
==========================================================
```

---

## 📊 STAGE 5: SCALING METRICS & MATHEMATICAL FORMULAS

1. **Throughput (Samples / Second):**
   $$\text{Throughput} = \frac{\text{Total Processed Samples} \times \text{Epochs}}{\text{Total Elapsed Seconds}}$$
2. **Distributed Scaling Efficiency (%):**
   $$\text{Efficiency} = \frac{\text{Throughput}_{K \text{ workers}}}{K \times \text{Throughput}_{1 \text{ worker}}} \times 100\%$$
3. **Ring-AllReduce Communication Volume per Worker:**
   $$\text{Volume}_{\text{worker}} = 2 \times \frac{N - 1}{N} \times S \quad (\text{independent of } N \text{ at scale!})$$

