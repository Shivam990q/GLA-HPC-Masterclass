# 💻 DAY 5: HANDS-ON LAB & COMMANDS PLAYBOOK
## Practical Execution for OpenVINO LLM Compression & Distributed Fine-Tuning
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Audience:** 60 B.Tech / M.Tech CS Students  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 🚀 Lab Overview

Every student executes these commands inside their **Google Colab environment** (or local Linux terminal) to compress a real Transformer model using Intel OpenVINO, measure inference speedup, and inspect multi-node Slurm fine-tuning scripts.

---

## 📋 LAB SECTION 1: Hardware Introspection & AMX Matrix Verification

```bash
# 1. Verify CPU architecture and core count
lscpu | grep -E "Model name|Socket|Core|Thread"

# 2. Check for Intel AMX (Advanced Matrix Extensions) and AVX-512 flags
lscpu | grep -E "amx_tile|amx_bf16|amx_int8|avx512"

# 3. Check memory capacity (Required for LLM parameter loading)
free -h
```

---

## 📋 LAB SECTION 2: Model Ingestion & OpenVINO IR Export

```python
# Save as export_openvino.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import openvino as ov
from pathlib import Path

MODEL_ID = "Qwen/Qwen2.5-0.5B-Instruct"
EXPORT_DIR = Path("./qwen_openvino_ir")

print(f"[INFO] Ingesting HuggingFace model: {MODEL_ID}...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)

print("[INFO] Compiling model to OpenVINO Intermediate Representation (IR)...")
ov_model = ov.convert_model(model, example_input=tokenizer("Hello Intel HPC", return_tensors="pt"))

EXPORT_DIR.mkdir(parents=True, exist_ok=True)
ov.save_model(ov_model, EXPORT_DIR / "model.xml")
tokenizer.save_pretrained(EXPORT_DIR)

print(f"[SUCCESS] OpenVINO IR Model saved to: {EXPORT_DIR}")
```

---

## 📋 LAB SECTION 3: NNCF Weight-Only INT4 Quantization

```python
# Save as quantize_int4.py
import openvino as ov
import nncf
from pathlib import Path

IR_PATH = Path("./qwen_openvino_ir/model.xml")
QUANT_DIR = Path("./qwen_openvino_int4")

print(f"[INFO] Loading base IR model from: {IR_PATH}...")
core = ov.Core()
model = core.read_model(IR_PATH)

print("[INFO] Applying NNCF Asymmetric INT4 Weight-Only Quantization...")
# Slashing 16-bit floating point weights to 4-bit integers
compressed_model = nncf.compress_weights(
    model,
    mode=nncf.CompressWeightsMode.INT4_ASYM,
    group_size=128,
    ratio=0.8
)

QUANT_DIR.mkdir(parents=True, exist_ok=True)
ov.save_model(compressed_model, QUANT_DIR / "model.xml")

# Measure file size drop
import os
fp_size = os.path.getsize("./qwen_openvino_ir/model.bin") / (1024 * 1024)
int4_size = os.path.getsize(QUANT_DIR / "model.bin") / (1024 * 1024)

print("==========================================================")
print(f"FP16 Weight Size:    {fp_size:.2f} MB")
print(f"INT4 Weight Size:    {int4_size:.2f} MB")
print(f"Reduction Ratio:     {((fp_size - int4_size) / fp_size) * 100:.1f}% Slashing!")
print("==========================================================")
```

---

## 📋 LAB SECTION 4: Latency & Throughput Benchmark (TTFT & TPS)

```python
# Save as benchmark_inference.py
import time
import openvino_genai as ov_genai

MODEL_PATH = "./qwen_openvino_int4"
PROMPT = "Explain the fundamental difference between Intel Xeon CPUs and Habana Gaudi accelerators for HPC workloads."

print(f"[INFO] Initializing OpenVINO GenAI LLM Pipeline on device: CPU...")
pipe = ov_genai.LLMPipeline(MODEL_PATH, "CPU")

print(f"[PROMPT]: {PROMPT}\n")
print("[OUTPUT STREAMING]:")

start_time = time.time()
first_token_time = None
token_count = 0

def streamer(subword):
    global first_token_time, token_count
    if first_token_time is None:
        first_token_time = time.time()
    token_count += 1
    print(subword, end="", flush=True)
    return False

pipe.generate(PROMPT, max_new_tokens=150, streamer=streamer)
end_time = time.time()

ttft = (first_token_time - start_time) * 1000 if first_token_time else 0
tps = token_count / (end_time - first_token_time) if first_token_time else 0

print("\n\n==========================================================")
print(f"Time to First Token (TTFT): {ttft:.2f} ms")
print(f"Tokens Per Second (TPS):    {tps:.2f} tokens/sec")
print(f"Total Generated Tokens:     {token_count}")
print("==========================================================")
```

---

## 📋 LAB SECTION 5: Multi-Node Slurm Distributed LoRA Fine-Tuning Script

```bash
cat << 'EOF' > ~/hpc_day05/scripts/run_distributed_lora.sh
#!/bin/bash
# ==============================================================================
# Slurm Batch Script: Multi-Node LoRA Fine-Tuning on Intel HPC Cluster
# ==============================================================================
#SBATCH --job-name=gla_llm_lora
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --partition=gaudi
#SBATCH --time=01:30:00

# 1. Activate oneAPI and PyTorch Environment
source /opt/intel/oneapi/setvars.sh 2>/dev/null
export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

# 2. Launch Distributed LoRA Fine-Tuning with Intel IPEX
srun python3 finetune_lora_cluster.py \
    --base_model Qwen/Qwen2.5-0.5B-Instruct \
    --dataset_path /scratch/gla_qa_dataset.json \
    --lora_r 16 \
    --lora_alpha 32 \
    --batch_size 8 \
    --epochs 3 \
    --output_dir /scratch/models/qwen_gla_lora
EOF
```
