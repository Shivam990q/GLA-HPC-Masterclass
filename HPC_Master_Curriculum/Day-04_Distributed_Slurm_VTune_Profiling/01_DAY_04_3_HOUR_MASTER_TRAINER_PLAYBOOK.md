# ⏱️ DAY 4: 3-HOUR COMPLETE MASTER TRAINER PLAYBOOK
## Distributed AI Training & Profiling Optimization with Intel VTune
**Course Code:** `GLA-HPC-BCSG701` | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Session:** Day 4 (Strictly 3 Hours / 180 Minutes)  
**Official Syllabus Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 🎯 1. Official Syllabus Scope (Day 4 Topics)
1. **Distributed TensorFlow training with Slurm**
2. **Profiling & debugging with Intel VTune**

---

## ⏰ 2. Realistic 180-Minute (3-Hour) Delivery Timeline

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                        DAY 4 TIMELINE (TOTAL: 180 MINUTES)                               |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  00:00 - 00:35 (35m) │ PART 1: Multi-Node Distributed Training with Slurm                |
|                      │        (Hostfile Generation, Process Binding, Horovod Multi-Node) |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  00:35 - 01:10 (35m) │ PART 2: Profiling Foundations & Intel VTune Architecture          |
|                      │        (PMU Counters, Hotspots Analysis, Sampling vs Probing)     |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:10 - 01:20 (10m) │ ☕ REJUVENATION BREAK (10 Minutes)                                |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:20 - 02:00 (40m) │ PART 3: Top-Down Microarchitecture Analysis (TMAM)                |
|                      │        (Frontend Bound, Bad Speculation, Memory Bound, Core Bound)|
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:00 - 02:40 (40m) │ PART 4: Memory Access & The Roofline Model with Intel Advisor     |
|                      │        (Arithmetic Intensity, FLOPs/Byte, Cache Misses, NUMA)     |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:40 - 03:00 (20m) │ PART 5: Optimization Hands-On, Straggler Elimination & 25 MCQs   |
|                      │        (Live bottleneck fix, 25 Evaluated MCQs, Day 5 GenAI teaser)|
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 🎙️ 3. Line-by-Line Minute-by-Minute Trainer Delivery Script

### PART 1: Multi-Node Distributed Training with Slurm (00:00 - 00:35 | 35 Mins)
* **Slide Alignment:** Day 4 Slide Deck (Slides 1–5: Multi-Node Slurm & Horovod Orchestration).
* **Concept:** Scaling deep learning from 1 node to multi-node supercomputer partitions.
* **Trainer Script:**
  > "Welcome to Day 4 of the HPC Masterclass!
  > Yesterday on Day 3, we studied Slurm batch scripts and the Horovod Ring-AllReduce concept.
  > Today, we execute **real multi-node distributed training** and answer the most important question in performance engineering: **'Why is my code slow?'**
  > When running across multiple nodes in Slurm:
  > - Slurm dynamically populates `SLURM_JOB_NODELIST` (e.g., `node01,node02,node03,node04`).
  > - The MPI launcher (`mpirun` or `srun`) uses this hostfile to spawn worker ranks across physical servers.
  > - But watch out for **Stragglers**! In synchronous Ring-AllReduce, if 1 node experiences a network glitch or thermal throttling, all 63 other nodes stall waiting at the barrier!
  > Today we learn how to profile our code and eliminate bottlenecks with surgical precision."

---

### PART 2: Profiling Foundations & Intel VTune (00:35 - 01:10 | 35 Mins)
* **Slide Alignment:** Day 4 Slide Deck (Slides 6–10: Performance Profiling & Hardware PMU).
* **Concept:** Measuring reality vs. guessing; Performance Monitoring Unit counters.
* **Trainer Script:**
  > "In high performance computing, **guessing why code is slow is strictly forbidden**.
  > You must measure!
  > What is the difference between benchmarking and profiling?
  > Benchmarking tells you: *'My model took 45 minutes to run.'*
  > Profiling tells you: *'Function `compute_gradients` took 32 minutes, and 48% of pipeline clock cycles were stalled on L3 cache misses!'*
  > Inside every Intel Xeon processor sits the **Performance Monitoring Unit (PMU)**—dedicated hardware silicon registers that count retired instructions, clock cycles, and cache misses.
  > **Intel VTune Profiler** taps into these PMU counters with less than 2% overhead using statistical sampling.
  > The first analysis we always run is **Hotspots Analysis**:
  > `vtune -collect hotspots ./my_model`
  > It generates a Flame Graph showing the exact functions consuming 80%+ of your CPU time."

---

### ☕ BREAK (01:10 - 01:20 | 10 Minutes)

---

### PART 3: Top-Down Microarchitecture Analysis (01:20 - 02:00 | 40 Mins)
* **Slide Alignment:** Day 4 Slide Deck (Slides 11–16: TMAM Quadrants).
* **Concept:** Frontend Bound, Bad Speculation, Backend Bound (Memory vs. Core).
* **Trainer Script:**
  > "Now look at Intel's crowning architectural methodology: the **Top-Down Microarchitecture Analysis Method (TMAM)**.
  > Every clock cycle, the CPU pipeline has slots to process instructions. Where do those slots go?
  > 1. **Retiring**: Useful work! Instructions finished and committed. (Aim for $\ge 60\%$).
  > 2. **Bad Speculation**: Cycles wasted because of branch mispredictions. The CPU guessed wrong on an `if` condition and had to flush its pipeline.
  > 3. **Frontend Bound**: Execution units are starving because the Instruction Cache missed or instruction decoding was delayed.
  > 4. **Backend Bound**: The most common in HPC!
  >    - **Core Bound**: ALUs/dividers are full.
  >    - **Memory Bound**: The CPU is stalled waiting for data from L1/L2/L3 caches or DDR5 RAM!
  > When VTune shows your code is Memory Bound, changing your algorithm to do more FLOPs won't help—you must fix data layout and cache blocking!"

---

### PART 4: Memory Access & The Roofline Model (02:00 - 02:40 | 40 Mins)
* **Slide Alignment:** Day 4 Slide Deck (Slides 17–22: Memory Walls & Roofline Model).
* **Concept:** Arithmetic intensity ($I$), memory ceilings, compute ceilings.
* **Trainer Script:**
  > "Next, look at the **Roofline Model** produced by **Intel Advisor**.
  > On the X-axis: **Arithmetic Intensity** ($\text{FLOPs} / \text{Byte}$).
  > On the Y-axis: **Performance** ($\text{GFLOPs} / \text{sec}$).
  > The chart has two ceilings:
  > - A slanted line: The **Memory Bandwidth Ceiling** ($y = \text{Bandwidth} \times x$).
  > - A flat line: The **Peak Computational Ceiling** ($y = \text{Peak FLOPS}$).
  > If your algorithm sits on the slanted roof (like Vector Addition or standard K-Means), it is **Memory Bound**. No matter how many ALUs you add, you cannot go faster until you increase arithmetic intensity or utilize cache blocking.
  > If your algorithm sits on the flat roof (like GEMM matrix multiplication or Deep Convolutions), it is **Compute Bound** and running at peak hardware capability!"

---

### PART 5: Optimization Hands-On & 25 MCQs (02:40 - 03:00 | 20 Mins)
* **Activities:**
  1. Have students run the VTune hotspot simulation and Roofline calculation notebook cells.
  2. Review the 5 core MCQs from [`03_DAY_04_STUDENT_CHEATSHEET_AND_MCQS.md`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-04_Distributed_Slurm_VTune_Profiling/03_DAY_04_STUDENT_CHEATSHEET_AND_MCQS.md).
  3. **Day 5 Grand Finale Teaser:** *"Tomorrow on Day 5, we enter the pinnacle of modern HPC: Generative AI, Large Language Models (LLMs), Intel AMX matrix engines, Habana Gaudi 2/3 clusters, and optimizing inference with OpenVINO!"*

---
**Playbook Status:** 100% Complete & Verified | GLA University HPC Masterclass Day 4
