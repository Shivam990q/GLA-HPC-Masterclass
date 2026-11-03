#!/usr/bin/env python3
"""
=============================================================================
INTEL oneAPI ACCELERATED MACHINE LEARNING - PRACTICE SCRIPT 04
Script: 04_random_forest_acceleration.py
Purpose: Benchmark Random Forest Classifier on 100,000 samples comparing
         stock Scikit-learn vs Intel Extension for Scikit-learn (oneDAL).
=============================================================================
"""

import time
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, accuracy_score
from sklearnex import patch_sklearn, unpatch_sklearn

def run_random_forest_benchmark():
    print("=" * 70)
    print(" SCRIPT 04: ACCELERATED RANDOM FOREST ENSEMBLE BENCHMARK")
    print("=" * 70)

    # 1. Dataset Generation
    n_samples = 100_000
    n_features = 20
    print(f"[*] Synthesizing dataset: {n_samples:,} samples, {n_features} features, 2 classes...")
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=14,
        n_redundant=4,
        weights=[0.85, 0.15],
        random_state=42
    )
    X = np.ascontiguousarray(X, dtype=np.float32)
    y = np.ascontiguousarray(y, dtype=np.int32)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"[*] Training Set: {len(X_train):,} samples | Test Set: {len(X_test):,} samples")

    # 2. Benchmark Stock Scikit-learn
    unpatch_sklearn()
    from sklearn.ensemble import RandomForestClassifier as StockRF

    print("\n[Phase 1] Training Stock Scikit-learn Random Forest (100 trees, max_depth=12, n_jobs=-1)...")
    t0 = time.perf_counter()
    rf_stock = StockRF(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
    rf_stock.fit(X_train, y_train)
    t_stock_fit = time.perf_counter() - t0

    t0 = time.perf_counter()
    probs_stock = rf_stock.predict_proba(X_test)[:, 1]
    t_stock_pred = time.perf_counter() - t0
    auc_stock = roc_auc_score(y_test, probs_stock)
    acc_stock = accuracy_score(y_test, rf_stock.predict(X_test))

    print(f"   -> Stock Training Time   : {t_stock_fit:.4f} seconds")
    print(f"   -> Stock Inference Time  : {t_stock_pred:.4f} seconds")
    print(f"   -> Stock Test Accuracy   : {acc_stock * 100:.2f}% (ROC-AUC: {auc_stock:.4f})")

    # 3. Benchmark Intel oneDAL
    print("\n[Phase 2] Enabling Intel oneDAL Acceleration via patch_sklearn(['RandomForestClassifier'])...")
    patch_sklearn(["RandomForestClassifier"])
    from sklearn.ensemble import RandomForestClassifier as IntelRF

    t0 = time.perf_counter()
    rf_intel = IntelRF(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
    rf_intel.fit(X_train, y_train)
    t_intel_fit = time.perf_counter() - t0

    t0 = time.perf_counter()
    probs_intel = rf_intel.predict_proba(X_test)[:, 1]
    t_intel_pred = time.perf_counter() - t0
    auc_intel = roc_auc_score(y_test, probs_intel)
    acc_intel = accuracy_score(y_test, rf_intel.predict(X_test))

    print(f"   -> Intel Training Time   : {t_intel_fit:.4f} seconds")
    print(f"   -> Intel Inference Time  : {t_intel_pred:.4f} seconds")
    print(f"   -> Intel Test Accuracy   : {acc_intel * 100:.2f}% (ROC-AUC: {auc_intel:.4f})")

    # 4. Comparative Evaluation
    speedup_fit = t_stock_fit / t_intel_fit
    speedup_pred = t_stock_pred / t_intel_pred
    auc_diff = abs(auc_stock - auc_intel)

    print("\n" + "=" * 70)
    print(" BENCHMARK COMPARATIVE SUMMARY")
    print("=" * 70)
    print(f"[*] Training Speedup Factor   : {speedup_fit:.2f}x Faster")
    print(f"[*] Inference Speedup Factor  : {speedup_pred:.2f}x Faster")
    print(f"[*] Test ROC-AUC Discrepancy  : {auc_diff:.5f} (Concordance: {100 - auc_diff*100:.2f}%)")
    print("=" * 70)

    assert auc_diff < 0.02, "Ensemble prediction accuracy diverged beyond 2% tolerance!"
    assert speedup_fit > 2.0, "Training speedup failed to reach minimum 2x threshold!"
    print("[+] TEST STATUS: PASSED - Accuracy parity and ensemble speedup confirmed!\n")

    unpatch_sklearn()

if __name__ == "__main__":
    run_random_forest_benchmark()
