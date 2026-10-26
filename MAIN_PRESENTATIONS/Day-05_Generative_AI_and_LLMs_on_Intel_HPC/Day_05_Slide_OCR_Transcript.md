# OCR Transcript: Day-05 - Day_05_Generative_AI_on_Intel_HPC_NotebookLM.pptx
Source File: C:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\NotebookLM_Master_Decks_Organized\Day_05_Generative_AI_on_Intel_HPC_NotebookLM.pptx
Total Slides: 15
Watermark Status: 100% REMOVED & VERIFIED CLEAN
Verified On: 10/13/2026 17:19:07

---

## Slide 1
Generative A1 & LLMs on Intel HPC From Hardware Architecture to Distributed Fine-Tuning. The Capstone Transforming theoretical A1 into hands-on, hardware-optimized, cluster-scale deployment.

---

## Slide 2
Hands-On Execution Practical cluster-based learning—submitting Slurm jobs, analyzing bare-metal performance, and profiling workloads. slurm Project-Oriented: Every daily lab builds directly toward end-to-end A1 workflows. 1 Concept Mastering core HPC architectures, parallel computing, and generative A1 theory. System Understanding Hardware-aware architecture navigation across Linux, Intel Xeon, Habana Gaudi ecosystems, and oneAPl toolkits.

---

## Slide 3
Frameworks: TensorFlow-MKL, Horovod, Intel A1 Analytics Toolkit Core Optimization Tools: Intel oneAPI, VTune Profiler, OpenVlN0 Toolkit Middleware & Schedulers: Linux OS & Slurm Workload Manager Hardware Foundation: Intel Xeon CPUs & Habana Gaudi Accelerators Industry-Grade Emulation Training mirrors real enterprise HPC environments. Learners operate strictly with the tools powering modern distributed A1 workflows. slurm

---

## Slide 4
ay 1: HPC & Linux oundation Day oneAPl & raditional M 7 Day 3: Deep Learning & Slurm Day 4: Distributed Training & Profiling Day 5: Generative A1 & LLMs on Intel HPC 1. Introduction to Generative A1 & LLMs on HPC architectures. 3. Optimizing LLM inference workloads with OpenVlN0. 2. Navigating Intel hardware for LLMs (Xeon, Habana Gaudi). e 4. Executing distributed fine- tuning of LLMs on HPC.

---

## Slide 5
The Generative A1 Bottleneck LLMs demand massive parameter storage, extreme parallel compute, and sustained memory bandwidth that single-node systems cannot provide. The Cluster-Scale Architecture Hardware-aware optimization paired with distributed cluster environments turns impossible models into real-time Generative A1 deployments.

---

## Slide 6
Intel Xeon vs. Habana Gaudi: Architectural Specialization Intel Xeon Processors General-purpose HPC + A1 Inference Advanced Matrix Extensions (AMX) built into the CPU Agile Inference, Data Prep, & Traditional ML High capacity DDR5+HBM for flexible workloads Habana Gaudi Accelerators Dedicated Deep Learning & Heavy Training Purpose-built Tensor Processing Cores (TPC) Massive Distributed Fine-Tuning & Parameter Updates Integrated HBM2e for sheer bandwidth Optimal HPC deployment requires matching the precise mathematical workload to the right architectural silicon.

---

## Slide 7
Accelerating Inference Directly on Intel Xeon Advanced Matrix Extensions (AMX) operate as a built-in A1 accelerator within the CPU architecture itself. AMX Maximizes existing HPC infrastructure—achieving high-throughput LLM inference without requiring discrete GPUs. Lab Execution Learners compile, optimize, and run TensorFlow-MKL models directly on bare-metal Xeon nodes, physically measuring inference throughput gains.

---

## Slide 8
Scaling Distributed Fine-Tuning with Habana Gaudi Purpose-built deep learning compute density paired with on-chip networking (ROCE) to scale effortlessly across massive clusters. Engineered specifically to eradicate the memory bandwidth bottlenecks that typically choke multi-billion Lab Execution Learners execute distributed parameter updates, allocating resources across multi-node Gaudi clusters to fine-tune generative models. parameter LLMs during training.

---

## Slide 9
Breaking the Generative A1 Inference Bottleneck Moving LLMs from theoretical research environments into real-world applications requires aggressive, hardware-aware efficiency. Raw models must be streamlined for latency-critical deployment. Raw 70B Parameter LLM / FP32 Lab Execution Intel OpenVlNO Toolkit 0 0 Optimized Low-Latency Model 0 Learners compile, optimize, and run TensorFlow-MKL models directly on bare-metal Xeon nodes, physically measuring inference throughput gains.

---

## Slide 10
Streamlining Generative A1 with Intel OpenVINO 1. Model Ingestion Importing raw, pre-trained TensorFlow or PyTorch LLMs. Hands-On Focus 2. Quantization Shrinking massive FP32 models down to INT8/FP16 precision without sacrificing generative accuracy. 3. Graph Optimization Automatically fusing neural layers and pruning dead execution nodes. 4. Hardware-Aware Execution Deploying the streamlined runtime directly onto Xeon CPUs or integrated Intel GPUs. Learners write OpenVlNO implementation code to physically compress a Generative A1 model and profile the resulting drop in inference latency.

---

## Slide 11
Distributing Domain-Specific Fine-Tuning Full-parameter training of LLMs from scratch is cost-prohibitive. We utilize distributed HPC architectures to fine-tune specific neural layers for targeted enterprise applications. Compute Nodes Domain-Specific Data Tool Integration Horovod: Managing synchronized distributed training across nodes. Pre-trained Base LLM Slurm: Orchestrating the batch job and allocating cluster resources. Optimized LLM Compute Nodes

---

## Slide 12
Orchestrating Cluster-Based Execution $ sbatch —nodes=4 fine tune 11m. sh Practical Learning Learners bypass local notebooks. They engineer bash scripts, explicitly allocate cluster resources, and submit batch jobs via Slurm—exactly mirroring the execution environments of top-tier supercomputers. Slurm Master Node Odes

---

## Slide 13
Ensuring Bare-Metal Efficiency with Profiling Fine-tuning an LLM is not finished simply because the code runs. True HPC engineering requires relentless bottleneck eradication. FLAME GRAPH: Call Stack Analysis unction unction Call Function Call Thread Lock Wait (20% time) Function Call Memory Stall & Cache Misses (45% time) Intel VTune Used by learners to identify memory stalls, pinpoint thread locks, and expose utilization gaps during live LLM distributed training. 100% CPU UTILIZATION 100% Core 0-16 Core 17-32 (85%) (92%) Mindset Shift GPU UTILIZATION GPU I (98%) GPU 2 (99%) GPU3 4 (99%) (55% - Underutilized) Shifting the developer's question from "Did the job execute?" to "Did the job execute optimally on the bare metal?"

---

## Slide 14
Executing the Complete End-to-End A1 Workflow Raw Data & Base Model (Ingestion) Xeon Inference Deployment (Hardware-accelerated execution) Ill Linux Shell Setup (Environment configuration) Day 5 culminates in a unified, industry- standard workflow, fusing every isolated skill Slurm Job Submission (Resource orchestration) into a single elite capability. OpenVINO Optimization (Quantization & graph compression) Gaudi Fine-Tuning via Horovod (Distributed cluster scaling) Gaudi

---

## Slide 15
Mastering the Next Generation of HPC Deployment Mastered Generative A1 and LLM conceptual architectures. Deployed targeted workloads across Intel Xeon and Habana Gaudi silicon. Compressed and accelerated complex inference pipelines using the OpenVlN0 toolkit. Orchestrated large-scale, distributed fine-tuning jobs across cluster nodes via Slurm. Ready to build, scale, and relentlessly optimize the future of enterprise A1.

---

