#!/bin/bash
# ==============================================================================
# slurm_llm_gaudi_finetune.slurm
# Enterprise Slurm Batch Job: Distributed LLM Fine-Tuning on Intel Habana Gaudi
# 4 Nodes x 8 Gaudi OAM Processors = 32 Total HPUs over On-Die 24x 100GbE RoCE
# ==============================================================================
#SBATCH --job-name=gaudi_llm_finetune
#SBATCH --output=gaudi_finetune_%j.out
#SBATCH --error=gaudi_finetune_%j.err
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=8
#SBATCH --cpus-per-task=16
#SBATCH --time=04:00:00
#SBATCH --partition=gaudi-cluster
#SBATCH --exclusive

set -eo pipefail

echo "=========================================================="
echo "SLURM JOB ID:             $SLURM_JOB_ID"
echo "TOTAL NODES:              $SLURM_NNODES"
echo "TOTAL HPU PROCESSORS:     $SLURM_NTASKS"
echo "NODE LIST:                $SLURM_JOB_NODELIST"
echo "START TIME:               $(date)"
echo "=========================================================="

# 1. Source Intel Habana SynapseAI Environment
source /etc/profile.d/habanalabs.sh 2>/dev/null || echo "Using system SynapseAI path"

# 2. Hardware telemetry check via hl-smi
echo "[*] Querying Habana System Management Interface (hl-smi)..."
hl-smi 2>/dev/null || echo "hl-smi not available, proceeding with allocated environment"

# 3. Configure Habana Communications Library (HCL) & RoCE Fabrics
export HABANA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7
export PT_HPU_LAZY_MODE=1              # Enables SynapseAI graph compiler JIT optimization
export PT_HPU_ENABLE_LAZY_COLLECTIVES=true
export HCL_BCAST_ALGORITHM=ring
export HCL_ALLREDUCE_ALGORITHM=ring

# 4. Generate dynamic hostfile from Slurm allocation
HOSTFILE="./gaudi_hosts_${SLURM_JOB_ID}.txt"
scontrol show hostnames "$SLURM_JOB_NODELIST" | awk '{print $1" slots=8"}' > "$HOSTFILE"
echo "[*] Generated Gaudi Cluster Hostfile:"
cat "$HOSTFILE"

# 5. Launch Distributed LoRA Fine-Tuning via mpirun
echo "[*] Launching 32-card Gaudi LoRA distributed fine-tuning..."
mpirun -np "$SLURM_NTASKS" \
       -hostfile "$HOSTFILE" \
       --bind-to core \
       python3 gaudi_llm_finetune_lora.py

echo "=========================================================="
echo "TRAINING COMPLETE! Clean up temporary hostfile."
rm -f "$HOSTFILE"
echo "END TIME: $(date)"
echo "=========================================================="
