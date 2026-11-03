# 📝 GLA University HPC Masterclass — Day 02: Evaluated Assessment Bank
## Intel AI Analytics Toolkit, oneDAL, NumPy MKL & Accelerated Classical Machine Learning

---

> **Assessment Purpose**: This evaluated assessment bank tests undergraduate computer science and AI/ML engineering students on the architectural bottlenecks of Python, CPython memory representation, Intel oneAPI Data Analytics Library (oneDAL), `scikit-learn-intelex` dynamic monkey-patching, AVX-512 hardware SIMD vectorization, and multi-threaded CPU performance tuning.
>
> **Target Audience**: B.Tech CSE / AI & ML Pre-Final & Final Year Students  
> **Total Questions**: 35 Questions (Divided into 3 Architectural Sections)  
> **Evaluation Mode**: Closed-Book / Lab Assessment / Placement Preparation  

---

## 📑 Assessment Blueprint & Sectional Breakdown

| Section | Domain Focus | Question Range | Weightage | Difficulty |
| :---: | :--- | :---: | :---: | :---: |
| **Section A** | CPython Memory Layout, Python GIL Bottleneck & oneAPI Architecture | Q01 – Q10 | 30% | Moderate |
| **Section B** | Intel Extension for Scikit-learn (`sklearnex`) & Dynamic Patching | Q11 – Q25 | 40% | Moderate to Advanced |
| **Section C** | Hardware Vectorization (AVX-512), OpenMP Thread Pools & Cache Optimization | Q26 – Q35 | 30% | Advanced |

---

# 📌 SECTION A: CPython Memory, Python GIL & oneAPI Architecture (Q01 – Q10)

#### Q01. In standard CPython 3.10+, how is a 64-bit floating-point number represented in virtual memory, and why does this representation impede SIMD hardware vectorization?
- **[A]** As a contiguous 8-byte IEEE-754 binary double word directly accessible by CPU registers.
- **[B]** As a heap-allocated `PyFloatObject` struct containing a 16-byte `PyObject_HEAD` (8-byte `ob_refcnt` + 8-byte `ob_type`) followed by an 8-byte `ob_fval` double, requiring pointer dereferencing that causes cache-line fragmentation.
- **[C]** As an interned 32-byte hash table entry indexed by object identity, preventing multithreaded concurrent reads.
- **[D]** As a memory-mapped virtual page buffer allocated via `mmap()`, incurring kernel page fault overhead on every floating-point addition.

---

#### Q02. What is the fundamental mechanism of the CPython Global Interpreter Lock (GIL), and why does it render naive multi-threaded CPU-bound loops ineffective?
- **[A]** The GIL is an OS-level kernel semaphore that prevents processes from accessing more than one CPU core simultaneously.
- **[B]** The GIL is an application-level mutex in the Python runtime that enforces that only one native OS thread executes Python bytecode evaluation loop (`ceval.c`) at any given moment, causing CPU-bound threads to serialize and thrash context switches.
- **[C]** The GIL disables hardware interrupt steering on Intel Xeon processors when Python scripts exceed 100% CPU utilization.
- **[D]** The GIL forces all multithreaded calculations to use 32-bit single-precision floating point instead of 64-bit double precision.

---

#### Q03. How does the Intel oneAPI Data Analytics Library (oneDAL) bypass the CPython GIL when executing computationally heavy Machine Learning algorithms like K-Means or Random Forest?
- **[A]** It rewrites CPython source code dynamically using Cython before running the script.
- **[B]** It runs the entire Python script inside a privileged WebAssembly sandbox that ignores OS thread limits.
- **[C]** It receives contiguous C-order NumPy arrays via Python C-API bindings, releases the GIL using `Py_BEGIN_ALLOW_THREADS`, and delegates parallel computation to a native compiled C++ multi-threaded engine using OpenMP and AVX-512.
- **[D]** It converts standard Python loops into GPU CUDA kernels using an automatic translation layer.

---

#### Q04. Contrast a standard Python `list` of 1,000,000 floats with a 1D NumPy array `float64` of the same length in terms of memory layout and cache behavior.
- **[A]** A Python `list` stores 8MB of contiguous floats; a NumPy array stores 24MB of pointer references.
- **[B]** A Python `list` stores an array of 8-byte pointers pointing to separate `PyFloatObject` structs scattered across the heap (~24MB overhead + pointer chasing cache misses); a NumPy array stores a single contiguous 8,000,000-byte (8MB) raw binary buffer with zero pointer indirection.
- **[C]** Both have identical cache-line spatial locality, but NumPy uses zlib compression.
- **[D]** A Python `list` is allocated in CPU L1 cache, whereas a NumPy array is allocated directly on NVMe SSD storage.

---

#### Q05. What is the overarching design objective of the Intel oneAPI unified programming model across modern compute architectures?
- **[A]** To replace Linux with a custom real-time operating system optimized for Intel Core i9 processors.
- **[B]** To provide a cross-architecture, open standard programming model (SYCL / C++) allowing developers to write high-performance code that compiles and executes seamlessly across CPUs, GPUs, FPGAs, and AI accelerators without proprietary vendor lock-in.
- **[C]** To deprecate all Python data science libraries in favor of pure Fortran 95 compilers.
- **[D]** To convert all classical machine learning algorithms into deep transformer neural networks automatically.

---

#### Q06. When NumPy is built with the Intel Math Kernel Library (oneMKL) instead of standard reference Netlib BLAS, how does it optimize matrix multiplication ($C = A \times B$)?
- **[A]** It converts the matrices into sparse coordinate format and runs a single-threaded loop.
- **[B]** It breaks the matrices into cache-blocking sub-matrices that fit L1/L2/L3 cache hierarchies, applies multi-threaded OpenMP parallel loops across CPU cores, and utilizes FMA (Fused Multiply-Add) SIMD vector instructions.
- **[C]** It uploads the matrices to a remote Intel Cloud server via encrypted REST API calls.
- **[D]** It executes the matrix multiplication symbolically using computer algebra algorithms.

---

#### Q07. Which Python command allows an engineer to inspect whether the currently active NumPy installation is linked against Intel MKL BLAS and LAPACK?
- **[A]** `numpy.check_mkl_status()`
- **[B]** `numpy.__mkl_version__`
- **[C]** `numpy.show_config()`
- **[D]** `numpy.inspect_hardware_acceleration()`

---

#### Q08. In the Intel AI Analytics Toolkit ecosystem, which library provides drop-in acceleration specifically for tabular data preprocessing and feature transformations in Pandas?
- **[A]** Intel Distribution of Modin (with OmniSci / Ray / Dask backends)
- **[B]** Intel PyTorch Extension (IPEX)
- **[C]** Intel Neural Compressor (INC)
- **[D]** Intel MPI Library

---

#### Q09. Why does standard Scikit-learn (`sklearn`) written in pure Python and Cython frequently experience CPU core underutilization on dual-socket 64-core Intel Xeon servers?
- **[A]** Intel Xeon servers automatically throttle Python processes to preserve power.
- **[B]** Standard Scikit-learn relies primarily on `joblib` process-based parallelism (`multiprocessing`), which incurs massive IPC (Inter-Process Communication) and memory serialization overhead (`pickle`), leading to memory bloat and synchronization stalls.
- **[C]** Cython disables OpenMP multithreading whenever dataset features exceed 10.
- **[D]** Scikit-learn algorithms are hardcoded to never use more than 4 threads simultaneously.

---

#### Q10. What is the fundamental difference between Intel oneDAL and Intel oneDNN?
- **[A]** oneDAL accelerates Classical Machine Learning (clustering, regression, trees, dimensionality reduction); oneDNN accelerates Deep Neural Network primitives (convolutions, pooling, activations, normalization).
- **[B]** oneDAL is for ARM processors, while oneDNN is exclusively for Intel GPUs.
- **[C]** oneDAL requires proprietary hardware licenses, while oneDNN is an open-source Python script.
- **[D]** oneDAL only works with Python 2.7, while oneDNN requires Python 3.12+.

---

# 📌 SECTION B: Intel Extension for Scikit-learn (`sklearnex`) & Patching (Q11 – Q25)

#### Q11. What is the minimum code modification required to accelerate an existing Scikit-learn Python codebase using `scikit-learn-intelex`?
- **[A]** Rewrite all estimator classes to inherit from `IntelEstimatorBase`.
- **[B]** Add `from sklearnex import patch_sklearn; patch_sklearn()` at the entry point of the script before importing `sklearn`.
- **[C]** Recompile Scikit-learn from C++ source code using `icc` or `icx`.
- **[D]** Replace all `.fit()` calls with `.fit_accelerated()`.

---

#### Q12. Under the hood, what mechanism does `patch_sklearn()` utilize to replace standard Scikit-learn estimators with Intel-optimized oneDAL implementations?
- **[A]** Dynamic bytecode modification of the Python `.pyc` files on the local filesystem.
- **[B]** Runtime dynamic monkey-patching: modifying `sys.modules` and swapping the class references inside `sklearn.cluster`, `sklearn.ensemble`, etc., with oneDAL C++ wrapper subclasses.
- **[C]** Intercepting OS system calls using Linux `ptrace` and modifying CPU registers.
- **[D]** Launching a background daemon container running Intel Distribution for Python.

---

#### Q13. Suppose an engineer wants to accelerate ONLY the `KMeans` and `RandomForestClassifier` algorithms while keeping all other Scikit-learn algorithms unchanged. Which command achieves this?
- **[A]** `patch_sklearn(only=["KMeans", "RandomForestClassifier"])`
- **[B]** `patch_sklearn(name=["KMeans", "RandomForestClassifier"])`
- **[C]** `patch_sklearn(filter="KMeans|RandomForestClassifier")`
- **[D]** `sklearnex.enable_specific(["KMeans", "RandomForestClassifier"])`

---

#### Q14. If a script needs to compare the performance of accelerated Intel estimators against vanilla Scikit-learn in the SAME Python runtime session, which function restores original Scikit-learn estimators without restarting the kernel?
- **[A]** `sklearnex.reset_sklearn()`
- **[B]** `sklearnex.disable()`
- **[C]** `sklearnex.unpatch_sklearn()`
- **[D]** `sklearn.reload_original()`

---

#### Q15. How can an engineer accelerate an unmodified legacy Python script `train_pipeline.py` from the command line without editing a single line of Python source code?
- **[A]** `python -m sklearnex train_pipeline.py`
- **[B]** `python --enable-intel-mkl train_pipeline.py`
- **[C]** `intel-python train_pipeline.py`
- **[D]** `python -O3 train_pipeline.py`

---

#### Q16. Which of the following machine learning algorithms is NOT currently accelerated by Intel Extension for Scikit-learn (`sklearnex`)?
- **[A]** Support Vector Classifier (`SVC` / `SVR`)
- **[B]** Principal Component Analysis (`PCA`)
- **[C]** Random Forest Classifier & Regressor (`RandomForestClassifier` / `RandomForestRegressor`)
- **[D]** Gaussian Mixture Models with Variational Bayesian Estimation (`BayesianGaussianMixture`)

---

#### Q17. When an estimator or a specific hyperparameter configuration is NOT supported by Intel oneDAL, what does `sklearnex` do?
- **[A]** It raises a fatal `IntelAccelerationError` and crashes execution.
- **[B]** It silently executes garbage data calculations.
- **[C]** It gracefully falls back to the original stock Scikit-learn implementation without interrupting execution.
- **[D]** It skips the model training step and returns default zero predictions.

---

#### Q18. Which environment variable can an engineer set to enable verbose diagnostic messages that explicitly indicate whether an estimator ran on the Intel oneDAL accelerated engine or fell back to stock Scikit-learn?
- **[A]** `INTEL_DEBUG_LEVEL=3`
- **[B]** `SKLEARNEX_VERBOSE=INFO`
- **[C]** `ONEAPI_LOG_FALLBACKS=1`
- **[D]** `MKL_VERBOSE=1`

---

#### Q19. What mathematical and architectural optimization allows Intel oneDAL K-Means to achieve 15x–30x speedups over standard Scikit-learn on large datasets (e.g., 500,000 samples, 50 features)?
- **[A]** It replaces Lloyd's clustering algorithm with a single-pass random coin toss.
- **[B]** It optimizes Euclidean distance matrix calculation using AVX-512 vector dot-products, maintains cluster centroids in contiguous CPU cache, and parallelizes sample-to-cluster assignment across cores with zero memory copies.
- **[C]** It truncates 64-bit floating point numbers to 8-bit integers before clustering.
- **[D]** It runs K-Means on the hard drive using virtual swap memory.

---

#### Q20. In terms of numerical precision, how do the results (e.g., cluster inertia, classification accuracy, PCA explained variance ratio) of `sklearnex` compare to stock Scikit-learn?
- **[A]** They deviate by over 25% due to aggressive lossy approximations.
- **[B]** They maintain strict IEEE-754 numerical equivalence within standard floating-point roundoff tolerances (relative deviation $< 10^{-4}$ or statistically equivalent random convergence).
- **[C]** Accelerated models are always 50% less accurate because they skip convergence checks.
- **[D]** Results are identical only if the random seed is set to `None`.

---

#### Q21. Which method in `sklearnex` PCA provides the accelerated transformation of high-dimensional data into principal component space?
- **[A]** `pca.accelerated_transform(X)`
- **[B]** `pca.transform(X)` (the standard Scikit-learn API signature remains 100% identical)
- **[C]** `pca.onedal_project(X)`
- **[D]** `pca.fit_and_project_intel(X)`

---

#### Q22. When training a `RandomForestClassifier` on 1,000,000 samples with `n_estimators=100`, how does Intel oneDAL achieve superior tree-building throughput compared to standard Scikit-learn with `n_jobs=-1`?
- **[A]** It uses single-threaded recursion to avoid thread contention.
- **[B]** It constructs an in-memory histogram representation of features, parallelizes binning and split-finding across CPU execution units via OpenMP, and avoids Python thread serialization.
- **[C]** It limits the maximum tree depth to 3 regardless of user parameters.
- **[D]** It trains only 1 tree and duplicates its weights 99 times.

---

#### Q23. If `patch_sklearn()` is called AFTER Scikit-learn classes have already been imported directly (e.g., `from sklearn.cluster import KMeans; patch_sklearn()`), what happens to the imported `KMeans` class reference?
- **[A]** Python automatically retroactively updates the local namespace reference to the accelerated class.
- **[B]** The already-imported `KMeans` in the local namespace remains bound to stock Scikit-learn; only subsequent imports or `sklearn.cluster.KMeans` lookups receive the patch.
- **[C]** The Python runtime throws a `SyntaxError`.
- **[D]** Scikit-learn uninstalls itself from `site-packages`.

---

#### Q24. How does `sklearnex` handle sparse matrix inputs (such as `scipy.sparse.csr_matrix`) for algorithms where oneDAL currently requires dense contiguous memory?
- **[A]** It crashes with a `TypeError: Sparse matrices forbidden`.
- **[B]** It silently converts all sparse matrices to 100GB dense arrays, causing an Out-Of-Memory (OOM) error.
- **[C]** It detects the sparse input format and automatically falls back to stock Scikit-learn's sparse-optimized Cython backend.
- **[D]** It converts all non-zero values to 1.0.

---

#### Q25. Which of the following commands installs `scikit-learn-intelex` via `pip` with all required dependencies?
- **[A]** `pip install scikit-learn-intelex`
- **[B]** `pip install intel-sklearn-turbo`
- **[C]** `pip install onedal-python-accel`
- **[D]** `pip install intel-ai-core-ml`

---

# 📌 SECTION C: Hardware Vectorization, AVX-512 & OpenMP Tuning (Q26 – Q35)

#### Q26. What does SIMD stand for in modern CPU microarchitecture, and how does it relate to vectorization in numerical computing?
- **[A]** Single Instruction, Multiple Data: a CPU execution paradigm where a single machine instruction operates on multiple data points packed in a wide vector register simultaneously.
- **[B]** Shared Instruction, Multi-Core Direct: a network protocol for cluster computing.
- **[C]** Sequential Instruction, Memory Decoupled: an optimization for hard disk storage buffers.
- **[D]** Synchronous Interface, Managed Dispatch: a thread synchronization primitive in the Linux kernel.

---

#### Q27. How wide are the vector registers in Intel AVX-512, and how many 64-bit double-precision floating-point numbers (`float64`) can be processed in a single CPU clock cycle per register?
- **[A]** 128 bits wide; 2 `float64` elements
- **[B]** 256 bits wide; 4 `float64` elements
- **[C]** 512 bits wide; 8 `float64` elements
- **[D]** 1024 bits wide; 16 `float64` elements

---

#### Q28. Which CPU flag listed in `/proc/cpuinfo` (Linux) or reported by CPU telemetry tools indicates hardware support for Intel Advanced Vector Extensions 512 Foundation instructions?
- **[A]** `sse4_2`
- **[B]** `avx2`
- **[C]** `avx512f`
- **[D]** `fma4`

---

#### Q29. What is the impact of setting the environment variable `OMP_NUM_THREADS=4` before running a oneDAL or NumPy MKL accelerated script on an 8-core machine?
- **[A]** It restricts the underlying native OpenMP thread pool to use exactly 4 worker threads, bounding CPU utilization to 4 cores.
- **[B]** It forces the Python interpreter to launch 4 distinct background processes.
- **[C]** It splits the input dataset into 4 files on disk.
- **[D]** It limits the maximum RAM usage of the program to 4 Gigabytes.

---

#### Q30. Why can setting `OMP_NUM_THREADS` to a number higher than the physical CPU core count (e.g., 64 threads on an 8-core CPU with Hyperthreading) actually DEGRADE Machine Learning training performance?
- **[A]** CPU registers shrink in size when too many threads are launched.
- **[B]** Excessive thread count causes severe lock contention, thread context switching overhead, and cache-line thrashing (L1/L2 cache invalidations).
- **[C]** OpenMP automatically disables vectorization when thread count exceeds 16.
- **[D]** The operating system terminates Python for violating safety quotas.

---

#### Q31. What is the typical cache-line size on modern x86_64 Intel CPUs, and why is memory alignment to this boundary critical for high-throughput vectorized ML kernels?
- **[A]** 16 bytes; prevents register overflows.
- **[B]** 64 bytes; unaligned memory accesses that cross a 64-byte cache-line boundary require two separate memory read cycles and bus transactions instead of one.
- **[C]** 256 bytes; ensures PCIe bus compatibility.
- **[D]** 4096 bytes; matches the operating system virtual memory page size.

---

#### Q32. What phenomenon known as "False Sharing" occurs in multi-threaded parallel computing when multiple CPU cores modify independent variables located on the SAME cache line?
- **[A]** Cores share RAM data without using any CPU cache.
- **[B]** The hardware cache coherence protocol (e.g., MESI) forces continuous cache-line invalidation and bus broadcasting across cores, causing severe memory latency spikes despite independent program variables.
- **[C]** The CPU mispredicts branch instructions in the machine learning loop.
- **[D]** The operating system writes duplicate variables to the swap partition.

---

#### Q33. Which environment variable controls thread affinity and binding to physical CPU cores in Intel OpenMP runtime (`libiomp5`)?
- **[A]** `KMP_AFFINITY` (e.g., `KMP_AFFINITY=granularity=fine,compact,1,0`)
- **[B]** `INTEL_CORE_PIN=TRUE`
- **[C]** `CPU_SET_AFFINITY_BIND=1`
- **[D]** `MKL_THREAD_ATTACH=PHYSICAL`

---

#### Q34. When benchmarked on an Intel Xeon or Core i7/i9 processor, why does accelerated K-Means clustering speedup increase dramatically as the dataset grows from 1,000 samples to 500,000 samples?
- **[A]** Intel processors run slowly on small numbers due to clock speed ramping.
- **[B]** On small datasets, fixed overheads (library initialization, thread pool spawning, Python C-API transitions) dominate runtime; on large datasets, computational throughput ($O(N \cdot K \cdot D)$) completely amortizes startup overhead, allowing sustained AVX-512 SIMD vector saturation.
- **[C]** Small datasets are intentionally throttled by the software license.
- **[D]** Scikit-learn disables multithreading on datasets with more than 10,000 rows.

---

#### Q35. What is the role of FMA (Fused Multiply-Add) instructions supported in AVX2 and AVX-512 during machine learning operations such as matrix multiplications and distance calculations?
- **[A]** It performs multiplication and addition as two separate CPU instructions, saving electrical power.
- **[B]** It computes $(A \times B) + C$ in a single hardware clock cycle with a single rounding step, doubling floating-point peak throughput and reducing roundoff error accumulation.
- **[C]** It compresses floating point matrices into 8-bit integers before arithmetic operations.
- **[D]** It offloads arithmetic operations to the hard drive storage controller.

---

# 🔑 MASTER ANSWER KEY & FORENSIC TECHNICAL RATIONALES

---

### Section A: CPython Memory, Python GIL & oneAPI Architecture

#### Q01 — Correct Answer: [B]
- **Forensic Technical Rationale**: In standard CPython, integers and floats are NOT raw unboxed primitive values. A Python `float` is represented by the C struct `PyFloatObject`, which embeds `PyObject_HEAD`: an 8-byte reference count (`ob_refcnt`), an 8-byte pointer to the type object (`ob_type`), and finally the 8-byte IEEE-754 double (`ob_fval`). This means a single 8-byte number consumes 24 bytes on 64-bit systems. Furthermore, an array of Python floats in a standard `list` is actually an array of 64-bit pointers pointing to disparate heap locations. When the CPU attempts SIMD vectorization (which requires reading 64 contiguous bytes in a single bus cycle), pointer chasing forces random memory lookups, invalidating cache lines and crippling vector execution units.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because CPython floats are heap-boxed objects, not raw primitive double words.
  - `[C]` is wrong because floats are not stored in hash tables; small ints (-5 to 256) are interned, but floats are distinct heap structs.
  - `[D]` is wrong because standard floats are allocated via Python's `pymalloc` small-object allocator, not kernel `mmap()`.

#### Q02 — Correct Answer: [B]
- **Forensic Technical Rationale**: The Global Interpreter Lock is a mutual exclusion lock implemented in `Python/ceval_gil.h` and `ceval.c`. It exists to protect CPython's internal memory management and reference counting mechanisms (`ob_refcnt`) from race conditions. Because increments and decrements of `ob_refcnt` are not atomic on the C level for performance reasons, the GIL mandates that only one native thread executes bytecode at any time. When multiple native threads execute CPU-bound Python code, they enter a state of severe lock contention, repeatedly releasing and re-acquiring the GIL every 5 milliseconds (`sys.getswitchinterval()`), resulting in execution times that are frequently *slower* than single-threaded execution.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because the GIL is an application-level mutex inside the CPython userspace process, not an OS kernel semaphore.
  - `[C]` is wrong because the GIL does not manipulate physical CPU interrupt steering.
  - `[D]` is wrong because precision is completely independent of the GIL.

#### Q03 — Correct Answer: [C]
- **Forensic Technical Rationale**: Intel oneDAL interfaces with Python through optimized C++ Python extension modules (using pybind11 / C-API). When a method like `KMeans.fit(X)` is invoked, `sklearnex` verifies that `X` is a C-contiguous array (or converts it). The extension module immediately calls the CPython macro `Py_BEGIN_ALLOW_THREADS`, which releases the GIL mutex. At this point, the native C++ oneDAL engine takes complete control of the machine's CPU cores, spawning native OpenMP threads across all physical cores and executing AVX-512 SIMD assembly instructions. Once the calculations conclude, it acquires the GIL via `Py_END_ALLOW_THREADS` and returns the resulting centroids as standard NumPy arrays.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because oneDAL does not use runtime Cython transpilation.
  - `[B]` is wrong because WebAssembly is not involved in native Intel HPC acceleration.
  - `[D]` is wrong because oneDAL on CPU does not transpile to NVIDIA CUDA.

#### Q04 — Correct Answer: [B]
- **Forensic Technical Rationale**: In a Python `list` of 1,000,000 numbers, the list object itself is an array of 1,000,000 pointers (8MB on 64-bit OS). Each pointer references an independent 24-byte `PyFloatObject` on the heap (24MB total). Total memory footprint is ~32MB. Because the memory allocator places these objects in non-contiguous heap fragments, scanning through the list results in a cache miss on almost every element. In contrast, a 1D NumPy array `np.zeros(1_000_000, dtype=np.float64)` allocates a single 8,000,000-byte (7.63 MiB) contiguous block of virtual memory. When the CPU loads an address, the hardware prefetcher streams 64-byte cache lines (8 contiguous doubles per line) directly into L1d cache with maximum spatial locality.
- **Why Other Options Are Wrong**:
  - `[A]` is inverted.
  - `[C]` is wrong because spatial locality is drastically different and NumPy does not compress in-memory data with zlib.
  - `[D]` is completely nonsensical; both allocate in virtual RAM.

#### Q05 — Correct Answer: [B]
- **Forensic Technical Rationale**: Intel oneAPI is an open, standards-based unified programming model designed to eliminate the software silos of proprietary accelerators (such as vendor-locked GPU programming languages). Built upon Khronos Group SYCL (an abstraction layer for standard modern C++), oneAPI allows developers to target multi-architecture systems—CPUs, discrete GPUs (Intel Arc/Data Center GPU Max), FPGAs, and AI accelerators—using a common codebase and unified domain-specific libraries (oneDAL, oneMKL, oneDNN, oneCCL).
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because oneAPI runs on standard Linux (RHEL, Ubuntu, Rocky) and Windows, not a proprietary OS.
  - `[C]` is wrong because oneAPI embraces Python and C++, not obsolete Fortran replacement mandates.
  - `[D]` is wrong because oneAPI accelerates both classical ML and deep learning, without forcing model conversion.

#### Q06 — Correct Answer: [B]
- **Forensic Technical Rationale**: Intel MKL's DGEMM (Double-precision General Matrix Multiply) is widely regarded as one of the fastest mathematical routines in existence. Instead of naive triple-nested loops ($O(N^3)$), MKL decomposes matrices into blocks (cache blocking/tiling) sized specifically to match the L1d, L2, and L3 cache capacities of the detected CPU model. It aligns matrices to 64-byte boundaries, distributes blocks across threads via an optimized OpenMP runtime, and unrolls inner loops with AVX-512 FMA instructions, computing 32 double-precision floating-point operations per cycle per core.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because dense matrix multiplication does not convert to sparse formats.
  - `[C]` is wrong because all MKL calculations execute 100% locally on the host CPU.
  - `[D]` is wrong because MKL is a high-performance numerical linear algebra library, not a symbolic algebra solver.

#### Q07 — Correct Answer: [C]
- **Forensic Technical Rationale**: Running `np.show_config()` in Python prints the compiled linear algebra dependencies of the NumPy installation. If built against Intel MKL, the output contains `blas_mkl_info` and `lapack_mkl_info` blocks specifying `mkl_rt`, `mkl_intel_lp64`, and `mkl_core`. If linked against standard OpenBLAS or Netlib, it reflects `openblas64_info` or `blas_opt_info`.
- **Why Other Options Are Wrong**:
  - `[A]`, `[B]`, and `[D]` are fabricated functions and attributes that do not exist in the NumPy API.

#### Q08 — Correct Answer: [A]
- **Forensic Technical Rationale**: Intel Distribution of Modin accelerates Pandas workflows by distributing DataFrame operations across all available CPU cores. Standard Pandas is single-threaded; Modin splits DataFrames into partitioned matrices and executes data transformations, group-bys, and joins concurrently across cores using Ray, Dask, or Intel OmniSci backends.
- **Why Other Options Are Wrong**:
  - `[B]` (IPEX) is specifically designed for PyTorch deep learning models.
  - `[C]` (INC) is a quantization and model compression toolkit for neural networks.
  - `[D]` (Intel MPI) is for distributed multi-node cluster communication.

#### Q09 — Correct Answer: [B]
- **Forensic Technical Rationale**: Standard Scikit-learn's `n_jobs` parameter relies on `joblib`. Because the CPython GIL prevents true multi-threading in pure Python code, `joblib` defaults to spawning separate worker operating system processes via `multiprocessing`. Each process requires a separate memory space, duplicating data and incurring serialization/deserialization overhead (`pickle`) across inter-process pipes. On a 64-core machine, spawning 64 worker processes creates massive OS scheduling contention, memory bandwidth saturation, and IPC bottlenecking.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because CPUs do not throttle based on the programming language name.
  - `[C]` is wrong because Cython supports OpenMP `prange` loops; Scikit-learn's limitations stem from architectural design and algorithmic memory patterns.
  - `[D]` is wrong because `n_jobs` can be set to any arbitrary integer.

#### Q10 — Correct Answer: [A]
- **Forensic Technical Rationale**: In the oneAPI library hierarchy, Intel oneDAL (Data Analytics Library) focuses specifically on data analysis, statistical operations, and classical machine learning (K-Means, PCA, Random Forest, SVM, KNN, Ridge Regression). In contrast, Intel oneDNN (Deep Neural Network Library) provides optimized low-level building blocks for deep learning frameworks (TensorFlow, PyTorch, OpenVINO), focusing on multi-dimensional tensors, 2D/3D convolutions, pooling, batch normalization, and matrix multiplications.
- **Why Other Options Are Wrong**:
  - `[B]`, `[C]`, and `[D]` are factually false statements regarding platform support, licensing, and Python versions.

---

### Section B: Intel Extension for Scikit-learn (`sklearnex`) & Patching

#### Q11 — Correct Answer: [B]
- **Forensic Technical Rationale**: The elegance of `scikit-learn-intelex` lies in its zero-code-refactoring design. Adding `from sklearnex import patch_sklearn; patch_sklearn()` at the top of a script enables the extension globally. Any subsequent import of `from sklearn.cluster import KMeans` or instantiation of Scikit-learn models automatically uses the Intel oneDAL accelerated versions with identical API signatures.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because no class re-inheritance is required.
  - `[C]` is wrong because `sklearnex` is a pre-compiled binary wheel installed via `pip` or `conda`.
  - `[D]` is wrong because standard `.fit()` and `.predict()` methods are preserved exactly.

#### Q12 — Correct Answer: [B]
- **Forensic Technical Rationale**: When `patch_sklearn()` executes, it traverses the `sys.modules` dictionary in the Python runtime. For every accelerated estimator supported by oneDAL, it substitutes the module attribute in Scikit-learn's namespace (e.g., `sklearn.cluster.KMeans`) with a proxy class from `daal4py.sklearn` / `sklearnex`. This proxy class inherits from Scikit-learn's base estimator classes to maintain full `isinstance()` compatibility, while overriding internal execution methods to forward data pointers to the compiled oneDAL C++ engine.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because filesystem `.pyc` files are never altered.
  - `[C]` is wrong because `ptrace` is a Linux debugging syscall, not a Python patching mechanism.
  - `[D]` is wrong because no container or background daemon is spawned.

#### Q13 — Correct Answer: [B]
- **Forensic Technical Rationale**: `patch_sklearn()` accepts an optional parameter `name`, which accepts a list of string estimator names: `patch_sklearn(name=["KMeans", "RandomForestClassifier"])`. When provided, only those specific classes are monkey-patched, leaving all other Scikit-learn estimators in their original stock implementation.
- **Why Other Options Are Wrong**:
  - `[A]`, `[C]`, and `[D]` use invalid argument keywords (`only`, `filter`, `enable_specific`) that raise `TypeError`.

#### Q14 — Correct Answer: [C]
- **Forensic Technical Rationale**: The function `unpatch_sklearn()` reverses the modifications made by `patch_sklearn()`. It restores the original cached references in `sys.modules` back to vanilla Scikit-learn classes. This is critical for benchmarking scripts where an engineer needs to measure vanilla Scikit-learn runtime and Intel-accelerated runtime within the same execution script.
- **Why Other Options Are Wrong**:
  - `[A]`, `[B]`, and `[D]` are non-existent function names.

#### Q15 — Correct Answer: [A]
- **Forensic Technical Rationale**: Invoking Python with the `-m sklearnex` flag executes the `__main__.py` module of the `sklearnex` package before executing the target script. This module automatically executes `patch_sklearn()` in the runtime environment and then uses `runpy.run_path()` to execute `train_pipeline.py`. This enables seamless acceleration for legacy enterprise scripts without modifying source files.
- **Why Other Options Are Wrong**:
  - `[B]`, `[C]`, and `[D]` are invalid flags and commands for standard CPython.

#### Q16 — Correct Answer: [D]
- **Forensic Technical Rationale**: Intel oneDAL accelerates high-frequency classical algorithms: K-Means, DBSCAN, PCA, t-SNE, Linear/Ridge/Logistic Regression, Random Forest (Classifier/Regressor), Extra Trees, KNN, and SVM. Specialized statistical estimators like `BayesianGaussianMixture` (variational Bayesian inference) are not currently part of oneDAL's C++ kernel suite; if called, `sklearnex` transparently routes them to stock Scikit-learn.
- **Why Other Options Are Wrong**:
  - `[A]`, `[B]`, and `[C]` are prime flagship algorithms fully accelerated by oneDAL.

#### Q17 — Correct Answer: [C]
- **Forensic Technical Rationale**: Robustness is a core design principle of `sklearnex`. If an engineer instantiates an estimator with unsupported hyperparameters (for instance, an exotic loss function or penalty), `sklearnex` detects the incompatibility, logs a fallback notice if verbose mode is enabled, and seamlessly dispatches the data to the stock Scikit-learn Cython/Python backend. The code never crashes and never produces invalid outputs.
- **Why Other Options Are Wrong**:
  - `[A]`, `[B]`, and `[D]` violate Scikit-learn design invariants and do not reflect `sklearnex` behavior.

#### Q18 — Correct Answer: [B]
- **Forensic Technical Rationale**: Setting `export SKLEARNEX_VERBOSE=INFO` (or `DEBUG`) in the environment configures `sklearnex`'s runtime logger. When an estimator runs, it prints informative messages such as:  
  `[sklearnex] sklearn.cluster.KMeans.fit: accelerated implementation is used`  
  or  
  `[sklearnex] sklearn.ensemble.RandomForestClassifier.fit: fallback to original Scikit-learn (reason: unsupported criterion)`.
- **Why Other Options Are Wrong**:
  - `[A]`, `[C]`, and `[D]` are unrelated environment variables.

#### Q19 — Correct Answer: [B]
- **Forensic Technical Rationale**: In K-Means clustering, the primary computational bottleneck is computing the Euclidean distance matrix between $N$ data samples and $K$ cluster centroids ($O(N \cdot K \cdot D)$) across multiple iterations. Intel oneDAL reformulates distance calculations using vectorized dot products ($\|x - c\|^2 = \|x\|^2 + \|c\|^2 - 2\langle x, c\rangle$), vectorizes the inner products across 512-bit ZMM registers using AVX-512 FMA, parallelizes sample assignment over OpenMP threads, and updates centroids without heap allocations.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because Lloyd's mathematical algorithm is preserved exactly.
  - `[C]` is wrong because calculations remain full 64-bit or 32-bit floating point.
  - `[D]` is wrong because disk paging would destroy performance.

#### Q20 — Correct Answer: [B]
- **Forensic Technical Rationale**: `sklearnex` does not use lossy or heuristic approximations. It implements the exact mathematical formulations defined in the Scikit-learn documentation. Due to differences in floating-point summation order in parallel reductions (which is non-associative in IEEE-754 arithmetic: $(a+b)+c \neq a+(b+c)$), slight roundoff differences ($< 10^{-5}$) may occur, but cluster inertias, decision boundaries, and classification accuracies match stock Scikit-learn with rigorous statistical parity.
- **Why Other Options Are Wrong**:
  - `[A]` and `[C]` are incorrect because accuracy is strictly maintained.
  - `[D]` is wrong because reproducible seeds produce identical parity checks.

#### Q21 — Correct Answer: [B]
- **Forensic Technical Rationale**: Because `patch_sklearn()` adheres strictly to the Scikit-learn API standard, all method names, parameter names, and attribute names (`.fit()`, `.transform()`, `.fit_transform()`, `.predict()`, `.components_`, `.explained_variance_ratio_`) remain completely identical. Code written for Scikit-learn runs without changing a single method invocation.
- **Why Other Options Are Wrong**:
  - `[A]`, `[C]`, and `[D]` are fabricated method names that do not exist.

#### Q22 — Correct Answer: [B]
- **Forensic Technical Rationale**: In Random Forest construction, evaluating split points for continuous features across thousands of samples is the dominant cost. oneDAL uses high-speed feature binning into compact histograms. By evaluating split criteria over discrete bins rather than sorting raw floats repeatedly, and by parallelizing the histogram accumulation across CPU vector lanes and OpenMP threads, oneDAL constructs trees up to 10x–20x faster than standard Scikit-learn while maintaining identical classification metrics.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because oneDAL is intensely multi-threaded.
  - `[C]` is wrong because tree depth follows user parameters (`max_depth`).
  - `[D]` is wrong because all trees are independently trained according to bootstrap bagging rules.

#### Q23 — Correct Answer: [B]
- **Forensic Technical Rationale**: In Python's import system, `from sklearn.cluster import KMeans` binds the name `KMeans` in the local module's `globals()` dictionary directly to the existing class object. If `patch_sklearn()` is called afterwards, it modifies `sys.modules['sklearn.cluster'].KMeans`, but the local variable `KMeans` in your script still points to the old, unpatched class object. To ensure the patch takes effect, `patch_sklearn()` must be called BEFORE importing estimators, or the estimator must be referenced via `sklearn.cluster.KMeans`.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because Python never mutates already-bound local variable symbols retroactively.
  - `[C]` and `[D]` are completely incorrect.

#### Q24 — Correct Answer: [C]
- **Forensic Technical Rationale**: Sparse matrices have non-contiguous memory layouts (arrays of `data`, `indices`, and `indptr`). Certain oneDAL algorithmic kernels (such as Random Forest) require dense contiguous memory for cache-blocked vectorization. When passed a sparse matrix for an algorithm that does not have a native sparse oneDAL kernel, `sklearnex` detects the format and automatically routes execution to stock Scikit-learn's sparse Cython implementation.
- **Why Other Options Are Wrong**:
  - `[A]` is wrong because `sklearnex` avoids raising errors for valid Scikit-learn input types.
  - `[B]` is wrong because automatic densification of massive sparse matrices would exhaust RAM.
  - `[D]` is wrong because data values are never modified.

#### Q25 — Correct Answer: [A]
- **Forensic Technical Rationale**: The official PyPI package distribution name registered by Intel is `scikit-learn-intelex`. Installing it via `pip install scikit-learn-intelex` installs both the `sklearnex` package and the underlying `daal4py` binary wheel containing compiled Intel oneDAL shared libraries.
- **Why Other Options Are Wrong**:
  - `[B]`, `[C]`, and `[D]` are non-existent package names.

---

### Section C: Hardware Vectorization, AVX-512 & OpenMP Tuning

#### Q26 — Correct Answer: [A]
- **Forensic Technical Rationale**: SIMD (Single Instruction, Multiple Data) is a fundamental classification in Flynn's Taxonomy of computer architectures. In a scalar CPU instruction, adding two numbers requires fetching two registers, issuing an addition instruction, and storing one result. In SIMD computing, wide hardware registers (128-bit, 256-bit, or 512-bit) store multiple numbers side by side. A single vector instruction (e.g., `_mm512_add_pd`) instructs the arithmetic logic unit (ALU) to execute 8 independent additions simultaneously in a single clock cycle.
- **Why Other Options Are Wrong**:
  - `[B]`, `[C]`, and `[D]` are fabricated definitions.

#### Q27 — Correct Answer: [C]
- **Forensic Technical Rationale**: Intel AVX-512 introduces 32 architectural vector registers named `zmm0` through `zmm31`. Each ZMM register is 512 bits wide (64 bytes). Because an IEEE-754 double-precision float (`float64`) is 64 bits (8 bytes) in size:  
  $$\frac{512 \text{ bits}}{64 \text{ bits/element}} = 8 \text{ elements}$$  
  A single AVX-512 instruction can process 8 double-precision numbers or 16 single-precision (`float32`) numbers concurrently per clock cycle.
- **Why Other Options Are Wrong**:
  - `[A]` describes SSE (128-bit registers, 2 doubles).
  - `[B]` describes AVX / AVX2 (256-bit registers, 4 doubles).
  - `[D]` is speculative; 1024-bit registers are not implemented in standard x86 CPUs.

#### Q28 — Correct Answer: [C]
- **Forensic Technical Rationale**: In Linux, `/proc/cpuinfo` lists the hardware capability flags reported by the CPU `CPUID` instruction. The fundamental baseline instruction set for AVX-512 is the Foundation set, designated by the flag `avx512f`. Additional extensions include `avx512dq` (Doubleword & Quadword), `avx512cd` (Conflict Detection), `avx512bw` (Byte & Word), and `avx512vl` (Vector Length Extensions).
- **Why Other Options Are Wrong**:
  - `[A]` is SSE 4.2.
  - `[B]` is AVX2 (256-bit).
  - `[D]` is AMD's older FMA4 instruction set.

#### Q29 — Correct Answer: [A]
- **Forensic Technical Rationale**: The OpenMP runtime library (`libgomp` on GCC or `libiomp5` on Intel compilers) reads the standard environment variable `OMP_NUM_THREADS` during initialization. Setting `OMP_NUM_THREADS=4` instructs the runtime to instantiate a thread team of exactly 4 worker threads. When oneDAL parallel loops execute, the workload is partitioned across these 4 threads, leaving remaining CPU cores idle or available for other system processes.
- **Why Other Options Are Wrong**:
  - `[B]` is wrong because OpenMP uses lightweight OS threads within the same process, not separate processes.
  - `[C]` and `[D]` are completely unrelated to file partitioning or RAM ceilings.

#### Q30 — Correct Answer: [B]
- **Forensic Technical Rationale**: Thread oversubscription occurs when the number of active threads significantly exceeds the number of physical hardware execution pipelines. In high-performance numerical routines, threads actively poll and compute in tight loops. Spawning 64 threads on an 8-core CPU forces the operating system kernel scheduler to preempt threads every few milliseconds. Each preemption requires saving and restoring 32 512-bit ZMM registers, flushes the CPU pipeline, and evicts cache lines from L1/L2 caches. The resulting context switching storm and memory bus saturation causes overall runtime to degrade severely.
- **Why Other Options Are Wrong**:
  - `[A]` is physically impossible; registers are fixed hardware circuits.
  - `[C]` is wrong because vectorization operates inside each thread independently of thread counts.
  - `[D]` is wrong because oversubscription is a performance issue, not an OS quota violation.

#### Q31 — Correct Answer: [B]
- **Forensic Technical Rationale**: On modern x86_64 microarchitectures, the L1/L2 cache hierarchy transfers data to and from memory in fixed 64-byte blocks called cache lines. An 8-element `float64` AVX-512 vector is exactly 64 bytes ($8 \times 8 = 64$). If an array is aligned to a 64-byte boundary (address divisible by 64), loading the vector requires exactly ONE cache access. If the array is unaligned (e.g., offset by 8 bytes), the 64-byte vector spans across TWO consecutive cache lines, forcing the CPU to issue two separate memory read cycles, perform bitwise shifting, and assemble the vector, increasing load latency.
- **Why Other Options Are Wrong**:
  - `[A]` describes SSE register width, not modern cache-line size.
  - `[C]` and `[D]` are incorrect cache-line dimensions for x86_64 CPUs.

#### Q32 — Correct Answer: [B]
- **Forensic Technical Rationale**: In multi-core CPUs, cache coherence is maintained via protocols like MESI (Modified, Exclusive, Shared, Invalid). Even if Thread A on Core 0 modifies variable `x` and Thread B on Core 1 modifies variable `y`, if both `x` and `y` reside within the SAME 64-byte cache line, Core 0's write transitions the entire cache line to the `Modified` state. This automatically invalidates Core 1's copy of the line. When Core 1 attempts to write to `y`, it incurs a cache miss, forcing a bus read transaction to retrieve the updated line from Core 0. This cyclical ping-ponging of cache lines across the inter-core interconnect is called False Sharing and destroys parallel scaling.
- **Why Other Options Are Wrong**:
  - `[A]`, `[C]`, and `[D]` describe unrelated concepts.

#### Q33 — Correct Answer: [A]
- **Forensic Technical Rationale**: `KMP_AFFINITY` is Intel's proprietary environment variable for controlling thread affinity in the Intel OpenMP runtime library (`libiomp5`). It allows engineers to bind worker threads to specific hardware threads, physical cores, or NUMA sockets. For example, `KMP_AFFINITY=granularity=fine,compact,1,0` packs threads onto adjacent cores to maximize cache sharing, whereas `scatter` distributes threads evenly across sockets to maximize memory bandwidth.
- **Why Other Options Are Wrong**:
  - `[B]`, `[C]`, and `[D]` are fabricated variable names.

#### Q34 — Correct Answer: [B]
- **Forensic Technical Rationale**: Every high-performance computing abstraction incurs a non-zero fixed invocation cost (Python-to-C++ wrapper translation, OpenMP thread barrier synchronization, buffer verification). On a tiny dataset of 1,000 samples, total execution time in vanilla Scikit-learn might be only 5 milliseconds; the startup overhead of oneDAL may equal or exceed that time, resulting in modest speedup (1.5x–2x). However, on 500,000 samples, the computational workload scales to billions of operations. The fixed 5ms overhead becomes negligible (<0.1% of runtime), and the continuous $8\times$ AVX-512 SIMD vectorization and multi-core parallelization delivers raw hardware compute throughput, yielding massive 15x–30x speedups.
- **Why Other Options Are Wrong**:
  - `[A]`, `[C]`, and `[D]` are factually incorrect.

#### Q35 — Correct Answer: [B]
- **Forensic Technical Rationale**: Fused Multiply-Add (FMA) instructions compute $(A \times B) + C$ as an indivisible hardware operation. In traditional architectures, multiplying and adding requires two instructions: a `MUL` followed by an `ADD`, with intermediate rounding between them. FMA executes the calculation in a single hardware cycle with only a single final rounding step. This doubles the theoretical peak floating-point operations per second (FLOPS) of each CPU core (e.g., 2 FMA units $\times$ 8 doubles $\times$ 2 operations = 32 FLOPS/cycle per core) while reducing mathematical truncation error in inner products.
- **Why Other Options Are Wrong**:
  - `[A]` is the opposite of FMA.
  - `[C]` describes quantization, not FMA.
  - `[D]` is completely nonsensical.

---

```
========================================================================================
                      END OF DAY 02 EVALUATED ASSESSMENT BANK
          GLA University Masterclass in High Performance Computing & Intel oneAPI
========================================================================================
```
