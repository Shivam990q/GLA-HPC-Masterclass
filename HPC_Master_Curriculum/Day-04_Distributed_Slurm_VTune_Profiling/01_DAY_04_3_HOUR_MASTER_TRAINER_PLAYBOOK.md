# ⏱️ DAY 4: 3-HOUR COMPLETE MASTER TRAINER PLAYBOOK
## Distributed AI Training & Performance Profiling with Intel VTune
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Session Duration:** Exactly 3 Hours (180 Minutes)  
**Official Syllabus Reference:** [`Intel & NEC - High Performance Computing.pdf` (Page 2)](file:///c:/Users/Rose/Videos/GLA%20Trainings/_official_syllabus_docs/Intel%20%26%20NEC%20-%20High%20Performance%20Computing.pdf)

---

## 🎯 1. Official Syllabus Scope (Day 4 — Strictly Preserved)

The official curriculum specifies **strictly 2 core topics for Day 4**:
1. **Distributed TensorFlow training with Slurm**
2. **Profiling & debugging with Intel VTune Profiler**

---

## ⏰ 2. Realistic 180-Minute (3-Hour) Delivery Timeline

```
+──────────────────────────────────────────────────────────────────────────────────────────+
|                        DAY 4 TIMELINE (TOTAL: 180 MINUTES)                               |
+──────────────────────────────────────────────────────────────────────────────────────────+
|  00:00 - 00:45 (45m) │ PART 1: Distributed TensorFlow Orchestration with Slurm           |
|                      │        (Multi-Node Task Mapping, Core Pinning, Socket Affinity)   |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  00:45 - 01:25 (40m) │ PART 2: The Optimization Gap & Inside Intel VTune Profiler        |
|                      │        (Why Unprofiled Code Fails, Top-Down Methodology / TMAM)   |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:25 - 01:35 (10m) │ ☕ REJUVENATION BREAK (10 Minutes)                                |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  01:35 - 02:20 (45m) │ PART 3: Hands-On Profiling: Hotspots & Memory Stalls              |
|                      │        (vtune CLI, Microarchitecture Exploration, Flame Graphs)   |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:20 - 02:45 (25m) │ PART 4: Performance Diagnostic Matrix & Hardware-Aware Fixes      |
|                      │        (I/O Wait, Thread Contention, Horovod Ring Tuning)         |
+──────────────────────┼───────────────────────────────────────────────────────────────────+
|  02:45 - 03:00 (15m) │ PART 5: Assessment, 25 MCQs & Wrap-Up                             |
|                      │        (5 Evaluated MCQs + Review & Day 5 Capstone Preview)       |
+──────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 🎙️ 3. Line-by-Line Minute-by-Minute Trainer Delivery Script

### PART 1: Distributed TensorFlow Orchestration with Slurm (00:00 - 00:45 | 45 Mins)
- **Concept:** Mapping distributed ranks across CPU sockets and cluster nodes.
- **What Trainer Says:**
  > "Yesterday we learned how to submit a single job with Slurm and wrap optimizers with Horovod.
  > Today on Day 4, we scale across the entire cluster!
  > Look at how Slurm maps distributed tasks:
  > `#SBATCH --nodes=4`
  > `#SBATCH --ntasks-per-node=2`
  > `#SBATCH --cpus-per-task=16`
  > Notice the rule of **Core Pinning**: If Linux randomly migrates your TensorFlow threads from CPU Socket 0 to Socket 1, all L1/L2 cache data is lost, causing severe memory stall penalties.
  > By using `mpirun --bind-to socket`, processes stay pinned to physical CPU silicon, maximizing cache hits!"

---

### PART 2: The Optimization Gap & Inside Intel VTune (00:45 - 01:25 | 40 Mins)
- **Concept:** Why throwing more nodes at unoptimized code wastes compute.
- **What Trainer Says:**
  > "Many engineers believe: *'My model runs slow, so let's request 16 nodes instead of 4.'*
  > But when they run it on 16 nodes, it runs at the SAME speed or even SLOWER!
  > Why? Because of the **Optimization Gap**:
  > If your code is waiting for disk reads, choked on thread locks, or saturating memory bandwidth, adding more nodes just multiplies the waiting time!
  > To close the gap, we must see inside the silicon using **Intel VTune Profiler**.
  > VTune uses the **Top-Down Microarchitecture Analysis Method (TMAM)**:
  > 1. *Frontend Bound:* Is the CPU waiting to fetch and decode instructions?
  > 2. *Bad Speculation:* Is the CPU mispredicting branch statements?
  > 3. *Backend Bound:* Is the CPU stalled waiting for memory (Memory Bound) or execution units (Core Bound)?
  > 4. *Retiring:* Are instructions actually finishing useful work?"

---

### ☕ BREAK (01:25 - 01:35 | 10 Minutes)

---

### PART 3: Hands-On Profiling with VTune CLI (01:35 - 02:20 | 45 Mins)
- **Concept:** Running `vtune -collect hotspots`.
- **What Students Run in Colab / Terminal:**
  ```bash
  # Collect hotspots analysis on Python training script
  vtune -collect hotspots -result-dir ./vtune_hotspots -- python3 train.py

  # Generate human-readable summary report
  vtune -report summary -result-dir ./vtune_hotspots
  ```
- **Trainer Walkthrough:**
  > "Look at the report: VTune pinpoints the EXACT function and line number consuming 78% of runtime!
  > It tells you whether the function is compute-bound or memory-bound."

---

### PART 4: Performance Diagnostic Matrix & Hardware-Aware Fixes (02:20 - 02:45 | 25 Mins)
- **What Trainer Says:**
  > "How do we translate VTune metrics into concrete engineering fixes?
  > - **Symptom 1:** High wait time between epochs? VTune shows Storage Latency spike -> Fix: Use pre-fetching and pinned memory in PyTorch/TF DataLoader (`pin_memory=True`).
  > - **Symptom 2:** Low CPU utilization? VTune shows Thread Lock / Spin Time -> Fix: Set `OMP_NUM_THREADS` and avoid oversubscribing physical cores.
  > - **Symptom 3:** Scaling drops at 4+ nodes? VTune shows Ring-Allreduce wait -> Fix: Increase Horovod Tensor Fusion buffer size (`HOROVOD_FUSION_THRESHOLD=67108864`)."

---

### PART 5: Assessment & Wrap-Up (02:45 - 03:00 | 15 Mins)
- Review 5 core MCQs and connect to Day 5 (Generative AI Capstone on Gaudi & OpenVINO).
