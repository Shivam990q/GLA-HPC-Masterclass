#!/usr/bin/env bash
# ==============================================================================
# Script Name   : 01_system_health_audit.sh
# Description   : Automated Linux system health audit & hardware telemetry
# Architecture  : POSIX compliant, bash 4.0+
# Author        : GLA HPC Masterclass Training Division
# Date          : 2026-10-24
# License       : MIT
# Usage         : ./01_system_health_audit.sh [-c] [-w <disk_threshold>] [-j <json_out>]
# ==============================================================================

set -euo pipefail

# ANSI Color Codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Default Configuration Parameters
DISK_WARN_THRESHOLD=80
ENABLE_COLOR=true
JSON_OUTPUT_FILE=""

usage() {
    cat << EOF
Usage: $(basename "$0") [OPTIONS]

Comprehensive Linux System & HPC Node Health Auditor.

Options:
    -w <pct>    Disk usage warning threshold in percent (Default: 80)
    -n          Disable ANSI color styling
    -j <file>   Export snapshot metrics to a JSON report file
    -h          Display this help message and exit

Examples:
    $(basename "$0")
    $(basename "$0") -w 85 -j /tmp/node_health.json
EOF
    exit 0
}

# Parse Command-Line Options
while getopts ":w:nj:h" opt; do
    case "${opt}" in
        w)
            if ! [[ "${OPTARG}" =~ ^[0-9]+$ ]] || [ "${OPTARG}" -lt 1 ] || [ "${OPTARG}" -gt 100 ]; then
                echo "Error: Threshold must be an integer between 1 and 100." >&2
                exit 1
            fi
            DISK_WARN_THRESHOLD="${OPTARG}"
            ;;
        n)
            ENABLE_COLOR=false
            RED=""
            GREEN=""
            YELLOW=""
            BLUE=""
            CYAN=""
            BOLD=""
            NC=""
            ;;
        j)
            JSON_OUTPUT_FILE="${OPTARG}"
            ;;
        h)
            usage
            ;;
        \?)
            echo "Error: Invalid option -${OPTARG}" >&2
            usage
            ;;
        :)
            echo "Error: Option -${OPTARG} requires an argument." >&2
            usage
            ;;
    esac
done

print_header() {
    local title="$1"
    echo -e "\n${BOLD}${CYAN}=== [ ${title} ] ========================================${NC}"
}

# Gather Telemetry Facts
HOSTNAME_VAL=$(hostname -f 2>/dev/null || hostname)
KERNEL_VAL=$(uname -r)
UPTIME_VAL=$(uptime -p 2>/dev/null || uptime | awk -F'( |,|:)+' '{print $6,"hrs",$7,"min"}')
TIMESTAMP_VAL=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

print_header "1. SYSTEM & KERNEL IDENTIFICATION"
echo -e "${BOLD}Hostname   :${NC} ${HOSTNAME_VAL}"
echo -e "${BOLD}Kernel     :${NC} ${KERNEL_VAL}"
echo -e "${BOLD}Uptime     :${NC} ${UPTIME_VAL}"
echo -e "${BOLD}Timestamp  :${NC} ${TIMESTAMP_VAL}"

print_header "2. CPU LOAD & EXECUTION METRICS"
CPU_CORES=$(nproc)
LOAD_AVGS=$(cat /proc/loadavg | awk '{print $1, $2, $3}')
LOAD_1M=$(echo "${LOAD_AVGS}" | awk '{print $1}')
LOAD_5M=$(echo "${LOAD_AVGS}" | awk '{print $2}')
LOAD_15M=$(echo "${LOAD_AVGS}" | awk '{print $3}')

echo -e "${BOLD}Total CPU Cores :${NC} ${CPU_CORES}"
echo -e "${BOLD}Load Average    :${NC} 1m: [${LOAD_1M}], 5m: [${LOAD_5M}], 15m: [${LOAD_15M}]"

# CPU Overload Detection
CPU_RATIO=$(awk -v l="${LOAD_1M}" -v c="${CPU_CORES}" 'BEGIN { printf "%.2f", l / c }')
if (( $(echo "${CPU_RATIO} > 1.0" | bc -l 2>/dev/null || awk -v r="${CPU_RATIO}" 'BEGIN { exit !(r > 1.0) }') )); then
    echo -e "${RED}[WARNING] CPU Load per Core is high (${CPU_RATIO}). System may be CPU-bound.${NC}"
else
    echo -e "${GREEN}[OK] CPU Load per Core is healthy (${CPU_RATIO}).${NC}"
fi

print_header "3. MEMORY & SWAP ALLOCATION"
if command -v free >/dev/null 2>&1; then
    MEM_TOTAL_MB=$(free -m | awk '/^Mem:/ {print $2}')
    MEM_USED_MB=$(free -m | awk '/^Mem:/ {print $3}')
    MEM_FREE_MB=$(free -m | awk '/^Mem:/ {print $4}')
    MEM_AVAIL_MB=$(free -m | awk '/^Mem:/ {print $7}')
    SWAP_TOTAL_MB=$(free -m | awk '/^Swap:/ {print $2}')
    SWAP_USED_MB=$(free -m | awk '/^Swap:/ {print $3}')
    
    MEM_USED_PCT=$(awk -v u="${MEM_USED_MB}" -v t="${MEM_TOTAL_MB}" 'BEGIN { printf "%.1f", (u/t)*100 }')
    
    echo -e "${BOLD}Total RAM    :${NC} ${MEM_TOTAL_MB} MB"
    echo -e "${BOLD}Used RAM     :${NC} ${MEM_USED_MB} MB (${MEM_USED_PCT}%)"
    echo -e "${BOLD}Available RAM:${NC} ${MEM_AVAIL_MB} MB"
    echo -e "${BOLD}Swap Status  :${NC} Used: ${SWAP_USED_MB} MB / Total: ${SWAP_TOTAL_MB} MB"
    
    if (( $(echo "${MEM_USED_PCT} > 90.0" | bc -l 2>/dev/null || awk -v p="${MEM_USED_PCT}" 'BEGIN { exit !(p > 90.0) }') )); then
        echo -e "${RED}[ALERT] Physical memory utilization exceeds 90%!${NC}"
    else
        echo -e "${GREEN}[OK] Memory utilization within safe limits.${NC}"
    fi
else
    echo "Warning: 'free' command not available."
fi

print_header "4. STORAGE PARTITION FORENSICS (Threshold: ${DISK_WARN_THRESHOLD}%)"
printf "${BOLD}%-24s %-8s %-8s %-8s %-8s %-20s${NC}\n" "Filesystem" "Size" "Used" "Avail" "Use%" "Mounted on"
echo "----------------------------------------------------------------------------------"

DISK_ALERT_COUNT=0
while read -r fs size used avail usepct mount; do
    pct_num="${usepct%\%}"
    if [[ "${pct_num}" =~ ^[0-9]+$ ]]; then
        if [ "${pct_num}" -ge "${DISK_WARN_THRESHOLD}" ]; then
            printf "${RED}%-24s %-8s %-8s %-8s %-8s %-20s [ALERT]${NC}\n" "${fs}" "${size}" "${used}" "${avail}" "${usepct}" "${mount}"
            ((DISK_ALERT_COUNT++))
        else
            printf "%-24s %-8s %-8s %-8s %-8s %-20s\n" "${fs}" "${size}" "${used}" "${avail}" "${usepct}" "${mount}"
        fi
    fi
done < <(df -h -P -x tmpfs -x devtmpfs -x overlay 2>/dev/null | tail -n +2)

if [ "${DISK_ALERT_COUNT}" -gt 0 ]; then
    echo -e "\n${RED}[WARNING] ${DISK_ALERT_COUNT} partition(s) exceeded the ${DISK_WARN_THRESHOLD}% storage threshold!${NC}"
else
    echo -e "\n${GREEN}[OK] All examined storage partitions are operating within safe bounds.${NC}"
fi

print_header "5. TOP 5 MEMORY-INTENSIVE PROCESSES"
printf "${BOLD}%-8s %-12s %-8s %-8s %-30s${NC}\n" "PID" "USER" "%CPU" "%MEM" "COMMAND"
echo "----------------------------------------------------------------------"
ps -eo pid,user,%cpu,%mem,comm --sort=-%mem | head -n 6 | tail -n +2 | while read -r p u c m cmd; do
    printf "%-8s %-12s %-8s %-8s %-30s\n" "${p}" "${u}" "${c}" "${m}" "${cmd}"
done

print_header "6. TOP 5 CPU-INTENSIVE PROCESSES"
printf "${BOLD}%-8s %-12s %-8s %-8s %-30s${NC}\n" "PID" "USER" "%CPU" "%MEM" "COMMAND"
echo "----------------------------------------------------------------------"
ps -eo pid,user,%cpu,%mem,comm --sort=-%cpu | head -n 6 | tail -n +2 | while read -r p u c m cmd; do
    printf "%-8s %-12s %-8s %-8s %-30s\n" "${p}" "${u}" "${c}" "${m}" "${cmd}"
done

# Optional JSON Export
if [ -n "${JSON_OUTPUT_FILE}" ]; then
    print_header "7. JSON TELEMETRY EXPORT"
    cat << EOF > "${JSON_OUTPUT_FILE}"
{
  "timestamp": "${TIMESTAMP_VAL}",
  "hostname": "${HOSTNAME_VAL}",
  "kernel": "${KERNEL_VAL}",
  "uptime": "${UPTIME_VAL}",
  "cpu": {
    "cores": ${CPU_CORES},
    "load_1m": ${LOAD_1M},
    "load_5m": ${LOAD_5M},
    "load_15m": ${LOAD_15M}
  },
  "memory": {
    "total_mb": ${MEM_TOTAL_MB:-0},
    "used_mb": ${MEM_USED_MB:-0},
    "available_mb": ${MEM_AVAIL_MB:-0},
    "used_percentage": ${MEM_USED_PCT:-0}
  },
  "disk_alerts": ${DISK_ALERT_COUNT}
}
EOF
    echo -e "${GREEN}[SUCCESS] JSON telemetry exported to: ${JSON_OUTPUT_FILE}${NC}"
fi

print_header "AUDIT SUMMARY COMPLETE"
echo -e "${GREEN}System health inspection finished successfully with return status 0.${NC}\n"
exit 0
