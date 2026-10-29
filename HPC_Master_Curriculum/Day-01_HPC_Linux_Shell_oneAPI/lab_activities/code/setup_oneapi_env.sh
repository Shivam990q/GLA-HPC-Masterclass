#!/usr/bin/env bash
# ==============================================================================
# Script: setup_oneapi_env.sh
# Purpose: Detects and sources Intel oneAPI environment variables
# ==============================================================================
set -e

ONEAPI_PATHS=(
    "/opt/intel/oneapi/setvars.sh"
    "/opt/intel/oneapi/oneapi-vars.sh"
    "$HOME/intel/oneapi/setvars.sh"
)

FOUND=0
for path in "${ONEAPI_PATHS[@]}"; do
    if [ -f "$path" ]; then
        echo "[+] Found Intel oneAPI environment script at: $path"
        source "$path" --force
        FOUND=1
        break
    fi
done

if [ $FOUND -eq 1 ]; then
    echo "[+] oneAPI environment sourced successfully!"
    echo "    • icpx version: $(command -v icpx || echo 'Not installed')"
    echo "    • dpcpp version: $(command -v dpcpp || echo 'Not installed')"
else
    echo "[-] Intel oneAPI setvars.sh not found in standard system locations."
    echo "    Falling back to standard GCC/Clang development environment."
fi
