# OCR Transcript: Day-04 - Day_04_Distributed_AI_Cluster_Optimization_NotebookLM.pptx
Source File: C:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\NotebookLM_Master_Decks_Organized\Day_04_Distributed_AI_Cluster_Optimization_NotebookLM.pptx
Total Slides: 13
Watermark Status: 100% REMOVED & VERIFIED CLEAN
Verified On: 10/13/2026 17:19:05

---

## Slide 1
High Performance Computing: A Practical Approach Day 4: Distributed A1 Training & Profiling Optimization. Moving from single-node execution to cluster-scale hardware-aware optimization.

---

## Slide 2
Cluster-Based Reality No simulated environments. Learners deploy ML/DL workloads directly on bare- metal HPC nodes, executing real enterprise -grade workflows. Hands-On Execution Linux, oneAPI, Slurm orchestration System Understanding HPC Architecture, Hardware topology Concept Parallel computing, distributed logic Project-Oriented Arc Every daily lab cascades into the next. From foundational ML processing to distributed training, culminating in end-to-end LLM fine-tuning on Intel hardware.

---

## Slide 3
DAY 4 FOCUS AREA * DAY 4 FOCUS AREA Qetimiza!ion lintel VTune Profiler, OpenVIN0 Toolkit Frameworks Layer TensorF10w-MKL, oneDNN, Horovod Intel Slurm Core Libraries Layer oneAPI, A1 Analytics Toolkit I Infrastructure Layer Workload Manager, Linux, SSH

---

## Slide 4
WORKFLOW OPTIMIZATION Scale out PROCESS via 01 02 03 04 Orchestrate distributed TensorF10w training using Slurm workload manager. Scale deep learning jobs across multiple HPC nodes with Horovod and MPI. Profile compute-intensive workloads to identify hardware bottlenecks . Apply hardware-aware optimizations using Intel VTune Profiler. Slurm Train via TF-MKL/Horovod Profile via V Tune Optimize & Re-run

---

## Slide 5
THE WALL exceeded tERROR% Memory 48 Modern Deep Learning models rapidly exceed the compute and memory capacity of any single bare-metal node. Vertical scaling has a hard physical ceiling. [Parallel Processing / Est. Time: 4 Hrs] THE TRANSITION Moving from vertical scaling to horizontal scaling (cluster synchronization via MPI/Horovod) . THE NEW CHALLENGE Horizontal scaling introduces severe friction: network overhead, data decomposition, and node synchronization bottlenecks.

---

## Slide 6
CLUSTER WORKFLOW & RESOURCE ALLOCATION USER EXECUTION Write ML script & Slurm batch configuration THE ORCHESTRATOR (SLUM) Queue workloads, check availability, dictate routing HARDWARE-AWARE RESOURCE ALLOCATION COMPUTE NODES Intel Xeon CPUs & GPUs parallel execution Slurm ensures jobs land on nodes with the specific oneAPI accelerators, memory profiles, and CPU topologies required by the DL model. C

---

## Slide 7
-nodes-4 #SBATCH - - -nodes-4 #SBATCH ntasks-per-node=2 #SBATCH -- -partition=gpu-intel #SBATCH - mpirun -np 8 python3 train_horovod.py Requesting horizontal scale across the cluster. Mapping execution tasks to hardware topology. Targeting specific Intel architecture. Launching distributed TF with MPI and Horovod. Key Takeaway: Moving to HPC means fundamentally transitioning from running a script to scheduling and orchestrating distributed workloads.

---

## Slide 8
CLUSTER WORKFLOW & RESOURCE ALLOCATION THE IDEAL CURVE-- THE OPTIMIZATION GAP - WHERE VTUNE STEPS IN THE REALITY CURVE 2 4 8 NUMBER OF NODES 16 32 WHY PROFILING MATTERS Throwing more nodes at an unoptimized TensorF10w model wastes expensive compute. Distributed training inherently introduces introduces communication overhead, 1/0 blocking, and CPU/GPU memory starvation. To close the gap, we must see inside the hardware.

---

## Slide 9
INSIDE INTEL VTUNE PROFILER Thread 1 Thread 2 [1/0 wait] Thread 3 [Lock Overhead] [Lock Overhead] [1/0 wait] Microarchitecture Exploration Peers beneath the TensorF10w-MKL abstraction to reveal exactly how cache, memory, and threading interact with Intel silicon. Hotspot Analysis Identifies the precise line of code where execution time is bottlenecking. Threading Efficiency Reveals if OpenMP threads are effectively mapped or if cores are idling. Memory Access Profiling Diagnoses whether the model is compute-bound or memory-bound.

---

## Slide 10
PERFORMANCE DIAGNOSTIC MATRIX OBSERVATION: The Symptom High wait times between training epochs. Low CPU/GPU Utilization during active training. Scaling efficiency drops sharply at 4+ nodes. VTUNE INSIGHT: The Metric Elevated 1/0 Wait / Storage Latency spikes. Threading overhead / Poor oneDNN mapping. MPI communication bottleneck / Horovod Ring-AllReduce latency. ACTION: Hardware-Aware Fix Implement data pre-fetching; optimize data decomposition pipelines. Tune OpenMP environment variables; adjust batch size to saturate compute units. Adjust tensor fusion buffer sizes; optimize network topology routing.

---

## Slide 11
ITERATIVE OPTIMIZATION PIPELINE 01. EXECUTE Submit TensorF10w job via Slurm script 04. OPTIMIZE Refactor Python code, tune Horovod, or adjust Slurm allocations Iterative Hardware-Aware Optimization 02. PROFILE Run Intel VTune alongside the job to capture raw hardware metrics 03. ANALYZE Identify hotspots and overheads in the VTune GUI/CLI

---

## Slide 12
DISTRIBUTED A1 WORKFLOW CODE & CONFIG slurm THE I-IPC CLUSTER Ill THE RESULT Monitored by VTune Python ML Script slurm Slurm Batch Config Optimized DL Model VTune Performance Report Distributed A1 on HPC is not just about seamless interaction between parallel writing ML models. It is the engineering of code, cluster orchestration, and silicon.

---

## Slide 13
THE PATH FORWARD Days 1-3 Linux Foundations, oneAPI & Traditional ML Day 4 Distributed A1 Training & VTune Profiling Day 5 Generative A1 & LLMs on Intel HPC THE PATH FORWARD The distributed execution techniques and hardware-profiling skills mastered today are the exact prerequisites required to deploy, fine-tune, and optimize massive Large Language Models (LLMs) on Intel Xeon and Habana Gaudi tomorrow. Next focus: LLM inference optimization via the OpenVIN0 Toolkit.

---

