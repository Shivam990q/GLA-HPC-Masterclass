#!/bin/bash
# ==============================================================================
# slurm_openvino_serving.slurm
# Enterprise Slurm Batch Job: High-Concurrency OpenVINO LLM Microservice Serving
# Runs FastAPI microservice with Intel AMX and oneDNN execution kernels
# ==============================================================================
#SBATCH --job-name=openvino_llm_api
#SBATCH --output=openvino_serving_%j.out
#SBATCH --error=openvino_serving_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --time=08:00:00
#SBATCH --partition=compute
#SBATCH --exclusive

set -eo pipefail

echo "=========================================================="
echo "SLURM JOB ID:             $SLURM_JOB_ID"
echo "SERVING NODE:             $SLURMD_NODENAME"
echo "CPUS ALLOCATED:           $SLURM_CPUS_PER_TASK"
echo "START TIME:               $(date)"
echo "=========================================================="

# 1. Source Intel oneAPI environment
source /opt/intel/oneapi/setvars.sh 2>/dev/null || echo "Using system environment"

# 2. Hardware-aware tuning for OpenVINO & Intel AMX on 4th/5th Gen Xeon
export OV_CPU_HETERO_INFERENCE=0
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores
export OMP_PROC_BIND=close
export KMP_AFFINITY=granularity=fine,compact,1,0
export KMP_BLOCKTIME=1

# 3. Export model if not already exported
if [ ! -d "./openvino_ir_model" ]; then
    echo "[*] OpenVINO IR model not found. Running export_openvino_ir.py..."
    python3 export_openvino_ir.py
fi

# 4. Launch FastAPI Server
PORT=8080
echo "[*] Launching OpenVINO LLM Serving Microservice on port $PORT..."
python3 -m uvicorn llm_fastapi_server:app --host 0.0.0.0 --port $PORT --workers 4

echo "=========================================================="
echo "SERVER SHUTDOWN: $(date)"
echo "=========================================================="
