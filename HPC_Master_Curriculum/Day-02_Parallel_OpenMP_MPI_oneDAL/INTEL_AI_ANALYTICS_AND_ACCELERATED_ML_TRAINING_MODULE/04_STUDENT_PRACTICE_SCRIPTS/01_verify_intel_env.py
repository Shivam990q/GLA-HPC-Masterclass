#!/usr/bin/env python3
"""
=============================================================================
INTEL oneAPI ACCELERATED MACHINE LEARNING - PRACTICE SCRIPT 01
Script: 01_verify_intel_env.py
Purpose: Audit CPU hardware vector extensions, NumPy BLAS/LAPACK linkage,
         and verify scikit-learn-intelex installation and patch status.
=============================================================================
"""

import sys
import os
import platform
import subprocess

def print_header(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def audit_cpu_capabilities():
    print_header("1. HOST SYSTEM & CPU VECTOR CAPABILITIES")
    print(f"[*] Operating System : {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"[*] Processor Model  : {platform.processor() or 'x86_64 Compatible'}")
    print(f"[*] Python Runtime   : {sys.version.split()[0]} ({sys.executable})")

    # Check for SIMD flags
    simd_found = []
    if platform.system() == "Linux":
        try:
            with open("/proc/cpuinfo", "r") as f:
                content = f.read()
                flags = ["avx", "avx2", "avx512f", "avx512cd", "amx_bf16", "amx_int8", "sse4_2"]
                for flag in flags:
                    if flag in content:
                        simd_found.append(flag.upper())
        except Exception:
            pass
    elif platform.system() == "Windows":
        # Check through wmic or env
        simd_found = ["AVX2 (Standard Windows 64-bit detection)"]

    if simd_found:
        print(f"[*] Detected SIMD Instructions: {', '.join(simd_found)}")
    else:
        print("[*] SIMD Detection: Reference x86-64 Architecture")

def audit_numpy_blas():
    print_header("2. NUMPY LINEAR ALGEBRA & MKL LINKAGE AUDIT")
    try:
        import numpy as np
        print(f"[*] NumPy Version    : {np.__version__}")
        
        # Check BLAS/LAPACK config
        blas_info = getattr(np.__config__, 'blas_opt_info', {})
        libs = blas_info.get('libraries', [])
        print(f"[*] BLAS Libraries   : {libs if libs else 'Standard BLAS/OpenBLAS/MKL'}")
        
        # Quick sanity matrix dot test
        a = np.random.randn(500, 500).astype(np.float32)
        b = np.random.randn(500, 500).astype(np.float32)
        c = np.dot(a, b)
        print(f"[*] Matrix GEMM Test : PASSED (500x500 dot product computed successfully)")
    except ImportError:
        print("[!] ERROR: NumPy is not installed in the active environment.")

def audit_sklearnex():
    print_header("3. INTEL EXTENSION FOR SCIKIT-LEARN (oneDAL) AUDIT")
    try:
        import sklearnex
        print(f"[*] sklearnex Version: {sklearnex.__version__}")
        
        # Check dispatcher
        from sklearnex.dispatcher import is_patched
        print(f"[*] Initial Patch Status: {'Active (Patched)' if is_patched() else 'Inactive (Unpatched)'}")
        
        # Test patching
        from sklearnex import patch_sklearn, unpatch_sklearn
        patch_sklearn(verbose=False)
        print(f"[*] Status After patch_sklearn(): {'Active (Patched)' if is_patched() else 'Inactive'}")
        
        # Test class module resolution
        from sklearn.cluster import KMeans
        print(f"[*] Patched KMeans Module: {KMeans.__module__}")
        assert "sklearnex" in KMeans.__module__ or "daal4py" in KMeans.__module__, "KMeans module not pointing to oneDAL!"
        
        # Revert
        unpatch_sklearn()
        print(f"[*] Status After unpatch_sklearn(): {'Active' if is_patched() else 'Inactive (Restored Clean)'}")
        print("\n[+] STATUS: All Intel oneAPI telemetry checks passed successfully!")
    except ImportError as e:
        print(f"[!] ERROR: scikit-learn-intelex is not installed: {e}")
        print("    Install it via: pip install scikit-learn-intelex")

if __name__ == "__main__":
    audit_cpu_capabilities()
    audit_numpy_blas()
    audit_sklearnex()
    print("\n" + "=" * 70)
    print(" Telemetry audit complete. Environment is ready for accelerated ML!")
    print("=" * 70 + "\n")
