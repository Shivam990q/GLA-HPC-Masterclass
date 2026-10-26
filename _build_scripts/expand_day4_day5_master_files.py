"""
expand_day4_day5_master_files.py
Part 3: Upgrades Day 4 and Day 5 files in HPC_Master_Curriculum
"""

import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# DAY 4 EXPANSIONS
# ==============================================================================

write_f("Day-04_Distributed_Slurm_VTune_Profiling/theory_notes/day04_vtune_hardware_counters.md", """# Day 4 Master Theory: Distributed Scaling, Intel VTune & Performance Engineering
**Program**: GLA University Block Teaching | High Performance Computing (Intel & NEC Edition)  
**Lead Trainer**: Shivam Gupta | Edulateral Foundation Master Curriculum  

---

## 1. The Discipline of Performance Engineering

Performance engineering is an empirical science. In high-performance computing, the fundamental law is:
> **"Never optimize without profiling first. Intuition about performance bottlenecks is almost always incorrect."**

Code optimization without measurement is guesswork. A developer might spend weeks rewriting loops in assembly, only to discover that the CPU was actually stalled waiting for data from DRAM across a NUMA UPI link.

---

## 2. Hardware Performance Monitoring Units (PMU) & Sampling

```
┌────────────────────────────────────────────────────────┐
│             Intel CPU Core Silicon Die                 │
│  ┌───────────────────────┐   ┌──────────────────────┐  │
│  │ Out-of-Order Engine   │   │ Hardware PMU Unit    │  │
│  │ • Instruction Fetch   │   │ • CPU_CLK_UNHALTED   │  │
│  │ • Branch Predictor    │   │ • INST_RETIRED       │  │
│  │ • Execution Ports     │   │ • L3_CACHE_MISS      │  │
│  │ • Load/Store Units    │   │ • UPI_REMOTE_DRAM    │  │
│  └───────────┬───────────┘   └──────────▲───────────┘  │
│              │                          │              │
│              └────[ Hardware Event ]────┘              │
└────────────────────────────────────────────────────────┘
```

Modern Intel processors embed dedicated hardware **Performance Monitoring Unit (PMU)** registers directly in the execution silicon:
- **Event-Based Sampling (EBS)**: VTune programs the PMU to count specific microarchitectural events (e.g. every 2,000,000 clock cycles). When the counter overflows, the PMU triggers a non-maskable hardware interrupt, capturing the exact instruction pointer (IP) and call stack with $<2\\%$ runtime intrusion.
- **Zero Source Code Instrumentation**: Analyzes compiled C++, Fortran, and Python binaries directly at the machine instruction level.

---

## 3. Top-Down Microarchitecture Analysis Method (TMAM)

Developed by Ahmad Yasin at Intel, TMAM classifies CPU pipeline slot utilization into four top-level categories:

```
┌────────────────────────────────────────────────────────────────────────┐
│            Top-Down Microarchitecture Analysis (TMAM) Tree             │
├───────────────────────────────────┬────────────────────────────────────┤
│           RETIRING                │          BAD SPECULATION           │
│  • Useful computational work      │  • Pipeline slots wasted on        │
│  • uOps committed to registers    │    mispredicted branches           │
│  • Target: > 50% for optimal code │  • Flush penalty: 15-20 cycles/miss│
├───────────────────────────────────┼────────────────────────────────────┤
│        FRONT-END BOUND            │          BACK-END BOUND            │
│  • Fetch latency / bandwidth      │  • Memory Bound (L1/L2/L3/DRAM)    │
│  • ICache misses & iTLB misses    │  • Core Bound (Execution ports)    │
│  • Starves execution pipeline     │  • Largest bottleneck in HPC & DL  │
└───────────────────────────────────┴────────────────────────────────────┘
```

### 3.1 Diagnosing Back-End Bound (Memory vs Core)
1. **Memory Bound**:
   - The execution ports are idle because load/store buffers are waiting for data from cache or DRAM.
   - Accessing local DRAM takes ~200 CPU cycles; accessing remote socket DRAM takes ~350 cycles.
   - **Remedy**: Cache blocking, loop tiling, contiguous data structures (SoA instead of AoS), and thread pinning.
2. **Core Bound**:
   - The data is present in registers/L1 cache, but execution ports or math dividers are saturated.
   - **Remedy**: SIMD vectorization (AVX-512), operator fusion, loop unrolling.

---

## 4. The Roofline Model: Calculating Operational Intensity

The Roofline Model visualizes the boundary between peak compute capability and peak memory bandwidth:

```
Attainable Performance (GFLOP/s)
  ^
  │                     Peak Compute Ceiling (Peak GFLOP/s)
  │                 ┌────────────────────────────────────────
  │                / 
  │               /  ◄── Knee Point (Balance Point)
  │              /
  │             / Memory Bandwidth Sloped Bound (Peak GB/s)
  │            /
  │           /
  └──────────┴─────────────────────────────────────────────>
           0.1      1.0       10.0      100.0   Operational Intensity
                                                (FLOPs / Byte)
```

- **Operational Intensity**: $I = \\frac{\\text{Total Floating Point Operations (FLOPs)}}{\\text{Total DRAM Bytes Transferred}}$.
- **Left of Knee Point**: **Memory-Bound Region**. Adding more CPU cores yields zero speedup; optimization must focus on reducing memory traffic.
- **Right of Knee Point**: **Compute-Bound Region**. The application is limited by arithmetic execution units; optimization must focus on SIMD vectorization and instruction throughput.
""")

# ==============================================================================
# DAY 5 EXPANSIONS
# ==============================================================================

write_f("Day-05_GenAI_LLMs_Gaudi_OpenVINO/theory_notes/day05_genai_llms_openvino_gaudi.md", """# Day 5 Master Theory: Generative AI & Large Language Models on Intel HPC
**Program**: GLA University Block Teaching | High Performance Computing (Intel & NEC Edition)  
**Lead Trainer**: Shivam Gupta | Edulateral Foundation Master Curriculum  

---

## 1. Large Language Model (LLM) Computational Anatomy

Modern Generative AI is dominated by Decoder-Only Transformer architectures (GPT-4, Llama 3, Mistral, Qwen):
$$Attention(Q, K, V) = \\text{softmax}\\left( \\frac{Q \\cdot K^T}{\\sqrt{d_k}} \\right) \\cdot V$$

---

## 2. The Two Phases of LLM Inference & The Memory Wall

LLM inference consists of two fundamentally distinct computational regimes:

```
┌────────────────────────────────────────────────────────────────────────┐
│                 THE TWO PHASES OF LLM INFERENCE                        │
├───────────────────────────────────┬────────────────────────────────────┤
│      PHASE 1: PREFILL PHASE       │        PHASE 2: DECODE PHASE       │
│     (Prompt Ingestion Phase)      │    (Autoregressive Generation)     │
├───────────────────────────────────┼────────────────────────────────────┤
│ • Processes all prompt tokens in  │ • Generates tokens one-by-one      │
│   parallel in a single pass       │   sequentially                     │
│ • Compute-Bound (High Intensity)  │ • Memory-Bandwidth Bound           │
│ • Matrix Multiplication (GEMM)    │ • Matrix-Vector Multiply (GEMV)    │
│ • Saturates AMX & systolic units  │ • Arithmetic Intensity ~ 1 FLOP/Byte│
│ • Measured as: Time-To-First-Token│ • Measured as: Tokens-Per-Second   │
└───────────────────────────────────┴────────────────────────────────────┘
```

### 2.1 Mathematical Derivation: Why Memory Bandwidth Caps Token Generation
Consider generating tokens with an **8-Billion Parameter Model** in 16-bit precision:
- **Model Weight Footprint**: $8 \\times 10^9 \\times 2\\text{ bytes} = \\mathbf{16\\text{ Gigabytes}}$.
- During the decode phase, to generate **one single token**, every single parameter in the 16 GB model must be streamed from DRAM into processor registers:
$$\\text{DRAM Traffic per Token} = 16\\text{ GB}$$
- If a server possesses a memory bandwidth of **$100\\text{ GB/s}$**:
$$\\text{Maximum Theoretical Speed} = \\frac{100\\text{ GB/s}}{16\\text{ GB/token}} = \\mathbf{6.25\\text{ tokens per second}}$$
- **The Takeaway**: No matter how many extra CPU cores or TFLOPs you add, generation speed CANNOT exceed 6.25 tokens/sec unless you:
  1. Increase memory bandwidth (e.g. HBM on NEC SX-Aurora or Habana Gaudi).
  2. Quantize model weights from 16-bit to 4-bit (reducing weight footprint from 16 GB to 4 GB, quadrupling speed to 25 tokens/sec!).

---

## 3. The KV-Cache Bottleneck & Attention Optimizations

```
Multi-Head Attention (MHA) vs Grouped-Query Attention (GQA)
MHA:  Query Heads [1..32]  ◄──►  Key/Value Heads [1..32]    (Massive KV-Cache)
GQA:  Query Heads [1..32]  ◄──►  Key/Value Heads [1..8]     (4x Smaller KV-Cache!)
```

### 3.1 KV-Cache Memory Consumption Formula
$$\\text{KV-Cache Bytes} = 2 \\times \\text{Layers} \\times \\text{KV\\_Heads} \\times d_{\\text{head}} \\times \\text{Sequence\\_Length} \\times \\text{Bytes\\_Per\\_Element} \\times \\text{Batch\\_Size}$$
For a 32-layer model with 32k context length, the KV-cache consumes tens of gigabytes per active user session. Grouped-Query Attention (GQA) groups query heads to share a reduced number of Key/Value heads, reducing memory bandwidth pressure by 4x.

---

## 4. Intel OpenVINO Toolkit & INT4 NNCF Quantization

```
OpenVINO Optimization Workflow
[ PyTorch / Hugging Face Model ]
               │
               ▼  (optimum-intel / Model Optimizer)
[ OpenVINO Intermediate Representation (IR) ]
• model.xml (Graph Architecture & Layer Topology)
• model.bin (Trained Tensor Weights)
               │
               ▼  (NNCF 4-Bit Weight-Only Quantization)
[ Compressed INT4 OpenVINO Runtime Engine ]
• Deploys across Intel Xeon (AVX-512/AMX), Intel GPUs & NPUs
```

### 4.1 Weight-Only Quantization (WOQ)
- Model weights are compressed to symmetric or asymmetric INT4 precision.
- Activations remain in floating point (BF16 or FP16).
- During the decode phase, weights are unpacked into registers on-the-fly, reducing DRAM bus traffic by 75% and delivering up to 3.8x faster token generation.
""")

print("[SUCCESS] Day 4 and Day 5 Master Upgrades applied successfully!")
