# 🎯 DAY 3 HPC QUIZ: MASTER ANSWER KEY & ARCHITECTURAL EXPLANATIONS
## Comprehensive Evaluated Question Guide for HPC Practitioners & Students
### Focus Areas: Slurm Workload Manager • Intel oneDNN & AMX • Habana Gaudi • Distributed Horovod

---

## 📊 Summary Assessment Matrix

| Question | Cognitive Tier | Syllabus Topic | Correct Option | Summary Key Takeaway |
|:---:|:---|:---|:---:|:---|
| **Q1** | Level 1: Foundational | Slurm Workload Manager | **B** | Slurm arbitrates multi-tenant node, CPU, memory, and GPU allocation. |
| **Q2** | Level 1: Foundational | HPC Policy & Access | **B** | Login node execution exhausts shared RAM/CPU and freezes access for all users. |
| **Q3** | Level 1: Foundational | Intel oneDNN Activation | **B** | TF_ENABLE_ONEDNN_OPTS=1 activates oneDNN AVX-512 and AMX JIT primitives. |
| **Q4** | Level 1: Foundational | Slurm Script Directives | **B** | #SBATCH --time=HH:MM:SS enforces maximum wall-clock runtime limit. |
| **Q5** | Level 1: Foundational | Slurm Queue States | **B** | PENDING (PD) indicates waiting in queue for compute resources. |
| **Q6** | Level 2: Conceptual | oneDNN Operator Fusion | **B** | Fuses Conv2D+BatchNorm+ReLU into cache to avoid slow DDR5 round-trips. |
| **Q7** | Level 2: Conceptual | Distributed Learning Rate | **B** | Linear Scaling Rule: scale {\\text{new}} = lr_{\\text{base}} \\times K$ as global batch expands. |
| **Q8** | Level 2: Conceptual | Slurm Job Substitution | **B** | %j dynamically substitutes unique numeric Slurm Job ID in log filenames. |
| **Q9** | Level 2: Conceptual | Slurm Compute Daemons | **B** | slurmd runs on compute nodes; slurmctld runs centrally on head node. |
| **Q10** | Level 2: Conceptual | Horovod Gradient Sync | **B** | hvd.DistributedOptimizer() wraps standard optimizer to execute Ring-AllReduce. |
| **Q11** | Level 3: Systems & Math | Ring-AllReduce Scaling | **B** | Ring communication volume is constant:  \\frac{N-1}{N} S \\to 2S$ as  \\to \\infty$. |
| **Q12** | Level 3: Systems & Math | Habana Gaudi Networking | **B** | 24 on-die 100/200 GbE RoCEv2 RDMA ports eliminate external PCIe NIC bottlenecks. |
| **Q13** | Level 3: Systems & Math | Intel Xeon AMX Silicon | **B** | 8 2D Tile registers (TMM0-TMM7) + TMUL systolic array (2,048 INT8 ops/cycle). |
| **Q14** | Level 3: Systems & Math | Slurm Parallel Launcher | **B** | srun connects to daemons to bind tasks across allocated nodes and cgroups. |
| **Q15** | Level 3: Systems & Math | Horovod Checkpointing | **B** | Restricting checkpoints to if hvd.rank() == 0: prevents disk race conditions. |

---

## 🏛️ Comprehensive Option-Wise Breakdown & Architectural Rationale

### Q1. What is the primary role of the Slurm workload manager in an HPC cluster?
- **Cognitive Level:** Level 1: Foundational
- **Topic:** Slurm Workload Manager
- **Options:**
  - **A)** Designing neural network layer connections
  - **B) [CORRECT] Managing multi-tenant cluster resource allocation, queueing, and job dispatching across compute nodes**
  - **C)** Compiling Python into machine assembly
  - **D)** Encrypting local hard drives
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** Slurm (Simple Linux Utility for Resource Management) is the industry-standard cluster workload manager. In high-performance supercomputers, compute nodes (CPUs, GPUs, high-speed RAM, interconnects) are shared across hundreds or thousands of researchers. Slurm performs three fundamental responsibilities: (1) arbitrating access to compute nodes to eliminate resource contention; (2) providing a framework for starting, executing, and monitoring batch jobs (sbatch) and interactive tasks (srun); and (3) enforcing fair-share policies, priority queues, and accounting.
  - **Why Options A, C, and D are Incorrect:**
    - Option A describes deep learning modeling frameworks (TensorFlow, PyTorch, Keras).
    - Option C describes JIT compilers (Numba, LLVM, PyPy).
    - Option D describes filesystem encryption tools (LUKS, dm-crypt).

---

### Q2. Why is running heavy deep learning training jobs directly on the cluster login/head node strictly prohibited?
- **Cognitive Level:** Level 1: Foundational
- **Topic:** HPC Policy & Cluster Access
- **Options:**
  - **A)** Because the login node has no operating system installed
  - **B) [CORRECT] Because it exhausts shared CPU/RAM, freezing terminal access for the entire institution**
  - **C)** Because TensorFlow cannot run on Linux servers
  - **D)** Because Python is disabled on login nodes
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** The head/login node is an interactive gateway node intended strictly for administrative tasks: editing code, inspecting job status (squeue), and submitting scripts to Slurm (sbatch). Because all users SSH into this single shared host, running memory-intensive or multi-threaded training jobs consumes all CPU cores, triggers the Linux Out-Of-Memory (OOM) killer, exhausts RAM, and locks SSH daemons, completely freezing terminal sessions for the entire institution. Heavy computation must always be dispatched to isolated compute nodes via Slurm.
  - **Why Options A, C, and D are Incorrect:**
    - Option A is physically false; the login node runs enterprise Linux (e.g., RHEL, Rocky Linux, Ubuntu).
    - Option C is false; Linux is the primary OS for TensorFlow and supercomputing.
    - Option D is false; Python is installed on login nodes to enable scripting and environment management.

---

### Q3. Which environment variable activates Intel oneDNN optimizations in standard TensorFlow?
- **Cognitive Level:** Level 1: Foundational
- **Topic:** Intel oneDNN Activation
- **Options:**
  - **A)** TF_GPU_ALLOCATOR=cuda
  - **B) [CORRECT] TF_ENABLE_ONEDNN_OPTS=1**
  - **C)** USE_MKL=true
  - **D)** INTEL_FAST_MODE=1
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** Since TensorFlow v2.9+, Intel oneDNN (oneAPI Deep Neural Network Library) primitives are compiled into the official upstream binary packages. Setting the environment variable export TF_ENABLE_ONEDNN_OPTS=1 tells the TensorFlow graph execution engine to replace generic Eigen C++ operator kernels with oneDNN hardware-optimized kernels. This enables JIT-compiled AVX-512 vector code, AMX matrix operations, and operator fusion.
  - **Why Options A, C, and D are Incorrect:**
    - Option A (TF_GPU_ALLOCATOR=cuda) configures NVIDIA CUDA memory allocators.
    - Options C and D (USE_MKL=true, INTEL_FAST_MODE=1) are non-existent variables in the TensorFlow runtime.

---

### Q4. What does the '#SBATCH --time=01:30:00' directive specify in a job submission script?
- **Cognitive Level:** Level 1: Foundational
- **Topic:** Slurm Script Directives
- **Options:**
  - **A)** The scheduled start time of the job (1:30 AM)
  - **B) [CORRECT] The maximum wall-clock runtime limit (1 hour, 30 minutes) before the job is terminated by Slurm**
  - **C)** The date of training completion
  - **D)** The user's SSH session timeout
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** #SBATCH --time=01:30:00 sets the maximum allowable elapsed wall-clock duration (HH:MM:SS) for the allocation. If the process does not terminate within 1 hour and 30 minutes, the slurmctld controller issues a SIGXCPU signal followed by SIGKILL, releasing the compute resources. Defining accurate walltimes allows the Slurm backfill scheduling algorithm to slip short jobs into temporary reservation gaps, significantly reducing queue wait times.
  - **Why Options A, C, and D are Incorrect:**
    - Option A is specified by #SBATCH --begin=YYYY-MM-DD[THH:MM:SS].
    - Options C and D are not controlled by the --time flag.

---

### Q5. What state is reported by 'squeue' when a job is waiting for compute nodes to become available?
- **Cognitive Level:** Level 1: Foundational
- **Topic:** Slurm Queue States
- **Options:**
  - **A)** RUNNING (R)
  - **B) [CORRECT] PENDING (PD)**
  - **C)** FAILED (F)
  - **D)** COMPLETED (CD)
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** In Slurm job lifecycle monitoring:
    - PD (PENDING): The job has been parsed, queued, and is awaiting resource availability (e.g., Reason=Resources or Reason=Priority).
    - R (RUNNING): The job is actively allocated nodes and executing processes.
    - F (FAILED): The job terminated with a non-zero exit code or hardware fault.
    - CD (COMPLETED): The job completed execution successfully across all allocated tasks.
  - **Why Options A, C, and D are Incorrect:** A indicates active execution, C indicates failure, and D indicates finished execution.

---

### Q6. What is 'Operator Fusion' in deep learning acceleration libraries like oneDNN?
- **Cognitive Level:** Level 2: Conceptual
- **Topic:** Intel oneDNN Architecture & Memory Hierarchy
- **Options:**
  - **A)** Merging two separate neural networks into one
  - **B) [CORRECT] Fusing consecutive operations (e.g., Conv2D + BatchNorm + ReLU) into a single pass through cache memory to avoid slow DRAM round-trips**
  - **C)** Joining two Python strings in memory
  - **D)** Merging two dataset CSV files on disk
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** Modern CPU and GPU deep learning performance is governed by the Roofline Model and memory bandwidth limits. In standard un-fused execution, a convolutional block operates as:
    1. Conv2D: Reads input from DRAM, computes convolution, writes feature maps back to DDR5 DRAM (~80ns latency).
    2. BatchNorm: Reads intermediate feature maps from DDR5 DRAM, scales/shifts, writes back to DDR5 DRAM.
    3. ReLU: Reads from DDR5 DRAM, applies activation threshold, writes back to DDR5 DRAM.
    Each intermediate DRAM round-trip saturates memory bus channels. oneDNN Operator Fusion generates JIT machine code that keeps the intermediate tensor resident in ultra-fast L1/L2 CPU cache registers. The hardware executes Conv2D $\to$ BatchNorm $\to$ ReLU in a single streaming compute sweep, reducing memory bus traffic by up to 75% and dramatically boosting throughput.
  - **Why Options A, C, and D are Incorrect:**
    - Option A describes ensemble modeling or multi-task learning.
    - Options C and D describe basic string concatenation and file I/O operations.

---

### Q7. When scaling from 1 node to 4 nodes with Horovod, why must the learning rate typically be scaled?
- **Cognitive Level:** Level 2: Conceptual
- **Topic:** Distributed Deep Learning Mathematics
- **Options:**
  - **A)** Because the learning rate automatically halves in multi-node mode
  - **B) [CORRECT] Because the effective global batch size is multiplied by 4, requiring proportionally larger gradient steps (Linear Scaling Rule)**
  - **C)** Because the CPU runs 4x colder
  - **D)** It should never be changed
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** In synchronous data-parallel distributed training (Horovod), each worker processes a local mini-batch of size $. When training across =4$ workers, the effective global batch size per optimization step is {\\text{global}} = 4 \\times B$. Because 4 mini-batches are aggregated via Ring-AllReduce into a single gradient step, the variance of the gradient estimator is reduced by a factor of 4. According to the Linear Scaling Rule (Goyal et al., 2017):
    \\eta_{\\text{new}} = \\eta_{\\text{base}} \\times K
    To take larger, confident steps along the optimization surface corresponding to the 4x larger sample size, the learning rate must be multiplied by 4. In practice, a gradual warm-up phase (e.g., over 5 epochs) is paired with this rule to prevent divergence during early training steps.
  - **Why Options A, C, and D are Incorrect:**
    - Option A is mathematically opposite of empirical training requirements.
    - Option C is physically irrelevant.
    - Option D leads to severe under-fitting and dramatically slower convergence.

---

### Q8. What does the '%j' placeholder represent in '#SBATCH --output=logs/job_%j.out'?
- **Cognitive Level:** Level 2: Conceptual
- **Topic:** Slurm Scripting Directives
- **Options:**
  - **A)** The job name
  - **B) [CORRECT] The unique numeric Slurm Job ID allocated by the controller**
  - **C)** The user's username
  - **D)** The submission timestamp
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** In Slurm submission scripts, %j is the dynamic replacement symbol for the unique numeric Job ID assigned by slurmctld (e.g., job_10482.out). Using %j guarantees that consecutive or concurrent job executions never overwrite each other's log outputs.
  - **Why Options A, C, and D are Incorrect:**
    - %x represents the Job Name.
    - %u represents the Username.
    - Timestamps are not standard Slurm replacement macros for filename patterns.

---

### Q9. Which daemon runs on each individual compute/worker node in a Slurm cluster?
- **Cognitive Level:** Level 2: Conceptual
- **Topic:** Slurm Cluster Architecture & Daemons
- **Options:**
  - **A)** slurmctld
  - **B) [CORRECT] slurmd**
  - **C)** systemd only
  - **D)** sshd only
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** Slurm uses a distributed master-worker architecture:
    - slurmd: The node supervisor daemon running locally on every compute node. It listens for instructions from slurmctld, provisions process execution via Linux cgroups (CPU, RAM, GPU constraints), manages process cleanup, and reports hardware node telemetry (cores, load, free memory) back to the head node.
    - slurmctld: The central management controller running on the master/head node that manages queues, partitions, and schedules allocations.
    - slurmdbd: The database daemon interfacing with MariaDB/MySQL for persistent job accounting.
  - **Why Options A, C, and D are Incorrect:**
    - Option A (slurmctld) runs exclusively on the controller node.
    - Options C and D (systemd, sshd) are general Linux system utilities, not the Slurm node daemon.

---

### Q10. In TensorFlow, how does Horovod distribute gradient updates across workers?
- **Cognitive Level:** Level 2: Conceptual
- **Topic:** Horovod Framework Architecture
- **Options:**
  - **A)** By uploading gradients to Google Drive
  - **B) [CORRECT] By wrapping the standard Keras/TF optimizer with hvd.DistributedOptimizer()**
  - **C)** By writing gradients to text files on the login node
  - **D)** By running independent training loops without synchronization
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** Horovod uses the Decorator Pattern to integrate with TensorFlow. By wrapping the optimizer:
    `python
    optimizer = hvd.DistributedOptimizer(tf.keras.optimizers.Adam(learning_rate=0.001 * hvd.size()))
    `
    Horovod intercepts the gradient computation step (pply_gradients()). During the backward pass, each worker computes local loss gradients. Before updating weights, hvd.DistributedOptimizer() executes an in-memory Ring-AllReduce collective across all workers (via NCCL or MPI). Once the exact global average gradients are resolved, each worker independently updates its local weights, guaranteeing mathematical synchronization without central parameter bottlenecks.
  - **Why Options A, C, and D are Incorrect:**
    - Options A and C are fictitious and introduce catastrophic filesystem latencies.
    - Option D describes independent un-synchronized models that never converge to a shared model.

---

### Q11. In the Ring-AllReduce algorithm used by Horovod, how does communication volume per worker scale with cluster size N?
- **Cognitive Level:** Level 3: Systems & Math
- **Topic:** Ring-AllReduce Communication Complexity
- **Options:**
  - **A)** It increases exponentially (O(2^N))
  - **B) [CORRECT] It is largely constant and independent of N, scaling as 2 * ((N-1)/N) * S bytes**
  - **C)** It drops to zero instantly
  - **D)** It requires a central parameter server to store all weights
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** Traditional Parameter Server architectures create a centralized network bottleneck where communication volume on the parameter server scales as (N \times S)$, throttling performance. Ring-AllReduce (patented in Baidu Research's work by Gibiansky) eliminates this bottleneck by arranging $ nodes in a logical ring. Given total gradient tensor size $ bytes split into $ equal chunks:
    1. **Scatter-Reduce Phase:** Requires -1$ communication rounds. In each round, each worker transmits $\\frac{S}{N}$ bytes to its right-hand neighbor and receives $\\frac{S}{N}$ bytes from its left-hand neighbor, summing incoming gradients. Total transmitted:
       T_{\\text{scatter}} = (N-1) \\times \\frac{S}{N} = \\frac{N-1}{N} S
    2. **AllGather Phase:** Requires another -1$ rounds to circulate the fully reduced chunks. Total transmitted:
       T_{\\text{gather}} = (N-1) \\times \\frac{S}{N} = \\frac{N-1}{N} S
    3. **Total Data Transferred per Worker:**
       T_{\\text{total}} = 2 \\cdot \\left(\\frac{N-1}{N}\\right) \\cdot S
    As the cluster scales to infinity ( \\to \\infty$), the term $\\frac{N-1}{N} \\to 1$. Thus, the total volume of data transmitted per worker asymptotically approaches $, completely independent of cluster scale $!
  - **Why Options A, C, and D are Incorrect:**
    - Option A ((2^N)$) is false; tree or ring topologies are sub-exponential.
    - Option C is physically impossible.
    - Option D describes legacy Parameter Server architectures, which Ring-AllReduce explicitly eliminates.

---

### Q12. Which architectural feature enables Habana Gaudi 2/3 to eradicate cluster networking bottlenecks?
- **Cognitive Level:** Level 3: Systems & Math
- **Topic:** Habana Gaudi Silicon Architecture
- **Options:**
  - **A)** A cooling fan attached to the CPU
  - **B) [CORRECT] 24 integrated 100/200 GbE RoCEv2 RDMA ports directly on the silicon die**
  - **C)** A USB-C connection cable
  - **D)** Integrated Wi-Fi 6
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** In conventional GPU clusters, scale-out networking requires dedicated PCIe network cards (e.g. InfiniBand or Ethernet NICs) routing through PCIe switches and motherboard traces. Habana Gaudi (Gaudi 2 and Gaudi 3) eliminates PCIe bottlenecks by integrating **24 on-die RDMA engines supporting 100/200 Gigabit Ethernet RoCEv2** directly onto the accelerator silicon:
    - 21 ports are dedicated to an all-to-all direct mesh interconnecting all 8 Gaudi cards within a single 8-OAM server chassis without any external network switches.
    - The remaining 3 ports per card (24 ports total per server) provide direct optical breakout for inter-chassis node-to-node scaling.
    This architecture provides standard Ethernet interoperability, eliminates costly proprietary switches, and bypasses PCIe bus saturation.
  - **Why Options A, C, and D are Incorrect:**
    - Option A describes basic thermal management.
    - Options C and D are consumer desktop interfaces incapable of datacenter terabit bandwidth.

---

### Q13. What silicon capability allows 4th/5th Gen Intel Xeon processors to achieve 2,048 INT8 ops/cycle?
- **Cognitive Level:** Level 3: Systems & Math
- **Topic:** Intel Xeon AMX (Advanced Matrix Extensions)
- **Options:**
  - **A)** Overclocking the system bus
  - **B) [CORRECT] Intel AMX (Advanced Matrix Extensions) with 8 2D Tile registers (TMM0-TMM7) and TMUL systolic array**
  - **C)** Increasing DDR5 RAM size
  - **D)** Disabling hyper-threading
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** Intel AMX (Advanced Matrix Extensions) is a dedicated on-die matrix math acceleration engine introduced in 4th Gen Intel Xeon Scalable processors (Sapphire Rapids) and refined in 5th Gen (Emerald Rapids). AMX architecture comprises:
    1. **2D Tile Registers (TMM0–TMM7):** 8 physical registers capable of holding two-dimensional sub-matrices (up to 16 rows by 64 bytes wide, totaling 1 KB per tile and 8 KB overall).
    2. **TMUL (Tile Matrix Multiply Unit):** A hardware systolic array attached to the tile registers. In each clock cycle, TMUL computes matrix dot products:
       - 2,048 INT8 operations per cycle per core (32-wide by 16-high multiply-accumulate).
       - 1,024 Bfloat16 (BF16) operations per cycle per core.
    This provides an 8x compute throughput speedup compared to prior-generation AVX-512 VNNI instructions, allowing enterprise servers to train and serve deep learning models directly on CPUs.
  - **Why Options A, C, and D are Incorrect:**
    - Option A produces minimal clock gains (~5-10%) and violates datacenter stability.
    - Option C increases memory capacity, not instruction-level compute throughput.
    - Option D manages logical core scheduling without altering execution unit width.

---

### Q14. How should an interactive parallel multi-task job be launched inside a Slurm allocation?
- **Cognitive Level:** Level 3: Systems & Math
- **Topic:** Slurm Execution Primitives
- **Options:**
  - **A)** bash script.sh
  - **B) [CORRECT] srun python3 app.py**
  - **C)** python3 app.py &
  - **D)** nohup python3 app.py
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** While sbatch submits asynchronous batch scripts and salloc reserves cluster resources, srun is the official Slurm job step launcher. Executing srun python3 app.py communicates directly with slurmctld and the worker node slurmd daemons. srun provisions parallel task instances across all requested nodes and sockets, attaches process tracking to Linux cgroups, manages core pinning and NUMA affinity, configures process communication interfaces (PMIx/PMI2), and pipes standard I/O streams back to the user's terminal in real time.
  - **Why Options A, C, and D are Incorrect:**
    - ash, &, and 
ohup are generic shell commands that bypass Slurm's process supervisor. They execute solely on the primary node as unconstrained OS processes without task orchestration or multi-node distribution.

---

### Q15. When training with Horovod, which worker rank is typically responsible for saving checkpoints and writing logs?
- **Cognitive Level:** Level 3: Systems & Math
- **Topic:** Distributed Deep Learning Best Practices
- **Options:**
  - **A)** All workers simultaneously
  - **B) [CORRECT] Rank 0 (Master worker) only, guarded by 'if hvd.rank() == 0:'**
  - **C)** The highest rank worker only
  - **D)** A random worker chosen each epoch
- **Detailed Technical Explanation:**
  - **Why Option B is Correct:** In data-parallel distributed training, all workers maintain bit-identical copies of neural network parameters at the end of each training step because gradients are synchronized via Ring-AllReduce. If all worker processes simultaneously attempt to serialize weights to a shared filesystem (NFS, Lustre, GPFS) or write metrics to TensorBoard, they trigger:
    1. File write race conditions and lock collisions.
    2. Severe I/O bandwidth degradation on the cluster storage fabric.
    3. Checkpoint corruption.
    Therefore, best practices mandate guarding all disk write and reporting operations with if hvd.rank() == 0:. Non-zero ranks focus purely on forward, backward, and all-reduce computation.
  - **Why Options A, C, and D are Incorrect:**
    - Option A leads to file corruption and NFS lock crashes.
    - Option C is non-standard and complicates orchestration.
    - Option D introduces non-deterministic checkpoint ownership and missing weights.

---
