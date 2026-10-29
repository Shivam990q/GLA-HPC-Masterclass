# 🏛️ GLA UNIVERSITY, MATHURA — DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
## HPC Masterclass | Day 5 In-Class Checkpoint Assessment
**Course**: B.Tech CSE 7th Sem — High Performance Computing Masterclass  
**Module**: Day 5 — Generative AI & Large Language Models on HPC (Intel AMX, Habana Gaudi, OpenVINO IR & NNCF INT4)  
**Duration**: 30 Minutes | **Total Questions**: 25 MCQs | **Maximum Marks**: 25  

**Student Name**: ___________________________ **Roll Number**: __________________ **Section**: ______

---

### 📝 Instructions for Candidates
1. All questions are compulsory. Each question carries exactly 1 mark.
2. Select the single best answer for each question.
3. No negative marking.

---

#### Q01. In Large Language Model (LLM) inference on modern server processors, why is the autoregressive token generation phase ('decode phase') classified as strictly memory-bandwidth bound rather than compute-bound?
- [ ] **(a)** Because the CPU halts its arithmetic logic units (ALUs) during token emission.
- [ ] **(b)** Because generating each new token requires streaming billions of model weight parameters and past KV-cache states from DRAM to on-chip caches for just a single batch of matrix-vector multiplications, resulting in an operational arithmetic intensity far below the machine's ridge point.
- [ ] **(c)** Because matrix multiplications cannot be performed on floating-point numbers.
- [ ] **(d)** Because the operating system requires an Ethernet handshake before each emitted token.

#### Q02. What is the primary microarchitectural purpose of Intel Advanced Matrix Extensions (AMX) introduced in 4th/5th Gen Intel Xeon Scalable processors (Sapphire Rapids / Emerald Rapids)?
- [ ] **(a)** To replace DDR5 memory controllers with optical transceivers.
- [ ] **(b)** To provide dedicated hardware 2D register tiles (TMM0-TMM7) and a systolic Tile Matrix Multiply Unit (TMUL) capable of performing 2,048 INT8 or 1,024 BF16 operations per cycle per core.
- [ ] **(c)** To convert Python bytecode into C++ at compile time.
- [ ] **(d)** To emulate ARM NEON instructions on x86 servers.

#### Q03. In the context of the Habana Gaudi 2 and Gaudi 3 deep learning accelerators, how is scale-out inter-node communication uniquely implemented compared to traditional GPU architectures?
- [ ] **(a)** Through standard USB-C external dongles connected to each server chassis.
- [ ] **(b)** By integrating 24 standard 100GbE (Gaudi 2) or 200GbE (Gaudi 3) RDMA over Converged Ethernet (RoCE v2) network ports directly onto each accelerator die, eliminating external PCIe NIC bottlenecks and vendor-proprietary switch lock-in.
- [ ] **(c)** Using optical fiber cables plugged directly into the CPU L3 cache controller.
- [ ] **(d)** By writing all intermediate tensors to local SATA hard drives for cluster exchange.

#### Q04. What two primary artifacts constitute the OpenVINO Intermediate Representation (IR) format produced when compiling a deep learning model?
- [ ] **(a)** A `.zip` archive containing Python source code and a Dockerfile.
- [ ] **(b)** An XML file (`.xml`) describing the network topology and computational graph, accompanied by a binary file (`.bin`) storing the optimized tensor weights and biases.
- [ ] **(c)** A `.json` configuration file and a `.tar.gz` Linux kernel image.
- [ ] **(d)** A C++ header file (`.h`) and an executable binary (`.elf`).

#### Q05. When applying Weight-Only INT4 Quantization using Intel NNCF (Neural Network Compression Framework) on an LLM, why are the attention projections and MLP weights quantized to INT4 while activations remain in FP16 / BF16?
- [ ] **(a)** Because INT4 activations are illegal under IEEE floating-point standards.
- [ ] **(b)** Because quantizing activations dynamically requires complex runtime calibration and can severely degrade model perplexity, whereas quantizing static weights alone cuts DRAM bandwidth consumption by ~4x with negligible loss in accuracy during memory-bound decoding.
- [ ] **(c)** Because OpenVINO cannot perform integer multiplication.
- [ ] **(d)** Because NNCF only supports convolution layers, not dense layers.

#### Q06. In the mathematical formulation of Low-Rank Adaptation (LoRA), given a frozen weight matrix $W_0 \in \mathbb{R}^{d \times k}$, how is the updated weight matrix $W$ parameterized during fine-tuning?
- [ ] **(a)** $W = W_0 \times (B + A)$
- [ ] **(b)** $W = W_0 + \Delta W = W_0 + \frac{\alpha}{r} (B \cdot A)$, where $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times k}$, and rank $r \ll \min(d, k)$.
- [ ] **(c)** $W = \frac{W_0}{\alpha \cdot r} + \log(B \cdot A)$
- [ ] **(d)** $W = W_0 - (A^T \cdot B^T)$

#### Q07. Calculate the theoretical KV-cache memory required for a 7-billion parameter transformer model with 32 layers, 32 attention heads, hidden dimension 4,096 ($d_{head} = 128$), running at FP16 (2 bytes per element), with a batch size of 8 and a context sequence length of 2,048 tokens.
- [ ] **(a)** 128 MB
- [ ] **(b)** 1.0 GB
- [ ] **(c)** 2.15 GB (approximately $2.0 \times 10^9$ bytes)
- [ ] **(d)** 64.0 GB

#### Q08. What is the primary role of the Habana SynapseAI Graph Compiler when executing PyTorch code on Gaudi HPUs via Lazy Mode (`PT_HPU_LAZY_MODE=1`)?
- [ ] **(a)** It translates Python syntax directly into HTML web documentation.
- [ ] **(b)** It traces PyTorch operations across multiple execution steps, constructs an optimized computational Directed Acyclic Graph (DAG), fuses compatible tensor kernels, schedules DMA transfers, and dispatches compiled recipes to the HPU engines with minimal host CPU intervention.
- [ ] **(c)** It forces PyTorch to execute in eager mode with line-by-line CPU synchronization.
- [ ] **(d)** It downsamples image datasets to thumbnail resolution before training.

#### Q09. Which specific OpenVINO execution plugin should be targeted to leverage Intel AMX acceleration on 4th or 5th Gen Intel Xeon Scalable processors?
- [ ] **(a)** `core.compile_model(model, 'GPU')`
- [ ] **(b)** `core.compile_model(model, 'CPU')` with execution precision set to `ov::element::bf16` or `ov::element::i8`.
- [ ] **(c)** `core.compile_model(model, 'NPU_V1')`
- [ ] **(d)** `core.compile_model(model, 'FPGA_BITSTREAM')`

#### Q10. What is the key functional difference between Continuous Batching (also known as Iteration-Level Batching) and traditional Static Batching in LLM serving engines?
- [ ] **(a)** Continuous batching requires all requests in a batch to have identical prompt lengths and generation lengths.
- [ ] **(b)** Continuous batching dynamically inserts newly arriving requests into the active iteration loop and evicts finished requests immediately upon emitting an EOS token, eliminating padding overhead and GPU idle time.
- [ ] **(c)** Continuous batching runs only on single-core microcontrollers.
- [ ] **(d)** Static batching generates tokens 10x faster than continuous batching.

#### Q11. In the Slurm workload manager, what does the directive `#SBATCH --gres=habana:8` specify when submitting a distributed training job?
- [ ] **(a)** It requests 8 gigabytes of RAM from the cluster master node.
- [ ] **(b)** It requests 8 generic accelerator resources (Habana Gaudi HPUs) allocated exclusively to the job on each assigned compute node.
- [ ] **(c)** It forces Slurm to rerun the job 8 times upon failure.
- [ ] **(d)** It sets the network timeout threshold to 8 minutes.

#### Q12. Which of the following quantization algorithms supported by Intel NNCF selectively identifies salient weight channels that correspond to large activation outliers and preserves their precision to maintain generative accuracy in INT4?
- [ ] **(a)** AWQ (Activation-aware Weight Quantization)
- [ ] **(b)** Random Uniform Dithering
- [ ] **(c)** Binary Thresholding
- [ ] **(d)** Zero-Order Linear Extrapolation

#### Q13. In Habana Gaudi architecture, what is the role of the Matrix Multiplication Engine (MME) versus the Tensor Processor Core (TPC)?
- [ ] **(a)** MME handles disk I/O, while TPC renders 3D graphics.
- [ ] **(b)** MME is a dedicated fixed-function systolic engine optimized for dense matrix multiplications and convolutions, while TPC is a fully programmable VLIW SIMD processor handling activations, normalizations, and custom non-linear tensor ops.
- [ ] **(c)** MME handles network packets; TPC manages CPU cooling fans.
- [ ] **(d)** TPC performs matrix multiplications, while MME compiles Python scripts.

#### Q14. Why is PagedAttention (as implemented in modern LLM serving engines) considered an architectural breakthrough for KV-cache memory management?
- [ ] **(a)** It eliminates the need for any KV-cache in transformer models.
- [ ] **(b)** It borrows the classic OS virtual memory paging concept to store KV-cache tensors in non-contiguous physical memory blocks, completely eliminating internal and external memory fragmentation and enabling near-zero memory waste (~4%).
- [ ] **(c)** It writes all attention matrices directly to NVMe SSDs.
- [ ] **(d)** It doubles the parameter count of the underlying neural network.

#### Q15. What command-line tool in the Habana Gaudi SynapseAI software stack provides real-time monitoring of HPU temperature, memory consumption, engine utilization, and power draw?
- [ ] **(a)** `nvidia-smi`
- [ ] **(b)** `hl-smi`
- [ ] **(c)** `rocm-smi`
- [ ] **(d)** `top-hpc`

#### Q16. When serving an OpenVINO LLM pipeline via a FastAPI microservice, what is the key architectural advantage of returning an asynchronous `StreamingResponse` using an `AsyncIterator` over returning a standard JSON response?
- [ ] **(a)** It encrypts the payload using AES-256 before transmission.
- [ ] **(b)** It yields generated tokens over an HTTP/1.1 chunked transfer stream immediately as they are decoded, drastically reducing Time-to-First-Token (TTFT) perceived latency from seconds to milliseconds for end users.
- [ ] **(c)** It forces the client browser to refresh the webpage automatically.
- [ ] **(d)** It converts text tokens into WAV audio files.

#### Q17. What does 'Group Size' (e.g., `group_size = 128`) mean when configuring INT4 weight quantization in NNCF or GPTQ?
- [ ] **(a)** The number of students working together on a single HPC node.
- [ ] **(b)** The number of consecutive weight elements along a channel that share a single floating-point scale factor and zero-point offset.
- [ ] **(c)** The number of CPU sockets installed on the server motherboard.
- [ ] **(d)** The total count of attention layers in the transformer model.

#### Q18. In a distributed Gaudi cluster running DeepSpeed or PyTorch FSDP (Fully Sharded Data Parallel), what does 'ZeRO Stage 3' shard across all cluster nodes?
- [ ] **(a)** Only the Python script source code files.
- [ ] **(b)** Optimizer states, gradients, and model parameters (weights), so that each accelerator only stores $1/N$ of the total model state during forward and backward passes.
- [ ] **(c)** The Linux operating system kernel image.
- [ ] **(d)** Only the validation dataset images.

#### Q19. What is the primary function of the OpenVINO Model Optimizer / `optimum-cli export openvino` tool when ingesting a Hugging Face PyTorch model?
- [ ] **(a)** It deletes all layers containing linear transformations to save disk space.
- [ ] **(b)** It traces the PyTorch model graph, performs hardware-agnostic optimizations (such as dead-code elimination, constant folding, and operator fusion), and serializes the network into the OpenVINO IR format (`.xml` and `.bin`).
- [ ] **(c)** It automatically generates a PowerPoint presentation explaining the model.
- [ ] **(d)** It uploads the model to a public FTP server.

#### Q20. If an LLM running on an Intel Xeon CPU achieves a Time-to-First-Token (TTFT) of 150 ms and an Inter-Token Latency (ITL) of 25 ms, what is its generation throughput in Tokens Per Second (TPS) during the decode phase?
- [ ] **(a)** 4.0 TPS
- [ ] **(b)** 40.0 TPS
- [ ] **(c)** 6.67 TPS
- [ ] **(d)** 150.0 TPS

#### Q21. In QLoRA (Quantized Low-Rank Adaptation), what innovative 4-bit data type is introduced to quantize the frozen base model weights without sacrificing zero-mean normal distribution fidelity?
- [ ] **(a)** IEEE 754 Single Precision
- [ ] **(b)** NormalFloat 4 (NF4)
- [ ] **(c)** Standard BCD (Binary Coded Decimal)
- [ ] **(d)** Signed 4-bit Twos Complement Integer

#### Q22. What is the primary purpose of the `compile_and_run_all.sh` test harness script in an HPC lab environment?
- [ ] **(a)** To wipe the cluster file system and restore factory settings.
- [ ] **(b)** To systematically validate environment dependencies, compile native/Python code, execute benchmarking workloads, and output rigorous PASS/FAIL assertions with execution timestamps.
- [ ] **(c)** To mine cryptocurrencies during idle server hours.
- [ ] **(d)** To shut down the server power supply safely.

#### Q23. How does Intel OpenVINO runtime achieve multi-socket CPU scaling on dual-socket 4th Gen Intel Xeon servers?
- [ ] **(a)** By turning off NUMA support in the server BIOS.
- [ ] **(b)** By partitioning threads into NUMA-aware execution streams (`ov::num_streams`), binding inference worker streams to localized CPU cores and memory nodes to avoid costly cross-socket UPI interconnect traffic.
- [ ] **(c)** By running one copy of Windows and one copy of Linux concurrently.
- [ ] **(d)** By duplicating all model weights across CPU L1 caches.

#### Q24. When configuring a multi-node Gaudi training job on Slurm, which environment variable ensures that PyTorch communications use Habana Collective Communications Library (HCCL) over RoCE interfaces?
- [ ] **(a)** `NCCL_DEBUG=INFO`
- [ ] **(b)** `HCCL_OVER_OFI=1` and `PT_HPU_ENABLE_LAZY_COLLECTIVES=true`
- [ ] **(c)** `CUDA_VISIBLE_DEVICES=none`
- [ ] **(d)** `MPI_BYPASS_ALL=1`

#### Q25. Why is INT4 weight-only quantization superior to INT8 weight-only quantization for LLM serving on memory-bandwidth-limited edge and server CPUs?
- [ ] **(a)** Because INT4 requires zero CPU power consumption.
- [ ] **(b)** Because INT4 cuts the weight tensor size in half compared to INT8 (and 4x compared to FP16), halving the bytes that must be read across the DDR5 memory bus per emitted token and translating directly to a near-2x boost in decode throughput.
- [ ] **(c)** Because INT4 models cannot produce hallucinations.
- [ ] **(d)** Because INT4 completely disables the softmax operator.

