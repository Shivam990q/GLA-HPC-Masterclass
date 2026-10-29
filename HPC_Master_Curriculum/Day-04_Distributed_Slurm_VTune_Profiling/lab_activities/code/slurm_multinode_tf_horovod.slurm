#!/bin/bash
# ==============================================================================
# slurm_multinode_tf_horovod.slurm
# Enterprise Slurm Batch Job: Multi-Node Distributed TensorFlow Training (Horovod)
# 4 Nodes x 4 Ranks/Node = 16 Total Distributed Worker Ranks over InfiniBand
# ==============================================================================
#SBATCH --job-name=tf_horovod_dist
#SBATCH --output=tf_dist_%j.out
#SBATCH --error=tf_dist_%j.err
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --time=02:00:00
#SBATCH --partition=gpu-cluster
#SBATCH --exclusive

set -eo pipefail

echo "=========================================================="
echo "SLURM JOB ID:             $SLURM_JOB_ID"
echo "TOTAL NODES:              $SLURM_NNODES"
echo "TOTAL TASKS:              $SLURM_NTASKS"
echo "NODE LIST:                $SLURM_JOB_NODELIST"
echo "CPUS PER TASK:            $SLURM_CPUS_PER_TASK"
echo "START TIME:               $(date)"
echo "=========================================================="

# 1. Load oneAPI / Intel MPI Environment
source /opt/intel/oneapi/setvars.sh 2>/dev/null || echo "Using system environment"

# 2. Hardware-aware tuning for Intel oneDNN & multi-threading
export TF_ENABLE_ONEDNN_OPTS=1
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export KMP_AFFINITY=granularity=fine,compact,1,0
export KMP_BLOCKTIME=1

# 3. Network fabric settings for InfiniBand / RoCE
export I_MPI_FABRICS=shm:ofi
export I_MPI_OFI_PROVIDER=mlx
export HOROVOD_FUSION_THRESHOLD=67108864 # 64 MB tensor fusion buffer
export HOROVOD_AUTOTUNE=1

# 4. Generate dynamic hostfile from Slurm allocation
HOSTFILE="./hosts_${SLURM_JOB_ID}.txt"
scontrol show hostnames "$SLURM_JOB_NODELIST" | awk '{print $1":4"}' > "$HOSTFILE"
echo "[*] Generated Horovod Hostfile:"
cat "$HOSTFILE"

# 5. Launch Distributed Training via mpirun / srun
echo "[*] Launching 16-rank distributed training..."
mpirun -np "$SLURM_NTASKS" \
       -ppn "$SLURM_NTASKS_PER_NODE" \
       -f "$HOSTFILE" \
       -genv OMP_NUM_THREADS="$SLURM_CPUS_PER_TASK" \
       python3 tf_distributed_profiling.py --epochs 10 --batch-size 256

echo "=========================================================="
echo "TRAINING COMPLETE! Clean up temporary hostfile."
rm -f "$HOSTFILE"
echo "END TIME: $(date)"
echo "=========================================================="
