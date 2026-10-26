"""
build_day5_zero_to_god_tier.py
Constructs the exhaustive 00_ZERO_TO_GOD_TIER_MASTER_DOSSIER for Day 5:
Generative AI, LLMs on Intel HPC, Gaudi Accelerators & OpenVINO Quantization.
Written assuming Shivam knows ZERO, building up to an authoritative, master-level systems engineer.
"""

import os
from pathlib import Path

DAY5_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\Day-05_GenAI_LLMs_Gaudi_OpenVINO\00_ZERO_TO_GOD_TIER_MASTER_DOSSIER")

# Subdirectories
d_concept = DAY5_DIR / "01_Concept_From_Absolute_Scratch"
d_script = DAY5_DIR / "02_Minute_By_Minute_Trainer_Script"
d_defense = DAY5_DIR / "03_Student_Cross_Questioning_Defense"
d_code = DAY5_DIR / "04_Step_By_Step_CLI_And_Code_Breakdown"
d_debug = DAY5_DIR / "05_Lab_Challenges_And_Error_Debugging"

for d in [d_concept, d_script, d_defense, d_code, d_debug]:
    d.mkdir(parents=True, exist_ok=True)

print(f"[*] Building Day 5 Zero-to-God-Tier Dossier in: {DAY5_DIR}")

# ==============================================================================
# 1. Concept from Absolute Scratch
# ==============================================================================
f5_1 = d_concept / "concept_breakdown_intuitive_analogy.md"
f5_1.write_text("""# Day 5: Generative AI, LLMs, Intel Gaudi & OpenVINO - Intuitive Analogies (Zero to Mastery)

## 1. How Does an LLM Actually Work? (The Speed-Reading vs Word-by-Word Typing Analogy)

Students use ChatGPT every day, but 99% have no idea what happens inside the silicon when they send a prompt.
An LLM generates text in two fundamentally distinct phases:

### Phase 1: The Prefill Phase (The Speed-Reader)
- You submit a prompt with 500 words.
- The model ingests all 500 words **at the exact same time**.
- This is dense matrix multiplication: $Q \\times K^T$. Every word attends to every other word.
- The GPU or Intel Xeon AMX engine runs at **100% compute capacity**.
- This is **Compute-Bound**: the ALUs are screaming, crunching billions of operations in a few milliseconds.

### Phase 2: The Decode Phase (The Scribe with a Hand Cart)
- Now the model must generate the answer, one word at a time.
- To produce word #1:
  - The model must read **every single parameter** of the 7-Billion parameter model from RAM into the CPU/GPU registers!
  - 14 Gigabytes of weight data must travel across the memory bus just to generate *one single word*!
- To produce word #2:
  - It must read the **entire 14 Gigabytes again**!
- To produce word #3:
  - It reads the **entire 14 Gigabytes again**!
- **The Bottleneck**:
  - The compute units are barely doing any math (they only multiply 1 token vector by the weights).
  - The processor spends 99% of its time waiting for the memory bus to stream 14 GB of weights across the bus.
  - The Decode Phase is strictly **Memory-Bandwidth Bound**!

---

## 2. What is Quantization (OpenVINO NNCF)? (The Suitcase Packing Analogy)

Imagine you are packing for a flight with a strict 7 kg weight limit:
- **FP32 Precision (32-bit float)**:
  - Like packing each shirt inside a heavy wooden crate. Each number takes 4 bytes.
  - Your 7B model weighs **28 Gigabytes**. It doesn't fit on your laptop.
- **FP16 / BF16 Precision (16-bit float)**:
  - You replace wooden crates with cardboard boxes. Each number takes 2 bytes.
  - The model weighs **14 Gigabytes**.
- **INT8 Quantization (8-bit integer)**:
  - You vacuum-seal the clothes in lightweight plastic. Each number takes 1 byte.
  - The model weighs **7 Gigabytes**.
  - **Memory bandwidth traffic is cut in half!** Tokens generate twice as fast!
- **INT4 Quantization (4-bit integer)**:
  - Extreme compression. Each number takes 0.5 bytes.
  - The model weighs **3.5 Gigabytes**. It can now run on an ordinary Intel Core laptop CPU or edge device at 25+ tokens per second!
- **Does it lose intelligence?**
  - Modern quantization techniques (like OpenVINO NNCF Weight Compression) maintain 99%+ of the model's original accuracy because neural network weights are naturally resilient to small rounding noise.

---

## 3. What is Intel Gaudi? (The Dedicated Bullet Train vs General Taxi)

- **NVIDIA GPU**:
  - Like a high-end sports taxi. Can do 3D graphics, gaming, crypto, simulation, and AI.
  - To talk to another taxi across the country, it has to get on the municipal highway (PCIe bus) and hire an external courier (Mellanox NIC).
- **Intel Gaudi (Gaudi 2 / Gaudi 3)**:
  - A purpose-built, high-speed bullet train designed *exclusively* for deep learning matrix multiplication.
  - It has no graphics engine; it cannot play video games.
  - It has **24 high-speed 100-Gigabit Ethernet ports built directly onto the silicon die**!
  - Gaudi chips plug directly into each other across standard enterprise networking cables without needing proprietary, multi-thousand-dollar NVLink switches.
  - It cuts the cost of building large AI training clusters by nearly 50%.
""", encoding="utf-8")

f5_2 = d_concept / "low_level_silicon_and_mathematical_foundations.md"
f5_2.write_text("""# Day 5: Low-Level Silicon & Mathematical Foundations (GenAI, KV-Cache & Quantization)

## 1. Autoregressive Transformer Architecture & Attention Mechanism
The Scaled Dot-Product Attention is formulated as:
$$\\text{Attention}(Q, K, V) = \\text{softmax}\\left(\\frac{Q K^T}{\\sqrt{d_k}}\\right) V$$

Where:
- $Q \\in \\mathbb{R}^{B \\times H \\times L \\times d_k}$ (Queries)
- $K \\in \\mathbb{R}^{B \\times H \\times L \\times d_k}$ (Keys)
- $V \\in \\mathbb{R}^{B \\times H \\times L \\times d_k}$ (Values)
- $B$ = Batch size, $H$ = Number of attention heads, $L$ = Sequence length, $d_k$ = Head dimension.

---

## 2. The KV-Cache Memory Calculation Formula
In autoregressive decoding, recomputing Key and Value matrices for all past tokens at every step requires $O(L^2)$ redundant operations.
Instead, we cache past Keys and Values in memory: the **KV-Cache**.

### Exact Formula for KV-Cache Size:
$$\\text{KV-Cache Bytes} = 2 \\times 2 \\times n_{\\text{layers}} \\times n_{\\text{heads}} \\times d_{\\text{head}} \\times L_{\\text{seq}} \\times B \\times \\text{sizeof}(\\text{dtype})$$

Where:
- Factor of 2: One for Keys ($K$), one for Values ($V$).
- Factor of 2 (if using FP16/BF16): 2 bytes per float.

### Real-World Example: Llama-2 7B / Llama-3 8B
- $n_{\\text{layers}} = 32$
- $n_{\\text{heads}} = 32$
- $d_{\\text{head}} = 128$
- Precision: 16-bit (2 bytes)

Per-token KV-cache cost across all 32 layers:
$$\\text{Cost per token} = 2 \\times 32 \\times 32 \\times 128 \\times 2 = 524,288 \\text{ bytes} = 0.524 \\text{ MB per token}$$

For a context length of $L = 4096$ tokens:
$$\\text{KV-Cache per request} = 4096 \\times 0.524 \\text{ MB} \\approx 2.15 \\text{ GB}$$

If your web server serves a concurrency of $B = 16$ simultaneous users:
$$\\text{Concurrent KV-Cache Memory} = 16 \\times 2.15 \\text{ GB} = 34.4 \\text{ GB}$$
Notice: The KV-cache memory (34.4 GB) exceeds the size of the 7B model itself (14 GB)!
This is why modern serving systems use **PagedAttention** (virtual memory paging for KV blocks) and INT8 KV-cache quantization.

---

## 3. Post-Training Quantization (PTQ) Mathematics
Quantization maps continuous 32-bit floating-point numbers $x \\in [x_{\\min}, x_{\\max}]$ to discrete 8-bit signed integers $q \\in [-128, 127]$.

### Affine (Asymmetric) Quantization:
$$q = \\text{clamp}\\left(\\left\\lfloor \\frac{x}{S} \\right\\rceil + Z, \\; q_{\\min}, \\; q_{\\max}\\right)$$

Where:
- **Scale Factor** $S$:
  $$S = \\frac{x_{\\max} - x_{\\min}}{q_{\\max} - q_{\\min}}$$
- **Zero-Point** $Z$:
  $$Z = \\text{round}\\left(\\frac{-x_{\\min}}{S}\\right) + q_{\\min}$$

### Dequantization (Matrix Multiply):
$$\\hat{x} = S \\times (q - Z)$$

In Intel oneDNN and OpenVINO, when two INT8 matrices are multiplied, the processor uses hardware INT8 Dot-Product instructions (`VPDPBUSD` on AVX-512 VNNI or Intel AMX `TDPBUSD`), computing thirty-two INT8 multiplications and accumulating into INT32 in a single clock cycle!
""", encoding="utf-8")

# ==============================================================================
# 2. Minute-by-Minute Trainer Script
# ==============================================================================
f5_3 = d_script / "morning_session_trainer_script.md"
f5_3.write_text("""# Day 5: Morning Session Trainer Script (9:00 AM - 12:30 PM)

## 09:00 AM - 09:30 AM: Grand Finale Opening Hook
- **Spoken Script**:
  > *"Good morning, everyone. Welcome to the final day of our High Performance Computing Master Class.
  > 
  > Over the past four days, we climbed from single-core vectorization, to multi-core shared memory with OpenMP, to distributed clusters with MPI and Slurm, to microarchitecture profiling with VTune.
  > 
  > Today, we deploy everything we have learned to the most demanding computational frontier on Earth: Generative AI and Large Language Models.
  > 
  > Everyone in technology today wants to build AI applications. But very few understand how AI models actually execute on silicon.
  > Today, we demystify the memory physics of LLMs, explore Intel Gaudi supercomputing accelerators, and use Intel OpenVINO to run multi-billion parameter models at production throughput."*

## 09:30 AM - 10:30 AM: The Anatomy of LLM Inference: Prefill vs Decode
- **Action**: Write the Prefill vs Decode breakdown on the whiteboard.
- **Spoken Script**:
  > *"When you prompt a 7B parameter model, what makes it slow?
  > In the prompt prefill phase, all tokens are processed together: pure matrix multiplication, compute-bound, 100% core saturation.
  > 
  > But once the model starts generating tokens one-by-one in the decode phase, the physics invert completely:
  > To generate ONE token, you must stream all 14 Gigabytes of FP16 model weights through the memory bus!
  > 
  > If your memory bandwidth is 100 GB/s, the absolute physical limit of generation speed is:
  > $100 / 14 \\approx 7.1$ tokens per second.
  > It does not matter if your CPU runs at 10 GHz; you cannot exceed 7 tokens per second because the memory bus cannot deliver the weights any faster.
  > 
  > How do we break this bottleneck?
  > Quantization. If we compress the model to INT4, weights drop to 3.5 GB.
  > Now generation speed jumps to $100 / 3.5 \\approx 28.5$ tokens per second! A 4x speedup from silicon memory reduction."*

## 10:30 AM - 10:45 AM: Tea Break

## 10:45 AM - 12:30 PM: Intel Gaudi Accelerators & OpenVINO NNCF Deep Dive
- **Action**: Display Intel Gaudi 2/3 die architecture and OpenVINO pipeline.
- **Spoken Script**:
  > *"Let's look at Intel Gaudi.
  > Why is Gaudi disrupting the AI data center market?
  > Look at the networking: NVIDIA GPUs require separate PCIe network cards and expensive proprietary NVLink switches.
  > Intel Gaudi integrates **24 ports of 100GbE RoCE v2 directly onto the chip**!
  > Gaudi clusters communicate across standard optical Ethernet cables with zero host PCIe hops.
  > 
  > And for deployment at the edge, Intel OpenVINO takes PyTorch models, optimizes the computation graph, fuses layers, and quantizes weights to INT8 and INT4."*
""", encoding="utf-8")

f5_4 = d_script / "afternoon_session_trainer_script.md"
f5_4.write_text("""# Day 5: Afternoon Session Trainer Script (1:30 PM - 4:30 PM)

## 01:30 PM - 02:15 PM: Live OpenVINO Quantization & Benchmark Walkthrough
- **Action**: Run `openvino_llm_benchmark.py` live on screen.
- **Spoken Script**:
  > *"Watch this terminal benchmark:
  > We benchmark FP32 PyTorch model versus OpenVINO INT8 quantized model on a sequence classification task.
  > 
  > PyTorch FP32 Latency: 48.5 ms per sample.
  > OpenVINO INT8 Latency: 9.2 ms per sample.
  > 
  > That is a **5.2x latency reduction** and a **75% memory footprint reduction**, running directly on standard Intel CPU cores using AVX-512 VNNI instructions."*

## 02:15 PM - 03:45 PM: Production LLM Serving Lab (FastAPI + Async Concurrency)
- **Action**: Students launch `llm_fastapi_server.py` and test endpoints using `curl` or Locust benchmark.
- **Spoken Script**:
  > *"Open `llm_fastapi_server.py`. Look at the asynchronous endpoint `/generate`.
  > Notice how the server manages concurrent requests without blocking the event loop.
  > 
  > Run the client stress test: send 50 concurrent requests.
  > Observe how OpenVINO's multithreaded runtime handles the workload with steady latency."*

## 03:45 PM - 04:30 PM: Course Finale, Valedictory & The Systems Engineer Mindset
- **Spoken Script**:
  > *"Over the past five days at GLA University, you have completed an intensive journey.
  > 
  > You are no longer standard software developers who write code and hope the computer runs it well.
  > You are now systems engineers who understand what happens to every byte, every register, every cache line, and every network packet.
  > 
  > As you graduate and step into the technology industry, remember:
  > Anyone can write code that runs.
  > Elite engineers write code that scales.
  > 
  > Thank you for your tremendous focus and dedication. Congratulations on completing the High Performance Computing Master Class."*
""", encoding="utf-8")

f5_5 = d_script / "whiteboard_sketches_and_visual_prompts.md"
f5_5.write_text("""# Day 5: Whiteboard Sketches & Visual Architecture Prompts

## Sketch 1: Transformer Inference: Prefill vs Decode Phases
```
PREFILL PHASE (Prompt: "Explain HPC in simple terms"):
[ "Explain", "HPC", "in", "simple", "terms" ]
       \         \     |     /         /
        +---------+----+----+---------+
                  |
        [ Dense Attention GEMM ]  <--- COMPUTE-BOUND (100% Core Utilization)
                  |
             Output: "High"

DECODE PHASE (Autoregressive Generation):
Step 1: "High"             -> Stream entire 14GB weights -> "Performance"
Step 2: "Performance"      -> Stream entire 14GB weights -> "Computing"
Step 3: "Computing"        -> Stream entire 14GB weights -> "is"
Step 4: "is"               -> Stream entire 14GB weights -> "fast"
                               ^
                               |
               STRICTLY MEMORY-BANDWIDTH BOUND!
```

## Sketch 2: Intel Gaudi Integrated Networking Architecture
```
+---------------------------------------------------------------+
|                      INTEL GAUDI DIE                          |
|  [ Matrix Math Engine (MME) ]    [ Tensor Processing Cores ]  |
|  [ Shared SRAM 96MB ]            [ 96GB HBM2e Memory ]        |
|                                                               |
|  [ 24x 100GbE RoCE v2 Integrated On-Die Network Engines ]     |
+-------------------------------+-------------------------------+
                                |
             Direct Optical Ethernet Cables
                 (No external PCIe NICs!)
                                v
                To Neighboring Gaudi Accelerators
```
""", encoding="utf-8")

# ==============================================================================
# 3. Student Cross-Questioning Defense
# ==============================================================================
f5_6 = d_defense / "nasty_trap_questions_and_killer_answers.md"
f5_6.write_text("""# Day 5: Student Cross-Questioning Defense - Nasty Trap Questions & Killer Answers

### Trap Q1: "Why shouldn't I just use vLLM with PagedAttention on an NVIDIA GPU? Why would anyone care about OpenVINO on CPUs?"
- **The Student's Angle**: Defending NVIDIA GPU dominance in LLM serving.
- **The Killer Response**:
  > *"In enterprise production, **Total Cost of Ownership (TCO) and Deployment Economics** drive architecture decisions.
  > 
  > An NVIDIA A100/H100 server costs $200,000 to purchase and thousands of dollars per month in data center power and cooling.
  > For 90% of internal enterprise use cases (document summarization, customer support chatbots, sentiment analysis, entity extraction), user queries arrive at rates of 5 to 50 requests per second—not 10,000 requests per second.
  > 
  > Every enterprise data center already has hundreds of Intel Xeon servers running business applications.
  > With **OpenVINO INT8/INT4 quantization and AMX systolic engines**, a modern Intel Xeon processor serves a 7B parameter model at 20-30 tokens per second per stream!
  > 
  > Why spend $200,000 on specialized GPU infrastructure when your existing CPU fleet can handle your entire production inference workload at zero additional hardware cost? That is why enterprise architects deploy OpenVINO."*

### Trap Q2: "What is PagedAttention, and why is standard KV-cache allocation inefficient?"
- **The Student's Angle**: Testing knowledge of modern LLM memory management algorithms (vLLM).
- **The Killer Response**:
  > *"In traditional serving systems, memory for the KV-cache is pre-allocated contiguously based on the maximum possible request context length (e.g., reserving 4,096 tokens in advance for every user).
  > 
  > This causes massive **Memory Fragmentation**:
  > 1. Internal Fragmentation: A user asks a question with only 100 tokens, but 4,096 tokens of memory were reserved. 97% of the reserved memory sits completely wasted.
  > 2. External Fragmentation: Dynamic memory allocators leave small gaps of unallocatable memory across RAM.
  > Traditional systems lose 60% to 80% of their memory to fragmentation, limiting concurrent batch sizes.
  > 
  > **PagedAttention** (inspired by OS Virtual Memory Paging) divides the KV-cache into fixed-size **Blocks / Pages** (e.g., 16 tokens per block).
  > Memory is allocated dynamically on-demand as tokens generate. Non-contiguous physical memory blocks are mapped through a virtual Page Table.
  > Fragmentation drops to under 4%, allowing serving systems to handle **2x to 4x higher concurrent batch sizes** on identical physical RAM."*
""", encoding="utf-8")

f5_7 = d_defense / "live_terminal_counter_demos.md"
f5_7.write_text("""# Day 5: Live Terminal Counter-Demos

## Demo 1: Inspecting OpenVINO Available Devices and Inference Precision
```bash
python3 -c "
import openvino as ov
core = ov.Core()
print('Available OpenVINO Devices:', core.available_devices)
for d in core.available_devices:
    print(f'{d} Full Name:', core.get_property(d, 'FULL_DEVICE_NAME'))
"
```

## Demo 2: Quick OpenVINO Benchmark Tool
```bash
# Benchmark throughput of an OpenVINO IR model
benchmark_app -m model.xml -d CPU -api async -t 10
```
""", encoding="utf-8")

# ==============================================================================
# 4. Step-by-Step CLI & Code Breakdown
# ==============================================================================
f5_8 = d_code / "line_by_line_code_walkthrough.md"
f5_8.write_text("""# Day 5: Line-by-Line Code Walkthrough (OpenVINO Quantization & FastAPI Serving)

### Code 1: OpenVINO Model Compilation
```python
import openvino as ov
from openvino.runtime import Core

# Line 5: Initialize the OpenVINO Core runtime engine
core = Core()

# Line 8: Read OpenVINO Intermediate Representation (.xml + .bin)
model = core.read_model(model="model.xml")

# Line 11: Compile model for target hardware (CPU) with throughput performance hint
compiled_model = core.compile_model(
    model=model, 
    device_name="CPU",
    config={"PERFORMANCE_HINT": "THROUGHPUT"}
)

# Line 18: Create asynchronous infer request
infer_request = compiled_model.create_infer_request()
```

### Code 2: FastAPI High-Concurrency Serving
```python
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="OpenVINO LLM Inference Service")

@app.post("/generate")
async def generate_text(prompt: str):
    # Asynchronous inference call prevents blocking event loop
    result = run_openvino_inference(prompt)
    return {"generated_text": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=4)
```
""", encoding="utf-8")

f5_9 = d_code / "compilation_and_execution_pipeline.md"
f5_9.write_text("""# Day 5: Compilation & Execution Pipeline

## Converting PyTorch Model to OpenVINO IR
```bash
# Export Hugging Face model directly to OpenVINO using optimum-intel
optimum-cli export openvino --model bert-base-uncased --task text-classification ./ov_bert_model/

# Quantize to INT8 with NNCF
nncf quantize --model ov_bert_model/openvino_model.xml --output ./ov_bert_int8/
```
""", encoding="utf-8")

# ==============================================================================
# 5. Lab Challenges & Error Debugging
# ==============================================================================
f5_10 = d_debug / "student_lab_challenges_with_solutions.md"
f5_10.write_text("""# Day 5: Student Lab Challenges with Step-by-Step Solutions

## Challenge 1: Measure Memory Footprint Reduction from INT8 Quantization
- **Goal**: Measure file size of `openvino_model.bin` in FP32 vs INT8.
- **Expected Outcome**: File size shrinks by approximately 4x (e.g., 440 MB down to 110 MB).

## Challenge 2: Multi-Stream Throughput Benchmark
- **Goal**: Configure OpenVINO to run 4 concurrent inference streams and measure throughput:
```python
compiled_model = core.compile_model(
    model, "CPU", 
    {"NUM_STREAMS": "4", "INFERENCE_NUM_THREADS": "8"}
)
```
""", encoding="utf-8")

f5_11 = d_debug / "common_student_syntax_errors_and_5_sec_fixes.md"
f5_11.write_text("""# Day 5: Common Student Errors & 5-Second Instant Fixes

### Error 1: `ImportError: No module named 'openvino'`
- **Cause**: OpenVINO is not installed in the active Python environment.
- **5-Second Fix**: `pip install openvino nncf optimum[openvino]`.

### Error 2: `RuntimeError: Dynamic shapes are not supported for this hardware target`
- **Cause**: Input tensors have variable dimensions (`-1`) that the backend cannot optimize statically.
- **5-Second Fix**:
  Reshape model with static bounds:
  ```python
  model.reshape({"input_ids": [1, 128], "attention_mask": [1, 128]})
  ```
""", encoding="utf-8")

print("[SUCCESS] Day 5: Zero-to-God-Tier Master Dossier Built Completely!")
