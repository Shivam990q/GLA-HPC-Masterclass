#!/usr/bin/env bash
# ==============================================================================
# Script Name   : 04_log_analyzer_report.sh
# Description   : Forensic Security Log Parser & SSH Brute-Force Incident Reporter
# Architecture  : POSIX compliant, bash 4.0+
# Author        : GLA HPC Masterclass Training Division
# Date          : 2026-10-24
# License       : MIT
# Usage         : ./04_log_analyzer_report.sh [-f <log_path>] [-t <threshold>] [-o <report.txt>]
# ==============================================================================

set -euo pipefail

# ANSI Color Codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

LOG_PATH="/var/log/auth.log"
BRUTE_FORCE_THRESHOLD=5
REPORT_OUTPUT=""

usage() {
    cat << EOF
Usage: $(basename "$0") [OPTIONS]

Forensic parser for SSH authentication logs (Debian/Ubuntu auth.log or RHEL secure).

Options:
    -f <path>       Path to authentication log file (Default: /var/log/auth.log or /var/log/secure)
    -t <threshold>  Brute-force alert threshold for failed logins from single IP (Default: 5)
    -o <file>       Export formatted incident report to file
    -h              Display this help message and exit

Examples:
    $(basename "$0") -f ./auth_traffic.log
    $(basename "$0") -f /var/log/auth.log -t 10 -o /tmp/security_incident_report.txt
EOF
    exit 0
}

while getopts ":f:t:o:h" opt; do
    case "${opt}" in
        f) LOG_PATH="${OPTARG}" ;;
        t)
            if ! [[ "${OPTARG}" =~ ^[0-9]+$ ]] || [ "${OPTARG}" -lt 1 ]; then
                echo "Error: Threshold must be a positive integer." >&2
                exit 1
            fi
            BRUTE_FORCE_THRESHOLD="${OPTARG}"
            ;;
        o) REPORT_OUTPUT="${OPTARG}" ;;
        h) usage ;;
        \?) echo "Error: Invalid option -${OPTARG}" >&2; usage ;;
        :)  echo "Error: Option -${OPTARG} requires an argument." >&2; usage ;;
    esac
done

# Fallback detection for RHEL/CentOS systems if default path does not exist
if [[ "${LOG_PATH}" == "/var/log/auth.log" && ! -f "${LOG_PATH}" && -f "/var/log/secure" ]]; then
    LOG_PATH="/var/log/secure"
fi

if [[ ! -f "${LOG_PATH}" ]]; then
    echo -e "${RED}[ERROR] Target log file does not exist: ${LOG_PATH}${NC}" >&2
    echo "Tip: For testing, provide a sample log using the -f flag." >&2
    exit 2
fi

echo -e "${BOLD}${CYAN}=== COMMENCING FORENSIC LOG AUDIT: ${LOG_PATH} ===${NC}"
echo "Analysis Timestamp : $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
echo "Alert Threshold    : >= ${BRUTE_FORCE_THRESHOLD} failed attempts"
echo "----------------------------------------------------------------------------------"

TOTAL_LINES=$(wc -l < "${LOG_PATH}")
TOTAL_FAILED=$(grep -c "Failed password" "${LOG_PATH}" || true)
TOTAL_ACCEPTED=$(grep -c "Accepted " "${LOG_PATH}" || true)
TOTAL_INVALID_USER=$(grep -c "invalid user" "${LOG_PATH}" || true)

echo -e "${BOLD}Summary Metrics:${NC}"
echo -e "  Total Log Entries Examined : ${TOTAL_LINES}"
echo -e "  Total Failed Passwords     : ${RED}${TOTAL_FAILED}${NC}"
echo -e "  Total Invalid User Probes  : ${YELLOW}${TOTAL_INVALID_USER}${NC}"
echo -e "  Total Successful Logins    : ${GREEN}${TOTAL_ACCEPTED}${NC}\n"

echo -e "${BOLD}${RED}1. TOP OFFENDING IP ADDRESSES (Failed Authentication)${NC}"
printf "%-20s %-12s %-15s\n" "IP Address" "Failed Count" "Status"
echo "--------------------------------------------------------"

# Extract IP addresses following "from" in Failed password lines
# Count frequencies and sort descending
OFFENDING_REPORT=$(awk '/Failed password/ {
    for (i = 1; i <= NF; i++) {
        if ($i == "from") {
            ip = $(i+1)
            count[ip]++
        }
    }
}
END {
    for (addr in count) {
        printf "%s %d\n", addr, count[addr]
    }
}' "${LOG_PATH}" | sort -k2 -nr)

if [[ -z "${OFFENDING_REPORT}" ]]; then
    echo "No failed password events detected in log."
else
    while read -r ip count; do
        if [ "${count}" -ge "${BRUTE_FORCE_THRESHOLD}" ]; then
            printf "${RED}%-20s %-12s [BRUTE-FORCE ALERT]${NC}\n" "${ip}" "${count}"
        else
            printf "%-20s %-12s Normal\n" "${ip}" "${count}"
        fi
    done <<< "${OFFENDING_REPORT}"
fi

echo -e "\n${BOLD}${YELLOW}2. TOP TARGETED USERNAMES (Probe Targets)${NC}"
printf "%-20s %-12s\n" "Username" "Attempts"
echo "----------------------------------------"
awk '/Failed password/ {
    for (i = 1; i <= NF; i++) {
        if ($i == "user") {
            user = $(i+1)
            count[user]++
        } else if ($i == "for" && $(i+1) != "invalid") {
            user = $(i+1)
            count[user]++
        }
    }
}
END {
    for (u in count) {
        printf "%s %d\n", u, count[u]
    }
}' "${LOG_PATH}" | sort -k2 -nr | head -n 10 | while read -r user count; do
    printf "%-20s %-12s\n" "${user}" "${count}"
done

echo -e "\n${BOLD}${GREEN}3. SUCCESSFUL SSH AUTHENTICATIONS (Audit Trail)${NC}"
printf "%-16s %-16s %-20s %-15s\n" "Date" "Time" "User" "Remote IP"
echo "------------------------------------------------------------------------"
grep "Accepted " "${LOG_PATH}" | awk '{
    for (i = 1; i <= NF; i++) {
        if ($i == "for") u = $(i+1)
        if ($i == "from") ip = $(i+1)
    }
    printf "%-16s %-16s %-20s %-15s\n", $1, $2, u, ip
}' | head -n 10

# Optional Report File Output
if [[ -n "${REPORT_OUTPUT}" ]]; then
    cat << EOF > "${REPORT_OUTPUT}"
================================================================================
GLA HPC MASTERCLASS - FORENSIC SECURITY AUDIT REPORT
Log Source       : ${LOG_PATH}
Audit Timestamp  : $(date -u +'%Y-%m-%dT%H:%M:%SZ')
Total Inspected  : ${TOTAL_LINES} lines
Failed Passwords : ${TOTAL_FAILED}
Accepted Logins  : ${TOTAL_ACCEPTED}
Brute Threshold  : ${BRUTE_FORCE_THRESHOLD} attempts
================================================================================

TOP OFFENDING IP ADDRESSES:
${OFFENDING_REPORT}

Report generated automatically by 04_log_analyzer_report.sh.
EOF
    echo -e "\n${GREEN}[SUCCESS] Complete report written to: ${REPORT_OUTPUT}${NC}"
fi

echo -e "\n${GREEN}[DONE] Log forensic triage completed successfully.${NC}"
exit 0
