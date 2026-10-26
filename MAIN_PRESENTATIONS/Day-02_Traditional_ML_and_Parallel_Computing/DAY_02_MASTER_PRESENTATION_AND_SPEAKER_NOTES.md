# 🎓 DAY 2: MASTER PRESENTATION & SPEAKER NOTES
## Traditional Machine Learning & Parallel Computing using Intel oneAPI
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Target Audience:** B.Tech / M.Tech Computer Science (60 Students)  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 🏛️ 1. Syllabus Boundary & Scope (Day 2)

```
+─────────────────────────────────────────────────────────────────────────────────────────+
|                                DAY 2 SYLLABUS BOUNDARY                                  |
+─────────────────────────────────────────────────────────────────────────────────────────+
|  [DAY 2: IN-SCOPE]                                                                      |
|  1. Breaking the Serial Bottleneck (Amdahl's Law, Task vs Data Parallelism)             |
|  2. Shared Memory Multithreading (OpenMP, Pragma Directives, Thread Private/Shared)     |
|  3. Distributed Memory Architecture (MPI, Point-to-Point, Collective Communications)    |
|  4. Intel oneAPI Math Kernel Library (oneMKL Vectorization for NumPy & SciPy)           |
|  5. Intel Extension for Scikit-learn (sklearnex, oneDAL Dynamic Patching)              |
|  6. Parallelizing Classical ML (k-Means, PCA, Random Forest, Support Vector Machines)   |
+─────────────────────────────────────────────────────────────────────────────────────────+
|  [DAY 3-5: FUTURE SCOPE - DO NOT PRE-EMPT ON DAY 2]                                     |
|  Deep Learning & TensorFlow-MKL (Day 3) | Slurm Cluster Job Submission (Day 3/4)        |
|  Horovod Multi-Node Ring-Allreduce (Day 4) | Intel VTune Profiler (Day 4)               |
|  Generative AI, LLMs & Habana Gaudi (Day 5)                                             |
+─────────────────────────────────────────────────────────────────────────────────────────+
```

---

## 📋 2. Complete Topic & Subtopic Breakdown (Day 2)

### Topic 1: Breaking the Serial Bottleneck
- **The Limits of Moore's Law & Dennard Scaling:** Why single-core clock frequencies flattened at ~4-5 GHz (thermal dissipation limits).
- **Amdahl's Law vs Gustafson's Law:** Theoretical speedup limits of parallel execution based on serial fractions.
- **Task Parallelism vs Data Parallelism:** Functional pipeline splitting vs SIMD vector/array slicing.

### Topic 2: Shared-Memory Multithreading with OpenMP
- **OpenMP Architecture:** Fork-Join execution model running inside a single symmetric multiprocessing (SMP) node.
- **Core Directives:** `#pragma omp parallel`, `#pragma omp for`, `#pragma omp barrier`, `#pragma omp atomic`.
- **Data Sharing Clauses:** `shared`, `private`, `firstprivate`, `reduction(+:sum)`.
- **Thread Scheduling:** `static` (deterministic block chunks) vs `dynamic` (work-stealing queue for imbalanced workloads).

### Topic 3: Distributed-Memory Message Passing with MPI
- **MPI (Message Passing Interface) Standard:** Scaling across physically separated cluster nodes communicating over high-speed networks.
- **Ranks and Communicators:** `MPI_COMM_WORLD`, `MPI_Comm_rank`, `MPI_Comm_size`.
- **Point-to-Point vs Collective Communication:**
  - *Point-to-point:* `MPI_Send`, `MPI_Recv`.
  - *Collectives:* `MPI_Bcast`, `MPI_Scatter`, `MPI_Gather`, `MPI_Reduce`, `MPI_Allreduce`.

### Topic 4: Accelerated Scientific Computing (oneMKL & NumPy)
- **Standard Python GIL Bottleneck:** The Global Interpreter Lock restricting CPU execution to single threads.
- **Intel oneMKL Integration:** Vectorized BLAS (Basic Linear Algebra Subprograms) executing across AVX-512 registers.
- **Zero-Code Change Acceleration:** Linking accelerated BLAS/LAPACK to NumPy and Pandas.

### Topic 5: Intel Extension for Scikit-learn (oneDAL)
- **What is `sklearnex`?** High-performance drop-in replacement library powered by Intel oneDAL (Data Analytics Library).
- **Dynamic Monkey Patching:**
  ```python
  from sklearnex import patch_sklearn
  patch_sklearn()
  import sklearn
  ```
- **Algorithms Accelerated:** Support Vector Classification/Regression (SVC/SVR), Random Forest, k-Means clustering, Principal Component Analysis (PCA), k-Nearest Neighbors (kNN).
- **Hardware Acceleration:** Automatic multi-core thread scaling and AVX-512 vectorization without rewriting mathematical code.

---

## 🖥️ 3. Slide-by-Slide Speaker Notes

*Mapped to the 12 Slides of `Day_02_NotebookLM_Master_Deck.pptx`*

- **Slide 1: High Performance Computing: A Practical Approach (Day 2)**  
  *Speaker Point:* "Yesterday, we mastered Linux, Shell automation, and oneAPI environment architecture. Today on Day 2, we break the serial bottleneck! We will turn single-threaded Python algorithms into parallel, multi-core engines."
- **Slide 2: Pedagogical Engine: Concept to Bare Metal**  
  *Speaker Point:* "Notice the flow: theory of parallel memory architectures -> understanding cache lines and memory domains -> compiling real C++ OpenMP and accelerated Python code."
- **Slide 3: The 5-Day Acceleration Pipeline**  
  *Speaker Point:* "Highlighting Day 2: Parallel Computing, OpenMP, MPI, and oneDAL Machine Learning."
- **Slide 4: Breaking the Serial Bottleneck Through Parallel Computing**  
  *Speaker Point:* "Why can't a single CPU core run your machine learning job 10x faster? Because clock frequency is capped. To get 10x speedup, you MUST use 16 or 32 physical cores in parallel."
- **Slide 5: Scaling Architectures: Shared vs. Distributed Memory**  
  *Speaker Point:* "Contrast OpenMP (intra-node shared memory via memory bus) vs MPI (inter-node message passing over network cables). This distinction is the bedrock of supercomputing."
- **Slide 6: Anatomy of Parallelism: Data Decomposition & Synchronization**  
  *Speaker Point:* "Show how a 1-million row matrix is split into contiguous 250,000-row chunks for Core 1, 2, 3, and 4. Emphasize why race conditions happen if two threads write to the same memory location simultaneously."
- **Slide 7: Bridging Hardware and Data Science with Intel oneAPI**  
  *Speaker Point:* "Data scientists shouldn't need a PhD in assembly language to get hardware speed. Intel oneAPI provides the AI Analytics Toolkit to bridge high-level Python directly to Xeon AVX-512 registers."
- **Slide 8: Accelerating Foundational Data Handling (NumPy / Pandas)**  
  *Speaker Point:* "Demonstrate that standard Python loops take seconds, but oneMKL vectorized matrix operations finish in milliseconds."
- **Slide 9: Algorithmic Acceleration via Intel Extension for Scikit-Learn**  
  *Speaker Point:* "Explain the 2-line code change: `from sklearnex import patch_sklearn; patch_sklearn()`. Show how this dynamically hooks into Intel oneDAL to achieve 10x-50x speedups on algorithms like SVM and k-Means."
- **Slide 10: Hands-On Lab: The Cluster Experience**  
  *Speaker Point:* "Guide students through compiling OpenMP code and running the patched Scikit-learn comparison benchmark."
- **Slide 11: The Foundational Architecture for Massive GenAI Scale**  
  *Speaker Point:* "Explain why Day 2 matters for Day 5 LLMs: You cannot train a 70-Billion parameter LLM if your basic data preprocessing pipeline chokes on single-threaded Python."
- **Slide 12: Comprehensive Learning Outcomes**  
  *Speaker Point:* "Review of achievements: Parallel decomposition mastered, OpenMP/MPI understood, Scikit-learn accelerated."

---

## 🔬 4. Lab Hands-On Synchronization

- **Lab 1:** Compiling OpenMP multi-threaded C++ code with `icpx -qopenmp`.
- **Lab 2:** Comparing raw Scikit-Learn vs `sklearnex` patched k-Means and SVM on a 500,000-sample dataset (measure 15x-30x speedup).
- **Lab 3:** OpenMP reduction variable demonstration avoiding data race conditions.
