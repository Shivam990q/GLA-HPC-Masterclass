#!/usr/bin/env python3
"""
habana_gaudi_synapse_check.py
Intel Habana Gaudi / Gaudi 2 / Gaudi 3 Hardware & SynapseAI Software Environment Inspector
GLA University — High Performance Computing | Lead: Shivam Gupta
"""

import subprocess
import sys
import shutil

def check_habana_gaudi_environment():
    print("======================================================================")
    print("   🧠 INTEL HABANA GAUDI HARDWARE & SYNAPSEAI STACK TELEMETRY       ")
    print("      GLA University High Performance Computing | Lead: Shivam Gupta  ")
    print("======================================================================")

    # 1. Check for `hl-smi` (Habana Labs System Management Interface)
    hlsmi_path = shutil.which("hl-smi")
    if hlsmi_path:
        print(f"[+] Found Habana System Management Interface: {hlsmi_path}")
        try:
            output = subprocess.check_output(["hl-smi", "-q"], text=True, stderr=subprocess.STDOUT)
            print("[+] Active Gaudi Accelerator Telemetry Head:")
            for line in output.splitlines()[:15]:
                print(f"    {line}")
        except Exception as e:
            print(f"[!] hl-smi query failed: {e}")
    else:
        print("[-] 'hl-smi' CLI not detected on host system.")
        print("    (Running in CPU/Emulation Mode: Host node lacks physical Habana Gaudi PCIe/OAM card)")

    # 2. Check Habana SynapseAI Kernel Drivers (/dev/accel*)
    print("\n[*] Checking Linux Kernel Habana Driver Interfaces (/dev/accel*):")
    try:
        import glob
        accel_devs = glob.glob("/dev/accel*")
        if accel_devs:
            print(f"[+] Discovered Habana Gaudi device nodes: {accel_devs}")
        else:
            print("[-] No /dev/accel* device files found in Linux /dev tree.")
    except Exception as e:
        print(f"[!] Error inspecting device nodes: {e}")

    # 3. Check for Habana PyTorch / TensorFlow Integration Modules
    print("\n[*] Checking Python Habana Framework Libraries (habana_frameworks):")
    try:
        import habana_frameworks.torch.core as htcore
        print("[+] Successfully imported habana_frameworks.torch (Habana PyTorch Bridge active!)")
    except ImportError:
        print("[-] 'habana_frameworks' not present in Python site-packages.")

    # 4. Gaudi Architecture Summary
    print("\n======================================================================")
    print("  🏛️ INTEL HABANA GAUDI 2 / 3 ARCHITECTURAL INSIGHTS:")
    print("  • Compute Engines  : Matrix Multiplication Engines (MME) + Tensor Processing Cores (TPC)")
    print("  • Memory Subsystem : 96 GB to 128 GB HBM2e (up to 3.7 TB/s aggregate bandwidth)")
    print("  • Integrated Scale : 24x 100GbE (Gaudi 2) / 24x 200GbE (Gaudi 3) RoCEv2 ports on-chip")
    print("  • Software Stack   : Intel SynapseAI Core (Graph Compiler, Runtime & TPC Kernels)")
    print("======================================================================")

if __name__ == "__main__":
    check_habana_gaudi_environment()
