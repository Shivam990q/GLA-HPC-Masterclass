#!/usr/bin/env bash
# ==============================================================================
# Script: 03_batch_loop_automation.sh
# Purpose: Level 3 — For Loops, Task Dispatching, and Output Redirection (>> / >)
# Target : GLA University HPC Masterclass (Lead: Shivam Gupta)
# ==============================================================================

# Define an array of simulated compute nodes
COMPUTE_NODES=("node-cpu-01" "node-cpu-02" "node-gpu-01" "node-ai-gaudi")
LOG_FILE="./cluster_dispatch.log"

# Clean up previous log if exists
> "$LOG_FILE"

echo "=========================================================="
echo "  STEP 3: CLUSTER BATCH LOOP & AUTOMATION"
echo "=========================================================="
echo "[*] Dispatching tasks across ${#COMPUTE_NODES[@]} compute nodes..."

# Loop through each node
for node in "${COMPUTE_NODES[@]}"; do
    STATUS="ACTIVE"
    TIMESTAMP=$(date '+%H:%M:%S')
    
    # Log formatted line to file using >> (append)
    echo "[${TIMESTAMP}] Dispatched batch job to ${node} -> Status: ${STATUS}" >> "$LOG_FILE"
    echo "  • Node ${node}: Assigned Batch Worker Task"
done

echo "----------------------------------------------------------"
echo "[+] All tasks dispatched! Displaying log file contents:"
cat "$LOG_FILE"
echo "=========================================================="
