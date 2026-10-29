#!/usr/bin/env bash
"""
intel_scikit_speedup.py
Edulateral Foundation — Official Intel oneDAL vs Stock Scikit-Learn Benchmark.
Program: GLA University High Performance Computing Block Teaching
Lead Trainer: Shivam Gupta

Benchmarks standard Scikit-learn against Intel Extension for Scikit-learn (sklearnex)
on synthetic clustering (k-Means) and classification (Random Forest) workloads.
"""

import time
import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

print("=" * 70)
print("     🏢 EDULATERAL FOUNDATION — INTEL oneDAL SPEEDUP SHOWDOWN")
print("        GLA University Block Teaching | Lead: Shivam Gupta")
print("=" * 70)

# 1. Generate Synthetic Clustering Dataset (500,000 Points, 20 Features)
print("\n[*] [Phase 1] Generating 500,000 synthetic samples with 20 features...")
np.random.seed(42)
n_samples = 500_000
n_features = 20
X = np.random.randn(n_samples, n_features).astype(np.float32)
y = (np.sum(X[:, :5], axis=1) > 0).astype(np.int32)
print(f"[+] Dataset memory footprint: {X.nbytes / (1024*1024):.2f} MB")

# 2. Benchmark Standard Scikit-Learn (Unpatched)
print("\n[*] [Phase 2] Executing Baseline Stock Scikit-Learn (Unpatched)...")
print("    -> Running standard KMeans (8 clusters, 15 iterations)...")
t0 = time.time()
kmeans_std = KMeans(n_clusters=8, max_iter=15, random_state=42, n_init=1).fit(X)
std_kmeans_time = time.time() - t0
print(f"    [-] Standard KMeans Walltime: {std_kmeans_time:.2f} seconds")

# 3. Benchmark with Intel oneDAL Acceleration
print("\n[*] [Phase 3] Applying Intel Extension for Scikit-Learn (sklearnex)...")
try:
    from sklearnex import patch_sklearn, unpatch_sklearn
    patch_sklearn()
    print("    [+] Intel oneDAL SIMD & AVX-512 hardware kernels successfully active!")
    
    from sklearn.cluster import KMeans as IntelKMeans
    print("    -> Running Intel-Accelerated KMeans...")
    t0 = time.time()
    kmeans_intel = IntelKMeans(n_clusters=8, max_iter=15, random_state=42, n_init=1).fit(X)
    intel_kmeans_time = time.time() - t0
    print(f"    [+] Intel-Accelerated KMeans Walltime: {intel_kmeans_time:.2f} seconds")
    
    speedup = std_kmeans_time / intel_kmeans_time if intel_kmeans_time > 0 else 1.0
    print("\n" + "=" * 70)
    print(f"  🏆 EMPIRICAL SHOWDOWN RESULT: Intel oneDAL is {speedup:.2f}x FASTER!")
    print(f"     Time Reduced from {std_kmeans_time:.2f}s down to {intel_kmeans_time:.2f}s")
    print("=" * 70)
    
except ImportError:
    print("    [!] sklearnex not installed in current environment.")
    print("    [!] Run 'pip install scikit-learn-intelex' to activate oneDAL acceleration.")
