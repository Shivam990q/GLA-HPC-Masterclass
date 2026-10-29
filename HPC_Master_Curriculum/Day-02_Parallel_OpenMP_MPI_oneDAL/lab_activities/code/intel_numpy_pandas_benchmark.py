#!/usr/bin/env python3
"""
intel_numpy_pandas_benchmark.py
Intel AI Analytics Toolkit: NumPy MKL BLAS Acceleration & Pandas Dataframe Operations
Run with: python3 intel_numpy_pandas_benchmark.py
"""

import time
import numpy as np
import pandas as pd

def benchmark_numpy_blas():
    print("================================================================")
    print("   🚀 INTEL oneAPI AI ANALYTICS TOOLKIT: NUMPY MKL BENCHMARK   ")
    print("================================================================")

    # Inspect BLAS / LAPACK configuration in active NumPy
    print("\n[*] Inspecting NumPy Linear Algebra Configuration:")
    try:
        np.show_config()
    except Exception as e:
        print(f"    Config dump error: {e}")

    # Matrix Multiplication Benchmark: 4096 x 4096 Double Precision (FP64)
    N = 3000
    print(f"\n[*] Generating two {N}x{N} double-precision floating-point matrices...")
    np.random.seed(42)
    A = np.random.randn(N, N).astype(np.float64)
    B = np.random.randn(N, N).astype(np.float64)

    memory_mb = (A.nbytes + B.nbytes) / (1024 * 1024)
    print(f"[+] Total Matrix Memory: {memory_mb:.2f} MB")

    # Warm-up run
    _ = np.dot(A[:100, :100], B[:100, :100])

    print("[*] Executing Matrix GEMM (A @ B) via Intel oneMKL BLAS...")
    t0 = time.time()
    C = np.dot(A, B)
    elapsed = time.time() - t0

    # 2 * N^3 floating point operations in GEMM
    total_flops = 2.0 * (N ** 3)
    gflops = (total_flops / elapsed) / 1e9

    print(f"[+] Matrix Multiplication Time : {elapsed:.3f} seconds")
    print(f"[+] Effective Compute Throughput : {gflops:.2f} GFLOPS")

def benchmark_pandas_operations():
    print("\n================================================================")
    print("   📊 PANDAS / MODIN DATA PROCESSING THROUGHPUT BENCHMARK       ")
    print("================================================================")

    N_ROWS = 2_000_000
    print(f"[*] Generating synthetic telemetry dataframe with {N_ROWS:,} rows...")
    t0 = time.time()
    df = pd.DataFrame({
        'cluster_id': np.random.randint(1, 16, size=N_ROWS),
        'cpu_util': np.random.uniform(10.0, 99.9, size=N_ROWS),
        'memory_gb': np.random.uniform(4.0, 512.0, size=N_ROWS),
        'temp_celsius': np.random.uniform(35.0, 85.0, size=N_ROWS),
        'job_status': np.random.choice(['RUNNING', 'COMPLETED', 'FAILED'], size=N_ROWS)
    })
    print(f"[+] Dataframe generated in {time.time()-t0:.2f}s (RAM: {df.memory_usage().sum()/(1024*1024):.1f} MB)")

    print("[*] Running complex groupby aggregation and filtering...")
    t0 = time.time()
    agg_result = df.groupby(['cluster_id', 'job_status']).agg(
        avg_cpu=('cpu_util', 'mean'),
        max_mem=('memory_gb', 'max'),
        p95_temp=('temp_celsius', lambda x: np.percentile(x, 95))
    ).reset_index()
    elapsed = time.time() - t0

    print(f"[+] Aggregation Completed in {elapsed:.3f} seconds")
    print(f"[+] Summary Result Head:\n{agg_result.head()}")

if __name__ == "__main__":
    benchmark_numpy_blas()
    benchmark_pandas_operations()
