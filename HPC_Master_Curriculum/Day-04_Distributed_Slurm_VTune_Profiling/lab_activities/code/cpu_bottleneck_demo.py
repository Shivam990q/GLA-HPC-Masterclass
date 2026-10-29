#!/usr/bin/env python3
"""
cpu_bottleneck_demo.py
Demonstrates Memory-Bound vs Compute-Bound profiles for Intel VTune Top-Down TMAM Profiling.
Used in Day 4 Hands-On Lab to analyze cache thrashing, arithmetic intensity, and vectorization.
"""

import time
import sys
import numpy as np

def run_memory_bound_benchmark(size=30_000_000):
    print(f"\n[*] 1. Memory-Bound Benchmark (Strided Cache-Thrashing Access):")
    arr = np.ones(size, dtype=np.float32)
    
    t0 = time.perf_counter()
    # Stride of 64 floats (256 bytes) guarantees every read accesses a distinct cache line
    # Causing massive L1/L2 cache misses and saturating off-chip DRAM bandwidth
    stride_sum = np.sum(arr[::64])
    t1 = time.perf_counter()
    
    elapsed = t1 - t0
    bytes_accessed = (size // 64) * 4
    bandwidth_gbps = (bytes_accessed / 1e9) / elapsed if elapsed > 0 else 0
    print(f"    [-] Stride Access Sum: {stride_sum:.0f}")
    print(f"    [-] Elapsed Time:      {elapsed*1000:.2f} ms")
    print(f"    [-] Effective BW:      {bandwidth_gbps:.2f} GB/s (Bound by Memory Latency)")
    return elapsed

def run_compute_bound_benchmark(size=500_000):
    print(f"\n[*] 2. Compute-Bound Benchmark (High Arithmetic Intensity):")
    # Small array fits 100% in L1/L2 cache (500k floats = 2 MB)
    arr = np.linspace(1.0, 2.0, size, dtype=np.float32)
    
    t0 = time.perf_counter()
    # High FLOPs per byte: transcendental operations in-place
    res = arr
    for _ in range(50):
        res = np.sin(res) * np.cos(res) + np.sqrt(np.abs(res))
    t1 = time.perf_counter()
    
    elapsed = t1 - t0
    total_flops = size * 50 * 4 # ~4 FLOPs per iteration
    gflops = (total_flops / 1e9) / elapsed if elapsed > 0 else 0
    print(f"    [+] Compute Result:    {np.sum(res):.4e}")
    print(f"    [+] Elapsed Time:      {elapsed*1000:.2f} ms")
    print(f"    [+] Performance:       {gflops:.2f} GFLOP/s (Bound by Vector ALUs / FMA)")
    return elapsed

def main():
    print("==========================================================")
    print("      INTEL VTUNE BOTTLENECK PROFILE DEMO (PYTHON)        ")
    print("==========================================================")
    t_mem = run_memory_bound_benchmark()
    t_comp = run_compute_bound_benchmark()
    print("\n==========================================================")
    print("VTune Profiling Interpretation Guide:")
    print(" - Memory-Bound: Top-Down TMAM will highlight 'Backend Bound -> Memory Bound'")
    print(" - Compute-Bound: Top-Down TMAM will highlight 'Retiring' or 'Core Bound (FPU)'")
    print("==========================================================")

if __name__ == "__main__":
    main()
