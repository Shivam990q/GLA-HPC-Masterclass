#!/usr/bin/env bash
# ==============================================================================
# Script: 02_conditions_and_exit_codes.sh
# Purpose: Level 2 — Conditionals (if/else), File Checks, and Exit Codes ($?)
# Target : GLA University HPC Masterclass (Lead: Shivam Gupta)
# ==============================================================================

# Target folder to test
WORKSPACE_DIR="${HOME}/hpc_day01/data"

echo "=========================================================="
echo "  STEP 2: CONDITIONALS & EXIT STATUS CODES"
echo "=========================================================="

# Check if directory exists
if [ -d "$WORKSPACE_DIR" ]; then
    echo "[+] Found existing directory: $WORKSPACE_DIR"
else
    echo "[-] Directory not found. Creating it now..."
    mkdir -p "$WORKSPACE_DIR"
    # $? holds the exit status of the previous command (0 = success, non-zero = failure)
    echo "[+] mkdir command completed with exit code: $?"
fi

# Create a small sample file inside
SAMPLE_FILE="${WORKSPACE_DIR}/sample.txt"
echo "HPC Batch Processing initialized on $(date)" > "$SAMPLE_FILE"

# Verify file exists
if [ -f "$SAMPLE_FILE" ]; then
    echo "[+] Verified file creation: $SAMPLE_FILE"
    echo "[+] File size: $(wc -c < "$SAMPLE_FILE") bytes"
fi
echo "=========================================================="
