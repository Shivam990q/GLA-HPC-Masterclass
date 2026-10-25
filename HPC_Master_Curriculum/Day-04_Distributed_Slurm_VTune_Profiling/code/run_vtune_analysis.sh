#!/usr/bin/env bash
# run_vtune_analysis.sh
set -eo pipefail

echo "=========================================================="
echo "           INTEL VTUNE PROFILING AUTOMATION               "
echo "=========================================================="

RESULT_DIR="./vtune_hotspots_report"
rm -rf "$RESULT_DIR"

echo "[*] Collecting Hotspots on target workload..."
vtune -collect hotspots -result-dir "$RESULT_DIR" -- python3 cpu_bottleneck_demo.py

echo "[*] Generating Summary Report from PMU Hardware Counters..."
vtune -report summary -result-dir "$RESULT_DIR"

echo "=========================================================="
echo "[+] VTune Profiling Completed! Open in GUI with: vtune-gui $RESULT_DIR"
