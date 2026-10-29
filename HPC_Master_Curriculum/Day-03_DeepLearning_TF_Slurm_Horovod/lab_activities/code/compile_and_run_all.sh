#!/usr/bin/env bash
# ==============================================================================
# compile_and_run_all.sh
# GLA University — Day 3 Hands-On Automated Build and Execution Harness
# ==============================================================================

set -euo pipefail

echo "======================================================================"
echo "   🚀 GLA UNIVERSITY: DAY 3 DEEP LEARNING, SLURM & HOROVOD SUITE     "
echo "======================================================================"

# 1. Environment & Module Audit
echo -e "\n[*] [Step 1] Auditing Deep Learning Software Stack..."
python3 --version
which sbatch 2>/dev/null && echo "[+] Slurm Workload Manager Detected" || echo "[-] Slurm not installed (Standalone server mode)"
which mpirun 2>/dev/null && echo "[+] MPI Runtime Detected" || echo "[-] OpenMPI/Intel MPI not found"

# 2. Intel oneDNN Operator Fusion Benchmark
echo -e "\n[*] [Step 2] Executing Intel oneDNN Operator Fusion Benchmark..."
python3 tf_onednn_benchmark.py

# 3. Habana Gaudi & SynapseAI Hardware Probe
echo -e "\n[*] [Step 3] Running Intel Habana Gaudi Hardware & SynapseAI Probe..."
python3 habana_gaudi_synapse_check.py

# 4. Intel Data Center GPU Max (XPU) Probe
echo -e "\n[*] [Step 4] Running Intel Data Center GPU Max (ITEX/XPU) Probe..."
python3 intel_gpu_xpu_check.py

# 5. Distributed Horovod Deep Learning Test
echo -e "\n[*] [Step 5] Checking Horovod Distributed Deep Learning Script..."
if python3 -c "import horovod" &>/dev/null; then
    echo "    [+] Horovod is installed. Running 2-worker simulation..."
    mpirun -np 2 python3 horovod_tf_training.py
else
    echo "    [-] Horovod module not installed in current Python env."
    echo "    [+] Syntax validating horovod_tf_training.py..."
    python3 -m py_compile horovod_tf_training.py
    echo "    [+] horovod_tf_training.py syntax verified cleanly!"
fi

# 6. Slurm Batch Scripts Syntax Verification
echo -e "\n[*] [Step 6] Validating Slurm Batch Scripts..."
bash -n slurm_dl_single_node.slurm && echo "    [+] slurm_dl_single_node.slurm bash syntax: OK"
bash -n slurm_dl_multi_node.slurm && echo "    [+] slurm_dl_multi_node.slurm bash syntax: OK"
bash -n slurm_batch_template.slurm && echo "    [+] slurm_batch_template.slurm bash syntax: OK"

echo -e "\n======================================================================"
echo "  🏆 ALL DAY 3 BENCHMARKS & SLURM SCRIPTS VALIDATED SUCCESSFULLY!"
echo "======================================================================"
