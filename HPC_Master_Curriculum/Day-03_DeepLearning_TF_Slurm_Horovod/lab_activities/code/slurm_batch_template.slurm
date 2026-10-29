#!/bin/bash
# ==============================================================================
# Project: Distributed Deep Learning via Slurm & Horovod
# Author : Shivam Gupta
# ==============================================================================
#SBATCH --job-name=gla_hpc_dl_train
#SBATCH --output=logs/dl_train_%j.out
#SBATCH --error=logs/dl_train_%j.err
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --time=01:00:00
#SBATCH --partition=compute_cluster

module load intel/oneapi
module load python/3.11-mkl

echo "=========================================================="
echo "Job ID       : $SLURM_JOB_ID"
echo "Nodes        : $SLURM_JOB_NODELIST"
echo "Tasks/Node   : $SLURM_NTASKS_PER_NODE"
echo "CPUs/Task    : $SLURM_CPUS_PER_TASK"
echo "=========================================================="

# Launch Horovod across allocated cluster nodes
srun python3 horovod_tf_training.py
