# 🏛️ GLA UNIVERSITY, MATHURA — DEPARTMENT OF COMPUTER SCIENCE & ENGINEERING
## HPC Masterclass | Day 5 Pre-Assessment Examination Paper
**Course**: B.Tech CSE 7th Sem — High Performance Computing Masterclass  
**Module**: Day 5 — Generative AI, LLMs, Accelerators & Foundation Prerequisites  
**Duration**: 60 Minutes | **Total Questions**: 50 MCQs | **Maximum Marks**: 50  

**Student Name**: ___________________________ **Roll Number**: __________________ **Section**: ______

---

### 📝 Instructions for Candidates
1. All questions are compulsory. Each question carries exactly 1 mark.
2. Darken the appropriate circle on the OMR sheet or mark your answer clearly.
3. No negative marking is applicable.

---

#### Q01. What is the primary computational bottleneck in the standard scaled dot-product self-attention mechanism $\text{Softmax}(\frac{QK^T}{\sqrt{d_k}})V$ when scaling to very long context sequence lengths ($N$)?
- [ ] **(a)** Disk write I/O speed.
- [ ] **(b)** Quadratic time and memory complexity $\mathcal{O}(N^2)$ due to the computation and materialization of the full $N \times N$ attention weight matrix.
- [ ] **(c)** Ethernet packet MTU size.
- [ ] **(d)** Linear complexity $\mathcal{O}(N)$ in the final output projection.

#### Q02. What is the primary numerical difference between IEEE 754 standard FP16 (Half Precision) and Google/Intel Bfloat16 (Brain Floating Point)?
- [ ] **(a)** FP16 uses 16 bits; BF16 uses 32 bits.
- [ ] **(b)** FP16 allocates 5 exponent bits and 10 mantissa bits, whereas BF16 allocates 8 exponent bits and 7 mantissa bits, giving BF16 the exact same dynamic range as standard FP32.
- [ ] **(c)** FP16 cannot represent negative numbers.
- [ ] **(d)** BF16 uses fixed-point integer arithmetic.

#### Q03. In general matrix multiplication (GEMM: $C = \alpha A \cdot B + \beta C$), where $A \in \mathbb{R}^{M \times K}$ and $B \in \mathbb{R}^{K \times N}$, how many total floating-point arithmetic operations (multiply-adds) are performed?
- [ ] **(a)** $M \times N$
- [ ] **(b)** $2 \cdot M \cdot N \cdot K$ floating-point operations (FLOPs)
- [ ] **(c)** $M + N + K$
- [ ] **(d)** $(M \cdot K)^2$

#### Q04. What is the definition of 'Arithmetic Intensity' in the Roofline Model of computer architecture?
- [ ] **(a)** The clock frequency of the CPU measured in GHz.
- [ ] **(b)** The ratio of floating-point operations performed to the total bytes of data transferred from main DRAM memory (FLOPs/Byte).
- [ ] **(c)** The number of cores per processor socket.
- [ ] **(d)** The total electrical power consumed per floating-point addition.

#### Q05. Why is the Prompt Prefill phase of LLM inference compute-bound, whereas the subsequent autoregressive Token Generation phase is memory-bandwidth bound?
- [ ] **(a)** Prefill runs on GPUs, while generation runs on hard drives.
- [ ] **(b)** Prefill processes all input prompt tokens concurrently as a large matrix-matrix multiplication (GEMM) with high arithmetic intensity, while generation processes one token at a time as a matrix-vector product (GEMV) requiring full weight streaming for a single token.
- [ ] **(c)** Generation uses double-precision floats, while prefill uses integers.
- [ ] **(d)** Prefill bypasses the attention mechanism entirely.

#### Q06. What is the primary function of a systolic array in AI accelerator hardware (such as Google TPU or Intel AMX TMUL)?
- [ ] **(a)** To sort database records using quicksort.
- [ ] **(b)** To stream data through a 2D grid of tightly-coupled processing elements, reusing inputs and intermediate weights directly between neighboring registers without continually reading and writing to the central register file.
- [ ] **(c)** To convert analog signals from microphones into digital audio.
- [ ] **(d)** To route TCP/IP packets between network switches.

#### Q07. What is the memory size in bytes required to store 7 billion model parameters in standard FP32 precision?
- [ ] **(a)** 7.0 GB
- [ ] **(b)** 14.0 GB
- [ ] **(c)** 28.0 GB (since each FP32 parameter occupies 4 bytes)
- [ ] **(d)** 56.0 GB

#### Q08. In the Transformer architecture, what is the role of the Key-Value (KV) cache during autoregressive inference?
- [ ] **(a)** It stores database passwords securely in memory.
- [ ] **(b)** It caches the computed Key and Value projection tensors of previously processed tokens so that past token representations do not have to be recomputed from scratch at every new token generation step.
- [ ] **(c)** It compiles Python functions into assembly code.
- [ ] **(d)** It compresses the text prompt using Huffman encoding.

#### Q09. What is the fundamental difference between Post-Training Quantization (PTQ) and Quantization-Aware Training (QAT)?
- [ ] **(a)** PTQ requires retraining the entire model on ImageNet; QAT does not.
- [ ] **(b)** PTQ quantizes an already-trained model's weights and activations using a small calibration dataset without retraining, whereas QAT models quantization noise during training using fake-quantization operators so the model adapts its weights to low-precision rounding.
- [ ] **(c)** PTQ only runs on mobile phones; QAT only runs on supercomputers.
- [ ] **(d)** QAT is strictly for image models, while PTQ is strictly for audio.

#### Q10. In symmetric uniform quantization of a real-valued tensor $x \in [-x_{max}, x_{max}]$ into signed $b$-bit integer representation, how is the scale factor $S$ defined?
- [ ] **(a)** $S = \frac{x_{max}}{2^{b-1} - 1}$
- [ ] **(b)** $S = x_{max} \times 2^b$
- [ ] **(c)** $S = \frac{2^b}{x_{max}}$
- [ ] **(d)** $S = \sqrt{x_{max}}$

#### Q11. What is the primary advantage of Asymmetric Quantization over Symmetric Quantization?
- [ ] **(a)** It eliminates the need for floating-point numbers.
- [ ] **(b)** It supports arbitrary asymmetric distributions (where min and max values differ significantly from zero, such as post-ReLU activations $[0, x_{max}]$) by introducing a non-zero integer Zero-Point ($Z$) offset.
- [ ] **(c)** It makes matrix multiplication 10x faster.
- [ ] **(d)** It requires only 1 bit per parameter.

#### Q12. What is the role of the Intel OpenVINO Model Optimizer?
- [ ] **(a)** To download models from torrent networks.
- [ ] **(b)** To convert source deep learning models (PyTorch, TensorFlow, ONNX) into hardware-optimized OpenVINO Intermediate Representation (IR) graphs.
- [ ] **(c)** To overclock CPU clock frequencies.
- [ ] **(d)** To compile Linux kernel device drivers.

#### Q13. Which Linux utility displays available CPU core topologies, NUMA nodes, and cache sizes?
- [ ] **(a)** `lscpu`
- [ ] **(b)** `lsusb`
- [ ] **(c)** `lsblk`
- [ ] **(d)** `lspci`

#### Q14. In high-performance interconnects for AI clusters, what does RDMA (Remote Direct Memory Access) achieve?
- [ ] **(a)** It automatically cleans dust from server heatsinks.
- [ ] **(b)** It enables an accelerator or server to directly access memory on a remote node without involving the operating system kernel or CPU on either side, achieving microsecond latency and zero-copy throughput.
- [ ] **(c)** It doubles the physical capacity of DDR5 RAM modules.
- [ ] **(d)** It replaces Ethernet switches with Bluetooth beacons.

#### Q15. What protocol brings RDMA capabilities over standard enterprise Ethernet infrastructure?
- [ ] **(a)** FTP
- [ ] **(b)** RoCE (RDMA over Converged Ethernet)
- [ ] **(c)** SMTP
- [ ] **(d)** Telnet

#### Q16. In deep learning distributed training, what collective communication operation combines gradient tensors from all participating nodes by summing them and distributes the identical result to all nodes?
- [ ] **(a)** All-to-All
- [ ] **(b)** All-Reduce
- [ ] **(c)** Broadcast
- [ ] **(d)** Gather

#### Q17. Why is Full Parameter Fine-Tuning of a 70B parameter model prohibitively expensive on standard academic HPC clusters?
- [ ] **(a)** Because Python limits variable names to 10 characters.
- [ ] **(b)** Because updating all parameters using an AdamW optimizer requires storing model weights (140GB in FP16), gradients (140GB), and first/second optimizer momentum states (560GB in FP32), totaling over 840 GB of accelerator memory solely for training states.
- [ ] **(c)** Because 70B models can only run on quantum computers.
- [ ] **(d)** Because Slurm cannot schedule jobs longer than 15 minutes.

#### Q18. What is the primary concept behind Parameter-Efficient Fine-Tuning (PEFT)?
- [ ] **(a)** Deleting half the training dataset to accelerate training.
- [ ] **(b)** Freezing the vast majority of pre-trained model parameters and fine-tuning only a tiny fraction (typically < 1%) of existing or newly added parameters for downstream domain tasks.
- [ ] **(c)** Replacing all attention layers with convolutional layers.
- [ ] **(d)** Training the model using random number generators.

#### Q19. What is the rank $r$ in LoRA (Low-Rank Adaptation)?
- [ ] **(a)** The military rank of the lead AI researcher.
- [ ] **(b)** The inner dimension of low-rank matrices $A \in \mathbb{R}^{r \times k}$ and $B \in \mathbb{R}^{d \times r}$, controlling the capacity and parameter count of the adaptation update.
- [ ] **(c)** The number of GPU cards in the cluster.
- [ ] **(d)** The total number of sentences in the training dataset.

#### Q20. In the Slurm workload manager, which command is used to query the status of all active queues, partitions, and cluster nodes?
- [ ] **(a)** `sinfo`
- [ ] **(b)** `srun`
- [ ] **(c)** `scancel`
- [ ] **(d)** `sbatch`

#### Q21. Which Slurm command prints the current queue of running and pending jobs?
- [ ] **(a)** `squeue`
- [ ] **(b)** `salloc`
- [ ] **(c)** `top`
- [ ] **(d)** `kill`

#### Q22. What does the Top-Down Microarchitecture Analysis Method (TMAM) Front-End Bound metric signify?
- [ ] **(a)** The server's front bezel door is unlocked.
- [ ] **(b)** The CPU core pipeline is stalled because the front-end fetch and decode units cannot deliver instructions (uOps) fast enough to the execution engine (e.g., due to instruction cache misses, ITLB misses, or branch target buffer stalls).
- [ ] **(c)** The frontend web browser has crashed.
- [ ] **(d)** The power supply cable is disconnected.

#### Q23. What is the typical memory bandwidth of high-end DDR5 server memory compared to High Bandwidth Memory (HBM2e / HBM3)?
- [ ] **(a)** DDR5 is 100x faster than HBM3.
- [ ] **(b)** DDR5 server channels typically deliver $\sim 300\text{--}400$ GB/s aggregate bandwidth across 8 channels, whereas HBM delivers $\sim 2\text{--}3.5$ TB/s per accelerator chip.
- [ ] **(c)** Both have exactly identical bandwidth.
- [ ] **(d)** HBM can only store 512 kilobytes of data.

#### Q24. In neural network quantization, what is an 'outlier feature' in activations?
- [ ] **(a)** A bug in the Python interpreter.
- [ ] **(b)** A very small number of activation channels that systematically exhibit activation magnitudes up to 100x larger than normal channels across all sequence positions.
- [ ] **(c)** A network cable that has fallen out of a switch port.
- [ ] **(d)** An erroneous token generated during translation.

#### Q25. What is the primary role of the Softmax function in self-attention?
- [ ] **(a)** To invert a matrix.
- [ ] **(b)** To normalize raw attention logit scores across the sequence dimension into a valid probability distribution where all weights are non-negative and sum to 1.0.
- [ ] **(c)** To convert text tokens into ASCII code points.
- [ ] **(d)** To encrypt tensor values for network transmission.

#### Q26. In OpenVINO, what is the 'CPU plugin'?
- [ ] **(a)** A physical hardware card inserted into a PCIe slot.
- [ ] **(b)** A runtime dynamic library (`openvino_intel_cpu_plugin.so`) that maps OpenVINO IR graph nodes to highly optimized execution primitives running on x86/ARM CPU cores using oneDNN, AVX-512, and AMX.
- [ ] **(c)** A browser extension for Google Chrome.
- [ ] **(d)** A compiler for HTML and JavaScript.

#### Q27. How many total bits are required to store one single numerical value in INT4 representation?
- [ ] **(a)** 1 bit
- [ ] **(b)** 4 bits (half a byte, allowing 16 discrete states: $-8$ to $+7$ or $0$ to $15$)
- [ ] **(c)** 8 bits
- [ ] **(d)** 16 bits

#### Q28. If a weight tensor contains 1,000,000 parameters, how much memory does it consume in FP16 versus INT4 (excluding metadata)?
- [ ] **(a)** 2 MB in FP16 vs 0.5 MB (500 KB) in INT4
- [ ] **(b)** 10 MB in FP16 vs 1 MB in INT4
- [ ] **(c)** 4 MB in FP16 vs 2 MB in INT4
- [ ] **(d)** 16 MB in FP16 vs 8 MB in INT4

#### Q29. In LLM generation metrics, what is 'Time-to-First-Token' (TTFT)?
- [ ] **(a)** The time taken to train the foundation model from scratch.
- [ ] **(b)** The total latency elapsed from the moment a user submits an input prompt until the first token of the response is generated and emitted by the server.
- [ ] **(c)** The duration of the server's nightly reboot cycle.
- [ ] **(d)** The time required to compress a model with NNCF.

#### Q30. In LLM generation metrics, what is 'Inter-Token Latency' (ITL)?
- [ ] **(a)** The time elapsed between generating consecutive output tokens during the autoregressive decode phase.
- [ ] **(b)** The physical network latency between two transatlantic subsea fiber cables.
- [ ] **(c)** The time it takes to allocate memory for the PyTorch runtime.
- [ ] **(d)** The idle time between consecutive student lab sessions.

#### Q31. What is the primary difference between Data Parallelism and Tensor Parallelism in distributed deep learning?
- [ ] **(a)** Data parallelism partitions different training dataset batches across multiple accelerators; Tensor parallelism shards individual weight matrices and layers across multiple accelerators within a single model step.
- [ ] **(b)** Data parallelism runs only on CPUs; Tensor parallelism runs only on mobile phones.
- [ ] **(c)** Data parallelism trains image models; Tensor parallelism trains audio models.
- [ ] **(d)** Data parallelism does not use network cables.

#### Q32. What happens when an LLM context length exceeds the physical memory capacity of the allocated KV-cache?
- [ ] **(a)** The model becomes infinitely intelligent.
- [ ] **(b)** The system throws an Out-Of-Memory (OOM) error, or must evict/truncate earlier context tokens (e.g., via sliding window attention) to prevent an unhandled memory fault.
- [ ] **(c)** The CPU doubles its clock frequency.
- [ ] **(d)** The output language switches automatically to German.

#### Q33. What is the purpose of the `optimum-intel` open-source library from Hugging Face and Intel?
- [ ] **(a)** To replace the Linux bash terminal with a GUI.
- [ ] **(b)** To provide seamless integration between the Hugging Face Transformers ecosystem and Intel hardware acceleration libraries, including OpenVINO and IPEX (Intel Extension for PyTorch).
- [ ] **(c)** To write synthetic benchmark reports for marketing.
- [ ] **(d)** To flash motherboard BIOS chips.

#### Q34. What is 'Non-Uniform Memory Access' (NUMA) in multi-socket enterprise servers?
- [ ] **(a)** A bug in the memory controller that corrupts data randomly.
- [ ] **(b)** A computer memory design where a processor core can access its own local memory socket faster than non-local memory attached to another processor socket.
- [ ] **(c)** A type of flash memory used in digital cameras.
- [ ] **(d)** A software library for rendering 3D animations.

#### Q35. Why is the Bfloat16 format preferred over FP16 during distributed training of Large Language Models?
- [ ] **(a)** Because BF16 requires half as many bits as FP16.
- [ ] **(b)** Because BF16's wide 8-bit dynamic range matches FP32, preventing gradient vanishing or gradient explosion during mixed-precision training without requiring complex dynamic loss scaling.
- [ ] **(c)** Because BF16 was invented in 1965.
- [ ] **(d)** Because BF16 can only run on single-core CPUs.

#### Q36. In OpenVINO IR files, what information is stored in the `.xml` file?
- [ ] **(a)** Raw floating-point tensor weight arrays.
- [ ] **(b)** The computational topology graph: nodes (operations), edges (data tensors), shapes, datatypes, and runtime parameters.
- [ ] **(c)** A compiled Linux kernel executable.
- [ ] **(d)** The student's attendance records.

#### Q37. What mathematical operation does the Self-Attention mechanism perform to measure token similarity?
- [ ] **(a)** Dot product between Query and Key vectors ($Q \cdot K^T$).
- [ ] **(b)** Bitwise XOR between token ASCII codes.
- [ ] **(c)** Fast Fourier Transform on prompt text.
- [ ] **(d)** Integer division of token IDs.

#### Q38. What is the primary role of Layer Normalization (or RMSNorm) in transformer layers?
- [ ] **(a)** To sort the tokens alphabetically.
- [ ] **(b)** To stabilize hidden state activation dynamics and gradients across training by normalizing activations across the feature dimension for each token independently.
- [ ] **(c)** To decrease CPU fan speed.
- [ ] **(d)** To encrypt model outputs.

#### Q39. How many total bits are used by an INT8 signed integer?
- [ ] **(a)** 4 bits
- [ ] **(b)** 8 bits (1 byte, representing $-128$ to $+127$)
- [ ] **(c)** 16 bits
- [ ] **(d)** 32 bits

#### Q40. In the context of HPC Slurm clusters, what is an 'Allocation'?
- [ ] **(a)** An administrative punishment for violating computer lab rules.
- [ ] **(b)** A dedicated set of compute nodes, CPU cores, memory, and accelerator resources granted by the Slurm controller to a specific job for a bounded duration.
- [ ] **(c)** A financial grant from the government.
- [ ] **(d)** A software license file stored in `/etc`.

#### Q41. What is the primary limitation of static batching during high-concurrency LLM serving?
- [ ] **(a)** It crashes the network switch.
- [ ] **(b)** Compute slots are wasted on padding tokens, and high-latency generation requests block newly arrived requests from entering execution until the entire batch finishes.
- [ ] **(c)** It cannot run on Linux systems.
- [ ] **(d)** It requires models to have fewer than 1,000 parameters.

#### Q42. What is the function of the `torch.no_grad()` context manager in PyTorch during LLM inference?
- [ ] **(a)** It disables student grade recording in the university database.
- [ ] **(b)** It deactivates the PyTorch autograd engine, preventing the allocation and caching of intermediate activations for gradient backpropagation and significantly reducing memory usage.
- [ ] **(c)** It converts PyTorch code into C++.
- [ ] **(d)** It shuts down the GPU.

#### Q43. What does 'Perplexity' measure in language modeling evaluation?
- [ ] **(a)** The physical temperature of the server CPU heatsink.
- [ ] **(b)** The exponentiated cross-entropy loss over a validation corpus, quantifying how surprised or uncertain the language model is when predicting the next token.
- [ ] **(c)** The network ping time between two HPC nodes.
- [ ] **(d)** The number of syntax errors in a Python program.

#### Q44. What is the theoretical speedup in weights transfer time when moving from FP16 weights to INT4 weights on a memory-bandwidth-bound inference engine?
- [ ] **(a)** 1.5x
- [ ] **(b)** 4.0x (since INT4 uses 4 bits per weight while FP16 uses 16 bits per weight)
- [ ] **(c)** 10.0x
- [ ] **(d)** 100.0x

#### Q45. What is the primary benefit of Operator Fusion (such as fusing Bias-Add, Scale, and ReLU into a single kernel) in deep learning inference engines?
- [ ] **(a)** It decreases the font size of the code.
- [ ] **(b)** It eliminates intermediate read/write round-trips to DRAM or high-level caches, executing consecutive operations directly within on-chip CPU/accelerator registers.
- [ ] **(c)** It allows the computer to run without electricity.
- [ ] **(d)** It automatically translates English prompts into French.

#### Q46. Which Python library provides a lightweight, asynchronous, high-performance web framework widely adopted for production LLM model serving?
- [ ] **(a)** Tkinter
- [ ] **(b)** FastAPI
- [ ] **(c)** Pygame
- [ ] **(d)** Matplotlib

#### Q47. In distributed PyTorch training, what role does the `rank` parameter play?
- [ ] **(a)** It indicates the salary tier of the system administrator.
- [ ] **(b)** It provides a unique integer identifier ($0$ to $N-1$) for each individual process participating in the distributed communication group.
- [ ] **(c)** It sets the display brightness of the monitor.
- [ ] **(d)** It specifies the number of hard drives in the RAID array.

#### Q48. What is a 'Checkpoint' in the context of deep learning model training on an HPC cluster?
- [ ] **(a)** A security gate where students present ID cards.
- [ ] **(b)** A saved serialization of model weights, optimizer states, epoch numbers, and scheduler states saved to persistent disk, allowing training to resume after hardware failures or Slurm time limits.
- [ ] **(c)** A type of network switch in the server rack.
- [ ] **(d)** A print statement in a loop.

#### Q49. What is the primary role of the tokenizer in an LLM pipeline?
- [ ] **(a)** To check if the user has paid their subscription fee.
- [ ] **(b)** To segment raw text strings into discrete sub-word token units and map them to corresponding numerical vocabulary IDs suitable for tensor embedding lookup.
- [ ] **(c)** To convert Python functions into machine assembly.
- [ ] **(d)** To regulate the clock speed of the server RAM.

#### Q50. Why is synchronous All-Reduce gradient exchange a critical scaling challenge on clusters lacking high-bandwidth low-latency networking (like RoCE or InfiniBand)?
- [ ] **(a)** Because standard gigabit Ethernet switches lack sufficient packet forwarding bandwidth, causing accelerators to sit idle waiting for gradient synchronization and causing parallel efficiency to collapse.
- [ ] **(b)** Because gigabit Ethernet switches delete random numbers.
- [ ] **(c)** Because PyTorch does not support Ethernet.
- [ ] **(d)** Because Slurm only runs over fiber optic cables.

