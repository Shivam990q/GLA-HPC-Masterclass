# OCR Transcript: Day-01 - Day_01_High_Performance_AI_Foundations_NotebookLM.pptx
Source File: C:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\NotebookLM_Master_Decks_Organized\Day_01_High_Performance_AI_Foundations_NotebookLM.pptx
Total Slides: 15
Watermark Status: 100% REMOVED & VERIFIED CLEAN
Verified On: 10/13/2026 17:18:57

---

## Slide 1
High Performance Computing: A Practical Approach // Program Pedagogy & Day 1 Foundations Bridging the gap between theoretical ML and hardware-aware, optimized cluster execution.

---

## Slide 2
A1 ENGINEERING: FROM WORKSTATION TO HPC CLUSTER Standard ML Workflow DATA IN PROCESSIVG TRAINING OUTPUT - Single-node limitation - Unoptimized execution - Standard local libraries Industry-Grade HPC Workflow 2 - Distributed parallel training - Hardware-aware execution - Massively scaled workloads Transitioning from writing baseline models to engineering optimized, cluster-scale A1.

---

## Slide 3
Our Pedagogical Engine [01] Concept Understand core HPC architectures and parallel computing theories. We don't just write code; we engineer execution. [03] Hands-On Deploy immediately on bare metal using Linux, oneAPI, and cluster environments. [02] System Understanding Analyze how silicon—Xeon CPUs, GPUs, and Gaudi accelerators—actually executes code. -4-

---

## Slide 4
The Core Pillars of Training Industry-Grade Tools Training mirrors real HPC environments utilizing Intel oneAPl, A1 Analytics Toolkit, TensorFlow-MKL, Horovod, VTune, Slurm, and OpenVlN0. Performance Focus Rigorous emphasis on parallel computing, distributed training, profiling, and hardware-aware optimization. Cluster-Based Learning Operate exclusively on HPC nodes, submitting ML/DL workloads via Slurm while analyzing real-time hardware telemetry. Project -Oriented Daily hands-on labs compound into a final, end-to-end A1 workflow encompassing distributed training and LLM optimization.

---

## Slide 5
The Software 8 Hardware Ecosystem Execution 8 Optimization Orchestration 8 Access Compute 8 Silicon

---

## Slide 6
The 5- Day Arc Day 5 Generative A1 & LLMs on Intel I-IPC (Gaudi, OpenVINO) Day 4 Distributed A1 Training (Horovod) & Profiling (VTune) You Are Here Day 1 Fundamentals of HPC, Linux, Shell & Toolkits Day 3 Deep Learning on HPC with TensorF10w-MKL, GPUs, and Slurm Day 2 Traditional ML using Intel oneAPI, OpenMP, and MPl

---

## Slide 7
eoe > init - -module day_@l_fundamentals > Loading dependencies. .. [0K] HPC Architecture Deconstructed [0K] The Hardware Continuum [0K] Linux OS & Environment Navigation [0K] Secure Shell (SSH) & Automation [0K] Toolkit Initialization (oneAPI & HPC) > Ready for input.

---

## Slide 8
Deconstructing HPC: Beyond the Laptop Standard Architecture Local Memory CPU Local Storage Bottlenecked by single-node limitations. HPC Cluster Architecture Compute CPU/ GPU Compute CPU/ GPU Compute CPU/ GPU Node Memory Node Memory Node Memory High-Speed Interconnects Shared Parallel Storage HPC relies on massive parallelization across interconnected compute nodes to solve complex problems exponentially faster than scalar systems.

---

## Slide 9
The Hardware Continuum Function Ideal Workload Intel Xeon CPUs Highly versatile scalar/vector processing. Traditional ML (Scikit-learn), Data preprocessing, orchestration. Intel GPUs Massively parallel matrix operations. Accelerated Deep Learning training, complex visualization workloads. Reference A1 Accelerators (Habana Gaudi) Purpose-built tensor processing architecture. Generative A1, large-scale LLM training, and high-throughput inference.

---

## Slide 10
Refezence Environment Navigation: Linux & The File System / home /scratch /work Cool Zone: Standard configuration files and scripts. Lower 1/0 speed. Hot Zone: Ephemeral, high-speed parallel storage. Model training data MUST reside here. Navigation cd /scratch/project Is -la Search grep find -r 'loss' output. log . -name '*.sh' Permissions chmod +x run_training.sh chown user :group dataset/ Mote

---

## Slide 11
Access & Automation Secure Access Secure Shell / SSH Head Node Shell Automation O .sh script Refezence Worker Node 01 Worker Node 02 Worker Node 03 SSH provides the secure gateway; Shell Scripting provides the automation engine for repeatable, scalable job execution.

---

## Slide 12
Refezence The Software Bridge: Intel oneAPI Python TensorF10w The Intel oneAPl Abstraction Layer Xeon CPU Intel GPU FPGA pyTorch A1 Accelerator Write once, deploy anywhere. oneAPl eliminates the need to rewrite code for different architectures.

---

## Slide 13
Refezence Inside the Intel [Compilers] Intel C++ and Fortran compilers explicitly optimized for underlying silicon hardware. Intel I-IPC Toolkit HPC Toolkit Base [MPI Library] Message Passing Interface toolkit enabling complex communication between distributed nodes. [Inspector / Trace] Memory and thread debugging tools to ensure parallel execution stability. Note: The HPC Toolkit layers precisely on top of the base oneAPl ecosystem to enable massive cluster-scale execution. Moue

---

## Slide 14
Refezenco Day 1 Synthesis: The Architecture of Execution SSH Secure remote connection Linux os Navigate parallel file system Shell Script Automate batch submission oneAPI Toolkit Hardware abstraction & compiling Intel Architecture Execution on Xeon/GPUs [Pipeline Execution Sequence] Unified workflow from remote access to hardware acceleration.

---

## Slide 15
Refezencø Foundation Established, > Loading Day 2: Parallel Computing & Traditional ML using Intel oneAPI. • Transitioning from architecture to optimization. • Leveraging OpenMP and MPI. e Accelerating Scikit-learn, Pandas, and NumPy.

---

