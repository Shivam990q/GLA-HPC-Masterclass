#!/usr/bin/env bash
# ==============================================================================
# Script Name   : 02_automated_backup_and_archive.sh
# Description   : Automated Directory Backup with SHA-256 Checksum & Retention Policy
# Architecture  : POSIX compliant, bash 4.0+
# Author        : GLA HPC Masterclass Training Division
# Date          : 2026-10-24
# License       : MIT
# Usage         : ./02_automated_backup_and_archive.sh -s <source> -d <dest> [-k <days>] [-c <gz|bz2|xz>]
# ==============================================================================

set -euo pipefail

# ANSI Color Codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Default Parameters
SOURCE_DIR=""
DEST_DIR=""
RETENTION_DAYS=7
COMPRESSION_ALGO="gz"
TEMP_STAGE_DIR=""

log_info()    { echo -e "${CYAN}[INFO]${NC} $(date +'%Y-%m-%d %H:%M:%S') - $1"; }
log_success() { echo -e "${GREEN}[SUCCESS]${NC} $(date +'%Y-%m-%d %H:%M:%S') - $1"; }
log_warn()    { echo -e "${YELLOW}[WARN]${NC} $(date +'%Y-%m-%d %H:%M:%S') - $1"; }
log_error()   { echo -e "${RED}[ERROR]${NC} $(date +'%Y-%m-%d %H:%M:%S') - $1" >&2; }

# Trap for Abnormal Interruption & Temporary Resource Cleanup
cleanup() {
    local exit_code=$?
    if [[ -n "${TEMP_STAGE_DIR}" && -d "${TEMP_STAGE_DIR}" ]]; then
        log_info "Cleaning up temporary staging directory: ${TEMP_STAGE_DIR}"
        rm -rf "${TEMP_STAGE_DIR}"
    fi
    if [[ ${exit_code} -ne 0 ]]; then
        log_error "Backup process aborted unexpectedly with exit status: ${exit_code}"
    fi
}
trap cleanup EXIT INT TERM

usage() {
    cat << EOF
Usage: $(basename "$0") -s <source_dir> -d <dest_dir> [OPTIONS]

Automated backup generator with cryptographic checksums and retention cleanup.

Mandatory Arguments:
    -s <dir>    Source directory path to archive
    -d <dir>    Destination directory path to store backup tarballs

Optional Arguments:
    -k <days>   Retention period in days (Old backups exceeding this will be pruned. Default: 7)
    -c <algo>   Compression algorithm: gz (gzip), bz2 (bzip2), xz (xz). Default: gz
    -h          Display this help message and exit

Examples:
    $(basename "$0") -s /home/student/project -d /mnt/backup/projects
    $(basename "$0") -s /etc -d /var/backups -k 14 -c xz
EOF
    exit 1
}

while getopts ":s:d:k:c:h" opt; do
    case "${opt}" in
        s) SOURCE_DIR="${OPTARG}" ;;
        d) DEST_DIR="${OPTARG}" ;;
        k)
            if ! [[ "${OPTARG}" =~ ^[0-9]+$ ]] || [ "${OPTARG}" -lt 1 ]; then
                log_error "Retention days (-k) must be a positive integer."
                exit 1
            fi
            RETENTION_DAYS="${OPTARG}"
            ;;
        c)
            case "${OPTARG}" in
                gz|bz2|xz) COMPRESSION_ALGO="${OPTARG}" ;;
                *) log_error "Invalid compression algorithm '${OPTARG}'. Supported: gz, bz2, xz"; exit 1 ;;
            esac
            ;;
        h) usage ;;
        \?) log_error "Invalid option: -${OPTARG}"; usage ;;
        :)  log_error "Option -${OPTARG} requires an argument."; usage ;;
    esac
done

if [[ -z "${SOURCE_DIR}" || -z "${DEST_DIR}" ]]; then
    log_error "Both source directory (-s) and destination directory (-d) are required."
    usage
fi

if [[ ! -d "${SOURCE_DIR}" ]]; then
    log_error "Source directory does not exist or is not a directory: ${SOURCE_DIR}"
    exit 2
fi

# Ensure Destination Directory Exists
mkdir -p "${DEST_DIR}"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BASE_NAME=$(basename "${SOURCE_DIR}")

# Determine Compression Options & File Extension
case "${COMPRESSION_ALGO}" in
    gz)  TAR_FLAGS="-czf"; EXT="tar.gz" ;;
    bz2) TAR_FLAGS="-cjf"; EXT="tar.bz2" ;;
    xz)  TAR_FLAGS="-cJf"; EXT="tar.xz" ;;
esac

ARCHIVE_NAME="backup_${BASE_NAME}_${TIMESTAMP}.${EXT}"
TARGET_PATH="${DEST_DIR}/${ARCHIVE_NAME}"
CHECKSUM_FILE="${TARGET_PATH}.sha256"

log_info "Initiating archival of '${SOURCE_DIR}'"
log_info "Target Archive: ${TARGET_PATH}"
log_info "Compression Algorithm: ${COMPRESSION_ALGO}"

# Create Ephemeral Working Dir
TEMP_STAGE_DIR=$(mktemp -d /tmp/backup_stage_XXXXXX)

# Perform Archival
PARENT_DIR=$(dirname "${SOURCE_DIR}")
tar ${TAR_FLAGS} "${TARGET_PATH}" -C "${PARENT_DIR}" "${BASE_NAME}"

ARCHIVE_SIZE=$(du -h "${TARGET_PATH}" | awk '{print $1}')
log_success "Archive generated successfully (Size: ${ARCHIVE_SIZE})"

# Compute SHA-256 Checksum
log_info "Generating SHA-256 cryptographic verification checksum..."
(
    cd "${DEST_DIR}"
    sha256sum "${ARCHIVE_NAME}" > "${ARCHIVE_NAME}.sha256"
)
log_success "Checksum saved to: ${CHECKSUM_FILE}"

# Self-Verification Test
log_info "Performing read-back verification drill..."
(
    cd "${DEST_DIR}"
    sha256sum -c "${ARCHIVE_NAME}.sha256" >/dev/null
)
log_success "Cryptographic integrity check passed 100%!"

# Retention Cleanup Policy
log_info "Executing retention pruning: Deleting archives older than ${RETENTION_DAYS} days in ${DEST_DIR}..."
PRUNED_COUNT=0
while IFS= read -r old_file; do
    if [[ -f "${old_file}" ]]; then
        log_warn "Pruning stale backup file: ${old_file}"
        rm -f "${old_file}" "${old_file}.sha256" 2>/dev/null || true
        ((PRUNED_COUNT++))
    fi
done < <(find "${DEST_DIR}" -maxdepth 1 -name "backup_${BASE_NAME}_*.tar.*" -type f -mtime +"${RETENTION_DAYS}")

log_info "Pruning completed: ${PRUNED_COUNT} stale archives eliminated."
log_success "Backup lifecycle completed with return code 0."
exit 0
