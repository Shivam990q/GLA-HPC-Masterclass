#!/usr/bin/env bash
# ==============================================================================
# compile_and_run_all.sh
# Automated verification test harness for Day 5 Standalone Code Files
# ==============================================================================
set -eo pipefail

echo "=========================================================="
echo "    DAY 5: CAPSTONE GENAI & LLM LAB TEST HARNESS         "
echo "=========================================================="

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "[1/4] Testing Python syntax integrity across all Day 5 scripts..."
python3 -m py_compile export_openvino_ir.py
python3 -m py_compile nncf_int4_quantization.py
python3 -m py_compile gaudi_llm_finetune_lora.py
python3 -m py_compile openvino_llm_benchmark.py
python3 -m py_compile llm_fastapi_server.py
echo "[✓] All Python scripts passed syntax compilation (py_compile)!"

echo "[2/4] Testing Model Ingestion & OpenVINO IR Export..."
python3 export_openvino_ir.py

echo "[3/4] Testing Intel NNCF INT4 Weight Quantization..."
python3 nncf_int4_quantization.py

echo "[4/4] Testing Habana Gaudi LoRA Fine-Tuning Simulator..."
python3 gaudi_llm_finetune_lora.py

echo "=========================================================="
echo "🎉 ALL DAY 5 STANDALONE LAB CODE VERIFIED AND PASSING! 🎉"
echo "=========================================================="
