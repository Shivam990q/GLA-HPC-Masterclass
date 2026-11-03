#!/usr/bin/env bash
# =============================================================================
# INTEL oneAPI ACCELERATED MACHINE LEARNING - AUTOMATED BENCHMARK RUNNER
# Script: run_all_benchmarks.sh
# Purpose: Execute all student practice scripts sequentially and summarize
# =============================================================================

set -e

# ANSI Color Codes
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo -e "${CYAN}======================================================================${NC}"
echo -e "${CYAN}   GLA HPC MASTERCLASS - DAY 02 AFTERNOON ML ACCELERATION SUITE       ${NC}"
echo -e "${CYAN}======================================================================${NC}"
echo -e "Starting automated benchmark evaluation at: $(date)"
echo ""

# Check python
if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
elif command -v python &>/dev/null; then
    PYTHON_CMD=python
else
    echo -e "${RED}[!] ERROR: Python is not found in PATH.${NC}"
    exit 1
fi

echo -e "${YELLOW}[*] Using Python: $($PYTHON_CMD --version)${NC}"
echo ""

run_benchmark() {
    local script_name="$1"
    local desc="$2"
    echo -e "${GREEN}>>> [RUNNING] $script_name: $desc${NC}"
    $PYTHON_CMD "$script_name"
    echo -e "${GREEN}>>> [FINISHED] $script_name${NC}"
    echo ""
}

# 1. Telemetry Audit
run_benchmark "01_verify_intel_env.py" "Hardware & oneAPI Telemetry Audit"

# 2. NumPy MKL DGEMM
run_benchmark "02_numpy_mkl_speedup.py" "NumPy MKL BLAS Matrix Multiply Speedup"

# 3. K-Means
run_benchmark "03_kmeans_acceleration.py" "Accelerated K-Means Customer Clustering"

# 4. Random Forest
run_benchmark "04_random_forest_acceleration.py" "Accelerated Random Forest Ensemble"

# 5. PCA Reduction
run_benchmark "05_pca_reduction_acceleration.py" "Accelerated PCA Dimensionality Reduction"

# 6. Full Benchmark Suite
run_benchmark "06_full_benchmark_suite.py" "Complete Multi-Algorithm Benchmark Suite"

echo -e "${CYAN}======================================================================${NC}"
echo -e "${CYAN}   ALL BENCHMARK SCRIPTS COMPLETED SUCCESSFULLY!                      ${NC}"
echo -e "${CYAN}======================================================================${NC}"
echo -e "CSV Report generated at: ${SCRIPT_DIR}/intel_ml_acceleration_results.csv"
