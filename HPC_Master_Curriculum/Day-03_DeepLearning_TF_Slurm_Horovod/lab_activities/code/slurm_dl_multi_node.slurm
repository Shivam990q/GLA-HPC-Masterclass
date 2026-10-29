#!/bin/bash
# ==============================================================================
# slurm_dl_multi_node.slurm
# GLA University — HPC Masterclass | Lead: Shivam Gupta
# Enterprise Slurm Batch Script: Multi-Node Distributed Training (Horovod + MPI)
# ==============================================================================
#SBATCH --job-name=gla_dl_distributed
#SBATCH --output=logs/dl_dist_%j.out
#SBATCH --error=logs/dl_dist_%j.err
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --time=04:00:00
#SBATCH --partition=gpu_cluster
#SBATCH --network=infiniband

set -euo pipefail

echo "======================================================================"
echo "   🌐 MULTI-NODE DISTRIBUTED DEEP LEARNING (HOROVOD + SLURM)"
echo "======================================================================"
echo "Slurm Job ID          : $SLURM_JOB_ID"
echo "Allocated Node List   : $SLURM_JOB_NODELIST"
echo "Number of Nodes       : $SLURM_JOB_NUM_NODES"
echo "Tasks Per Node        : $SLURM_NTASKS_PER_NODE"
echo "Total MPI Ranks       : $(( SLURM_JOB_NUM_NODES * SLURM_NTASKS_PER_NODE ))"
echo "CPUs Per Task         : $SLURM_CPUS_PER_TASK"
echo "Start Timestamp       : $(date -u)"
echo "======================================================================"

# 1. Load Software Environment Modules
if command -v module &>/dev/null; then
    module purge
    module load intel/oneapi
    module load openmpi/4.1.5
    module load python/3.11-mkl
fi

# 2. Fabric and Threading Configuration
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export TF_ENABLE_ONEDNN_OPTS=1
export HOROVOD_FUSION_THRESHOLD=67108864 # 64MB Tensor fusion buffer for InfiniBand

# InfiniBand RDMA Driver Parameters
export UCX_TLS=rc,self,sm
export UCX_NET_DEVICES=mlx5_0:1

mkdir -p logs checkpoints

# 3. Launch Distributed Training via srun
echo -e "\n[*] Launching Horovod Distributed Workers across $SLURM_JOB_NUM_NODES Nodes via srun..."
srun --mpi=pmix \
     --cpu-bind=cores \
     python3 horovod_tf_training.py

echo -e "\n[+] Distributed Training Job ID $SLURM_JOB_ID finished at: $(date -u)"
