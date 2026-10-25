# ⏱️ DAY 5: 3-HOUR COMPLETE MASTER TRAINER PLAYBOOK
## Generative AI & Large Language Models on Intel HPC: Habana Gaudi & OpenVINO
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Session Duration:** Exactly 3 Hours (180 Minutes)  
**Official Syllabus Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 🎯 1. Official Syllabus Scope (Page 2 of PDF — Day 5 Capstone)

The official curriculum specifies **strictly 4 core topics for Day 5**:
1. **Introduction to Generative AI & LLMs on HPC**
2. **Intel hardware for LLMs (Xeon, Habana Gaudi)**
3. **Optimizing LLM inference with OpenVINO Toolkit**
4. **Fine-tuning LLMs on HPC**

---

## ⏰ 2. Realistic 180-Minute (3-Hour) Delivery Timeline

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                        DAY 5 TIMELINE (TOTAL: 180 MINUTES)                               |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  00:00 - 00:35 (35m) │ PART 1: Introduction to Generative AI & LLMs on HPC               |
|                      │        (Transformer Silicon Physics, Memory Wall, KV-Cache Math)  |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  00:35 - 01:10 (35m) │ PART 2: Intel Hardware for LLMs: Xeon AMX vs Habana Gaudi         |
|                      │        (AMX Tile Registers vs 24x 100GbE RoCE On-Die Networking)  |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:10 - 01:20 (10m) │ ☕ REJUVENATION BREAK (10 Minutes)                                |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:20 - 02:10 (50m) │ PART 3: Optimizing LLM Inference with Intel OpenVINO Toolkit       |
|                      │        (Hands-on IR Export, NNCF INT4 Quantization, TTFT/TPS)     |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:10 - 02:45 (35m) │ PART 4: Fine-Tuning LLMs on HPC via Slurm & PEFT/LoRA             |
|                      │        (Distributed Parameter Updates, #SBATCH Script, Serving)   |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:45 - 03:00 (15m) │ PART 5: Capstone Assessment, MCQs & Course Graduation             |
|                      │        (5 Evaluated MCQs + Capstone Walkthrough & Certification)  |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 🎙️ 3. Line-by-Line Minute-by-Minute Trainer Delivery Script

### PART 1: Introduction to Generative AI & LLMs on HPC (00:00 - 00:35 | 35 Mins)
*Slides Mapped: 1 to 5 in `Day-05_Master_Presentation.pptx`*

#### [00:00 - 00:15] The Generative AI Scaling Bottleneck (Slides 1 - 5)
- **What Trainer Shivam Says (Hinglish/English):**
  > "Welcome to Day 5 — the grand capstone of our supercomputing journey!
  > Over the last 4 days, you mastered Linux, oneAPI, OpenMP multithreading, MPI message passing, Slurm job scheduling, and VTune microarchitecture profiling.
  > Today, we bring every single skill together to solve the most demanding problem in modern computing: deploying, optimizing, and fine-tuning Large Language Models on enterprise Intel HPC hardware.
  > Let's start with a brutal physical truth: Why do LLMs break ordinary computers?"

#### [00:15 - 00:35] The Physics of LLMs: Memory Wall & KV-Cache
- **What Trainer Shivam Says:**
  > "When you generate text with an LLM, generating token #100 requires reading ALL previous 99 tokens from memory!
  > This divides text generation into two distinct phases:
  > 1. **Prefill Phase (Prompt Processing):** Compute-bound. All input prompt tokens are ingested simultaneously in a massive matrix multiplication.
  > 2. **Decode Phase (Token by Token Generation):** Memory-bandwidth bound! To emit just ONE single new word, the processor must stream all 7 Billion weights from RAM into registers!
  > If your memory bandwidth is slow, your model generates 1 word per second.
  > Furthermore, look at the **KV-Cache (Key-Value Cache)**. Storing attention matrices across layers for long context windows consumes gigabytes of memory per user!
  > In HPC, we defeat the memory wall using high-bandwidth memory (HBM), hardware matrix accelerators, and model quantization."
- **Whiteboard Sketch 1 (Draw on board):**
  ```
  [ Prefill Phase ] (Prompt Ingestion)       [ Decode Phase ] (Token Generation)
  Matrix x Matrix = COMPUTE-BOUND            Vector x Matrix = MEMORY-BANDWIDTH BOUND
  All prompt tokens processed together       Must load ALL 7B weights to output 1 token!
  (High Arithmetic Intensity: FLOPs/Byte)    (Low Arithmetic Intensity -> Bandwidth Starvation)
  ```

---

### PART 2: Intel Hardware for LLMs: Xeon AMX vs Habana Gaudi (00:35 - 01:10 | 35 Mins)
*Slides Mapped: 6 to 8 in `Day-05_Master_Presentation.pptx`*

#### [00:35 - 00:55] Intel Xeon Scalable Processors & Intel AMX
- **What Trainer Shivam Says:**
  > "Most developers think you cannot run LLMs without buying a 50-lakh rupee GPU cluster. That is completely false.
  > Look at 4th Gen Intel Xeon Scalable processors (Sapphire Rapids). They feature **Intel AMX (Advanced Matrix Extensions)**.
  > AMX is a built-in systolic array matrix accelerator sitting directly on each CPU core!
  > It operates on 16x16 tile registers (TMM0 to TMM7), executing 2048 INT8 operations or 1024 BF16 operations per clock cycle.
  > For enterprise chatbots, code generation, and medium-scale LLM inference, Xeon CPUs with AMX give real-time responses at a fraction of GPU infrastructure cost."

#### [00:55 - 01:10] Habana Gaudi 2 / Gaudi 3 AI Accelerators
- **What Trainer Shivam Says:**
  > "Now, what if you need to train or fine-tune a massive 70-Billion parameter model?
  > Here is where **Habana Gaudi** dominates.
  > Gaudi is not a GPU that was modified for AI. It is an application-specific processor designed purely for deep learning.
  > It has 24 Tensor Processor Cores (TPCs) and 96GB to 128GB of High-Bandwidth Memory (HBM).
  > But its absolute superpower is this: **24 integrated 100GbE RoCE (RDMA over Converged Ethernet) ports directly on the silicon die!**
  > In typical clusters, GPUs must route network data through external PCIe slots and switches, causing bottlenecks. Gaudi connects node-to-node directly through its silicon die, allowing near-linear scaling across thousands of accelerators."

---

### ☕ BREAK (01:10 - 01:20 | 10 Minutes)

---

### PART 3: Optimizing LLM Inference with OpenVINO (01:20 - 02:10 | 50 Mins)
*Slides Mapped: 9 to 10 in `Day-05_Master_Presentation.pptx` | Colab Cells: 1 to 14*

#### [01:20 - 01:45] The 4-Step OpenVINO Compression Pipeline
- **What Trainer Shivam Says:**
  > "Open your Colab notebook right now.
  > **Intel OpenVINO Toolkit** is our enterprise tool for turning slow, bloated models into ultra-fast inference engines.
  > The pipeline has 4 steps:
  > 1. **Model Ingestion:** Loading pre-trained HuggingFace weights (PyTorch/Safetensors).
  > 2. **IR Conversion:** Compiling to OpenVINO Intermediate Representation (`.xml` graph structure + `.bin` weights).
  > 3. **NNCF Weight-Only Quantization:** Compressing 16-bit or 32-bit floating point weights down to **INT4 (4-bit integers)**!
  > 4. **Hardware Execution:** Automatically mapping matrix computations to Intel AMX on CPUs or Xe-Cores on GPUs."

#### [01:45 - 02:10] Hands-On: Measuring INT4 Quantization Speedup
- **What Students Run in Colab:**
  ```python
  import openvino as ov
  import nncf

  # 1. Inspect model size before quantization (FP16: ~2.5 GB)
  # 2. Apply NNCF Weight-Only INT4 Quantization
  compressed_model = nncf.compress_weights(model, mode=nncf.CompressWeightsMode.INT4_ASYM)

  # 3. Save compressed model (Slashing size down to ~700 MB - 72% reduction!)
  ov.save_model(compressed_model, "qwen_int4.xml")
  ```
- **Trainer Observation:**
  > "Look at the terminal: model size dropped from 2.5GB to 700MB. And because memory footprint shrunk by 72%, memory bandwidth is no longer choked, and token generation speed increases by 2.5x!"

---

### PART 4: Fine-Tuning LLMs on HPC via Slurm & LoRA (02:10 - 02:45 | 35 Mins)
*Slides Mapped: 11 to 14 in `Day-05_Master_Presentation.pptx` | Colab Cells: 15 to 20*

#### [02:10 - 02:30] Parameter-Efficient Fine-Tuning (PEFT / LoRA)
- **Concept:** Why full-parameter fine-tuning is obsolete.
- **What Trainer Shivam Says:**
  > "To adapt an LLM for GLA University course Q&A, do we need to retrain all 7 Billion parameters? NO!
  > We use **LoRA (Low-Rank Adaptation)**.
  > We freeze all 7 Billion original weights. We attach tiny adapter matrices $A$ and $B$ to the attention projection layers.
  > Trainable parameters drop from 7,000,000,000 down to 20,000,000 (a 99.7% reduction!).
  > We can train this on a multi-node cluster in just 30 minutes!"

#### [02:30 - 02:45] Orchestrating Distributed Fine-Tuning via Slurm
- **What Students Inspect:**
  ```bash
  #!/bin/bash
  #SBATCH --job-name=gla_llm_lora
  #SBATCH --nodes=2
  #SBATCH --partition=gaudi
  #SBATCH --time=01:00:00

  # Launch distributed LoRA fine-tuning across allocated nodes
  srun python3 finetune_lora.py --model_name qwen2.5 --batch_size 16
  ```

---

### PART 5: Capstone Assessment & Course Graduation (02:45 - 03:00 | 15 Mins)
*Slides Mapped: 15 in `Day-05_Master_Presentation.pptx`*

#### [02:45 - 02:55] 5-Question Final Knowledge Check
1. *Q1: Why is the Decode phase of LLM generation memory-bandwidth bound?*  
   **Answer:** Emitting each new token requires loading all model weights from RAM; low arithmetic intensity starves compute cores.
2. *Q2: What is the hardware function of Intel AMX in Xeon processors?*  
   **Answer:** Dedicated matrix tile acceleration (TMUL) for BF16 and INT8 matrix math directly on the CPU die.
3. *Q3: What makes Habana Gaudi uniquely suited for multi-node cluster scaling?*  
   **Answer:** 24 integrated 100GbE RoCE ports directly on the silicon die, eliminating external PCIe switch bottlenecks.
4. *Q4: What does OpenVINO NNCF INT4 weight quantization achieve?*  
   **Answer:** Reduces model size by ~70-75%, slashes memory bandwidth requirements, and doubles token generation speed.
5. *Q5: In LoRA fine-tuning, what percentage of weights are frozen vs trained?*  
   **Answer:** >99% frozen; only tiny low-rank adapter matrices are trained.

#### [02:55 - 03:00] Course Conclusion & Valedictory
- **What Trainer Shivam Says:**
  > "Congratulations to all 60 students of GLA University! Over 5 days, you have mastered the entire supercomputing continuum: from Linux and oneAPI foundations, to OpenMP, MPI, Slurm, VTune profiling, and cutting-edge Generative AI deployment. You are now equipped with the exact technical skills used in the world's leading supercomputing and AI laboratories!"
