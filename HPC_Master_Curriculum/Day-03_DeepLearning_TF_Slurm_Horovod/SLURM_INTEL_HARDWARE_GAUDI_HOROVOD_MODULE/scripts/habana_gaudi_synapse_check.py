#!/usr/bin/env python3
"""
Habana Gaudi 2 / Gaudi 3 AI Accelerator & SynapseAI Architecture Probe
Course: GLA-HPC-BCSG701 | Supercomputing Masterclass
"""
import sys
import os

print("==========================================================")
print("     HABANA GAUDI 2 / GAUDI 3 ARCHITECTURE & NETWORK PROBE")
print("==========================================================")

# Habana Gaudi processors are controlled by the SynapseAI software stack and habanalabs kernel driver
has_habana = False
try:
    import habana_frameworks.torch.core as htcore
    has_habana = True
    print("[*] Habana SynapseAI Runtime: ACTIVE (habanalabs driver bound)")
except ImportError:
    print("[*] Habana SynapseAI Runtime: Emulating production hardware telemetry.")

# Physical Silicon Specifications for Habana Gaudi 2 / Gaudi 3
gaudi_specs = {
    "Accelerator Family": "Habana Gaudi 2 / Gaudi 3 Deep Learning Processor",
    "Target Workload": "Large-Scale LLM Pre-training & Vision Distributed DL",
    "Matrix Multiplication Engines": "Dual MME (3D Tensor Systolic Array)",
    "Tensor Processor Cores (TPC)": "8 custom VLIW SIMD Cores (Non-linear activations)",
    "High-Bandwidth Memory (Gaudi 2)": "96 GB HBM2e (2.45 TB/s)",
    "High-Bandwidth Memory (Gaudi 3)": "128 GB HBM3 (3.7 TB/s)",
    "Integrated RoCEv2 RDMA Ports": "24 x 100 GbE (Gaudi 2) / 24 x 200 GbE (Gaudi 3) directly on-die",
    "Scale-Out Interconnect": "All-to-All Direct Mesh (Zero external switch latency)",
    "Peak BF16 TFLOPS (Gaudi 2)": 432.0,
    "Peak FP8 / BF16 TFLOPS (Gaudi 3)": 1835.0
}

for k, v in gaudi_specs.items():
    print(f"{k:<32} : {v}")

print("----------------------------------------------------------")
print("[+] Strategic Architectural Advantage:")
print("    By integrating 24 high-speed RoCEv2 RDMA networking ports directly on the silicon,")
print("    Gaudi eliminates external PCIe NIC cards and proprietary cluster switches, delivering")
print("    near-linear scaling across thousands of nodes in supercomputing centers.")
print("==========================================================")
