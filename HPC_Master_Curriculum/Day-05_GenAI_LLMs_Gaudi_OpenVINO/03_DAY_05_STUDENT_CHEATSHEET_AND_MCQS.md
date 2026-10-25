# 📝 DAY 5: STUDENT QUICK REFERENCE & OFFICIAL MCQ BANK
## 1-Page Cheat Sheet + 25 Evaluated Capstone Assessment Questions
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Lead Trainer:** Shivam Gupta | **Target Audience:** 60 B.Tech / M.Tech CS Students  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 📌 PART 1: 1-Page Student Command & Silicon Cheat Sheet

### 1. Silicon Architecture Comparison
| Hardware Platform | Core Microarchitecture | Primary Strength | Ideal Workload |
| :--- | :--- | :--- | :--- |
| **Intel Xeon Scalable CPU** | 32-64 High-Clock Cores + AMX Tile Matrix Engines | Agile, low-latency, general orchestration, large DDR5 RAM | Preprocessing, general enterprise inference, mixed ML/DL |
| **Intel Data Center GPU Max** | 128 Xe-Cores + 1024-bit Vector Engines | Massive FP32/FP16 SIMD parallelism, high concurrency | Computer vision, dense GEMM, 3D simulation |
| **Habana Gaudi 2 / Gaudi 3** | 24 Tensor Processor Cores (TPC) + 96-128GB HBM | 24x 100GbE RoCE on-die networking, massive tensor contraction | Large-scale distributed LLM training & fine-tuning |

### 2. OpenVINO LLM Compression Workflow
```python
# 1. Convert PyTorch model to OpenVINO IR (.xml + .bin)
ov_model = ov.convert_model(model, example_input=inputs)

# 2. Compress weights to INT4 (Slashing memory bandwidth choke)
compressed = nncf.compress_weights(ov_model, mode=nncf.CompressWeightsMode.INT4_ASYM)

# 3. Save optimized model
ov.save_model(compressed, "model_int4.xml")

# 4. Run low-latency inference
pipe = ov_genai.LLMPipeline("model_int4", "CPU")
response = pipe.generate("Your prompt here")
```

### 3. Key LLM Metrics & Slurm Submission
- **TTFT (Time-To-First-Token):** Milliseconds taken to process prompt and emit token #1 (Prefill speed).
- **TPS (Tokens-Per-Second):** Number of text tokens generated per second during continuous generation (Decode speed).
- **LoRA Parameters:** Retaining >99% base model frozen weights while updating low-rank adapter matrices $A$ and $B$.

---

## 🎯 PART 2: Day 5 Official Syllabus Checklist

- [ ] 01. Generative AI & Large Language Models on HPC architectures
- [ ] 02. Auto-regressive decoding & transformer memory wall
- [ ] 03. Prefill phase (compute-bound) vs Decode phase (memory-bandwidth bound)
- [ ] 04. KV-Cache memory consumption formula and scaling
- [ ] 05. Intel Xeon Sapphire Rapids Advanced Matrix Extensions (AMX)
- [ ] 06. AMX tile registers (TMM0-TMM7) and TMUL systolic execution
- [ ] 07. Habana Gaudi architecture (TPCs, MME engines, HBM bandwidth)
- [ ] 08. On-die 24x 100GbE RoCE networking vs external PCIe switches
- [ ] 09. Intel OpenVINO Toolkit architecture & cross-silicon execution
- [ ] 10. Intermediate Representation (IR) file structure (`.xml` + `.bin`)
- [ ] 11. Weight-only quantization concepts (FP32 -> FP16 -> INT8 -> INT4)
- [ ] 12. NNCF (Neural Network Compression Framework) quantization workflow
- [ ] 13. Benchmarking TTFT (Time to First Token) and TPS (Tokens Per Second)
- [ ] 14. Full-parameter training vs Parameter-Efficient Fine-Tuning (PEFT)
- [ ] 15. LoRA (Low-Rank Adaptation) mathematical decomposition ($W = W_0 + B \cdot A$)
- [ ] 16. Multi-node Slurm job scheduling for distributed LoRA fine-tuning
- [ ] 17. Production microservice serving via streaming REST API endpoints

---

## 📝 PART 3: 25 Official Multiple-Choice Questions (With Answers & Explanations)

#### Q1. Why is the token decoding phase of Large Language Models considered memory-bandwidth bound?
- A) Because the model does zero matrix operations
- B) Because emitting each new token requires streaming all model weights from RAM into registers, yielding low arithmetic intensity
- C) Because the hard disk is constantly spinning
- D) Because Python strings are slow  
**Answer: B** | *Explanation: During single-token auto-regressive generation, arithmetic intensity is low (~1-2 FLOPs per byte loaded), causing compute units to starve while waiting for DRAM transfers.*

#### Q2. What hardware unit in 4th Gen Intel Xeon processors delivers up to 16x higher matrix multiplication throughput?
- A) Intel Turbo Boost
- B) Intel AMX (Advanced Matrix Extensions)
- C) Hyper-Threading
- D) QuickAssist Technology  
**Answer: B** | *Explanation: Intel AMX introduces dedicated 2D tile registers and a Tile Matrix Multiply Unit (TMUL) for INT8 and BF16 tensor math.*

#### Q3. What is the role of the KV-Cache in transformer inference?
- A) Caching user passwords
- B) Storing Key and Value projection vectors of previously computed tokens to avoid re-evaluating the entire prompt on every new token
- C) Storing the model weights on SSD
- D) Managing network socket buffers  
**Answer: B** | *Explanation: The KV-cache preserves past key/value states so attention only needs to be computed for the newest token.*

#### Q4. What is the key on-die architectural feature of Habana Gaudi that eliminates cluster networking bottlenecks?
- A) 24 integrated 100GbE RoCE (RDMA over Converged Ethernet) ports
- B) An integrated optical disc drive
- C) HDMI 2.1 video output
- D) Wi-Fi 7 wireless module  
**Answer: A** | *Explanation: Gaudi integrates 24x 100GbE RoCE network controllers directly onto the processor die, bypassing external PCIe switch latency.*

#### Q5. What does the Intel OpenVINO Toolkit Intermediate Representation (IR) consist of?
- A) A single `.exe` file
- B) An `.xml` file (network topology) and a `.bin` file (weights and biases)
- C) A `.py` source file only
- D) A `.pdf` documentation file  
**Answer: B** | *Explanation: OpenVINO IR splits the model into human-readable XML graph topology and binary tensor weights.*

#### Q6. What does NNCF Weight-Only INT4 quantization achieve on Large Language Models?
- A) Increases model file size by 4x
- B) Slashes weight memory footprint by ~70-75% with minimal accuracy degradation, drastically reducing DRAM transfer bottlenecks
- C) Converts text tokens into images
- D) Deletes 90% of model layers  
**Answer: B** | *Explanation: Compressing FP16 weights to 4-bit integers reduces the data moved over the memory bus by up to 75%, accelerating token generation.*

#### Q7. In Parameter-Efficient Fine-Tuning with LoRA, what happens to the base model weights?
- A) They are randomly deleted
- B) They are completely frozen, while two low-rank matrices ($A$ and $B$) are trained
- C) They are converted to float64
- D) They are retrained from scratch  
**Answer: B** | *Explanation: LoRA freezes pre-trained weights $W_0$ and adds trainable low-rank decomposition matrices $\Delta W = B \cdot A$.*

#### Q8. What does TTFT stand for in LLM benchmarking?
- A) Total Time For Training
- B) Time To First Token
- C) Tensor Transfer Fast Track
- D) Tile Type Floating Target  
**Answer: B** | *Explanation: Time To First Token measures latency between user prompt submission and the first emitted response token.*

#### Q9. If an LLM generates 150 tokens in 3 seconds after the first token, what is its generation throughput?
- A) 15 tokens/sec
- B) 50 tokens/sec
- C) 150 tokens/sec
- D) 450 tokens/sec  
**Answer: B** | *Explanation: Throughput = 150 tokens / 3 seconds = 50 tokens per second (TPS).*

#### Q10. Which Slurm directive requests 2 physical compute nodes for a distributed training job?
- A) `#SBATCH --partition=debug`
- B) `#SBATCH --nodes=2`
- C) `#SBATCH --memory=100G`
- D) `#SBATCH --cpus=2`  
**Answer: B** | *Explanation: `--nodes=2` instructs Slurm to allocate two discrete compute nodes.*

#### Q11. Which data type is natively supported by Intel AMX tile registers for mixed-precision neural network execution?
- A) Bfloat16 (BF16) and INT8
- B) Float128
- C) Boolean only
- D) Int64 only  
**Answer: A** | *Explanation: Intel AMX accelerates Bfloat16 floating-point and INT8 integer matrix math.*

#### Q12. In OpenVINO GenAI, which hardware device string targets local CPU execution?
- A) `"GPU"`
- B) `"CPU"`
- C) `"NPU"`
- D) `"RAM"`  
**Answer: B** | *Explanation: `"CPU"` directs OpenVINO to run kernels across host x86 CPU cores using AVX-512 and AMX.*

#### Q13. Why does LoRA drastically reduce the memory required during fine-tuning compared to full fine-tuning?
- A) It removes the tokenizer
- B) It drastically reduces optimizer states (like Adam moments $m$ and $v$) from billions of parameters to millions
- C) It compresses training text files into zip archives
- D) It runs only on single threads  
**Answer: B** | *Explanation: Adam optimizer maintains two 32-bit floats per trainable parameter; slashing trainable parameters by 99% slashes optimizer VRAM footprint.*

#### Q14. What does the term "Systolic Array" refer to in matrix acceleration hardware?
- A) A network of data registers that rhythmically pump data through processing units without returning to memory at each step
- B) A medical monitoring device
- C) An Ethernet packet sniffer
- D) An operating system file buffer  
**Answer: A** | *Explanation: Systolic arrays (used in Google TPUs and Intel AMX) stream data through 2D grids of Multiply-Accumulate units to maximize data reuse.*

#### Q15. Which Python framework is commonly used alongside OpenVINO for model weight compression?
- A) Flask
- B) NNCF (Neural Network Compression Framework)
- C) Django
- D) Beautiful Soup  
**Answer: B** | *Explanation: Intel NNCF provides state-of-the-art quantization, pruning, and sparsity algorithms.*

#### Q16. What is the memory footprint of an uncompressed 7-Billion parameter LLM in FP16 precision?
- A) ~700 MB
- B) ~7 GB
- C) ~14 GB
- D) ~70 GB  
**Answer: C** | *Explanation: In FP16, each parameter requires 2 bytes. 7,000,000,000 * 2 bytes = 14 Gigabytes.*

#### Q17. After applying INT4 quantization (0.5 bytes per parameter), approximately how much memory does a 7B model require?
- A) ~3.5 GB
- B) ~14 GB
- C) ~28 GB
- D) ~700 MB  
**Answer: A** | *Explanation: 7 Billion * 0.5 bytes = ~3.5 Gigabytes (slashing memory by 75%).*

#### Q18. What is the purpose of Intel Extension for PyTorch (IPEX)?
- A) Replacing PyTorch with TensorFlow
- B) Exposing hardware-specific optimizations (AVX-512, AMX, Intel GPUs) natively within standard PyTorch code
- C) Drawing GUI windows
- D) Encrypting disk drives  
**Answer: B** | *Explanation: IPEX provides drop-in optimizations and Graph Compiler integration for PyTorch on Intel architectures.*

#### Q19. What is RoCE in high-performance datacenter networking?
- A) Remote Operating Cloud Engine
- B) RDMA (Remote Direct Memory Access) over Converged Ethernet
- C) Read Only Cluster Execution
- D) Routing Protocol for Clusters  
**Answer: B** | *Explanation: RoCE allows zero-copy direct memory access between servers over standard Ethernet networks.*

#### Q20. What is the benefit of streaming responses from an LLM inference endpoint?
- A) It reduces total tokens generated
- B) It drastically improves perceived user latency because tokens appear immediately as generated rather than waiting for the entire paragraph
- C) It eliminates the need for RAM
- D) It prevents network disconnections  
**Answer: B** | *Explanation: Streaming outputs words in real time, delivering sub-second perceived interactivity.*

#### Q21. Which tool can profile memory stalls and thread contention during distributed LLM training?
- A) Wireshark
- B) Intel VTune Profiler
- C) Ping
- D) Traceroute  
**Answer: B** | *Explanation: Intel VTune analyzes CPU/accelerator microarchitecture to identify memory bandwidth saturation and thread locks.*

#### Q22. In the self-attention formula $\text{softmax}(Q K^T / \sqrt{d_k}) V$, why is division by $\sqrt{d_k}$ performed?
- A) To convert floats to integers
- B) To scale dot products and prevent softmax gradients from vanishing in regions with extremely small gradients
- C) To divide by zero safely
- D) To reduce model parameters  
**Answer: B** | *Explanation: For large head dimensions $d_k$, dot products grow large, pushing softmax into regions with vanishing gradients; scaling prevents this.*

#### Q23. What command launches multi-task distributed jobs inside a Slurm allocation?
- A) `sinfo`
- B) `srun`
- C) `scancel`
- D) `scontrol`  
**Answer: B** | *Explanation: `srun` spawns parallel tasks across all assigned compute nodes and cores.*

#### Q24. Which open-source library provides the FastAPI framework for building production REST inference microservices?
- A) `torchvision`
- B) `fastapi`
- C) `numpy`
- D) `scipy`  
**Answer: B** | *Explanation: FastAPI is an asynchronous, high-performance web framework for Python.*

#### Q25. What is the culmination outcome of the 5-Day GLA University HPC Curriculum?
- A) Writing simple local Python scripts
- B) Mastering end-to-end hardware-aware distributed AI workflows: from Linux cluster management to LLM fine-tuning and OpenVINO optimization on Intel supercomputing silicon
- C) Reinstalling Windows on laptops
- D) Learning Microsoft Excel macros  
**Answer: B** | *Explanation: The training completes the entire journey from silicon and Linux fundamentals to enterprise distributed AI and Generative LLM deployment.*
