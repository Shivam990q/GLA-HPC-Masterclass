# 🌲 DAY 4: ARROW WORKFLOWS & TOPIC TREES
## Distributed AI Training, Slurm Multi-Node Clusters & Intel VTune Profiling Optimization
### Visual Step-by-Step Execution Pathways for HPC Engineers & Trainers

---

## 📌 TABLE OF TOPIC TREES
1. [Tree 1: Multi-Node Slurm Cluster Job Dispatch Pipeline](#tree-1-multi-node-slurm-cluster-job-dispatch-pipeline)
2. [Tree 2: Distributed Data Parallel (DDP) Gradient Synchronization Loop](#tree-2-distributed-data-parallel-ddp-gradient-synchronization-loop)
3. [Tree 3: Horovod Ring-AllReduce Internal Mechanics (Scatter-Reduce & AllGather)](#tree-3-horovod-ring-allreduce-internal-mechanics)
4. [Tree 4: Intel VTune Top-down Microarchitecture Analysis Method (TMAM) Decision Tree](#tree-4-intel-vtune-tmam-decision-tree)
5. [Tree 5: Intel Advisor Roofline Analysis & Diagnostic Optimization Path](#tree-5-intel-advisor-roofline-diagnostic-path)
6. [Tree 6: InfiniBand RDMA Kernel-Bypass vs Standard TCP/IP Network Flow](#tree-6-infiniband-rdma-vs-standard-tcpip-flow)

---

## TREE 1: Multi-Node Slurm Cluster Job Dispatch Pipeline

```
[ Engineer / User writes sbatch script ]
   │
   ▼
[ sbatch --nodes=4 --ntasks-per-node=2 job.sh ]
   │
   ├──► Submits job payload to Slurm Head Node
   ▼
[ slurmctld (Cluster Controller Daemon) ]
   │
   ├──► Queries slurmdbd for user bank account, fair-share priority, QoS limits
   ├──► Validates requested resources (4 nodes x 2 tasks = 8 total MPI ranks)
   ├──► Evaluates node availability & partition state (idle / allocated / draining)
   ▼
[ Job State: PENDING (Priority / Resources) ]
   │
   ├──► High-priority queue position reached & compute nodes allocated
   ▼
[ slurmctld dispatches Job Allocation RPC ]
   │
   ├──► Node 01 (Master Compute Node)
   ├──► Node 02 (Worker Compute Node)
   ├──► Node 03 (Worker Compute Node)
   └──► Node 04 (Worker Compute Node)
   │
   ▼
[ slurmd on each node receives allocation ]
   │
   ├──► Creates Linux cgroup container (/sys/fs/cgroup/cpu/slurm_job_XXXX)
   ├──► Enforces hardware boundaries: CPU core pinning, RAM limits, NUMA socket mapping
   ├──► Initializes PMIx (Process Management Interface Exascale) wire protocol
   ▼
[ slurmd forks local tasks (2 tasks per node) ]
   │
   ├──► Rank 0, 1 on Node 01
   ├──► Rank 2, 3 on Node 02
   ├──► Rank 4, 5 on Node 03
   └──► Rank 6, 7 on Node 04
   │
   ▼
[ MPI / oneCCL Communicator Bootstrap ]
   │
   ├──► Ranks exchange out-of-band InfiniBand QP (Queue Pair) connection parameters
   ▼
[ Parallel Execution of Distributed AI Training Script ]
```

---

## TREE 2: Distributed Data Parallel (DDP) Gradient Synchronization Loop

```
[ Step 0: Master Rank 0 initializes Neural Network Weights ]
   │
   ▼
[ Collective Broadcast: Rank 0 ──► Ranks 1, 2, 3, 4, 5, 6, 7 ]
   │ (Guarantees all workers start with identical initial model parameters)
   ▼
[ Training Epoch Begins: Distributed DataLoader ]
   │
   ├──► Global Dataset partitioned via DistributedSampler
   ├──► Rank 0 receives Mini-Batch Slice 0
   ├──► Rank 1 receives Mini-Batch Slice 1
   └──► Rank N receives Mini-Batch Slice N
   │
   ▼
[ Parallel Forward Pass on Local Mini-Batch ]
   │
   ├──► Local Forward: Predictions = Model(X_local)
   ├──► Local Loss Computation: L_local = Loss(Predictions, Y_local)
   ▼
[ Parallel Backward Pass on Local Mini-Batch ]
   │
   ├──► Autograd propagates gradients through layers in reverse order
   ├──► Local Gradients: G_local = dL / dWeights
   ▼
[ Gradient Aggregation via Collective Ring-AllReduce ]
   │
   ├──► Gradients gathered across all 8 ranks over InfiniBand interconnect
   ├──► G_global = (1 / 8) * sum(G_local_i)
   ▼
[ Local Optimizer Step on Every Rank ]
   │
   ├──► W_new = W_old - Learning_Rate * G_global
   │ (Because G_global is identical on all ranks, models remain perfectly synchronized!)
   ▼
[ Checkpoint Evaluation: Only Rank 0 saves weights to disk ]
   │
   └──► Next Batch Iteration or Next Epoch
```

---

## TREE 3: Horovod Ring-AllReduce Internal Mechanics

```
[ P = 4 Workers in Logical Ring: Rank 0 ──► Rank 1 ──► Rank 2 ──► Rank 3 ──► Rank 0 ]
   │
   ▼
[ Gradient Tensor Buffer (Size N) divided into P = 4 equal chunks: C0, C1, C2, C3 ]
   │
   ▼
+─────────────────────────────────────────────────────────────────────────────+
| PHASE 1: SCATTER-REDUCE (P - 1 = 3 Transmission Steps)                     |
+─────────────────────────────────────────────────────────────────────────────+
   │
   ├──► Step 1:
   │    Rank 0 sends chunk C0 to Rank 1; Rank 1 sums chunk C0 into its buffer
   │    Rank 1 sends chunk C1 to Rank 2; Rank 2 sums chunk C1 into its buffer
   │    Rank 2 sends chunk C2 to Rank 3; Rank 3 sums chunk C2 into its buffer
   │    Rank 3 sends chunk C3 to Rank 0; Rank 0 sums chunk C3 into its buffer
   │
   ├──► Step 2:
   │    Each rank sends the updated chunk to successor for next chunk reduction
   │
   ├──► Step 3:
   │    Final Scatter-Reduce step completes!
   │    Result: Each of the 4 ranks now holds ONE fully reduced chunk:
   │    - Rank 0 holds Sum(C3)
   │    - Rank 1 holds Sum(C0)
   │    - Rank 2 holds Sum(C1)
   │    - Rank 3 holds Sum(C2)
   │
   ▼
+─────────────────────────────────────────────────────────────────────────────+
| PHASE 2: ALLGATHER (P - 1 = 3 Transmission Steps)                           |
+─────────────────────────────────────────────────────────────────────────────+
   │
   ├──► Step 1:
   │    Each rank sends its fully reduced chunk to its neighbor in the ring
   │    Rank 0 sends Sum(C3) to Rank 1
   │    Rank 1 sends Sum(C0) to Rank 2
   │    Rank 2 sends Sum(C1) to Rank 3
   │    Rank 3 sends Sum(C2) to Rank 0
   │
   ├──► Step 2 & 3:
   │    Transmission continues until all chunks circulate the full ring!
   │
   ▼
[ Complete! Every rank now holds all P fully reduced chunks: Sum(C0, C1, C2, C3) ]
[ Total Data Moved per Rank = 2 * ((P - 1) / P) * N (Independent of Cluster Size!) ]
```

---

## TREE 4: Intel VTune TMAM Decision Tree

```
[ Pipeline Slot Available on CPU Core ]
   │
   ├── Did the slot successfully execute and retire an instruction?
   │     ├──► YES ──► [ RETIRING ] (> 40% Target)
   │     │            └──► Productive computation! Code is utilizing hardware well.
   │     │
   │     └──► NO  ──► Pipeline slot was stalled / wasted!
   │                    │
   │                    ├── Did the slot waste cycles on a mispredicted branch?
   │                    │     ├──► YES ──► [ BAD SPECULATION ] (< 10% Target)
   │                    │     │            ├── Branch Target Buffer (BTB) miss
   │                    │     │            └── Action: Eliminate dynamic branches, use SIMD masks
   │                    │     │
   │                    │     └──► NO  ──► Pipeline was stalled by execution bottlenecks
   │                    │                    │
   │                    │                    ├── Was the CPU waiting for instructions to arrive?
   │                    │                    │     ├──► YES ──► [ FRONTEND BOUND ] (< 15% Target)
   │                    │                    │     │            ├── ICache miss or complex decoder stall
   │                    │                    │     │            └── Action: Inlining, code locality
   │                    │                    │     │
   │                    │                    │     └──► NO  ──► [ BACKEND BOUND ] (Main Bottleneck)
   │                    │                    │                    │
   │                    │                    │                    ├── Waiting for data from memory?
   │                    │                    │                    │     └──► [ MEMORY BOUND ]
   │                    │                    │                    │          ├── L1/L2/L3 Cache Misses
   │                    │                    │                    │          ├── DRAM Bandwidth Saturation
   │                    │                    │                    │          └── NUMA Remote Socket Access
   │                    │                    │                    │
   │                    │                    │                    └── Execution units congested?
   │                    │                    │                          └──► [ CORE BOUND ]
   │                    │                    │                               ├── Divider unit stalls
   │                    │                    │                               └── Port saturation
```

---

## TREE 5: Intel Advisor Roofline Diagnostic Path

```
[ Program Execution Profiled by Intel Advisor ]
   │
   ├── Measure Total Floating Point Operations (FLOPs)
   └── Measure Total Bytes Transferred to/from DRAM (Bytes)
   │
   ▼
[ Calculate Arithmetic Intensity (AI) = FLOPs / Bytes ]
   │
   ▼
[ Compare AI against System Balance Knee Point (Peak FLOPs / Peak Bandwidth) ]
   │
   ├──► AI < Knee Point (Left of Knee: Low Arithmetic Intensity)
   │     │
   │     ▼
   │  [ APPLICATION IS STRICTLY MEMORY BOUND ]
   │     ├── The compute cores are starving waiting for memory buses!
   │     ├── Increasing CPU core clock frequency has ZERO impact on performance!
   │     │
   │     └──► Actionable HPC Remediations:
   │          ├── 1. Cache Blocking / Tiling (Keep matrices inside L2/L3 cache)
   │          ├── 2. Operator Fusion (Fuse Convolution + Bias + ReLU in single kernel)
   │          ├── 3. Memory Layout Alignment (Use PyTorch Channels-Last NHWC format)
   │          └── 4. Eliminate redundant memory allocations & tensor clones
   │
   └──► AI > Knee Point (Right of Knee: High Arithmetic Intensity)
         │
         ▼
      [ APPLICATION IS STRICTLY COMPUTE BOUND ]
         ├── Memory bandwidth is sufficient; CPU arithmetic units are saturated!
         │
         └──► Actionable HPC Remediations:
              ├── 1. Enable Vectorization (Compile with -mavx512f -mavx512vnni)
              ├── 2. Mixed Precision Acceleration (Convert FP32 ──► BF16 / INT8)
              ├── 3. Utilize Intel AMX (Advanced Matrix Extensions) Tile Units
              └── 4. Scale thread concurrency across all available CPU sockets
```

---

## TREE 6: InfiniBand RDMA vs Standard TCP/IP Flow

```
+─────────────────────────────────────────────────────────────────────────────+
| OPTION A: STANDARD LINUX ETHERNET TCP/IP STACK                              |
+─────────────────────────────────────────────────────────────────────────────+
[ User-Space App Buffer ]
   │ (Copy 1: Context switch into Linux Kernel Space)
   ▼
[ Linux Kernel TCP Socket Buffer (sk_buff) ]
   │ (TCP Protocol: Checksumming, Sliding Window, Ack Processing)
   ▼
[ Linux Kernel Network Device Driver ]
   │ (Copy 2: DMA transfer to NIC TX ring)
   ▼
[ Ethernet Network Interface Card (NIC) ]
   │ ──► [ Physical Network Wire (~25-50 μs Latency + 100% CPU Core Load) ] ──►
   ▼
[ Destination Ethernet NIC ]
   │ (Copy 3: DMA transfer to Kernel RX ring)
   ▼
[ Destination Linux Kernel TCP Buffer ]
   │ (Copy 4: Context switch back to User Space)
   ▼
[ Destination User-Space App Buffer ]

===============================================================================

+─────────────────────────────────────────────────────────────────────────────+
| OPTION B: SUPERCOMPUTER INFINIBAND RDMA (KERNEL-BYPASS)                     |
+─────────────────────────────────────────────────────────────────────────────+
[ User-Space App Buffer (Registered Pin-Locked Memory) ]
   │
   ▼ (Zero OS Context Switches, Zero Kernel Memory Copies!)
[ InfiniBand Host Channel Adapter (HCA) Hardware DMA Engine ]
   │
   ▼
[ Physical InfiniBand Fabric (sub-1.0 μs Latency, 200/400 Gbps Bandwidth) ]
   │
   ▼
[ Destination InfiniBand HCA Hardware DMA Engine ]
   │
   ▼ (Direct user-space memory placement via PCIe)
[ Destination User-Space App Buffer ]
```

---
*GLA University HPC Masterclass | Day 4 Arrow Workflows & Topic Trees Completed*
