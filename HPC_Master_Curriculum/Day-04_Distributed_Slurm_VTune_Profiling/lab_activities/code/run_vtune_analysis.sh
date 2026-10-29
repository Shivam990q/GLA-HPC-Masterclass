#!/usr/bin/env bash
# ==============================================================================
# run_vtune_analysis.sh
# Automated Intel VTune Profiling & Top-Down TMAM Exploration Script
# ==============================================================================
set -eo pipefail

echo "=========================================================="
echo "           INTEL VTUNE PROFILING AUTOMATION               "
echo "=========================================================="

REPORT_BASE="./vtune_reports"
mkdir -p "$REPORT_BASE"

# 1. Source Intel oneAPI environment if available
source /opt/intel/oneapi/setvars.sh 2>/dev/null || echo "Using system environment"

if command -v vtune &>/dev/null; then
    echo "[*] 1. Collecting CPU Performance Hotspots..."
    vtune -collect hotspots -result-dir "${REPORT_BASE}/hotspots" -- python3 cpu_bottleneck_demo.py
    
    echo "[*] 2. Collecting Top-Down Microarchitecture Exploration (TMAM)..."
    vtune -collect uarch-exploration -result-dir "${REPORT_BASE}/tmam" -- python3 cpu_bottleneck_demo.py
    
    echo "[*] 3. Collecting Memory Access & Cache Footprint Analysis..."
    vtune -collect memory-access -result-dir "${REPORT_BASE}/memory" -- python3 cpu_bottleneck_demo.py
    
    echo "[*] 4. Exporting Summary Reports..."
    vtune -report summary -result-dir "${REPORT_BASE}/tmam" -format text -report-output "${REPORT_BASE}/tmam_summary.txt"
    
    echo "[*] 5. Running Automated TMAM Parser..."
    python3 parse_vtune_report.py "${REPORT_BASE}/tmam_summary.txt"
    
    echo "=========================================================="
    echo "[+] VTune Analysis Complete! GUI: vtune-gui ${REPORT_BASE}/hotspots"
    echo "=========================================================="
else
    echo "[!] Intel VTune CLI binary not found in current PATH."
    echo "[*] Running native software benchmark and TMAM diagnostic simulator..."
    python3 cpu_bottleneck_demo.py
    python3 parse_vtune_report.py
    echo "=========================================================="
    echo "[+] Local benchmark & diagnostic simulation completed successfully!"
    echo "=========================================================="
fi
