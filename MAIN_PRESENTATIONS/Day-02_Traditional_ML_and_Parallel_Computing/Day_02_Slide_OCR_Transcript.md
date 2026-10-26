# OCR Transcript: Day-02 - Day_02_High_Performance_AI_Acceleration_NotebookLM.pptx
Source File: C:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\NotebookLM_Master_Decks_Organized\Day_02_High_Performance_AI_Acceleration_NotebookLM.pptx
Total Slides: 12
Watermark Status: 100% REMOVED & VERIFIED CLEAN
Verified On: 10/13/2026 17:18:59

---

## Slide 1
High Performance Computing: A Practical Approach End-to-End Acceleration: From oneAPl Traditional ML to Distributed LLMs Mastering Parallel Computing, Hardware-Aware Optimization, Cluster-Based Workflows. and

---

## Slide 2
A Project-Oriented Pedagogical Engine Concept to Bare Metal Introduces core HPC theories, followed immediately by practical execution on Linux, oneAPI, and GPUs. End-to-End A1 Workflows Performance Engineering Relentless focus on parallel computing, distributed training, profiling, and hardware-aware optimization. Industry-Grade Tooling Training utilizes Intel oneAPI, A1 Analytics Toolkit, TensorFlow-MKL, Horovod, VTune, Slurm, and OpenVIN0. Cluster-Based Execution Active ML/DL workload deployment. Learners submit jobs with Slurm and analyze live hardware performance. _J

---

## Slide 3
The 5- Day 1 Day Acceleration Pipeline DEEP DIVE TARGET Foundations • HPC Architecture (Xeon/GPUs) • Linux basics • Shell Scripting • Secured Shell (SSH) Day 2 Optimized Traditional ML • Intel oneAPI • Parallel Computing • OpenMP/MP1 • Optimized Scikit- learn/Pandas. Day 3 Deep Learning on Clusters • TensorFlow-MKL . oneDNN • Slurm scheduling • Hardware-aware ML optimization. Day 4 Distributed A1 Training • Scaling distributed TensorFlow via Horovod • debugging/profiling with Intel VTune. -J Day 5 GenAl & LLMs • Fine-tuning and inference on Habana Gaudi and Xeon using the OpenVINO Toolkit.

---

## Slide 4
Breaking the Serial Bottleneck Through Parallel Computing Traditional Single-Thread Constraints Harnessing Intel Multi-Core Architectures Core Concepts Introduced: Multithreading I Distributed Systems I Task vs. Data Parallelism

---

## Slide 5
Scaling Architectures: Shared vs. Distributed Memory OpenMP (Multithreading) MPl (Message Passing Interface) Scope: Mechanism: Use Case: Intra-node (Shared Memory) . Compiler directives, spawning threads to share local resources. Maximizing the compute power of a single Intel Xeon processor. Scope: Mechanism: Use Case: _l Inter-node (Distributed Systems) . Message passing, active data exchange over network protocols. Scaling workloads horizontally across a vast HPC cluster. __l

---

## Slide 6
Anatomy of Parallelism: Data Decomposition & Synchronization CPU CORE 1 MONOLITHIC DATA ARRAY CPU CORE 2 CPU CORE 3 UNIFIED OUTPUT BLOCK Splitting massive datasets efficiently across available compute resources. CPU CORE 4 Managing thread communication, utilizing locks/barriers, and ensuring data integrity without race conditions.

---

## Slide 7
Bridging Hardware and Data Science with Intel oneAPl The Intel A1 Analytics Toolkit: Python, Pandas, NumPy, Scikit-Learn Zero-Code Change Acceleration oneAPl empowers data scientists to use familiar high-level Python tools while natively reaping bare-metal parallel performance. Intel oneAPl Base Toolkit (featuring libraries like oneDAL and oneMKL) Intel Xeon CPUs, Intel GPUs, and A1 Accelerators

---

## Slide 8
Accelerating Foundational Data Handling Standard Python Bottlenecked by single-thread execution. Intel-Optimized NumPy/Pandas Seamlessly multi-threaded via Intel oneAPI Math Kernel Library (oneMKL) . Vectorized operations drastically accelerate data frame manipulation and preprocesiing for massive HPC datasets before machine learning even begins.

---

## Slide 9
Algorithmic Acceleration via Intel Extension for Scikit-Learn import sklearn Dynamic Patching from sklearnex import patch_sklearn Mechanism: Dynamic patching routes standard ML algorithms (SVM, K-Means, PCA) through oneDAL (Data Analytics Library) to natively leverage Intel CPU vectorized and multi-core scaling.

---

## Slide 10
Day 2 Hands-On Lab: The Cluster Experience 11 ij ooo sbatch run_optimized_ml.sh Access: SSH into the secure Linux cluster. Environment: Load the Intel oneAPl • Toolkit environment modules. Execute: Decompose the dataset and 3. trigger the patched Scikit-Learn script. Scale: Submit the parallelized batch job • via Slurm to multiple compute nodes. Analyze: Monitor hardware utilization • to verify successful parallel execution.

---

## Slide 11
The Foundational Architecture for Massive GenAI Scale Day 2 Base: Optimized Data Pipelines & OpenMP/MP1 Baselines Slurm Job Scheduling & Hardware-Aware Optimization Days 3-5 Scale: Distributed TensorF10w (Horovod) & LLM Inference (Gaudi/OpenVINO) You cannot efficiently train a distributed Large Language Model if your underlying data pipelines and basic compute node architectures are bottlenecked. The parallelization principles mastered in Day 2 are the exact architectures required to scale deep learning across HPC clusters.

---

## Slide 12
Comprehensive Learning Outcomes CORE CORE L3 CACHE MEMORY CONTROLLER u NIT Architectural Mastery Deep understanding of Intel Xeon/GPU ecosystems and secure navigation of Linux cluster environments (SSH, Shell Scripting). Distributed Scale Proficiency in Sturm resource allocation and Horovod frameworks to break past single-node compute limits. Uncompromised Performance Ability to profile workloads with Intel VTune and optimize data from basic NumPy arrays up to complex ML models. Future-Ready A1 Hands-on deployment, fine-tuning, and OpenVINO- optimized inference of Generative A1 and LLMs on cutting-edge Habana Gaudi and Xeon hardware.

---

