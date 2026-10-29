#!/bin/bash
# ==============================================================================
# slurm_dl_single_node.slurm
# GLA University — HPC Masterclass | Lead: Shivam Gupta
# Enterprise Slurm Batch Script: Single-Node Deep Learning Training with oneDNN
# ==============================================================================
#SBATCH --job-name=gla_dl_single
#SBATCH --output=logs/dl_single_%j.out
#SBATCH --error=logs/dl_single_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=64G
#SBATCH --time=02:00:00
#SBATCH --partition=compute
#SBATCH --cpu-bind=cores

set -euo pipefail

echo "======================================================================"
echo "   🖥️ SLURM JOB METADATA & RESOURCE ALLOCATION"
echo "======================================================================"
echo "Job ID                : $SLURM_JOB_ID"
echo "Submitted by User     : $USER"
echo "Assigned Node         : $SLURMD_NODENAME"
echo "Allocated CPUs        : $SLURM_CPUS_PER_TASK cores"
echo "Allocated Memory      : 64 GB"
echo "Job Submit Directory  : $SLURM_SUBMIT_DIR"
echo "Start Timestamp       : $(date -u)"
echo "======================================================================"

# 1. Load Software Environment Modules
if command -v module &>/dev/null; then
    module purge
    module load intel/oneapi
    module load python/3.11-mkl
fi

# 2. Hardware-Aware Intel oneDNN & Thread Binding Configuration
export TF_ENABLE_ONEDNN_OPTS=1
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export KMP_AFFINITY=granularity=fine,compact,1,0
export KMP_BLOCKTIME=1

echo -e "\n[*] Active Environment Configuration:"
echo "    TF_ENABLE_ONEDNN_OPTS : $TF_ENABLE_ONEDNN_OPTS"
echo "    OMP_NUM_THREADS       : $OMP_NUM_THREADS"
echo "    KMP_AFFINITY          : $KMP_AFFINITY"

# 3. Create Logs Directory
mkdir -p logs checkpoints

# 4. Execute Deep Learning Job
echo -e "\n[*] Executing TensorFlow oneDNN Benchmark..."
python3 tf_onednn_benchmark.py

echo -e "\n[+] Slurm Job ID $SLURM_JOB_ID completed successfully at: $(date -u)"
