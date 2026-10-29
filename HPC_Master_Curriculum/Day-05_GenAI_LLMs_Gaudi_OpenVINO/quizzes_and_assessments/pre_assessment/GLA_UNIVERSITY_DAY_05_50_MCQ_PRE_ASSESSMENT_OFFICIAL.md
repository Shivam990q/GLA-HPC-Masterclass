# 🏛️ GLA UNIVERSITY, MATHURA — DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
## HPC Masterclass | Day 5 Comprehensive Pre-Assessment (50 MCQs)
**Course**: B.Tech CSE 7th Sem — High Performance Computing Masterclass  
**Module**: Day 5 Prerequisite & Foundational Knowledge: Computer Architecture, Matrix Acceleration, Quantization & Distributed Systems  
**Total Questions**: 50 | **Duration**: 60 Minutes | **Maximum Marks**: 50

---

### 📋 Master Evaluation Key & Forensic Solution Guide (Instructor Copy)

| Q# | Correct Answer | Cognitive Bloom Level | Core Concept Focus |
|:--:|:--------------:|:---------------------:|:-------------------|
| **01** | **B** | `Understand` | What is the primary computational bottleneck in th... |
| **02** | **B** | `Knowledge` | What is the primary numerical difference between I... |
| **03** | **B** | `Knowledge` | In general matrix multiplication (GEMM: $C = \alph... |
| **04** | **B** | `Understand` | What is the definition of 'Arithmetic Intensity' i... |
| **05** | **B** | `Analyze` | Why is the Prompt Prefill phase of LLM inference c... |
| **06** | **B** | `Understand` | What is the primary function of a systolic array i... |
| **07** | **C** | `Apply` | What is the memory size in bytes required to store... |
| **08** | **B** | `Understand` | In the Transformer architecture, what is the role ... |
| **09** | **B** | `Understand` | What is the fundamental difference between Post-Tr... |
| **10** | **A** | `Apply` | In symmetric uniform quantization of a real-valued... |
| **11** | **B** | `Understand` | What is the primary advantage of Asymmetric Quanti... |
| **12** | **B** | `Knowledge` | What is the role of the Intel OpenVINO Model Optim... |
| **13** | **A** | `Knowledge` | Which Linux utility displays available CPU core to... |
| **14** | **B** | `Understand` | In high-performance interconnects for AI clusters,... |
| **15** | **B** | `Knowledge` | What protocol brings RDMA capabilities over standa... |
| **16** | **B** | `Understand` | In deep learning distributed training, what collec... |
| **17** | **B** | `Analyze` | Why is Full Parameter Fine-Tuning of a 70B paramet... |
| **18** | **B** | `Understand` | What is the primary concept behind Parameter-Effic... |
| **19** | **B** | `Knowledge` | What is the rank $r$ in LoRA (Low-Rank Adaptation)... |
| **20** | **A** | `Knowledge` | In the Slurm workload manager, which command is us... |
| **21** | **A** | `Knowledge` | Which Slurm command prints the current queue of ru... |
| **22** | **B** | `Understand` | What does the Top-Down Microarchitecture Analysis ... |
| **23** | **B** | `Analyze` | What is the typical memory bandwidth of high-end D... |
| **24** | **B** | `Understand` | In neural network quantization, what is an 'outlie... |
| **25** | **B** | `Knowledge` | What is the primary role of the Softmax function i... |
| **26** | **B** | `Knowledge` | In OpenVINO, what is the 'CPU plugin'?... |
| **27** | **B** | `Knowledge` | How many total bits are required to store one sing... |
| **28** | **A** | `Apply` | If a weight tensor contains 1,000,000 parameters, ... |
| **29** | **B** | `Knowledge` | In LLM generation metrics, what is 'Time-to-First-... |
| **30** | **A** | `Knowledge` | In LLM generation metrics, what is 'Inter-Token La... |
| **31** | **A** | `Understand` | What is the primary difference between Data Parall... |
| **32** | **B** | `Understand` | What happens when an LLM context length exceeds th... |
| **33** | **B** | `Knowledge` | What is the purpose of the `optimum-intel` open-so... |
| **34** | **B** | `Understand` | What is 'Non-Uniform Memory Access' (NUMA) in mult... |
| **35** | **B** | `Analyze` | Why is the Bfloat16 format preferred over FP16 dur... |
| **36** | **B** | `Knowledge` | In OpenVINO IR files, what information is stored i... |
| **37** | **A** | `Knowledge` | What mathematical operation does the Self-Attentio... |
| **38** | **B** | `Understand` | What is the primary role of Layer Normalization (o... |
| **39** | **B** | `Knowledge` | How many total bits are used by an INT8 signed int... |
| **40** | **B** | `Knowledge` | In the context of HPC Slurm clusters, what is an '... |
| **41** | **B** | `Analyze` | What is the primary limitation of static batching ... |
| **42** | **B** | `Apply` | What is the function of the `torch.no_grad()` cont... |
| **43** | **B** | `Understand` | What does 'Perplexity' measure in language modelin... |
| **44** | **B** | `Apply` | What is the theoretical speedup in weights transfe... |
| **45** | **B** | `Understand` | What is the primary benefit of Operator Fusion (su... |
| **46** | **B** | `Knowledge` | Which Python library provides a lightweight, async... |
| **47** | **B** | `Knowledge` | In distributed PyTorch training, what role does th... |
| **48** | **B** | `Knowledge` | What is a 'Checkpoint' in the context of deep lear... |
| **49** | **B** | `Knowledge` | What is the primary role of the tokenizer in an LL... |
| **50** | **A** | `Analyze` | Why is synchronous All-Reduce gradient exchange a ... |

---

### 🔬 Complete Questions with Technical Explanations

#### Question 01
What is the primary computational bottleneck in the standard scaled dot-product self-attention mechanism $\text{Softmax}(\frac{QK^T}{\sqrt{d_k}})V$ when scaling to very long context sequence lengths ($N$)?

- **(a)** Disk write I/O speed.
- **(b)** **[CORRECT]** Quadratic time and memory complexity $\mathcal{O}(N^2)$ due to the computation and materialization of the full $N \times N$ attention weight matrix.
- **(c)** Ethernet packet MTU size.
- **(d)** Linear complexity $\mathcal{O}(N)$ in the final output projection.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Multiplying the Query matrix ($N \times d_k$) by the transposed Key matrix ($d_k \times N$) yields an $N \times N$ attention score matrix. Both compute operations and activation memory grow quadratically $\mathcal{O}(N^2)$ with context length $N$.

---

#### Question 02
What is the primary numerical difference between IEEE 754 standard FP16 (Half Precision) and Google/Intel Bfloat16 (Brain Floating Point)?

- **(a)** FP16 uses 16 bits; BF16 uses 32 bits.
- **(b)** **[CORRECT]** FP16 allocates 5 exponent bits and 10 mantissa bits, whereas BF16 allocates 8 exponent bits and 7 mantissa bits, giving BF16 the exact same dynamic range as standard FP32.
- **(c)** FP16 cannot represent negative numbers.
- **(d)** BF16 uses fixed-point integer arithmetic.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: BF16 preserves the 8-bit exponent of single-precision FP32, allowing it to represent values from $\sim 10^{-38}$ to $10^{38}$ without underflow or overflow, whereas FP16 has only a 5-bit exponent (range $\sim 6 \times 10^{-5}$ to $65504$), often requiring loss scaling in deep learning.

---

#### Question 03
In general matrix multiplication (GEMM: $C = \alpha A \cdot B + \beta C$), where $A \in \mathbb{R}^{M \times K}$ and $B \in \mathbb{R}^{K \times N}$, how many total floating-point arithmetic operations (multiply-adds) are performed?

- **(a)** $M \times N$
- **(b)** **[CORRECT]** $2 \cdot M \cdot N \cdot K$ floating-point operations (FLOPs)
- **(c)** $M + N + K$
- **(d)** $(M \cdot K)^2$

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: Computing each of the $M \times N$ entries in matrix $C$ requires an inner product of length $K$, consisting of $K$ multiplications and $K$ additions, totaling $2 \cdot M \cdot N \cdot K$ operations.

---

#### Question 04
What is the definition of 'Arithmetic Intensity' in the Roofline Model of computer architecture?

- **(a)** The clock frequency of the CPU measured in GHz.
- **(b)** **[CORRECT]** The ratio of floating-point operations performed to the total bytes of data transferred from main DRAM memory (FLOPs/Byte).
- **(c)** The number of cores per processor socket.
- **(d)** The total electrical power consumed per floating-point addition.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Arithmetic intensity ($I = \text{FLOPs} / \text{Bytes}$) measures how many arithmetic operations are executed per byte of memory accessed from DRAM. Low arithmetic intensity indicates a memory-bound workload; high arithmetic intensity indicates a compute-bound workload.

---

#### Question 05
Why is the Prompt Prefill phase of LLM inference compute-bound, whereas the subsequent autoregressive Token Generation phase is memory-bandwidth bound?

- **(a)** Prefill runs on GPUs, while generation runs on hard drives.
- **(b)** **[CORRECT]** Prefill processes all input prompt tokens concurrently as a large matrix-matrix multiplication (GEMM) with high arithmetic intensity, while generation processes one token at a time as a matrix-vector product (GEMV) requiring full weight streaming for a single token.
- **(c)** Generation uses double-precision floats, while prefill uses integers.
- **(d)** Prefill bypasses the attention mechanism entirely.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Technical Rationale**: In prefill, batching across all prompt tokens ($N$ tokens) allows weights loaded from memory to be reused across all tokens ($M=N$, GEMM), yielding high arithmetic intensity. In autoregressive decoding ($M=1$, GEMV), all weights must be read from DRAM just to multiply against a single input token vector.

---

#### Question 06
What is the primary function of a systolic array in AI accelerator hardware (such as Google TPU or Intel AMX TMUL)?

- **(a)** To sort database records using quicksort.
- **(b)** **[CORRECT]** To stream data through a 2D grid of tightly-coupled processing elements, reusing inputs and intermediate weights directly between neighboring registers without continually reading and writing to the central register file.
- **(c)** To convert analog signals from microphones into digital audio.
- **(d)** To route TCP/IP packets between network switches.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Systolic arrays pass data through a grid of multiply-accumulate (MAC) units in a rhythmic wave. Data read from memory is reused across multiple PEs in adjacent rows/columns, drastically slashing register file and cache access energy.

---

#### Question 07
What is the memory size in bytes required to store 7 billion model parameters in standard FP32 precision?

- **(a)** 7.0 GB
- **(b)** 14.0 GB
- **(c)** **[CORRECT]** 28.0 GB (since each FP32 parameter occupies 4 bytes)
- **(d)** 56.0 GB

> **Correct Answer**: **(C)**  
> **Bloom's Cognitive Level**: `Apply`  
> **Technical Rationale**: 7 billion parameters $\times 4$ bytes/parameter $= 28 \times 10^9$ bytes $\approx 28.0$ GB (or $26.07$ GiB).

---

#### Question 08
In the Transformer architecture, what is the role of the Key-Value (KV) cache during autoregressive inference?

- **(a)** It stores database passwords securely in memory.
- **(b)** **[CORRECT]** It caches the computed Key and Value projection tensors of previously processed tokens so that past token representations do not have to be recomputed from scratch at every new token generation step.
- **(c)** It compiles Python functions into assembly code.
- **(d)** It compresses the text prompt using Huffman encoding.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Without a KV-cache, generating token $t$ would require re-evaluating the attention layer for all preceding tokens $1, \dots, t-1$, leading to $\mathcal{O}(N^3)$ cumulative computation. Caching past keys and values reduces incremental cost per step to $\mathcal{O}(N)$.

---

#### Question 09
What is the fundamental difference between Post-Training Quantization (PTQ) and Quantization-Aware Training (QAT)?

- **(a)** PTQ requires retraining the entire model on ImageNet; QAT does not.
- **(b)** **[CORRECT]** PTQ quantizes an already-trained model's weights and activations using a small calibration dataset without retraining, whereas QAT models quantization noise during training using fake-quantization operators so the model adapts its weights to low-precision rounding.
- **(c)** PTQ only runs on mobile phones; QAT only runs on supercomputers.
- **(d)** QAT is strictly for image models, while PTQ is strictly for audio.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: PTQ is fast and requires no gradient descent or hyperparameter tuning, making it ideal for large foundation models. QAT simulates quantization rounding errors during the forward pass and adjusts weights via straight-through estimator (STE) backprop, achieving higher accuracy at high compute cost.

---

#### Question 10
In symmetric uniform quantization of a real-valued tensor $x \in [-x_{max}, x_{max}]$ into signed $b$-bit integer representation, how is the scale factor $S$ defined?

- **(a)** **[CORRECT]** $S = \frac{x_{max}}{2^{b-1} - 1}$
- **(b)** $S = x_{max} \times 2^b$
- **(c)** $S = \frac{2^b}{x_{max}}$
- **(d)** $S = \sqrt{x_{max}}$

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Apply`  
> **Technical Rationale**: For symmetric quantization, zero maps exactly to integer 0 (zero-point $Z=0$). The grid covers $[-(2^{b-1}-1), 2^{b-1}-1]$, so the scaling factor is $S = \frac{x_{max}}{2^{b-1}-1}$.

---

#### Question 11
What is the primary advantage of Asymmetric Quantization over Symmetric Quantization?

- **(a)** It eliminates the need for floating-point numbers.
- **(b)** **[CORRECT]** It supports arbitrary asymmetric distributions (where min and max values differ significantly from zero, such as post-ReLU activations $[0, x_{max}]$) by introducing a non-zero integer Zero-Point ($Z$) offset.
- **(c)** It makes matrix multiplication 10x faster.
- **(d)** It requires only 1 bit per parameter.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Asymmetric quantization maps [min_val, max_val] to [q_min, q_max] via q = round(x/S) + Z. For non-negative distributions (like ReLU or GELU activations), symmetric quantization wastes half the integer representation range on non-existent negative values.

---

#### Question 12
What is the role of the Intel OpenVINO Model Optimizer?

- **(a)** To download models from torrent networks.
- **(b)** **[CORRECT]** To convert source deep learning models (PyTorch, TensorFlow, ONNX) into hardware-optimized OpenVINO Intermediate Representation (IR) graphs.
- **(c)** To overclock CPU clock frequencies.
- **(d)** To compile Linux kernel device drivers.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: Model Optimizer ingests third-party framework models, eliminates redundant operations, performs constant folding and layer fusion, and outputs `.xml` and `.bin` IR files.

---

#### Question 13
Which Linux utility displays available CPU core topologies, NUMA nodes, and cache sizes?

- **(a)** **[CORRECT]** `lscpu`
- **(b)** `lsusb`
- **(c)** `lsblk`
- **(d)** `lspci`

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: `lscpu` queries sysfs and CPUID to report CPU architecture, vendor, model, socket count, core count, thread count per core, NUMA node topology, and L1d/L1i/L2/L3 cache capacities.

---

#### Question 14
In high-performance interconnects for AI clusters, what does RDMA (Remote Direct Memory Access) achieve?

- **(a)** It automatically cleans dust from server heatsinks.
- **(b)** **[CORRECT]** It enables an accelerator or server to directly access memory on a remote node without involving the operating system kernel or CPU on either side, achieving microsecond latency and zero-copy throughput.
- **(c)** It doubles the physical capacity of DDR5 RAM modules.
- **(d)** It replaces Ethernet switches with Bluetooth beacons.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: RDMA bypasses the OS network stack. Network adapters (NICs) transfer data directly between application virtual memory buffers on different physical servers without CPU context switching or data copying.

---

#### Question 15
What protocol brings RDMA capabilities over standard enterprise Ethernet infrastructure?

- **(a)** FTP
- **(b)** **[CORRECT]** RoCE (RDMA over Converged Ethernet)
- **(c)** SMTP
- **(d)** Telnet

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: RoCE (specifically RoCE v2, which encapsulates InfiniBand transport packets inside standard UDP/IP) allows RDMA communications to run over commodity Lossless Ethernet switches using Priority Flow Control (PFC).

---

#### Question 16
In deep learning distributed training, what collective communication operation combines gradient tensors from all participating nodes by summing them and distributes the identical result to all nodes?

- **(a)** All-to-All
- **(b)** **[CORRECT]** All-Reduce
- **(c)** Broadcast
- **(d)** Gather

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: All-Reduce performs an element-wise reduction (such as summation) across tensors from all $P$ ranks and deposits the globally reduced tensor on every rank, which is essential for synchronous Distributed Data Parallel (DDP) gradient synchronization.

---

#### Question 17
Why is Full Parameter Fine-Tuning of a 70B parameter model prohibitively expensive on standard academic HPC clusters?

- **(a)** Because Python limits variable names to 10 characters.
- **(b)** **[CORRECT]** Because updating all parameters using an AdamW optimizer requires storing model weights (140GB in FP16), gradients (140GB), and first/second optimizer momentum states (560GB in FP32), totaling over 840 GB of accelerator memory solely for training states.
- **(c)** Because 70B models can only run on quantum computers.
- **(d)** Because Slurm cannot schedule jobs longer than 15 minutes.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Technical Rationale**: AdamW stores 16 bytes per parameter: FP16 weight (2B), FP16 gradient (2B), FP32 master weight (4B), FP32 momentum (4B), and FP32 variance (4B). For 70B parameters, $70 \times 16 = 1,120$ GB of raw accelerator memory is required without even accounting for activation memory.

---

#### Question 18
What is the primary concept behind Parameter-Efficient Fine-Tuning (PEFT)?

- **(a)** Deleting half the training dataset to accelerate training.
- **(b)** **[CORRECT]** Freezing the vast majority of pre-trained model parameters and fine-tuning only a tiny fraction (typically < 1%) of existing or newly added parameters for downstream domain tasks.
- **(c)** Replacing all attention layers with convolutional layers.
- **(d)** Training the model using random number generators.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: PEFT techniques (e.g. LoRA, Prefix Tuning, Adapters) freeze pre-trained foundation weights, drastically minimizing trainable parameters, optimizer memory footprint, and gradient synchronization bandwidth across cluster nodes.

---

#### Question 19
What is the rank $r$ in LoRA (Low-Rank Adaptation)?

- **(a)** The military rank of the lead AI researcher.
- **(b)** **[CORRECT]** The inner dimension of low-rank matrices $A \in \mathbb{R}^{r \times k}$ and $B \in \mathbb{R}^{d \times r}$, controlling the capacity and parameter count of the adaptation update.
- **(c)** The number of GPU cards in the cluster.
- **(d)** The total number of sentences in the training dataset.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: In LoRA, the adapter update is $\Delta W = B \cdot A$. The rank $r$ (commonly set to 8, 16, 32, or 64) determines the number of columns in $B$ and rows in $A$, defining the subspace dimension into which the task-specific adaptations are projected.

---

#### Question 20
In the Slurm workload manager, which command is used to query the status of all active queues, partitions, and cluster nodes?

- **(a)** **[CORRECT]** `sinfo`
- **(b)** `srun`
- **(c)** `scancel`
- **(d)** `sbatch`

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: `sinfo` reports the state of Slurm partitions and individual node allocations (idle, allocated, drained, down).

---

#### Question 21
Which Slurm command prints the current queue of running and pending jobs?

- **(a)** **[CORRECT]** `squeue`
- **(b)** `salloc`
- **(c)** `top`
- **(d)** `kill`

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: `squeue` displays active jobs in the Slurm scheduler, including Job ID, Partition, User, State (R=Running, PD=Pending), and Node allocations.

---

#### Question 22
What does the Top-Down Microarchitecture Analysis Method (TMAM) Front-End Bound metric signify?

- **(a)** The server's front bezel door is unlocked.
- **(b)** **[CORRECT]** The CPU core pipeline is stalled because the front-end fetch and decode units cannot deliver instructions (uOps) fast enough to the execution engine (e.g., due to instruction cache misses, ITLB misses, or branch target buffer stalls).
- **(c)** The frontend web browser has crashed.
- **(d)** The power supply cable is disconnected.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Front-End Bound indicates inefficiencies in fetching instructions from memory/caches and decoding them into uOps before they can reach the allocator and out-of-order execution reservation stations.

---

#### Question 23
What is the typical memory bandwidth of high-end DDR5 server memory compared to High Bandwidth Memory (HBM2e / HBM3)?

- **(a)** DDR5 is 100x faster than HBM3.
- **(b)** **[CORRECT]** DDR5 server channels typically deliver $\sim 300\text{--}400$ GB/s aggregate bandwidth across 8 channels, whereas HBM delivers $\sim 2\text{--}3.5$ TB/s per accelerator chip.
- **(c)** Both have exactly identical bandwidth.
- **(d)** HBM can only store 512 kilobytes of data.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Technical Rationale**: Standard DDR5 channels provide ~300-400 GB/s across an entire dual-socket CPU package. HBM stacks wide 1024-bit memory dies on an interposer directly adjacent to the compute silicon, delivering 2.0 to 3.5+ TB/s per chip.

---

#### Question 24
In neural network quantization, what is an 'outlier feature' in activations?

- **(a)** A bug in the Python interpreter.
- **(b)** **[CORRECT]** A very small number of activation channels that systematically exhibit activation magnitudes up to 100x larger than normal channels across all sequence positions.
- **(c)** A network cable that has fallen out of a switch port.
- **(d)** An erroneous token generated during translation.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Studies (e.g. LLM.int8(), SmoothQuant, AWQ) revealed that in LLMs larger than 6.7B parameters, certain channels consistently produce activation values exceeding 100x the average magnitude, making activation quantization challenging without special handling.

---

#### Question 25
What is the primary role of the Softmax function in self-attention?

- **(a)** To invert a matrix.
- **(b)** **[CORRECT]** To normalize raw attention logit scores across the sequence dimension into a valid probability distribution where all weights are non-negative and sum to 1.0.
- **(c)** To convert text tokens into ASCII code points.
- **(d)** To encrypt tensor values for network transmission.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: $\text{Softmax}(z_i) = \frac{e^{z_i}}{\sum_j e^{z_j}}$ transforms raw dot-product scores into an attention distribution that determines how much each token attends to other tokens.

---

#### Question 26
In OpenVINO, what is the 'CPU plugin'?

- **(a)** A physical hardware card inserted into a PCIe slot.
- **(b)** **[CORRECT]** A runtime dynamic library (`openvino_intel_cpu_plugin.so`) that maps OpenVINO IR graph nodes to highly optimized execution primitives running on x86/ARM CPU cores using oneDNN, AVX-512, and AMX.
- **(c)** A browser extension for Google Chrome.
- **(d)** A compiler for HTML and JavaScript.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: The OpenVINO CPU plugin translates the computational graph into optimized instruction sequences (using oneDNN kernels) tuned for the target CPU's specific vector and matrix extensions.

---

#### Question 27
How many total bits are required to store one single numerical value in INT4 representation?

- **(a)** 1 bit
- **(b)** **[CORRECT]** 4 bits (half a byte, allowing 16 discrete states: $-8$ to $+7$ or $0$ to $15$)
- **(c)** 8 bits
- **(d)** 16 bits

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: INT4 uses 4 bits, representing $2^4 = 16$ distinct quantization levels, packing two weights per byte in memory.

---

#### Question 28
If a weight tensor contains 1,000,000 parameters, how much memory does it consume in FP16 versus INT4 (excluding metadata)?

- **(a)** **[CORRECT]** 2 MB in FP16 vs 0.5 MB (500 KB) in INT4
- **(b)** 10 MB in FP16 vs 1 MB in INT4
- **(c)** 4 MB in FP16 vs 2 MB in INT4
- **(d)** 16 MB in FP16 vs 8 MB in INT4

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Apply`  
> **Technical Rationale**: FP16 requires 2 bytes per parameter: $1,000,000 \times 2 = 2,000,000 \text{ bytes} = 2.0$ MB. INT4 requires 0.5 bytes per parameter: $1,000,000 \times 0.5 = 500,000 \text{ bytes} = 0.5$ MB, delivering a 4x reduction.

---

#### Question 29
In LLM generation metrics, what is 'Time-to-First-Token' (TTFT)?

- **(a)** The time taken to train the foundation model from scratch.
- **(b)** **[CORRECT]** The total latency elapsed from the moment a user submits an input prompt until the first token of the response is generated and emitted by the server.
- **(c)** The duration of the server's nightly reboot cycle.
- **(d)** The time required to compress a model with NNCF.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: TTFT measures the latency of the prompt prefill phase: ingestion, tokenization, KV-cache initialization, and initial forward pass to produce token #1.

---

#### Question 30
In LLM generation metrics, what is 'Inter-Token Latency' (ITL)?

- **(a)** **[CORRECT]** The time elapsed between generating consecutive output tokens during the autoregressive decode phase.
- **(b)** The physical network latency between two transatlantic subsea fiber cables.
- **(c)** The time it takes to allocate memory for the PyTorch runtime.
- **(d)** The idle time between consecutive student lab sessions.

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: ITL (also referred to as time per output token) measures the duration of a single autoregressive step, directly dictating how smooth the streaming text appears to the reader.

---

#### Question 31
What is the primary difference between Data Parallelism and Tensor Parallelism in distributed deep learning?

- **(a)** **[CORRECT]** Data parallelism partitions different training dataset batches across multiple accelerators; Tensor parallelism shards individual weight matrices and layers across multiple accelerators within a single model step.
- **(b)** Data parallelism runs only on CPUs; Tensor parallelism runs only on mobile phones.
- **(c)** Data parallelism trains image models; Tensor parallelism trains audio models.
- **(d)** Data parallelism does not use network cables.

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: In Data Parallelism (DDP), each rank holds a replica of the model and processes distinct data slices. In Tensor Parallelism (e.g. Megatron-LM), individual linear transformations ($Y = XW$) are sliced column-wise or row-wise across multiple devices.

---

#### Question 32
What happens when an LLM context length exceeds the physical memory capacity of the allocated KV-cache?

- **(a)** The model becomes infinitely intelligent.
- **(b)** **[CORRECT]** The system throws an Out-Of-Memory (OOM) error, or must evict/truncate earlier context tokens (e.g., via sliding window attention) to prevent an unhandled memory fault.
- **(c)** The CPU doubles its clock frequency.
- **(d)** The output language switches automatically to German.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Because the KV-cache grows linearly with context length and batch size, exceeding available accelerator memory results in a CUDA/HPU out-of-memory exception unless dynamic paging or token eviction policies are active.

---

#### Question 33
What is the purpose of the `optimum-intel` open-source library from Hugging Face and Intel?

- **(a)** To replace the Linux bash terminal with a GUI.
- **(b)** **[CORRECT]** To provide seamless integration between the Hugging Face Transformers ecosystem and Intel hardware acceleration libraries, including OpenVINO and IPEX (Intel Extension for PyTorch).
- **(c)** To write synthetic benchmark reports for marketing.
- **(d)** To flash motherboard BIOS chips.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: `optimum-intel` enables users to load models using standard Hugging Face APIs (e.g. `OVModelForCausalLM.from_pretrained()`) while executing through the optimized OpenVINO runtime.

---

#### Question 34
What is 'Non-Uniform Memory Access' (NUMA) in multi-socket enterprise servers?

- **(a)** A bug in the memory controller that corrupts data randomly.
- **(b)** **[CORRECT]** A computer memory design where a processor core can access its own local memory socket faster than non-local memory attached to another processor socket.
- **(c)** A type of flash memory used in digital cameras.
- **(d)** A software library for rendering 3D animations.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: In a multi-socket server, each CPU socket has dedicated DDR channels. Accessing memory attached to a remote socket requires routing data over inter-socket interconnects (e.g., Intel UPI), increasing latency and reducing effective bandwidth.

---

#### Question 35
Why is the Bfloat16 format preferred over FP16 during distributed training of Large Language Models?

- **(a)** Because BF16 requires half as many bits as FP16.
- **(b)** **[CORRECT]** Because BF16's wide 8-bit dynamic range matches FP32, preventing gradient vanishing or gradient explosion during mixed-precision training without requiring complex dynamic loss scaling.
- **(c)** Because BF16 was invented in 1965.
- **(d)** Because BF16 can only run on single-core CPUs.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Technical Rationale**: Mixed-precision training with FP16 frequently underflows small gradient values to zero unless dynamic loss scaling is meticulously tuned. BF16 shares the exact exponent range as FP32, virtually eliminating gradient underflow.

---

#### Question 36
In OpenVINO IR files, what information is stored in the `.xml` file?

- **(a)** Raw floating-point tensor weight arrays.
- **(b)** **[CORRECT]** The computational topology graph: nodes (operations), edges (data tensors), shapes, datatypes, and runtime parameters.
- **(c)** A compiled Linux kernel executable.
- **(d)** The student's attendance records.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: The `.xml` file stores the computational graph structure in structured XML syntax, defining how tensor inputs and outputs flow through operations.

---

#### Question 37
What mathematical operation does the Self-Attention mechanism perform to measure token similarity?

- **(a)** **[CORRECT]** Dot product between Query and Key vectors ($Q \cdot K^T$).
- **(b)** Bitwise XOR between token ASCII codes.
- **(c)** Fast Fourier Transform on prompt text.
- **(d)** Integer division of token IDs.

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: Scaled dot-product attention computes the inner product between the query vector of token $i$ and the key vector of token $j$, quantifying their contextual correlation in the latent embedding space.

---

#### Question 38
What is the primary role of Layer Normalization (or RMSNorm) in transformer layers?

- **(a)** To sort the tokens alphabetically.
- **(b)** **[CORRECT]** To stabilize hidden state activation dynamics and gradients across training by normalizing activations across the feature dimension for each token independently.
- **(c)** To decrease CPU fan speed.
- **(d)** To encrypt model outputs.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: LayerNorm and RMSNorm prevent activations from exploding or decaying across dozens of stacked transformer layers, ensuring stable gradient flow during backpropagation.

---

#### Question 39
How many total bits are used by an INT8 signed integer?

- **(a)** 4 bits
- **(b)** **[CORRECT]** 8 bits (1 byte, representing $-128$ to $+127$)
- **(c)** 16 bits
- **(d)** 32 bits

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: An INT8 integer uses 8 bits (1 byte) in two's complement format, spanning the range $-128$ to $+127$.

---

#### Question 40
In the context of HPC Slurm clusters, what is an 'Allocation'?

- **(a)** An administrative punishment for violating computer lab rules.
- **(b)** **[CORRECT]** A dedicated set of compute nodes, CPU cores, memory, and accelerator resources granted by the Slurm controller to a specific job for a bounded duration.
- **(c)** A financial grant from the government.
- **(d)** A software license file stored in `/etc`.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: Slurm grants an allocation (nodes, cores, accelerators) via `salloc` or `sbatch` within which the user executes parallel applications via `srun`.

---

#### Question 41
What is the primary limitation of static batching during high-concurrency LLM serving?

- **(a)** It crashes the network switch.
- **(b)** **[CORRECT]** Compute slots are wasted on padding tokens, and high-latency generation requests block newly arrived requests from entering execution until the entire batch finishes.
- **(c)** It cannot run on Linux systems.
- **(d)** It requires models to have fewer than 1,000 parameters.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Technical Rationale**: Because generation length varies wildly across user queries (e.g., 10 tokens vs 500 tokens), static batching forces finished requests to wait idle and wastes memory/compute on padding tokens.

---

#### Question 42
What is the function of the `torch.no_grad()` context manager in PyTorch during LLM inference?

- **(a)** It disables student grade recording in the university database.
- **(b)** **[CORRECT]** It deactivates the PyTorch autograd engine, preventing the allocation and caching of intermediate activations for gradient backpropagation and significantly reducing memory usage.
- **(c)** It converts PyTorch code into C++.
- **(d)** It shuts down the GPU.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Apply`  
> **Technical Rationale**: During inference, backward passes are never performed. `torch.no_grad()` disables tracking of computational history, slashing activation memory overhead.

---

#### Question 43
What does 'Perplexity' measure in language modeling evaluation?

- **(a)** The physical temperature of the server CPU heatsink.
- **(b)** **[CORRECT]** The exponentiated cross-entropy loss over a validation corpus, quantifying how surprised or uncertain the language model is when predicting the next token.
- **(c)** The network ping time between two HPC nodes.
- **(d)** The number of syntax errors in a Python program.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Perplexity is calculated as $\exp\left(-\frac{1}{N}\sum_{i=1}^N \log P(w_i | w_{<i})\right)$. Lower perplexity indicates that the model assigns higher probability to the ground-truth tokens.

---

#### Question 44
What is the theoretical speedup in weights transfer time when moving from FP16 weights to INT4 weights on a memory-bandwidth-bound inference engine?

- **(a)** 1.5x
- **(b)** **[CORRECT]** 4.0x (since INT4 uses 4 bits per weight while FP16 uses 16 bits per weight)
- **(c)** 10.0x
- **(d)** 100.0x

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Apply`  
> **Technical Rationale**: Data transfer time is proportional to total bytes: $\frac{16 \text{ bits}}{4 \text{ bits}} = 4.0\text{x}$ reduction in memory traffic across the memory bus.

---

#### Question 45
What is the primary benefit of Operator Fusion (such as fusing Bias-Add, Scale, and ReLU into a single kernel) in deep learning inference engines?

- **(a)** It decreases the font size of the code.
- **(b)** **[CORRECT]** It eliminates intermediate read/write round-trips to DRAM or high-level caches, executing consecutive operations directly within on-chip CPU/accelerator registers.
- **(c)** It allows the computer to run without electricity.
- **(d)** It automatically translates English prompts into French.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Understand`  
> **Technical Rationale**: Unfused operators write intermediate tensors back to main memory, only for the next operator to immediately read them back. Fusing operators keeps intermediate values in registers, eliminating memory bandwidth bottlenecks.

---

#### Question 46
Which Python library provides a lightweight, asynchronous, high-performance web framework widely adopted for production LLM model serving?

- **(a)** Tkinter
- **(b)** **[CORRECT]** FastAPI
- **(c)** Pygame
- **(d)** Matplotlib

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: FastAPI is built on Starlette and Pydantic, supporting asynchronous concurrency (`async`/`await`), streaming responses, and automatic OpenAPI documentation, making it the industry standard for LLM serving wrappers.

---

#### Question 47
In distributed PyTorch training, what role does the `rank` parameter play?

- **(a)** It indicates the salary tier of the system administrator.
- **(b)** **[CORRECT]** It provides a unique integer identifier ($0$ to $N-1$) for each individual process participating in the distributed communication group.
- **(c)** It sets the display brightness of the monitor.
- **(d)** It specifies the number of hard drives in the RAID array.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: In a distributed process group with world size $W$, each process is assigned an integer rank from $0$ to $W-1$. Rank 0 is designated as the master coordinator.

---

#### Question 48
What is a 'Checkpoint' in the context of deep learning model training on an HPC cluster?

- **(a)** A security gate where students present ID cards.
- **(b)** **[CORRECT]** A saved serialization of model weights, optimizer states, epoch numbers, and scheduler states saved to persistent disk, allowing training to resume after hardware failures or Slurm time limits.
- **(c)** A type of network switch in the server rack.
- **(d)** A print statement in a loop.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: Checkpoints serialize the complete training state to persistent storage (e.g. Lustre / GPFS), safeguarding against cluster node failures and allowing jobs to be chained across time-limited Slurm allocations.

---

#### Question 49
What is the primary role of the tokenizer in an LLM pipeline?

- **(a)** To check if the user has paid their subscription fee.
- **(b)** **[CORRECT]** To segment raw text strings into discrete sub-word token units and map them to corresponding numerical vocabulary IDs suitable for tensor embedding lookup.
- **(c)** To convert Python functions into machine assembly.
- **(d)** To regulate the clock speed of the server RAM.

> **Correct Answer**: **(B)**  
> **Bloom's Cognitive Level**: `Knowledge`  
> **Technical Rationale**: Tokenizers (e.g. Byte-Pair Encoding, WordPiece) break text into sub-word tokens, translating human text into discrete integer token sequences that index into the model's embedding matrix.

---

#### Question 50
Why is synchronous All-Reduce gradient exchange a critical scaling challenge on clusters lacking high-bandwidth low-latency networking (like RoCE or InfiniBand)?

- **(a)** **[CORRECT]** Because standard gigabit Ethernet switches lack sufficient packet forwarding bandwidth, causing accelerators to sit idle waiting for gradient synchronization and causing parallel efficiency to collapse.
- **(b)** Because gigabit Ethernet switches delete random numbers.
- **(c)** Because PyTorch does not support Ethernet.
- **(d)** Because Slurm only runs over fiber optic cables.

> **Correct Answer**: **(A)**  
> **Bloom's Cognitive Level**: `Analyze`  
> **Technical Rationale**: Synchronous DDP requires all nodes to synchronize gradients after every forward/backward pass. Low-bandwidth networking (e.g. 1GbE / 10GbE) introduces high transfer latency, dominating iteration time and stalling high-throughput compute engines.

---

