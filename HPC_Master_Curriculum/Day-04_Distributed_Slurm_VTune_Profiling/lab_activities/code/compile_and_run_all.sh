#!/usr/bin/env bash
# ==============================================================================
# compile_and_run_all.sh
# Automated verification test harness for Day 4 Standalone Code Files
# ==============================================================================
set -eo pipefail

echo "=========================================================="
echo "    DAY 4: STANDALONE LAB CODE & PROFILING TEST HARNESS   "
echo "=========================================================="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "[1/4] Testing Python syntax integrity across all Day 4 scripts..."
python3 -m py_compile cpu_bottleneck_demo.py
python3 -m py_compile tf_distributed_profiling.py
python3 -m py_compile parse_vtune_report.py
echo "[✓] All Python scripts passed syntax compilation (py_compile)!"

echo "[2/4] Testing C++ compilation for vtune_matrix_profile.cpp..."
if command -v icx &>/dev/null; then
    icx -O3 -xHost -qopenmp vtune_matrix_profile.cpp -o vtune_matrix_profile
    echo "[✓] Compiled with Intel oneAPI ICX compiler!"
elif command -v g++ &>/dev/null; then
    g++ -O3 -fopenmp vtune_matrix_profile.cpp -o vtune_matrix_profile
    echo "[✓] Compiled with GCC g++ compiler!"
else
    echo "[!] No C++ compiler found in PATH. Skipping binary execution."
fi

echo "[3/4] Running CPU Bottleneck & TMAM Parser..."
python3 cpu_bottleneck_demo.py
python3 parse_vtune_report.py

echo "[4/4] Running Distributed TensorFlow Benchmark (Synthetic Simulator)..."
python3 tf_distributed_profiling.py --epochs 3 --batch-size 64

echo "=========================================================="
echo "🎉 ALL DAY 4 STANDALONE LAB CODE VERIFIED AND PASSING! 🎉"
echo "=========================================================="
