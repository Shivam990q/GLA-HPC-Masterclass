#!/bin/bash
# ==============================================================================
# slurm_vtune_profile.slurm
# Enterprise Slurm Batch Job: Intel VTune Hotspots & TMAM Profiling on HPC Node
# ==============================================================================
#SBATCH --job-name=vtune_hpc_profile
#SBATCH --output=vtune_job_%j.out
#SBATCH --error=vtune_job_%j.err
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --time=00:30:00
#SBATCH --partition=compute
#SBATCH --exclusive

set -eo pipefail

echo "=========================================================="
echo "SLURM JOB ID:        $SLURM_JOB_ID"
echo "RUNNING ON NODE:     $SLURMD_NODENAME"
echo "ALLOCATED CORES:     $SLURM_CPUS_PER_TASK"
echo "START TIME:          $(date)"
echo "=========================================================="

# 1. Source Intel oneAPI environment
source /opt/intel/oneapi/setvars.sh 2>/dev/null || echo "Using system oneAPI installation"

# 2. Set OpenMP CPU core pinning and thread count
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
export OMP_PLACES=cores
export OMP_PROC_BIND=close

# 3. Create output directory for VTune results
REPORT_DIR="./vtune_results_job_${SLURM_JOB_ID}"
mkdir -p "$REPORT_DIR"

echo "[*] Step 1: Compiling native C++ benchmark..."
icx -O3 -xHost -qopenmp vtune_matrix_profile.cpp -o vtune_matrix_profile 2>/dev/null || \
g++ -O3 -fopenmp vtune_matrix_profile.cpp -o vtune_matrix_profile

echo "[*] Step 2: Collecting Intel VTune Hotspots..."
if command -v vtune &>/dev/null; then
    vtune -collect hotspots -result-dir "${REPORT_DIR}/hotspots" -- ./vtune_matrix_profile
    echo "[*] Step 3: Collecting Intel VTune Microarchitecture Exploration (TMAM)..."
    vtune -collect uarch-exploration -result-dir "${REPORT_DIR}/tmam" -- ./vtune_matrix_profile
    echo "[*] Step 4: Generating Summary Reports..."
    vtune -report summary -result-dir "${REPORT_DIR}/hotspots" -format text -report-output "${REPORT_DIR}/hotspots_summary.txt"
    vtune -report summary -result-dir "${REPORT_DIR}/tmam" -format text -report-output "${REPORT_DIR}/tmam_summary.txt"
    echo "[+] VTune profiling completed! Reports saved in: $REPORT_DIR"
else
    echo "[!] VTune CLI binary not found in PATH. Running native benchmark directly..."
    ./vtune_matrix_profile
fi

echo "=========================================================="
echo "END TIME:            $(date)"
echo "=========================================================="
