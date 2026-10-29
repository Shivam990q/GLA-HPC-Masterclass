#!/usr/bin/env python3
"""
intel_gpu_xpu_check.py
Intel Data Center GPU Max (Ponte Vecchio) & Intel Extension for TensorFlow (ITEX/XPU) Probe
GLA University — High Performance Computing | Lead: Shivam Gupta
"""

import sys
import shutil
import subprocess

def check_intel_gpu_environment():
    print("======================================================================")
    print("   🎮 INTEL DATA CENTER GPU MAX & XPU RUNTIME TELEMETRY               ")
    print("      GLA University High Performance Computing | Lead: Shivam Gupta  ")
    print("======================================================================")

    # 1. Check for `xpu-smi` (Intel XPU System Management Interface)
    xpusmi_path = shutil.which("xpu-smi")
    if xpusmi_path:
        print(f"[+] Found Intel XPU-SMI tool: {xpusmi_path}")
        try:
            output = subprocess.check_output(["xpu-smi", "discovery"], text=True, stderr=subprocess.STDOUT)
            print("[+] Discovered Intel GPU Max Hardware Nodes:")
            for line in output.splitlines()[:15]:
                print(f"    {line}")
        except Exception as e:
            print(f"[!] xpu-smi discovery failed: {e}")
    else:
        print("[-] 'xpu-smi' CLI not found.")
        print("    (Running in CPU/Emulation Mode: Host node lacks physical Intel Data Center GPU)")

    # 2. Check for Intel Extension for TensorFlow (ITEX)
    print("\n[*] Checking Intel Extension for TensorFlow (`intel_extension_for_tensorflow` / `itex`):")
    try:
        import intel_extension_for_tensorflow as itex
        print(f"[+] ITEX imported successfully! Version: {itex.__version__}")
        import tensorflow as tf
        xpu_devices = tf.config.list_physical_devices('XPU')
        print(f"[+] Discovered Physical XPU Devices: {xpu_devices}")
    except ImportError:
        print("[-] 'intel_extension_for_tensorflow' not installed in active Python environment.")
        print("    Install via: pip install intel-extension-for-tensorflow[xpu]")

    # 3. Intel GPU Architecture Summary
    print("\n======================================================================")
    print("  🏛️ INTEL DATA CENTER GPU MAX SERIES (PONTE VECCHIO) ARCHITECTURE:")
    print("  • Microarchitecture : Intel Xe-HPC (High Performance Computing)")
    print("  • Compute Units     : Xe Vector Engines (XVE) + Xe Matrix Engines (XMX)")
    print("  • Packaging         : EMIB 2.5D bridging + Foveros 3D die stacking (47 active tiles)")
    print("  • Memory Hierarchy  : Up to 128 GB HBM2e memory delivering >3.2 TB/s bandwidth")
    print("  • Programming Model : SYCL / DPC++, oneAPI, and ITEX pluggable device backend")
    print("======================================================================")

if __name__ == "__main__":
    check_intel_gpu_environment()
