#!/usr/bin/env bash
# ==============================================================================
# Project: Automated HPC Node Profiler & Benchmark Orchestrator
# Author : Shivam Gupta
# ==============================================================================
set -eo pipefail

LOG_DIR="./hpc_runs"
mkdir -p "$LOG_DIR"
TIMESTAMP=$(date '+%Y%m%d_%H%M%S')
LOG_FILE="$LOG_DIR/run_$TIMESTAMP.log"

exec > >(tee -a "$LOG_FILE") 2>&1

echo "=========================================================="
echo "    HIGH PERFORMANCE COMPUTING AUTOMATED PIPELINE         "
echo "=========================================================="
echo "Host Machine : $(hostname)"
echo "Current User : $(whoami)"
echo "Timestamp    : $(date '+%Y-%m-%d %H:%M:%S')"
echo "Kernel       : $(uname -r)"

echo "----------------------------------------------------------"
echo "[1] Analyzing Silicon Microarchitecture..."
CORES=$(nproc)
echo "[+] Detected Accessible CPU Cores: $CORES"

if grep -q "avx512" /proc/cpuinfo 2>/dev/null; then
    echo "[+] Silicon Feature: AVX-512 (512-bit SIMD Ultra Vector Engine Active)"
elif grep -q "avx2" /proc/cpuinfo 2>/dev/null; then
    echo "[+] Silicon Feature: AVX2 (256-bit Vector Engine Active)"
else
    echo "[-] Standard x86 Vector Instructions"
fi

echo "----------------------------------------------------------"
echo "[2] Tuning Parallel Environment Variables..."
export OMP_NUM_THREADS=$CORES
export PYTHONUNBUFFERED=1
echo "[+] Set OMP_NUM_THREADS to $CORES"

echo "----------------------------------------------------------"
echo "[3] Running Side-by-Side Benchmark..."
python3 compute_engine.py standard
python3 compute_engine.py accelerated

echo "----------------------------------------------------------"
echo "[+] Pipeline Completed Successfully. Archived to: $LOG_FILE"
echo "=========================================================="
