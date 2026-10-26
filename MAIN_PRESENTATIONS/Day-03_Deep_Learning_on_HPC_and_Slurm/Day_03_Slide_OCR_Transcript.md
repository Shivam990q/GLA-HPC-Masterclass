# OCR Transcript: Day-03 - Day_03_Distributed_Deep_Learning_on_HPC_NotebookLM.pptx
Source File: C:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\NotebookLM_Master_Decks_Organized\Day_03_Distributed_Deep_Learning_on_HPC_NotebookLM.pptx
Total Slides: 15
Watermark Status: 100% REMOVED & VERIFIED CLEAN
Verified On: 10/13/2026 17:19:02

---

## Slide 1
Day 3: Deep Learning on HPC TensorFlow, Slurm, Intel GPUs & Distributed Training HIGH PERFORMANCE COMPUTING - A PRACTICAL APPROACH

---

## Slide 2
Day 3 Pedagogical Blueprint Core HPC Principles - Hardware-aware ML optimization - Parallel computing paradigms - Mathematics of distributed training Industry-Grade Tooling •F TensorFIcnv oneDNN library - Intel-Optimized TensorF10w & oneDNN - Habana Gaudi Accelerator architecture - Horovod ring-allreduce mechanisms Practical Cluster Execution S sbatch myscript.sh - Slurm job scheduling & resource allocation - Writing & executing batch jobs - Deploying distributed DL models on nodes

---

## Slide 3
The Deep Learning HPC Stack Application: TensorFlow & Horovod High-level Python frameworks for deep learning and distributed scaling. Middleware: Intel oneAPI Toolkit (oneDNN, MKL) Hardware-aware optimization libraries translating code to silicon. OS / Resource: Linux & Slurm Environment management and cluster job scheduling. Hardware: Intel Xeon CPUs & Habana Gaudi Accelerators Physical compute resources for parallelized execution. TensorFlow Intel oneAPI oneDNN Horovod MKL slurm Linux

---

## Slide 4
Why Hardware-Aware Optimization Matters Unoptimized deep learning workflows leave immense compute power on the table. Hardware-aware optimization aligns ML primitives with the specific parallel computing architecture of the underlying silicon, maximizing memory bandwidth and minimizing execution overhead. Hardware-Agnostic ML Memory Bottleneck Memory Bottleneck Idle Core Space Memory Bottleneck Idle Core Space Vector Registers (Packed Data) Maximized Memory Bandwidth Hardware-Aware ML Optimized Compute Units Full Compute Utilization

---

## Slide 5
Injecting Performance with oneDNN & MKL Standard Pipeline Python Script (Keras/TF) Optimized Pipeline Python Script (Keras/TF) Intel-Optimized TensorFlow: Integrates natively with high-level code, requiring zero script rewrites. Default TensorFlow Engine Intel oneAPI (oneDNN & tensorflow-mkl) TensorFlow Engine oneDNN: Accelerates core neural network primitives like convolutions and matrix multiplications. Standard CPU Execution (Sub-optimal) Highly Parallelized Hardware Execution MKL: Optimizes the underlying mathematical operations specifically for Intel architectures.

---

## Slide 6
Hardware Selection: Xeon vs. Gaudi Comparison Matrix Dimension Architecture Focus Ideal DL Workload HPC Cluster Role Intel Xeon (Scalable CPUs) Scalable, versatile multithreaded compute cores. Mixed ML/DL pipelines, complex data preprocessing, and model inference. General-purpose compute nodes, login nodes, head nodes. Habana Gaudi (A1 Accelerators) Dedicated, high-throughput Deep Learning matrix engines. Massive compute-bound DL training, Generative A1, and LLMs. High-throughput parallelized training nodes. O Takeaway: Target Xeon nodes for end-to-end workload flexibility and preprocessing. Target Gaudi nodes for pure deep learning training and massive scaling speed.

---

## Slide 7
Managing Multi-Tenant HPC Resources In an HPC environment, heavy ML workloads cannot run directly on the login node. You must package your environment and submit it to a cluster resource manager to queue and allocate specific hardware. Compute Nodes (Xeon / Gaudi) (SSH) Custer Clush Topology Head / Login Node intel Job Scheduler / Queue (Slurm) job_scliptl . sh > job_script2. sh > job_script3. sh Node 1 User Workstation Node 3 Node 2 Node 4

---

## Slide 8
System & Hands-On: Slurm Job Scheduling eco # ! /bin/bash Identifies the batch job in the cluster queue. The execution command that launches the parallel workload across all allocated resources. #SBATCH #SBATCH #SBATCH #SBATCH --j ob-name=d I _ t r --nodes=4 --partition=gaudi --time=02 : 00 : 00 srun python train_model.py Resource allocation: Requests 4 discrete compute nodes. Targets specific hard- ware queues (e.g., Gaudi accelerators vs Xeon CPUs). Hard time limit ensures cluster efficiency and prevents hung jobs.

---

## Slide 9
The Distributed Training Challenge As deep learning models scale beyond a single node, we must split the workload. The primary barrier to linear scaling is network overhead: the time it takes to synchronize gradients across all nodes eventually outweighs the compute gains. Ideal Linear Scaling o The Communication Bottleneck Actual Scaling (Diminishing Returns) Number of Nodes

---

## Slide 10
Solving the Bottleneck with Horovod Instead of a traditional Parameter Server architecture that chokes central bandwidth, Horovod utilizes the Ring-Allreduce algorithm. Nodes pass gradient segments in a continuous ring, maximizing network bandwidth and enabling near-linear scaling. Parameter Server Architecture Ring-Allreduce Architecture Worker Node Worker Node Centralized Parameter Server bandwidth choke Worker Node Worker Node point. O Worker Node O Decentralized , Worker Node Worker Node Worker Node o balanced gradient exchange.

---

## Slide 11
Implementing Horovod in TensorFlow Standard TF Script import tensorflow as tf opt = " model. compile (optimizer—opt , loss= mse I) Horovod TF Script import tensorflow as tf horovod . tensorflow. keras as hvd import hvd. init (j gpus = tf. config. set_visible_devices ( gpus 'GPU opt = tf.optimizers * hvd.size()) " ppt = hvd . Distributed0ptimizer(opt) model. compile (optimizer-opt , loss= ' mse Takeaway: Transforming a single-node script into a distributed cluster script requires only minor wrapper adjustments to initialize the ring and handle synchronization.

---

## Slide 12
Launching Distributed TF with Slurm To execute the distributed script, we rely on Slurm's job launcher to spawn the Horovod processes across the allocated nodes. The scheduler maps the Horovod ranks directly to the physical Slurm tasks for seamless execution. srun - Scheduler Launcher (Slurm) —mpi=pmix —n 16 python train_distributed.py Physical Allocation (16 Tasks across 4 Nodes)

---

## Slide 13
Lab Objective: End-to-End A1 Workflow Step 1: Prepare Load a standard baseline Deep Learning model on a login node. Step 2: Optimize Integrate Intel- optimized TensorFlow variables (oneDNN/MKL) to maximize core utility. Step 3: Distribute Ü Wrap the model optimizer using (hvd. init) Horovod hvd. in it) for the ring-allreduce architecture. Step 4: Execute Write a #SBATCH Slurm script targeting Habana Gaudi nodes and deploy via srun.

---

## Slide 14
The Complete Deep Learning HPC Workflow Write Code python script . py Accelerate Middleware: Intel oneDNN / MKL Optimization Queue Scheduler: Slurm Batch Script #SBATCH - -nodes—4 - -ntasks=16 Distribute Network: O O Horovod Ring-Allreduce hvd. init() hvd. allreduce() Compute 4 Hardware: Intel Xeon / Habana Gaudi Clusters Intel' Xeon@ Scalable Processors / Habana' Gaudi' A1 Processors

---

## Slide 15
Day 3 Achieved: Scaled & Deployed You have successfully mapped hardware-aware optimizations ( ) into distributed oneDNN ML workflows (Horovod) and scheduled them across HPC nodes (Slurm/Gaudi) Maximum Scale & Speed Achieved gvul Next Up (Day 4): Distributed A1 Training & Profiling Optimization We will open the black box of compute-intensive workloads to profile, debug, and eliminate bottlenecks using Intel V Tune.

---

