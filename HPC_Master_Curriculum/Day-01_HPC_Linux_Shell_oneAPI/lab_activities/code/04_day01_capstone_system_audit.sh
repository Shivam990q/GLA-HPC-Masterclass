#!/usr/bin/env bash
# ==============================================================================
# Script: 04_day01_capstone_system_audit.sh
# Level 4 Capstone: Automated HPC Node Resource & Health Audit
# GLA University HPC Masterclass | Lead Trainer: Shivam Gupta
# ==============================================================================
set -e

REPORT="node_health_audit.log"
echo "=========================================================="
echo "    LEVEL 4 CAPSTONE: SUPERCOMPUTING NODE HEALTH AUDIT    "
echo "=========================================================="
echo "[*] Generating audit report to: $REPORT"
echo "[*] Timestamp    : $(date '+%Y-%m-%d %H:%M:%S')"
echo "[*] Host Machine : $(hostname)"
echo "[*] OS Kernel    : $(uname -s -r)"
echo "[*] Architecture : $(uname -m)"

# 1. Memory / Swap Check
echo "----------------------------------------------------------"
echo "1. Memory & Resource Snapshot:"
if command -v free >/dev/null 2>&1; then
    free -h
else
    echo "Physical Memory Telemetry available via /proc/meminfo:"
    head -n 5 /proc/meminfo 2>/dev/null || echo "Windows Git-Bash Memory Space Active"
fi

# 2. CPU / Architecture Check
echo "----------------------------------------------------------"
echo "2. CPU Model & Core Count:"
if command -v lscpu >/dev/null 2>&1; then
    lscpu | head -n 12
elif [ -f /proc/cpuinfo ]; then
    grep -E "model name|cpu cores|cache size" /proc/cpuinfo | head -n 6
else
    echo "CPU Info: $(uname -m) processor detected."
fi

# 3. Process Table Snapshot
echo "----------------------------------------------------------"
echo "3. Active Top Processes:"
ps aux 2>/dev/null | head -n 6 || ps -ef | head -n 6

echo "=========================================================="
echo "[+] Capstone Audit Finished Successfully!"
echo "=========================================================="
