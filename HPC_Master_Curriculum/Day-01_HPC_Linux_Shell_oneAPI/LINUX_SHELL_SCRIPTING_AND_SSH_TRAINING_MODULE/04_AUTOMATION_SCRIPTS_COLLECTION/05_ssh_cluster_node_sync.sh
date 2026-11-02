#!/usr/bin/env bash
# ==============================================================================
# Script Name   : 05_ssh_cluster_node_sync.sh
# Description   : Cluster Node Connectivity Probe & Rsync File Synchronizer
# Architecture  : POSIX compliant, bash 4.0+
# Author        : GLA HPC Masterclass Training Division
# Date          : 2026-10-24
# License       : MIT
# Usage         : ./05_ssh_cluster_node_sync.sh -n <nodes_file_or_list> -s <src> -d <dst> [-k <key>] [-dry]
# ==============================================================================

set -euo pipefail

# ANSI Color Codes
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

NODES_INPUT=""
SOURCE_DIR=""
DEST_DIR=""
SSH_KEY=""
SSH_USER=""
DRY_RUN=false
CONNECT_TIMEOUT=5

log_info()    { echo -e "${CYAN}[INFO]${NC} $(date +'%H:%M:%S') - $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $(date +'%H:%M:%S') - $1"; }
log_warn()    { echo -e "${YELLOW}[WARN]${NC} $(date +'%H:%M:%S') - $1"; }
log_error()   { echo -e "${RED}[ERROR]${NC} $(date +'%H:%M:%S') - $1" >&2; }

usage() {
    cat << EOF
Usage: $(basename "$0") -n <nodes_file_or_csv> -s <src_dir> -d <dest_dir> [OPTIONS]

Synchronizes files across multiple remote cluster compute nodes via SSH and rsync.

Required Arguments:
    -n <targets>  Path to node list file OR comma-separated hostnames (e.g. "node01,node02,node03")
    -s <src_dir>  Local source directory to replicate
    -d <dest_dir> Remote destination path on target nodes

Optional Arguments:
    -u <user>     Remote SSH username (Default: current shell user)
    -i <key_file> Path to specific SSH private identity file
    -t <seconds>  SSH connection timeout in seconds (Default: 5)
    -n            Dry-run mode (Passes -n to rsync, simulating transfer)
    -h            Display this help message and exit

Examples:
    $(basename "$0") -n "192.168.1.101,192.168.1.102" -s /opt/shared/app -d /opt/shared/app
    $(basename "$0") -n ./cluster_nodes.txt -s ~/datasets -d ~/datasets -i ~/.ssh/id_ed25519
EOF
    exit 1
}

while getopts ":n:s:d:u:i:t:Dh" opt; do
    case "${opt}" in
        n) NODES_INPUT="${OPTARG}" ;;
        s) SOURCE_DIR="${OPTARG}" ;;
        d) DEST_DIR="${OPTARG}" ;;
        u) SSH_USER="${OPTARG}" ;;
        i) SSH_KEY="${OPTARG}" ;;
        t) CONNECT_TIMEOUT="${OPTARG}" ;;
        D) DRY_RUN=true ;;
        h) usage ;;
        \?) log_error "Invalid option: -${OPTARG}"; usage ;;
        :)  log_error "Option -${OPTARG} requires an argument."; usage ;;
    esac
done

if [[ -z "${NODES_INPUT}" || -z "${SOURCE_DIR}" || -z "${DEST_DIR}" ]]; then
    log_error "Missing mandatory arguments: -n, -s, and -d are all required."
    usage
fi

if [[ ! -d "${SOURCE_DIR}" ]]; then
    log_error "Local source directory does not exist: ${SOURCE_DIR}"
    exit 2
fi

# Build Node Array
declare -a NODE_LIST=()
if [[ -f "${NODES_INPUT}" ]]; then
    while IFS= read -r line || [[ -n "${line}" ]]; do
        line=$(echo "${line}" | tr -d '\r' | xargs)
        if [[ -n "${line}" && ! "${line}" =~ ^# ]]; then
            NODE_LIST+=("${line}")
        fi
    done < "${NODES_INPUT}"
else
    IFS=',' read -r -a NODE_LIST <<< "${NODES_INPUT}"
fi

if [[ ${#NODE_LIST[@]} -eq 0 ]]; then
    log_error "No valid nodes specified."
    exit 3
fi

# Construct Base SSH Options
SSH_OPTS=("-o" "BatchMode=yes" "-o" "ConnectTimeout=${CONNECT_TIMEOUT}" "-o" "StrictHostKeyChecking=accept-new")
if [[ -n "${SSH_KEY}" ]]; then
    if [[ ! -f "${SSH_KEY}" ]]; then
        log_error "Specified private key does not exist: ${SSH_KEY}"
        exit 4
    fi
    SSH_OPTS+=("-i" "${SSH_KEY}")
fi

RSYNC_FLAGS="-avz --delete"
if [[ "${DRY_RUN}" == "true" ]]; then
    RSYNC_FLAGS="${RSYNC_FLAGS} -n"
    log_warn "DRY-RUN MODE ACTIVE: No remote filesystem changes will be applied."
fi

echo -e "\n${BOLD}${CYAN}=== CLUSTER NODE SYNCHRONIZATION ORCHESTRATOR ===${NC}"
echo "Total Nodes Targeted : ${#NODE_LIST[@]}"
echo "Source Directory     : ${SOURCE_DIR}"
echo "Destination Directory: ${DEST_DIR}"
echo "Dry Run Simulation   : ${DRY_RUN}"
echo "----------------------------------------------------------------------"

PASS_COUNT=0
FAIL_COUNT=0

for raw_node in "${NODE_LIST[@]}"; do
    node=$(echo "${raw_node}" | xargs)
    target_host="${node}"
    if [[ -n "${SSH_USER}" ]]; then
        target_host="${SSH_USER}@${node}"
    fi
    
    echo -e "\n${BOLD}--> Checking Node: [${target_host}]${NC}"
    
    # 1. Connectivity & Key Authentication Probe
    if ssh "${SSH_OPTS[@]}" "${target_host}" "echo '[SSH_OK] Connected to \$(hostname) with kernel \$(uname -r)'" 2>/dev/null; then
        log_success "Connectivity check passed for ${node}."
    else
        log_error "Unable to authenticate/connect to ${node}. Check network, SSH daemon, or key permissions."
        ((FAIL_COUNT++))
        continue
    fi
    
    # 2. Remote Destination Directory Preparation
    ssh "${SSH_OPTS[@]}" "${target_host}" "mkdir -p '${DEST_DIR}'"
    
    # 3. Synchronize via rsync over SSH
    log_info "Synchronizing payload to ${target_host}:${DEST_DIR}..."
    SSH_CMD_STRING="ssh ${SSH_OPTS[*]}"
    
    if rsync ${RSYNC_FLAGS} -e "${SSH_CMD_STRING}" "${SOURCE_DIR}/" "${target_host}:${DEST_DIR}/"; then
        log_success "Replication completed for node: ${node}"
        ((PASS_COUNT++))
    else
        log_error "Rsync sync failed for node: ${node}"
        ((FAIL_COUNT++))
    fi
done

echo -e "\n${BOLD}${CYAN}=== REPLICATION SUMMARY REPORT ===${NC}"
echo -e "${GREEN}Successful Syncs : ${PASS_COUNT}${NC}"
echo -e "${RED}Failed Nodes     : ${FAIL_COUNT}${NC}"
echo -e "${BOLD}Total Nodes      : ${#NODE_LIST[@]}${NC}"

if [[ ${FAIL_COUNT} -gt 0 ]]; then
    exit 1
fi
exit 0
