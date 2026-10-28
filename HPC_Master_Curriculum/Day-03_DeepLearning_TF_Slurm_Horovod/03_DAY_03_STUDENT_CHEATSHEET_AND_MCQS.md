# 📝 DAY 3: STUDENT QUICK REFERENCE & OFFICIAL MCQ BANK
## 1-Page Cheat Sheet + 25 Evaluated Assessment Questions
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 📌 PART 1: 1-Page Student Command & Slurm Cheat Sheet

> [!TIP]
> ### ⚡ 2-MINUTE INSTANT-RECALL MASTERY BOX (80-90% IMMEDIATE KNOWLEDGE)
> * **oneDNN Operator Fusion:** Fuses `Conv2D + BatchNorm + ReLU` inside CPU cache, eliminating intermediate DRAM memory traffic (2x-3.5x speedup).
> * **Slurm Architecture:** `slurmctld` (controller on login node) schedules jobs to `slurmd` (worker daemons on compute nodes) using `#SBATCH` directives.
> * **Ring-AllReduce Scaling:** Decentralized ring communication sends $2 \cdot \frac{N - 1}{N} \cdot S$ bytes per worker, eliminating central Parameter Server network bottlenecks.
> * **Top 5 Life-Saving Code Snippets:**
>   1. `export TF_ENABLE_ONEDNN_OPTS=1` (Force-enable Intel oneDNN hardware operator acceleration)
>   2. `sbatch --partition=gpu-intel --nodes=2 job.sh` (Submit distributed batch training job to Slurm queue)
>   3. `squeue -u $USER && scancel <job_id>` (Monitor active jobs and kill runaway processes)
>   4. `hvd.init() && opt = hvd.DistributedOptimizer(opt)` (Wrap TensorFlow optimizer for multi-worker ring synchronization)
>   5. `hvd.callbacks.BroadcastGlobalVariablesHook(0)` (Synchronize initial weights from Rank 0 to all workers to prevent deadlock)

### 1. Essential Slurm Commands
| Command | What It Does | Example |
| :--- | :--- | :--- |
| `sbatch <script.sh>` | Submits non-interactive batch script to queue | `sbatch train.sh` |
| `squeue -u $USER` | Displays currently running and pending jobs | `squeue -u shivam` |
| `scancel <job_id>` | Terminates/cancels a running or queued job | `scancel 10452` |
| `sinfo` | Displays cluster node partitions and node states | `sinfo` |
| `srun <command>` | Spawns parallel tasks interactively across nodes | `srun -n 4 python3 app.py` |

### 2. Core `#SBATCH` Script Directives
```bash
#SBATCH --job-name=my_job         # Human-readable job identifier
#SBATCH --output=logs/%x_%j.out   # Standard output log (%x=job name, %j=job ID)
#SBATCH --error=logs/%x_%j.err    # Standard error log
#SBATCH --nodes=2                 # Number of discrete physical compute nodes
#SBATCH --ntasks-per-node=4       # Number of MPI/process tasks per node
#SBATCH --cpus-per-task=8         # Number of CPU threads per task
#SBATCH --time=02:00:00           # Hard runtime limit (HH:MM:SS)
#SBATCH --partition=gpu-intel     # Specific target hardware partition
```

### 3. Horovod Ring-Allreduce Integration
```python
import horovod.tensorflow as hvd
hvd.init()
# Scale learning rate by number of cluster ranks:
opt = tf.optimizers.Adam(lr * hvd.size())
# Wrap optimizer for decentralized ring synchronization:
opt = hvd.DistributedOptimizer(opt)
```

---

## 🎯 PART 2: Day 3 Official Syllabus Checklist

- [ ] 01. Deep Learning workflows on HPC systems
- [ ] 02. Hardware-aware ML optimization principles
- [ ] 03. Intel-optimized TensorFlow (`tensorflow-mkl`, `oneDNN`)
- [ ] 04. Operator fusion (Conv + Bias + ReLU in cache lines)
- [ ] 05. Deploying DL models on Intel Xeon CPUs and Habana Gaudi
- [ ] 06. Slurm architecture: `slurmctld` (controller) and `slurmd` (worker)
- [ ] 07. Login node vs Compute node execution policies
- [ ] 08. Writing robust `#SBATCH` batch submission scripts
- [ ] 09. Job monitoring via `squeue` and cancellation via `scancel`
- [ ] 10. The distributed training communication bottleneck
- [ ] 11. Parameter Server architecture vs Ring-Allreduce algorithm
- [ ] 12. Horovod distributed framework concepts and wrappers

---

## 📝 PART 3: 25 Official Multiple-Choice Questions (With Answers & Explanations)

#### Q1. What is the primary role of the Slurm workload manager in an HPC cluster?
- A) Designing neural network architectures
- B) Managing multi-tenant cluster resource allocation, queueing, and job dispatching across compute nodes
- C) Compiling Python into HTML
- D) Encrypting local hard drives  
**Answer: B** | *Explanation: Slurm allocates compute resources (nodes, cores, GPUs) fairly among users and executes submitted batch jobs.*

#### Q2. Why is running heavy deep learning training jobs directly on the cluster login/head node strictly prohibited?
- A) Because the login node has no operating system
- B) Because it exhausts CPU/RAM shared by all users, degrading responsiveness or crashing the access gateway for the entire institution
- C) Because TensorFlow cannot run on Linux
- D) Because Python is disabled on login nodes  
**Answer: B** | *Explanation: The login node is a shared resource for light tasks; compute-heavy jobs must be scheduled onto worker nodes via Slurm.*

#### Q3. Which environment variable activates Intel oneDNN optimizations in standard TensorFlow?
- A) `TF_GPU_ALLOCATOR=cuda`
- B) `TF_ENABLE_ONEDNN_OPTS=1`
- C) `USE_MKL=true`
- D) `INTEL_FAST_MODE=1`  
**Answer: B** | *Explanation: Setting `TF_ENABLE_ONEDNN_OPTS=1` triggers oneDNN graph optimizations and vector kernels in TensorFlow.*

#### Q4. In the Ring-Allreduce algorithm used by Horovod, how does communication time scale with the number of compute nodes $N$?
- A) It increases exponentially ($O(2^N)$)
- B) It is largely independent of $N$, scaling as $2 \frac{N-1}{N} \frac{M}{B}$ where bandwidth is fully saturated
- C) It drops to zero instantly
- D) It requires a central server to store all weights  
**Answer: B** | *Explanation: Ring-Allreduce passes data only to adjacent neighbors, eliminating the central bandwidth choke point of parameter servers.*

#### Q5. What does the `#SBATCH --time=01:30:00` directive specify?
- A) The time of day the job must start (1:30 AM)
- B) The maximum wall-clock runtime limit (1 hour, 30 minutes) before the job is safely terminated by Slurm
- C) The date of training
- D) The user's login session timeout  
**Answer: B** | *Explanation: Slurm terminates jobs that exceed their requested wall-time to prevent runaway processes from blocking queues.*

#### Q6. What does `squeue -u $USER` display?
- A) The list of all files in the current folder
- B) The status (PENDING, RUNNING, COMPLETED) of all jobs submitted by the current user
- C) The cluster temperature
- D) The system log files  
**Answer: B** | *Explanation: `squeue -u <username>` filters active and queued cluster jobs for that specific user.*

#### Q7. Which command immediately cancels a running Slurm job with ID `45102`?
- A) `kill 45102`
- B) `scancel 45102`
- C) `stop 45102`
- D) `delete 45102`  
**Answer: B** | *Explanation: `scancel <job_id>` is the official Slurm command to terminate queued or active jobs.*

#### Q8. What is "Operator Fusion" in deep learning acceleration libraries like oneDNN?
- A) Combining two separate neural networks into one
- B) Fusing consecutive mathematical operations (e.g., Convolution + Bias + Activation) into a single pass through cache memory to avoid DRAM trips
- C) Joining two Python strings
- D) Merging two dataset files on disk  
**Answer: B** | *Explanation: Operator fusion keeps intermediate feature maps in fast L1/L2 cache, eradicating slow DRAM read/write cycles.*

#### Q9. When scaling from 1 node to 4 nodes with Horovod, why must the learning rate typically be scaled?
- A) Because the learning rate automatically halves
- B) Because the effective global batch size is multiplied by 4, requiring larger gradient steps to maintain convergence dynamics (Linear Scaling Rule)
- C) Because the CPU runs 4x colder
- D) It should never be changed  
**Answer: B** | *Explanation: According to the Linear Scaling Rule, when global batch size increases by $K$, learning rate should scale proportionally.*

#### Q10. What does the `%j` placeholder represent in `#SBATCH --output=logs/job_%j.out`?
- A) The job name
- B) The unique numeric Slurm Job ID
- C) The user's name
- D) The date of submission  
**Answer: B** | *Explanation: Slurm dynamically substitutes `%j` with the allocated Job ID, ensuring unique log filenames.*

#### Q11. Which daemon runs on each individual compute/worker node in a Slurm cluster?
- A) `slurmctld`
- B) `slurmd`
- C) `systemd`
- D) `sshd` only  
**Answer: B** | *Explanation: `slurmd` is the node agent that monitors resources and spawns tasks on compute nodes; `slurmctld` runs on the controller.*

#### Q12. What is the primary bottleneck in scaling distributed deep learning models beyond a single node?
- A) Disk storage capacity
- B) Inter-node network communication and gradient synchronization latency
- C) Python version differences
- D) Screen resolution  
**Answer: B** | *Explanation: As nodes increase, network gradient exchanges become the primary limiter to linear scaling.*

#### Q13. Which Intel AI accelerator features 24 integrated 100GbE RoCE ports to eradicate cluster communication bottlenecks?
- A) Intel Xeon E5-2670
- B) Habana Gaudi 2 / Gaudi 3
- C) Intel Core i7-13700K
- D) Intel UHD Graphics  
**Answer: B** | *Explanation: Gaudi integrates high-speed RDMA networking directly on the processor die for seamless distributed scaling.*

#### Q14. In TensorFlow, how does Horovod distribute gradient updates across workers?
- A) By uploading gradients to Google Drive
- B) By wrapping the standard Keras/TF optimizer with `hvd.DistributedOptimizer()`
- C) By saving gradients as text files on the login node
- D) By running multiple independent training loops without communication  
**Answer: B** | *Explanation: `hvd.DistributedOptimizer` intercepts backward-pass gradients and performs allreduce before updating weights.*

#### Q15. What state is reported by `squeue` when a job is waiting for compute nodes to become available?
- A) `RUNNING (R)`
- B) `PENDING (PD)`
- C) `FAILED (F)`
- D) `COMPLETED (CD)`  
**Answer: B** | *Explanation: `PD` (Pending) indicates the job is queued waiting for requested resources or priority.*

#### Q16. Which Slurm directive requests 8 CPU cores per distributed task for OpenMP multithreading?
- A) `#SBATCH --cpus-per-task=8`
- B) `#SBATCH --cores=8`
- C) `#SBATCH --threads=8`
- D) `#SBATCH --cpu-count=8`  
**Answer: A** | *Explanation: `--cpus-per-task` defines the number of hardware threads/cores allocated to each task.*

#### Q17. In deep learning on CPUs, which instruction set extension enables low-precision INT8 neural network inference?
- A) MMX
- B) AVX-512 VNNI (Vector Neural Network Instructions)
- C) SSE2
- D) BIOS  
**Answer: B** | *Explanation: VNNI accelerates 8-bit integer dot products across 512-bit vector registers.*

#### Q18. What command displays the overall status and available partitions of an entire Slurm cluster?
- A) `sinfo`
- B) `top`
- C) `htop`
- D) `cluster_view`  
**Answer: A** | *Explanation: `sinfo` summarizes node availability, partitions, and hardware states.*

#### Q19. What does the Parameter Server architecture suffer from when scaling to 16+ distributed nodes?
- A) High CPU overheating on worker nodes
- B) Network bandwidth saturation and CPU bottleneck on the central parameter server
- C) Immediate loss of training data
- D) Software license expiration  
**Answer: B** | *Explanation: The central parameter server cannot ingest incoming gradient streams from multiple nodes simultaneously.*

#### Q20. In a multi-node Horovod job, what does `hvd.rank()` return?
- A) The global rank (ID) of the current worker process
- B) The CPU clock frequency
- C) The total memory available
- D) The learning rate  
**Answer: A** | *Explanation: `hvd.rank()` uniquely identifies the process in the distributed communicator.*

#### Q21. Which tool in Intel oneAPI provides the low-level deep learning primitives utilized by TensorFlow-MKL?
- A) Intel oneDNN
- B) Intel VTune
- C) Intel Inspector
- D) Intel Advisor  
**Answer: A** | *Explanation: Intel oneDNN (Deep Neural Network Library) provides optimized convolution, inner product, and pooling primitives.*

#### Q22. How should an interactive multi-task job be launched inside a Slurm environment?
- A) `bash script.sh`
- B) `srun python3 app.py`
- C) `python3 app.py &`
- D) `nohup python3 app.py`  
**Answer: B** | *Explanation: `srun` connects directly to the Slurm scheduler to launch tasks across assigned nodes and cores.*

#### Q23. What does `#SBATCH --partition=gaudi` request?
- A) A specific queue targeting Habana Gaudi accelerator nodes
- B) An operating system reinstallation
- C) A specific hard drive format
- D) An internet download queue  
**Answer: A** | *Explanation: Partitions in Slurm represent specific queues mapped to distinct hardware configurations.*

#### Q24. When training with Horovod, which worker rank is typically responsible for saving checkpoints and writing logs?
- A) All workers simultaneously
- B) Rank 0 (Master worker) only
- C) The last worker rank only
- D) A random worker chosen each epoch  
**Answer: B** | *Explanation: Restricting checkpointing to Rank 0 (`if hvd.rank() == 0:`) prevents file collisions and duplicate disk writes.*

#### Q25. What supercomputing discipline is introduced on Day 4 to diagnose bottlenecks in distributed jobs?
- A) Frontend design
- B) Microarchitecture profiling and debugging with Intel VTune Profiler
- C) Spreadsheet auditing
- D) Mobile app development  
**Answer: B** | *Explanation: Day 4 introduces Intel VTune to inspect hardware telemetry, thread locks, and cache misses.*
