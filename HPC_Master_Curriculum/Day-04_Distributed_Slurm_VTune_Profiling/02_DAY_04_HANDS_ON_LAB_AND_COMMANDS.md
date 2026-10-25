# 💻 DAY 4: HANDS-ON LAB & COMMANDS PLAYBOOK
## Practical Execution for Multi-Node Slurm & Intel VTune Profiling
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 📋 LAB SECTION 1: Multi-Node Slurm Distributed Launch Script

```bash
cat << 'EOF' > run_distributed_tf.sh
#!/bin/bash
# ==============================================================================
# Slurm Batch Script: Distributed Deep Learning across 4 Cluster Nodes
# ==============================================================================
#SBATCH --job-name=gla_dist_tf
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=2
#SBATCH --cpus-per-task=16
#SBATCH --time=02:00:00
#SBATCH --partition=compute

# 1. Prepare environment modules
source /opt/intel/oneapi/setvars.sh 2>/dev/null
export TF_ENABLE_ONEDNN_OPTS=1
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PROC_BIND=close
export OMP_PLACES=cores

echo "[INFO] Running distributed job on: $(hostname) with $SLURM_NNODES nodes"

# 2. Launch with mpirun pinning processes to physical CPU sockets
mpirun -np 8 --bind-to socket python3 train_cluster.py
EOF
```

---

## 📋 LAB SECTION 2: Profiling with Intel VTune Command-Line Interface (CLI)

```bash
# 1. Check if vtune is in PATH
which vtune 2>/dev/null || echo "[NOTE] Sourcing oneAPI environment: source /opt/intel/oneapi/setvars.sh"

# 2. Run Hotspots Analysis on training workload
vtune -collect hotspots -result-dir ./vtune_hotspots_run -- python3 -c "
import numpy as np
import time

print('[INFO] Simulating heavy compute workload for VTune profiling...')
a = np.random.rand(4000, 4000).astype(np.float32)
b = np.random.rand(4000, 4000).astype(np.float32)

start = time.time()
for _ in range(5):
    c = np.dot(a, b)
print(f'[DONE] Completed 5 matrix multiplications in {time.time() - start:.2f} seconds')
"

# 3. Generate Human-Readable Text Summary Report
vtune -report summary -result-dir ./vtune_hotspots_run

# 4. Generate Top Function Hotspots Breakdown
vtune -report hotspots -result-dir ./vtune_hotspots_run
```

---

## 📋 LAB SECTION 3: Microarchitecture & Memory Access Analysis

```bash
# Collect Memory Access and Cache Profiling (DRAM Bandwidth & LLC Misses)
# vtune -collect memory-access -result-dir ./vtune_memory_run -- python3 train.py

# Collect Threading & Synchronization Overhead (Lock wait time & Spin time)
# vtune -collect threading -result-dir ./vtune_threading_run -- python3 train.py
```
