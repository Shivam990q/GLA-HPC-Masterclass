#!/usr/bin/env bash
# ==============================================================================
# Script Name   : 03_batch_user_provisioning.sh
# Description   : Batch HPC User Account Provisioning from CSV with SSH Public Key Injection
# Architecture  : POSIX compliant, bash 4.0+
# Author        : GLA HPC Masterclass Training Division
# Date          : 2026-10-24
# License       : MIT
# Usage         : sudo ./03_batch_user_provisioning.sh -f <users.csv> [-d]
# ==============================================================================

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

CSV_FILE=""
DRY_RUN=false

log_info()    { echo -e "${CYAN}[INFO]${NC} $(date +'%H:%M:%S') - $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $(date +'%H:%M:%S') - $1"; }
log_warn()    { echo -e "${YELLOW}[WARN]${NC} $(date +'%H:%M:%S') - $1"; }
log_error()   { echo -e "${RED}[ERROR]${NC} $(date +'%H:%M:%S') - $1" >&2; }

usage() {
    cat << EOF
Usage: sudo $(basename "$0") -f <users.csv> [OPTIONS]

Batch provision HPC user accounts, home directories, groups, and SSH keys.

CSV Format (comma-separated, header line skipped):
    username,uid,primary_group,secondary_groups,login_shell,ssh_public_key

Example CSV line:
    researcher1,2001,hpcusers,slurm:gpu,/bin/bash,ssh-ed25519 AAAAC3NzaC1lZDI1NTE5... user@domain

Options:
    -f <file>   Path to the users CSV definition file
    -d          Dry-run mode (Simulate and validate without modifying system state)
    -h          Display this help message and exit
EOF
    exit 1
}

while getopts ":f:dh" opt; do
    case "${opt}" in
        f) CSV_FILE="${OPTARG}" ;;
        d) DRY_RUN=true ;;
        h) usage ;;
        \?) log_error "Invalid option: -${OPTARG}"; usage ;;
        :)  log_error "Option -${OPTARG} requires an argument."; usage ;;
    esac
done

if [[ -z "${CSV_FILE}" ]]; then
    log_error "CSV file path (-f) is required."
    usage
fi

if [[ ! -f "${CSV_FILE}" ]]; then
    log_error "Specified CSV file does not exist: ${CSV_FILE}"
    exit 2
fi

# Privilege Verification (Bypass for dry-run if desired, but recommended for production)
if [[ "${EUID}" -ne 0 && "${DRY_RUN}" == "false" ]]; then
    log_error "This script must be executed with administrative/root privileges (sudo)."
    exit 3
fi

if [[ "${DRY_RUN}" == "true" ]]; then
    log_warn "DRY-RUN MODE ENABLED: No system modifications will be written to disk."
fi

LINE_NUM=0
SUCCESS_COUNT=0
SKIP_COUNT=0

while IFS=',' read -r username uid primary_group secondary_groups login_shell ssh_pubkey || [ -n "${username}" ]; do
    ((LINE_NUM++))
    
    # Strip carriage returns and leading/trailing whitespace
    username=$(echo "${username}" | tr -d '\r' | xargs)
    uid=$(echo "${uid}" | tr -d '\r' | xargs)
    primary_group=$(echo "${primary_group}" | tr -d '\r' | xargs)
    secondary_groups=$(echo "${secondary_groups}" | tr -d '\r' | xargs)
    login_shell=$(echo "${login_shell}" | tr -d '\r' | xargs)
    ssh_pubkey=$(echo "${ssh_pubkey}" | tr -d '\r' | xargs)
    
    # Skip Header or Empty Lines
    if [[ "${LINE_NUM}" -eq 1 && "${username}" =~ ^(username|user|Name) ]]; then
        continue
    fi
    if [[ -z "${username}" || "${username}" =~ ^# ]]; then
        continue
    fi
    
    log_info "Processing record [Line ${LINE_NUM}]: User='${username}', UID='${uid}', Group='${primary_group}'"
    
    # Check if User Already Exists
    if id "${username}" &>/dev/null; then
        log_warn "User '${username}' already exists in passwd database. Skipping creation."
        ((SKIP_COUNT++))
        continue
    fi
    
    # Ensure Primary Group Exists
    if [[ "${DRY_RUN}" == "false" ]]; then
        if ! getent group "${primary_group}" >/dev/null; then
            log_info "Creating missing primary group: ${primary_group}"
            groupadd "${primary_group}"
        fi
        
        # User Creation Command
        USERADD_ARGS=("-m" "-g" "${primary_group}" "-s" "${login_shell}")
        if [[ -n "${uid}" && "${uid}" =~ ^[0-9]+$ ]]; then
            USERADD_ARGS+=("-u" "${uid}")
        fi
        if [[ -n "${secondary_groups}" && "${secondary_groups}" != "none" ]]; then
            USERADD_ARGS+=("-G" "${secondary_groups}")
        fi
        USERADD_ARGS+=("${username}")
        
        useradd "${USERADD_ARGS[@]}"
        log_success "Account created: ${username}"
        
        # Configure SSH Directory & Authorized Keys
        USER_HOME=$(getent passwd "${username}" | cut -d: -f6)
        SSH_DIR="${USER_HOME}/.ssh"
        AUTH_KEYS="${SSH_DIR}/authorized_keys"
        
        mkdir -p "${SSH_DIR}"
        chmod 700 "${SSH_DIR}"
        
        if [[ -n "${ssh_pubkey}" && "${ssh_pubkey}" =~ ^ssh- ]]; then
            echo "${ssh_pubkey}" > "${AUTH_KEYS}"
            chmod 600 "${AUTH_KEYS}"
            log_success "Installed SSH public key into: ${AUTH_KEYS}"
        fi
        
        # Enforce Ownership
        chown -R "${username}:${primary_group}" "${SSH_DIR}"
    else
        log_info "[DRY-RUN] Would create user '${username}' (UID: ${uid:-auto}, Shell: ${login_shell})"
        if [[ -n "${ssh_pubkey}" ]]; then
            log_info "[DRY-RUN] Would inject SSH key: ${ssh_pubkey:0:30}..."
        fi
    fi
    
    ((SUCCESS_COUNT++))
done < "${CSV_FILE}"

echo -e "\n${BOLD}${CYAN}=== BATCH PROVISIONING SUMMARY ===${NC}"
echo -e "${GREEN}Successfully Provisioned : ${SUCCESS_COUNT}${NC}"
echo -e "${YELLOW}Skipped Existing Users   : ${SKIP_COUNT}${NC}"
echo -e "${BOLD}Total Records Inspected  : ${LINE_NUM}${NC}"
exit 0
