#!/usr/bin/env python3
"""
=============================================================================
INTEL oneAPI ACCELERATED MACHINE LEARNING - PRACTICE SCRIPT 02
Script: 02_numpy_mkl_speedup.py
Purpose: Benchmark Double-Precision General Matrix Multiply (DGEMM) to
         demonstrate hardware SIMD vectorization & cache-blocked MKL BLAS
         versus unvectorized CPython scalar execution.
=============================================================================
"""

import time
import numpy as np

def run_dgemm_benchmark():
    print("=" * 70)
    print(" SCRIPT 02: NUMPY MKL BLAS MATRIX MULTIPLICATION BENCHMARK")
    print("=" * 70)

    # 1. Naive CPython loop benchmark on small dimension
    N_small = 180
    print(f"\n[Test 1] Naive CPython 3-Nested Loop on Matrix Size: {N_small} x {N_small}")
    A_small = np.random.randn(N_small, N_small).tolist()
    B_small = np.random.randn(N_small, N_small).tolist()
    C_small = [[0.0] * N_small for _ in range(N_small)]

    t0 = time.perf_counter()
    for i in range(N_small):
        for k in range(N_small):
            aik = A_small[i][k]
            for j in range(N_small):
                C_small[i][j] += aik * B_small[k][j]
    t_naive = time.perf_counter() - t0
    
    flops_naive = 2 * (N_small ** 3)
    gflops_naive = (flops_naive / t_naive) / 1e9
    print(f"   -> Naive Loop Execution Time : {t_naive:.4f} seconds")
    print(f"   -> Compute Throughput        : {gflops_naive:.4f} GFLOPS")

    # 2. NumPy MKL BLAS on small dimension
    print(f"\n[Test 2] NumPy MKL Vectorized Matrix Multiply on: {N_small} x {N_small}")
    A_np_small = np.array(A_small, dtype=np.float64)
    B_np_small = np.array(B_small, dtype=np.float64)

    t0 = time.perf_counter()
    C_np_small = np.dot(A_np_small, B_np_small)
    t_mkl_small = time.perf_counter() - t0
    gflops_mkl_small = (flops_naive / t_mkl_small) / 1e9
    print(f"   -> MKL BLAS Execution Time   : {t_mkl_small * 1000:.3f} milliseconds")
    print(f"   -> Compute Throughput        : {gflops_mkl_small:.2f} GFLOPS")
    print(f"   -> Instantaneous Speedup     : {t_naive / t_mkl_small:,.1f}x Faster")

    # 3. HPC Scale Benchmark: 4096 x 4096 DGEMM
    N_large = 4096
    print(f"\n[Test 3] HPC-Scale Double-Precision DGEMM: {N_large} x {N_large}")
    print(f"   -> Total Floating-Point Operations: {2 * (N_large**3) / 1e9:.2f} Billion FLOPs")
    
    A_large = np.random.randn(N_large, N_large).astype(np.float64)
    B_large = np.random.randn(N_large, N_large).astype(np.float64)

    # Warmup
    _ = np.dot(A_large[:256, :256], B_large[:256, :256])

    t0 = time.perf_counter()
    C_large = np.dot(A_large, B_large)
    t_mkl_large = time.perf_counter() - t0
    
    flops_large = 2.0 * (N_large ** 3)
    gflops_large = (flops_large / t_mkl_large) / 1e9
    
    print(f"   -> Elapsed Time              : {t_mkl_large:.4f} seconds")
    print(f"   -> Sustained Compute Speed   : {gflops_large:,.2f} GFLOPS ({gflops_large/1e3:.3f} TFLOPS)")

    # Extrapolate naive time
    time_naive_extrapolated_hours = (t_naive / (N_small**3) * (N_large**3)) / 3600.0
    print(f"\n[*] Theoretical naive loop duration for 4096 x 4096 : ~{time_naive_extrapolated_hours:.1f} Hours")
    print(f"[*] MKL Vectorized execution duration for 4096 x 4096 : {t_mkl_large:.2f} Seconds")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    run_dgemm_benchmark()
