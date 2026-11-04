#!/bin/bash
# ==============================================================================
# SLURM PRODUCTION BATCH SUBMISSION SCRIPT
# Course: GLA-HPC-BCSG701 | Supercomputing Masterclass
# Module: Distributed Deep Learning on HPC (TensorFlow + oneDNN + Horovod)
# ==============================================================================
#SBATCH --job-name=gla_dl_horovod         # Human-readable job identifier
#SBATCH --output=/scratch/logs/%x_%j.out   # Standard output log (%x=job name, %j=job ID)
#SBATCH --error=/scratch/logs/%x_%j.err    # Standard error log
#SBATCH --partition=compute-ai            # Target partition / hardware queue
#SBATCH --nodes=2                         # Number of physical discrete compute nodes
#SBATCH --ntasks-per-node=4               # Number of MPI tasks (accelerators/ranks) per node
#SBATCH --cpus-per-task=8                 # CPU hardware threads allocated per task
#SBATCH --time=02:00:00                   # Hard walltime limit (HH:MM:SS) - kills job at 2 hrs
#SBATCH --mem=64G                         # Memory allocation per compute node

set -eo pipefail

echo "=========================================================="
echo "          SLURM DISTRIBUTED DEEP LEARNING EXECUTION       "
echo "=========================================================="
echo "JOB ID              : ${SLURM_JOB_ID}"
echo "JOB NAME            : ${SLURM_JOB_NAME}"
echo "ALLOCATED NODES     : ${SLURM_JOB_NODELIST}"
echo "TOTAL MPI TASKS     : ${SLURM_NTASKS}"
echo "TASKS PER NODE      : ${SLURM_NTASKS_PER_NODE}"
echo "CPUS PER TASK       : ${SLURM_CPUS_PER_TASK}"
echo "SUBMISSION PARTITION: ${SLURM_JOB_PARTITION}"
echo "START TIME          : $(date)"
echo "=========================================================="

# 1. Environment & Toolkit Initialization
if [ -f /opt/intel/oneapi/setvars.sh ]; then
    source /opt/intel/oneapi/setvars.sh 2>/dev/null || true
fi

# 2. Intel oneDNN & Hardware Thread Affinity Optimization
export TF_ENABLE_ONEDNN_OPTS=1
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
export KMP_AFFINITY=granularity=fine,compact,1,0
export KMP_BLOCKTIME=1

# 3. Create Scratch Logs Directory
mkdir -p /scratch/logs /scratch/checkpoints

# 4. Multi-Node Distributed Training Launch via OpenMPI / Horovod
echo "[*] Launching ${SLURM_NTASKS} distributed worker ranks across ${SLURM_JOB_NUM_NODES} nodes..."
mpirun -n ${SLURM_NTASKS} \
    -ppn ${SLURM_NTASKS_PER_NODE} \
    -bind-to core \
    python3 distributed_tf_horovod.py

echo "=========================================================="
echo "[+] Slurm batch job ${SLURM_JOB_ID} successfully completed at $(date)"
echo "=========================================================="

