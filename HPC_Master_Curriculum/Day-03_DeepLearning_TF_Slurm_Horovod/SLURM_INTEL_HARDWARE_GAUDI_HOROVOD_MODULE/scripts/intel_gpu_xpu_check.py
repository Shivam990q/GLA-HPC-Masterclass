#!/usr/bin/env python3
"""
Intel Data Center GPU Max 1550 (Ponte Vecchio) Capability & Architecture Probe
Course: GLA-HPC-BCSG701 | Supercomputing Masterclass
"""
import sys
import os

print("==========================================================")
print("     INTEL DATA CENTER GPU MAX 1550 ARCHITECTURE PROBE    ")
print("==========================================================")

# In high-performance supercomputing environments, Intel XPUs are surfaced via
# Intel oneAPI Level Zero and SYCL runtime.
has_sycl = False
try:
    import dpctl
    devices = dpctl.get_devices()
    has_sycl = True
    print(f"[*] Intel oneAPI DPC++/SYCL Runtime Detected: {len(devices)} physical devices found.")
    for idx, dev in enumerate(devices):
        print(f"    - Device [{idx}]: {dev.name} (Backend: {dev.backend})")
except ImportError:
    print("[*] Intel DPC++ Runtime (dpctl): Emulating hardware specification telemetry.")

# Hardware Specification Audit for Intel GPU Max 1550 (Ponte Vecchio)
specs = {
    "Accelerator Model": "Intel Data Center GPU Max 1550 (Ponte Vecchio)",
    "Architecture": "Xe-HPC Microarchitecture",
    "Compute Tiles": "2 Stacks connected via EMIB (Embedded Multi-die Interconnect Bridge)",
    "Xe Cores": 128,
    "XMX (Xe Matrix Engines)": 1024,
    "Vector Engine Bit-width": "512-bit SIMD per lane",
    "High-Bandwidth Memory": "128 GB HBM2e",
    "Memory Bandwidth": "3.2 TB/s",
    "Interconnect": "8 XeLink Bridges (All-to-All GPU interconnect)",
    "Peak BF16 / FP16 TFLOPS": 839.0,
    "Peak FP64 Vector TFLOPS": 52.4
}

for k, v in specs.items():
    print(f"{k:<26} : {v}")

print("----------------------------------------------------------")
print("[+] Primary Target Use Cases: Aurora Supercomputer Scientific HPC & Large-Scale AI")
print("[+] Software Frameworks     : Intel oneAPI, SYCL/DPC++, OpenMP GPU Offload, PyTorch-IPEX")
print("==========================================================")

