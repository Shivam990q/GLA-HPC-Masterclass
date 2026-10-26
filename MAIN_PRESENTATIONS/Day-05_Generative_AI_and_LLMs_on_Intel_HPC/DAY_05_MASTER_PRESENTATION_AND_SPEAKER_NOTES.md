# 🎓 DAY 5: MASTER PRESENTATION & SPEAKER NOTES
## Generative AI & Large Language Models on Intel HPC: Habana Gaudi & OpenVINO
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Audience:** B.Tech / M.Tech Computer Science (60 Students)  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 🏛️ 1. Syllabus Boundary & Scope (Day 5 - The Capstone)

```
+─────────────────────────────────────────────────────────────────────────────────────────+
|                                DAY 5 SYLLABUS BOUNDARY                                  |
+─────────────────────────────────────────────────────────────────────────────────────────+
|  [DAY 5: IN-SCOPE - CAPSTONE MILESTONES]                                                |
|  1. Introduction to Generative AI & LLMs on HPC (Transformer Math, KV-Cache, Memory Wall)|
|  2. Silicon Engines: Intel Xeon Sapphire Rapids (AMX) vs Habana Gaudi 2/3 Accelerators  |
|  3. Accelerating LLM Inference Directly on Xeon CPUs (Intel AMX TMUL Tile Registers)    |
|  4. Scaling Distributed LLM Training & Fine-Tuning with Habana Gaudi SynapseAI & RoCE   |
|  5. Model Compression & Acceleration with Intel OpenVINO Toolkit (IR Export, NNCF INT4) |
|  6. Parameter-Efficient Fine-Tuning (PEFT / LoRA) on Multi-Node Clusters via Slurm      |
|  7. Complete End-to-End Capstone AI Workflow (Ingest -> Fine-Tune -> Quantize -> Serve) |
+─────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 📋 2. Complete Topic & Subtopic Breakdown (Day 5)

### Topic 1: Generative AI & LLMs on HPC Architectures
- **The Physics of Large Language Models:** Auto-regressive token generation, multi-head self-attention:
  $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{Q K^T}{\sqrt{d_k}}\right) V$$
- **The Memory Wall in LLMs:** Why generating tokens is memory-bandwidth bound rather than compute-bound.
- **The KV-Cache Footprint:** Storing key and value projection tensors in high-speed RAM for every token in the context window:
  $$\text{KV Cache Size} = 2 \times 2 \times n_{\text{layers}} \times n_{\text{heads}} \times d_{\text{head}} \times \text{tokens} \times \text{bytes per parameter}$$
  *(For a 70B model with 4096 tokens, KV-cache consumes ~10GB of RAM per concurrent user!).*

### Topic 2: Silicon Specialization: Intel Xeon AMX vs Habana Gaudi 2/3
- **Intel Xeon 4th/5th Gen (Sapphire Rapids / Emerald Rapids):**
  - Advanced Matrix Extensions (AMX): Two hardware tile units (TMUL) operating on 16x16 matrix registers (TMM0-TMM7).
  - Native hardware support for BF16 (Bfloat16) and INT8 matrix multiplication, delivering up to 16x higher throughput than legacy AVX-512.
  - Ideal for agile low-latency enterprise LLM inference without requiring costly discrete GPUs.
- **Habana Gaudi 2 / Gaudi 3 Accelerators:**
  - Purpose-built tensor processing architecture: 24 Tensor Processor Cores (TPCs) + 2 Matrix Multiplication Engines (MMEs).
  - 96GB HBM2e (Gaudi 2, 2.45 TB/s bandwidth) or 128GB HBM3 (Gaudi 3, 3.7 TB/s bandwidth).
  - **The Game-Changing Architectural Differentiator:** 24 integrated 100GbE RoCE (RDMA over Converged Ethernet) ports directly on the silicon die, eliminating external PCIe NIC bottlenecks for cluster scaling.

### Topic 3: Breaking the Inference Bottleneck with Intel OpenVINO
- **What is Intel OpenVINO?** Open Visual Inference and Neural Network Optimization toolkit delivering zero-latency hardware execution across Intel CPUs, integrated GPUs, discrete GPUs, and NPUs.
- **The 4-Step OpenVINO Pipeline:**
  1. *Model Ingestion:* Importing pre-trained HuggingFace PyTorch / Safetensors models (e.g. Qwen2.5, Llama-3, TinyLlama).
  2. *Graph Compilation to Intermediate Representation (IR):* Generating `.xml` (topology structure) and `.bin` (fused weight tensors).
  3. *Weight-Only Quantization with NNCF (Neural Network Compression Framework):* Compressing 32-bit floating point weights down to INT4 (4-bit asymmetric integer weights), slashing model size by 75% and eradicating DRAM memory bandwidth bottlenecks.
  4. *Hardware-Aware Execution:* Running compiled models on Intel AMX execution units with optimized CPU thread pools.

### Topic 4: Distributed Domain-Specific LLM Fine-Tuning
- **Why Full-Parameter Fine-Tuning is Obsolete for Enterprises:** Training all 70B weights requires massive GPU clusters and millions of dollars.
- **Parameter-Efficient Fine-Tuning (PEFT / LoRA):**
  - Low-Rank Adaptation: Freezing base model weights $W_0$ and training two low-rank decomposition matrices $A$ and $B$:
    $$\Delta W = B \cdot A, \quad \text{where } B \in \mathbb{R}^{d \times r}, A \in \mathbb{R}^{r \times k}, \quad r \ll \min(d, k)$$
  - Slashing trainable parameters from 7 Billion down to 20 Million (99.7% reduction!).
- **Multi-Node Cluster Orchestration:** Wrapping LoRA training with Intel Extension for PyTorch (IPEX) and submitting across multi-node Gaudi/Xeon partitions via Slurm.

### Topic 5: Profiling LLMs with Intel VTune
- Capturing live microarchitectural telemetry during token generation:
  - Identifying Memory Stalls (DRAM bandwidth saturation during KV-cache reads).
  - Pinpointing Thread Contention during multi-head attention splits.
  - Verifying 100% AMX tile register utilization.

### Topic 6: The Capstone End-to-End Enterprise Pipeline
```
[ 01. Ingestion ] ──► [ 02. Fine-Tuning ] ──► [ 03. Compression ] ──► [ 04. Cluster Serving ]
HuggingFace Base     Distributed LoRA on      OpenVINO NNCF INT4      High-Throughput FastAPI
Model & GLA Dataset  Gaudi/Xeon via Slurm     Quantization            Microservice on Xeon AMX
```

---

## 🖥️ 3. Slide-by-Slide Speaker Notes

*Mapped to the 15 Slides of `Day_05_NotebookLM_Master_Deck.pptx`*

- **Slide 1: Generative AI & LLMs on Intel HPC: The Capstone**  
  *Speaker Point:* "Welcome to Day 5 — the grand capstone of our 5-day supercomputing journey! Over the past 4 days, you mastered Linux, oneAPI, OpenMP, MPI, Slurm, and VTune. Today, we bring every single skill together to deploy, fine-tune, compress, and serve modern Large Language Models on enterprise Intel hardware!"
- **Slide 2: Hands-On Execution & Pedagogical Blueprint**  
  *Speaker Point:* "Notice our approach today: No abstract theory. We examine the exact silicon physics of Transformers, compress models with OpenVINO, and run live inference."
- **Slide 3: Industry-Grade Tools & Ecosystem**  
  *Speaker Point:* "Show the toolchain: HuggingFace + PyTorch on top, OpenVINO and IPEX in middleware, Slurm orchestrating compute, and Intel Xeon AMX / Habana Gaudi executing the math."
- **Slide 4: The 5-Day Arc — Day 5 Deep Dive**  
  *Speaker Point:* "Celebrate the culmination: Day 1 foundation -> Day 2 multi-core -> Day 3 DL & Slurm -> Day 4 VTune -> Day 5 Generative AI Capstone."
- **Slide 5: The Generative AI Bottleneck: Beyond the Workstation**  
  *Speaker Point:* "Explain the harsh reality: A single laptop cannot run a 70B model because 70 Billion parameters in FP16 require 140 Gigabytes of high-bandwidth memory just to load! HPC cluster architectures and hardware-aware optimization turn impossible models into real-time reality."
- **Slide 6: Intel Xeon vs. Habana Gaudi: Architectural Specialization**  
  *Speaker Point:* "Deconstruct the two champions: Intel Xeon with AMX built into the CPU (agile, cost-effective, high-throughput enterprise inference) vs Habana Gaudi with 24 Tensor Processor Cores and 24 on-die 100GbE RoCE ports (massive distributed multi-billion parameter fine-tuning)."
- **Slide 7: Accelerating Inference Directly on Intel Xeon (AMX)**  
  *Speaker Point:* "Reveal the secret weapon: You don't always need a million-dollar GPU cluster. Intel 4th Gen Xeon processors have Advanced Matrix Extensions (AMX) tile registers on the silicon die, delivering up to 16x matrix multiplication throughput compared to standard CPUs."
- **Slide 8: Scaling Distributed Fine-Tuning with Habana Gaudi**  
  *Speaker Point:* "Highlight Gaudi's crown jewel: The integrated RoCE networking. In typical GPU servers, data must pass through PCIe switches to reach external network cards. Gaudi integrates the network directly onto the processor die, eliminating cluster communication bottlenecks."
- **Slide 9: Breaking the Inference Bottleneck: Raw 70B vs Compressed Model**  
  *Speaker Point:* "Contrast raw FP32 weights (massive latency, memory choke) with OpenVINO optimized models (INT4/INT8 precision, fused attention layers, sub-millisecond token latency)."
- **Slide 10: Streamlining Generative AI with Intel OpenVINO**  
  *Speaker Point:* "Deconstruct the 4 steps: Model Ingestion -> NNCF INT4 Quantization -> Layer Fusion -> Hardware-Aware Execution on Xeon AMX."
- **Slide 11: Distributing Domain-Specific Fine-Tuning (LoRA)**  
  *Speaker Point:* "Explain Low-Rank Adaptation: Why retrain 7 Billion parameters when you can train 20 Million parameters using low-rank matrices $A$ and $B$ and achieve 99% of the fine-tuned domain accuracy?"
- **Slide 12: Orchestrating Cluster-Based Execution via Slurm**  
  *Speaker Point:* "Demonstrate the real cluster workflow: Writing a `#SBATCH --nodes=4 --partition=gaudi` script to launch distributed LoRA fine-tuning."
- **Slide 13: Ensuring Bare-Metal Efficiency with VTune Profiling**  
  *Speaker Point:* "Show the Flame Graph: Emphasize that a model isn't ready for production just because it runs. We profile memory stalls and thread locks to verify that every core and matrix register is 100% utilized."
- **Slide 14: Executing the Complete End-to-End AI Workflow**  
  *Speaker Point:* "Walk through the full master diagram: Raw Data -> Linux Setup -> Slurm Submission -> Gaudi Fine-Tuning -> OpenVINO Quantization -> Xeon Microservice Deployment."
- **Slide 15: Mastering the Next Generation of HPC Deployment**  
  *Speaker Point:* "Final graduation message: You are no longer just programmers writing scripts. You are High Performance Computing engineers capable of harnessing supercomputing clusters and cutting-edge silicon to power the future of artificial intelligence!"

---

## 🔬 4. Lab Hands-On Synchronization (Colab Notebook Ready!)

*All 23 interactive cells implemented in `Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb`*

- **Lab 1 (Silicon Audit):** Inspecting Xeon AMX and AVX-512 flags via `lscpu`.
- **Lab 2 (Memory Math):** Calculating exact VRAM and KV-Cache requirements for 1B, 7B, 13B, and 70B parameter models.
- **Lab 3 (OpenVINO Export):** Exporting a HuggingFace Transformer model to OpenVINO Intermediate Representation (`.xml` + `.bin`).
- **Lab 4 (NNCF INT4 Quantization):** Compressing model weights down to 4-bit integers and physically measuring 72% file size reduction.
- **Lab 5 (Latency Benchmark):** Benchmarking Time-To-First-Token (TTFT) and Tokens-Per-Second (TPS) before and after optimization.
- **Lab 6 (Distributed LoRA Script):** Writing the multi-node Slurm batch submission script for domain fine-tuning.
- **Lab 7 (Production Microservice):** Launching a live streaming FastAPI inference endpoint powered by the compiled OpenVINO engine.
