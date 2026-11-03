#!/usr/bin/env python3
"""
=============================================================================
INTEL oneAPI ACCELERATED MACHINE LEARNING - PRACTICE SCRIPT 06
Script: 06_full_benchmark_suite.py
Purpose: Complete Automated Multi-Algorithm Benchmark Suite. Evaluates:
         - K-Means Clustering
         - Principal Component Analysis (PCA)
         - Random Forest Classifier
         - K-Nearest Neighbors (KNN)
         - Ridge Regression
         Generates an ASCII summary table and exports results to CSV.
=============================================================================
"""

import time
import os
import csv
import numpy as np
from sklearn.datasets import make_blobs, make_classification, make_regression
from sklearnex import patch_sklearn, unpatch_sklearn

def run_suite():
    print("=" * 80)
    print("      INTEL AI ANALYTICS TOOLKIT: COMPREHENSIVE ML BENCHMARK SUITE")
    print("=" * 80)

    results = []

    # -------------------------------------------------------------
    # 1. K-Means (500k samples, 10 features, 8 clusters)
    # -------------------------------------------------------------
    print("\n[*] Benchmarking 1/5: K-Means Clustering (500,000 samples)...")
    X_km, _ = make_blobs(n_samples=500_000, n_features=10, centers=8, random_state=42)
    X_km = np.ascontiguousarray(X_km, dtype=np.float32)

    unpatch_sklearn()
    from sklearn.cluster import KMeans as StockKMeans
    t0 = time.perf_counter()
    StockKMeans(n_clusters=8, n_init=5, max_iter=150, random_state=42).fit(X_km)
    t_stock_km = time.perf_counter() - t0

    patch_sklearn(["KMeans"])
    from sklearn.cluster import KMeans as IntelKMeans
    t0 = time.perf_counter()
    IntelKMeans(n_clusters=8, n_init=5, max_iter=150, random_state=42).fit(X_km)
    t_intel_km = time.perf_counter() - t0

    sp_km = t_stock_km / t_intel_km
    results.append({
        "Algorithm": "K-Means Clustering",
        "Dataset Shape": "500,000 x 10",
        "Stock Time (s)": f"{t_stock_km:.3f}",
        "Intel Time (s)": f"{t_intel_km:.3f}",
        "Speedup": f"{sp_km:.2f}x"
    })
    print(f"    -> Stock: {t_stock_km:.3f}s | Intel: {t_intel_km:.3f}s | Speedup: {sp_km:.2f}x")

    # -------------------------------------------------------------
    # 2. PCA (250k samples, 50 features -> 5 components)
    # -------------------------------------------------------------
    print("\n[*] Benchmarking 2/5: Principal Component Analysis (250,000 samples)...")
    np.random.seed(42)
    X_pca = np.random.randn(250_000, 50).astype(np.float32)

    unpatch_sklearn()
    from sklearn.decomposition import PCA as StockPCA
    t0 = time.perf_counter()
    StockPCA(n_components=5, svd_solver="full", random_state=42).fit(X_pca)
    t_stock_pca = time.perf_counter() - t0

    patch_sklearn(["PCA"])
    from sklearn.decomposition import PCA as IntelPCA
    t0 = time.perf_counter()
    IntelPCA(n_components=5, svd_solver="full", random_state=42).fit(X_pca)
    t_intel_pca = time.perf_counter() - t0

    sp_pca = t_stock_pca / t_intel_pca
    results.append({
        "Algorithm": "PCA (SVD Solver)",
        "Dataset Shape": "250,000 x 50",
        "Stock Time (s)": f"{t_stock_pca:.3f}",
        "Intel Time (s)": f"{t_intel_pca:.3f}",
        "Speedup": f"{sp_pca:.2f}x"
    })
    print(f"    -> Stock: {t_stock_pca:.3f}s | Intel: {t_intel_pca:.3f}s | Speedup: {sp_pca:.2f}x")

    # -------------------------------------------------------------
    # 3. Random Forest (80k samples, 20 features, 100 trees)
    # -------------------------------------------------------------
    print("\n[*] Benchmarking 3/5: Random Forest Classifier (80,000 samples, 100 trees)...")
    X_rf, y_rf = make_classification(n_samples=80_000, n_features=20, n_informative=12, random_state=42)
    X_rf = np.ascontiguousarray(X_rf, dtype=np.float32)
    y_rf = np.ascontiguousarray(y_rf, dtype=np.int32)

    unpatch_sklearn()
    from sklearn.ensemble import RandomForestClassifier as StockRF
    t0 = time.perf_counter()
    StockRF(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1).fit(X_rf, y_rf)
    t_stock_rf = time.perf_counter() - t0

    patch_sklearn(["RandomForestClassifier"])
    from sklearn.ensemble import RandomForestClassifier as IntelRF
    t0 = time.perf_counter()
    IntelRF(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1).fit(X_rf, y_rf)
    t_intel_rf = time.perf_counter() - t0

    sp_rf = t_stock_rf / t_intel_rf
    results.append({
        "Algorithm": "Random Forest (100 Trees)",
        "Dataset Shape": "80,000 x 20",
        "Stock Time (s)": f"{t_stock_rf:.3f}",
        "Intel Time (s)": f"{t_intel_rf:.3f}",
        "Speedup": f"{sp_rf:.2f}x"
    })
    print(f"    -> Stock: {t_stock_rf:.3f}s | Intel: {t_intel_rf:.3f}s | Speedup: {sp_rf:.2f}x")

    # -------------------------------------------------------------
    # 4. K-Nearest Neighbors (50k train, 5k query, 20 features)
    # -------------------------------------------------------------
    print("\n[*] Benchmarking 4/5: K-Nearest Neighbors Classifier (50,000 train, 5k query)...")
    X_knn, y_knn = make_classification(n_samples=55_000, n_features=20, n_classes=4, random_state=42)
    X_tr_knn, X_te_knn = X_knn[:50_000], X_knn[50_000:]
    y_tr_knn, y_te_knn = y_knn[:50_000], y_knn[50_000:]

    unpatch_sklearn()
    from sklearn.neighbors import KNeighborsClassifier as StockKNN
    t0 = time.perf_counter()
    m_sk_knn = StockKNN(n_neighbors=5, n_jobs=-1).fit(X_tr_knn, y_tr_knn)
    _ = m_sk_knn.predict(X_te_knn)
    t_stock_knn = time.perf_counter() - t0

    patch_sklearn(["KNeighborsClassifier"])
    from sklearn.neighbors import KNeighborsClassifier as IntelKNN
    t0 = time.perf_counter()
    m_in_knn = IntelKNN(n_neighbors=5, n_jobs=-1).fit(X_tr_knn, y_tr_knn)
    _ = m_in_knn.predict(X_te_knn)
    t_intel_knn = time.perf_counter() - t0

    sp_knn = t_stock_knn / t_intel_knn
    results.append({
        "Algorithm": "K-Nearest Neighbors (k=5)",
        "Dataset Shape": "50,000 x 20",
        "Stock Time (s)": f"{t_stock_knn:.3f}",
        "Intel Time (s)": f"{t_intel_knn:.3f}",
        "Speedup": f"{sp_knn:.2f}x"
    })
    print(f"    -> Stock: {t_stock_knn:.3f}s | Intel: {t_intel_knn:.3f}s | Speedup: {sp_knn:.2f}x")

    # -------------------------------------------------------------
    # 5. Ridge Regression (200k samples, 40 features)
    # -------------------------------------------------------------
    print("\n[*] Benchmarking 5/5: Ridge Regression (200,000 samples)...")
    X_rg, y_rg = make_regression(n_samples=200_000, n_features=40, noise=0.1, random_state=42)
    X_rg = np.ascontiguousarray(X_rg, dtype=np.float32)

    unpatch_sklearn()
    from sklearn.linear_model import Ridge as StockRidge
    t0 = time.perf_counter()
    StockRidge(alpha=1.0).fit(X_rg, y_rg)
    t_stock_rg = time.perf_counter() - t0

    patch_sklearn(["Ridge"])
    from sklearn.linear_model import Ridge as IntelRidge
    t0 = time.perf_counter()
    IntelRidge(alpha=1.0).fit(X_rg, y_rg)
    t_intel_rg = time.perf_counter() - t0

    sp_rg = t_stock_rg / t_intel_rg
    results.append({
        "Algorithm": "Ridge Regression",
        "Dataset Shape": "200,000 x 40",
        "Stock Time (s)": f"{t_stock_rg:.3f}",
        "Intel Time (s)": f"{t_intel_rg:.3f}",
        "Speedup": f"{sp_rg:.2f}x"
    })
    print(f"    -> Stock: {t_stock_rg:.3f}s | Intel: {t_intel_rg:.3f}s | Speedup: {sp_rg:.2f}x")

    # -------------------------------------------------------------
    # Formatted Summary Output Table
    # -------------------------------------------------------------
    print("\n" + "=" * 80)
    print("                    CONSOLIDATED PERFORMANCE RESULTS TABLE")
    print("=" * 80)
    header = f"{'Algorithm':<28} | {'Dataset Shape':<15} | {'Stock (s)':<10} | {'Intel (s)':<10} | {'Speedup':<8}"
    print(header)
    print("-" * 80)
    for r in results:
        print(f"{r['Algorithm']:<28} | {r['Dataset Shape']:<15} | {r['Stock Time (s)']:<10} | {r['Intel Time (s)']:<10} | {r['Speedup']:<8}")
    print("=" * 80)

    # Export to CSV
    csv_file = "intel_ml_acceleration_results.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Algorithm", "Dataset Shape", "Stock Time (s)", "Intel Time (s)", "Speedup"])
        writer.writeheader()
        writer.writerows(results)
    print(f"\n[+] Results successfully exported to: {os.path.abspath(csv_file)}\n")

    unpatch_sklearn()

if __name__ == "__main__":
    run_suite()
