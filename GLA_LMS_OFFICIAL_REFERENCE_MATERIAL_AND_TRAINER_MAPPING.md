# 🏢 GLA UNIVERSITY // LMS OFFICIAL REFERENCE MATERIAL & INSTRUCTIONAL MAPPING

**Course Title**: High Performance Computing (HPC) & Heterogeneous AI Systems  
**Course Code**: GLA-HPC-BCSG701 (Block Teaching Mode)  
**Host Department**: Department of Computer Engineering & Applications, GLA University, Mathura  
**Contracting Organization**: Edulateral Foundation, Bangalore  
**Technical Alliance**: Intel Unnati Labs & NEC Supercomputing Center of Excellence  
**Target Delivery Dates**: November 16 – November 20, 2026 (Daily: 9:00 AM – 4:30 PM)  
**Target Audience**: 7th Semester B.Tech Computer Science & Engineering Students  

---

## 👥 1. Official Trainer Allocation & Instructional Split

| Day | Date & Time | Topic Focus | Lead Instructor (Morning 09:00 - 12:30) | Co-Trainer / Lab Lead (Afternoon 01:30 - 04:30) |
| :--- | :--- | :--- | :--- | :--- |
| **Day 1** | Nov 16, 2026 | **HPC Fundamentals, Linux Systems & Intel oneAPI** | **Shivam Gupta (~SEED~)**<br>• Silicon Microarchitecture & Memory Wall Latency<br>• AVX-512 SIMD & FMA Arithmetic<br>• Linux Kernel `task_struct`, Core Pinning & TLB<br>• Intel oneAPI DPC++/SYCL Unified Shared Memory | **Rajat Garg (Ramāpriya Das)**<br>• GLA LMS Syllabus & Attendance Onboarding<br>• Supercomputing Center of Excellence Overview<br>• Lab 1 & 2 Execution Supervision<br>• Daily MCQ Assessment Governance |
| **Day 2** | Nov 17, 2026 | **Parallel Computing, OpenMP, MPI & Intel oneDAL** | **Shivam Gupta (~SEED~)**<br>• OpenMP Fork-Join & The False Sharing Trap<br>• MESI Cache Coherence Protocol & Reduction Tree<br>• MPI Point-to-Point & Collective Algorithms<br>• Intel oneDAL Accelerated Scikit-Learn | **Rajat Garg (Ramāpriya Das)**<br>• Parallel Scaling Laws (Amdahl vs Gustafson)<br>• Enterprise Clustering Case Studies<br>• Multi-Node MPI Ring Benchmark Lab<br>• Day 2 MCQ Evaluation Upload |
| **Day 3** | Nov 18, 2026 | **Deep Learning on HPC & Slurm Workload Manager** | **Shivam Gupta (~SEED~)**<br>• GEMM Matrix Computations in Neural Networks<br>• Slurm Controller Daemon Architecture (`slurmctld`)<br>• Horovod Ring-AllReduce vs Parameter Server<br>• Intel AMX Systolic Tiles & IPEX BF16 | **Rajat Garg (Ramāpriya Das)**<br>• Cluster Scheduling Policies & Fair-Share Math<br>• Multi-GPU Deep Learning Industry Trends<br>• PyTorch DDP Distributed Lab Supervision<br>• Day 3 MCQ Evaluation Upload |
| **Day 4** | Nov 19, 2026 | **Distributed AI, Slurm & Intel VTune Profiling** | **Shivam Gupta (~SEED~)**<br>• Intel VTune Top-Down Microarchitecture Analysis<br>• Retiring vs Bad Speculation vs Memory-Bound<br>• Cache-Aware Roofline Model ($I = \text{FLOPs}/\text{Byte}$)<br>• Dual-Socket NUMA Memory Latency & `numactl` | **Rajat Garg (Ramāpriya Das)**<br>• Hardware Performance Monitoring in Industry<br>• InfiniBand HDR vs RoCE v2 Networking Topology<br>• Memory-Access Hotspot Profiling Lab<br>• Day 4 MCQ Evaluation Upload |
| **Day 5** | Nov 20, 2026 | **Generative AI, LLMs on Intel HPC, Gaudi & OpenVINO** | **Shivam Gupta (~SEED~)**<br>• Transformer Attention Silicon Physics ($QK^T / \sqrt{d_k}$)<br>• Prefill (Compute-Bound) vs Decode (Memory-Bound)<br>• KV-Cache Sizing Formula & PagedAttention<br>• Intel Gaudi 2/3 On-Die 24x 100GbE RoCE v2<br>• OpenVINO NNCF INT8/INT4 Model Compression<br>• Asynchronous High-Concurrency FastAPI Serving | **Rajat Garg (Ramāpriya Das)**<br>• Enterprise GenAI Economics & TCO (Gaudi vs H100)<br>• Capstone Project Grading Rubric Verification<br>• Customer Support Chatbot Deployment Lab<br>• Course Valedictory & Edulateral Certification |

---

## 📚 2. GLA LMS Official Reference Reading Material

The following peer-reviewed textbooks, industry manuals, and technical specifications must be listed in the GLA LMS course syllabus under **Required & Supplementary Reading**:

### Core HPC & Silicon Architecture:
1. **Computer Architecture: A Quantitative Approach (6th Edition)**  
   *Authors*: John L. Hennessy and David A. Patterson (Morgan Kaufmann / Elsevier).  
   *Key Chapters*: Chapter 2 (Memory Hierarchy Design), Chapter 4 (Data-Level Parallelism in Vector, SIMD, and GPU Architectures), Chapter 5 (Thread-Level Parallelism & Cache Coherence).
2. **Data Parallel C++: Mastering SYCL for Heterogeneous Systems with oneAPI**  
   *Authors*: James Reinders, Ben Ashbaugh, James Brodman, Michael Kinsner, John Pennycook, Xinmin Tian.  
   *Publisher*: Apress (Open Access). Available free at: https://link.springer.com/book/10.1007/978-1-4842-5574-2
3. **Intel® oneAPI Programming Guide**  
   *Publisher*: Intel Corporation Technical Documentation.  
   *URL*: https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit-documentation.html
4. **Linux Kernel Development (3rd Edition)**  
   *Author*: Robert Love (Addison-Wesley Professional).  
   *Key Chapters*: Chapter 3 (Process Management), Chapter 4 (Process Scheduling & CFS), Chapter 12 (Memory Management).

### Parallel Programming & Distributed Workloads:
5. **Using OpenMP: Portable Shared Memory Parallel Programming**  
   *Authors*: Barbara Chapman, Gabriele Jost, Ruud van der Pas (The MIT Press).
6. **Using MPI: Portable Parallel Programming with the Message-Passing Interface (3rd Edition)**  
   *Authors*: William Gropp, Ewing Lusk, Anthony Skjellum (The MIT Press).
7. **Slurm Workload Manager Official Documentation**  
   *Publisher*: SchedMD LLC. Available at: https://slurm.schedmd.com/documentation.html

### Deep Learning, Accelerators & Generative AI:
8. **Attention Is All You Need** (Foundational Transformer Paper)  
   *Authors*: Ashish Vaswani, Noam Shazeer, Niki Parmar, et al. (NeurIPS 2017). https://arxiv.org/abs/1706.03762
9. **Habana® Gaudi® 2 & 3 Architecture Whitepaper**  
   *Publisher*: Habana Labs / Intel Corporation. https://habana.ai/gaudi/
10. **Intel® OpenVINO™ Toolkit Official Documentation**  
    *Publisher*: Intel Corporation. https://docs.openvino.ai/latest/home.html
11. **vLLM: Efficient Memory Management for Large Language Model Serving with PagedAttention**  
    *Authors*: Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, et al. (SOSP 2023). https://arxiv.org/abs/2309.06180

---

## 📦 3. Master PPTX Presentations & LMS Deliverables

All PowerPoint slide decks have been compiled in native 16:9 widescreen format, following both the official **Edulateral presentation standards** and the modern **NotebookLM high-density dark-mode design system**:

### Ready-to-Upload GLA LMS Presentation Decks:
| Day | Deck Title | Local File Path | Description |
| :--- | :--- | :--- | :--- |
| **Day 1 LMS Deck** | HPC Foundations, Linux & oneAPI | [`HPC_Master_Curriculum/LMS_Upload_Decks/Day_01_HPC_Foundations_Linux_oneAPI_LMS.pptx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/LMS_Upload_Decks/Day_01_HPC_Foundations_Linux_oneAPI_LMS.pptx) | Complete Day 1 deck for LMS upload covering HPC intro, Xeon/GPU/Gaudi silicon, Linux CLI, SSH, oneAPI Base & HPC Toolkit. |
| **Day 2 LMS Deck** | Traditional ML & Parallel Computing | [`HPC_Master_Curriculum/LMS_Upload_Decks/Day_02_Traditional_ML_Parallel_Computing_LMS.pptx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/LMS_Upload_Decks/Day_02_Traditional_ML_Parallel_Computing_LMS.pptx) | Complete Day 2 deck for LMS upload covering Parallel computing, OpenMP multithreading, MPI distributed systems, oneDAL & sklearnex. |
| **Day 3 LMS Deck** | Deep Learning on HPC & Slurm | [`HPC_Master_Curriculum/LMS_Upload_Decks/Day_03_Deep_Learning_HPC_Slurm_LMS.pptx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/LMS_Upload_Decks/Day_03_Deep_Learning_HPC_Slurm_LMS.pptx) | Complete Day 3 deck for LMS upload covering TensorFlow-MKL, oneDNN, Habana Gaudi, Slurm scheduling, and Horovod Ring-Allreduce. |
| **Day 4 LMS Deck** | Distributed AI & VTune Profiling | [`HPC_Master_Curriculum/LMS_Upload_Decks/Day_04_Distributed_AI_VTune_Profiling_LMS.pptx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/LMS_Upload_Decks/Day_04_Distributed_AI_VTune_Profiling_LMS.pptx) | Complete Day 4 deck for LMS upload covering Distributed TensorFlow with Slurm, Intel VTune microarchitecture & hotspot profiling. |
| **Day 5 LMS Deck** | Generative AI & LLMs on Intel HPC | [`HPC_Master_Curriculum/LMS_Upload_Decks/Day_05_GenAI_LLMs_Gaudi_OpenVINO_LMS.pptx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/LMS_Upload_Decks/Day_05_GenAI_LLMs_Gaudi_OpenVINO_LMS.pptx) | Complete Day 5 deck for LMS upload covering GenAI on HPC, Xeon AMX, Gaudi RoCE, OpenVINO INT8 quantization, and distributed fine-tuning. |

### Evaluation MCQs & Assessment Tools:
| Assessment Item | Local File Path | Description |
| :--- | :--- | :--- |
| **Complete 5-Day MCQ Bank** | [`HPC_Master_Curriculum/EDULATERAL_OFFICIAL_MCQ_BANK/`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/EDULATERAL_OFFICIAL_MCQ_BANK) | 125 Evaluative MCQs across all 5 Days with answer keys and technical rationales. |
| **Interactive Web Quiz** | [`HPC_Master_Curriculum/EDULATERAL_OFFICIAL_MCQ_BANK/interactive_quiz_evaluation.html`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/EDULATERAL_OFFICIAL_MCQ_BANK/interactive_quiz_evaluation.html) | Standalone browser-based interactive assessment engine for classroom delivery. |
| **Master Forensic Audit** | [`HPC_Master_Curriculum/NOTEBOOKLM_PPTS_COMPREHENSIVE_TOC_AUDIT_AND_ORGANIZATION.md`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/NOTEBOOKLM_PPTS_COMPREHENSIVE_TOC_AUDIT_AND_ORGANIZATION.md) | Slide-by-slide OCR transcript, 5-day TOC audit, ratings, and copy-pasteable lab code companion. |

