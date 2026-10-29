#!/usr/bin/env bash
# ==============================================================================
# Script: hpc_node_audit.sh
# Purpose: Automated Node Introspection & Memory Hierarchy Audit
# Lead Trainer: Shivam Gupta | GLA University HPC Workshop
# ==============================================================================
set -eo pipefail

LOG_FILE="node_audit_report.log"
exec > >(tee -a "$LOG_FILE") 2>&1

echo "=========================================================="
echo "    GLA SUPERCOMPUTING NODE HEALTH & MEMORY AUDIT        "
echo "=========================================================="
echo "[*] Timestamp    : $(date '+%Y-%m-%d %H:%M:%S')"
echo "[*] Hostname     : $(hostname)"
echo "[*] Kernel       : $(uname -r)"
echo "[*] Architecture : $(uname -m)"

echo "----------------------------------------------------------"
echo "1. Physical Memory (RAM) & Swap Status:"
free -h

echo "----------------------------------------------------------"
echo "2. L1, L2, and L3 Cache Geometries:"
lscpu -C 2>/dev/null || grep -E "cache" /proc/cpuinfo | head -n 4

echo "----------------------------------------------------------"
echo "3. Active Linux Kernel Process Table Snapshot:"
ps aux --sort=-%mem | head -n 5

echo "=========================================================="
echo "[+] Node Audit Completed Successfully. Logged to: $LOG_FILE"
