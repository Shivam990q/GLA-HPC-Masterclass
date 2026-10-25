#!/usr/bin/env bash
# ==============================================================================
# EDULATERAL FOUNDATION — 1-CLICK OFFLINE LAB ENVIRONMENT SETUP
# Program: GLA University High Performance Computing Block Teaching
# Lead Trainer: Shivam Gupta | Target: Ubuntu 20.04/22.04 LTS / RHEL 8/9 (x86_64)
# ==============================================================================
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}====================================================================${NC}"
echo -e "${BLUE}   🏢 EDULATERAL FOUNDATION — HIGH PERFORMANCE COMPUTING LAB SETUP  ${NC}"
echo -e "${BLUE}   GLA University Block Teaching (Nov 16-20, 2026) | Offline Deploy ${NC}"
echo -e "${BLUE}====================================================================${NC}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_NAME="hpc-edulateral"

echo -e "\n${YELLOW}[Step 1/5] Auditing Host CPU & Silicon Architecture...${NC}"
CPU_MODEL=$(lscpu | grep "Model name:" | sed 's/Model name:[ \t]*//' || echo "Unknown CPU")
CPU_CORES=$(nproc)
echo -e "  -> Detected CPU: ${GREEN}${CPU_MODEL}${NC}"
echo -e "  -> Total Hardware Execution Threads: ${GREEN}${CPU_CORES}${NC}"

if grep -q "avx512" /proc/cpuinfo; then
    echo -e "  -> Vector Extensions: ${GREEN}AVX-512 Supported (512-bit ZMM registers)${NC}"
elif grep -q "avx2" /proc/cpuinfo; then
    echo -e "  -> Vector Extensions: ${GREEN}AVX2 Supported (256-bit YMM registers)${NC}"
else
    echo -e "  -> Vector Extensions: ${YELLOW}Standard SSE Mode${NC}"
fi

echo -e "\n${YELLOW}[Step 2/5] Initializing Isolated Python Environment...${NC}"
if command -v conda &> /dev/null; then
    echo -e "  -> Conda detected. Initializing environment '${ENV_NAME}'..."
    conda create -y -n "${ENV_NAME}" python=3.10 || true
    # Activate conda env
    source "$(conda info --base)/etc/profile.d/conda.sh"
    conda activate "${ENV_NAME}"
else
    echo -e "  -> Conda not found. Using local Python 3 venv in ~/hpc_env..."
    python3 -m venv "$HOME/hpc_env"
    source "$HOME/hpc_env/bin/activate"
fi

echo -e "\n${YELLOW}[Step 3/5] Installing Offline Wheel Packages from USB Pen Drive...${NC}"
WHEELS_DIR="${SCRIPT_DIR}/02_PYTHON_WHEELS"
if [ -d "${WHEELS_DIR}" ] && [ "$(ls -A "${WHEELS_DIR}"/*.whl 2>/dev/null)" ]; then
    echo -e "  -> Found offline wheels in ${WHEELS_DIR}. Installing with --no-index..."
    pip install --no-index --find-links="${WHEELS_DIR}" numpy scipy pandas scikit-learn scikit-learn-intelex openvino fastapi uvicorn
else
    echo -e "  -> ${YELLOW}Offline wheel directory not populated or empty. Installing standard local packages...${NC}"
    pip install numpy scipy pandas scikit-learn scikit-learn-intelex || true
fi

echo -e "\n${YELLOW}[Step 4/5] Configuring Intel HPC Runtime & OpenMP Affinity...${NC}"
cat << 'EOF' > "$HOME/.edulateral_hpc_rc"
# Edulateral HPC Environment Variables
export OMP_NUM_THREADS=$(nproc)
export KMP_AFFINITY=granularity=fine,compact,1,0
export KMP_BLOCKTIME=1
export TF_ENABLE_ONEDNN_OPTS=1
export MKL_DYNAMIC=FALSE
export OMP_PROC_BIND=close
export OMP_PLACES=cores
EOF

# Append to bashrc if not already present
if ! grep -q "edulateral_hpc_rc" "$HOME/.bashrc"; then
    echo "source \$HOME/.edulateral_hpc_rc" >> "$HOME/.bashrc"
fi
source "$HOME/.edulateral_hpc_rc"
echo -e "  -> Hardware threads pinned. OMP_NUM_THREADS=${OMP_NUM_THREADS}."

echo -e "\n${YELLOW}[Step 5/5] Generating Offline Synthetic Benchmark Datasets...${NC}"
if [ -f "${SCRIPT_DIR}/generate_synthetic_datasets.py" ]; then
    python "${SCRIPT_DIR}/generate_synthetic_datasets.py" "${SCRIPT_DIR}/03_BENCHMARK_DATASETS"
fi

echo -e "\n${GREEN}====================================================================${NC}"
echo -e "${GREEN} ✅ EDULATERAL OFFLINE HPC LAB ENVIRONMENT READY!                     ${NC}"
echo -e "${GREEN}    Run 'source ~/.edulateral_hpc_rc' in new terminals.              ${NC}"
echo -e "${GREEN}    Begin Day 1 exercises in 'HPC_Master_Curriculum/Day-01_*'       ${NC}"
echo -e "${GREEN}====================================================================${NC}"
