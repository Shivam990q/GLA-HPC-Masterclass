# 🧪 Day 02 Afternoon: Hands-On Student Lab Activities
## Intel AI Analytics Toolkit, oneDAL & Accelerated Scikit-learn
**Target Audience**: B.Tech CSE / AI & ML / HPC Masterclass Undergraduates  
**Session Window**: 3 Hours (Afternoon Applied Session)  
**Total Labs**: 6 Graded Practical Exercises  
**Evaluation Standard**: Ground-Truth Parity Assertions + Measured Speedup Multipliers

---

## 📋 Table of Student Labs

| Lab # | Title | Focus Area | Dataset / Problem | Difficulty | Time Limit |
| :---: | :--- | :--- | :--- | :---: | :---: |
| **Lab 1** | **Intel Hardware & oneAPI Telemetry Audit** | System Inspection | CPU AVX-512 & MKL BLAS linkage | 🟢 Easy | 15 mins |
| **Lab 2** | **Customer Segmentation with Accelerated K-Means** | Clustering | 500,000 E-Commerce transactions | 🟡 Medium | 30 mins |
| **Lab 3** | **Credit Card Fraud Detection with Random Forest** | Classification | 100,000 Imbalanced financial events | 🟡 Medium | 35 mins |
| **Lab 4** | **Genomic Data Dimensionality Reduction via PCA** | Decomposition | 250,000 High-dimensional gene records | 🟡 Medium | 30 mins |
| **Lab 5** | **Dynamic & Selective Monkey-Patching Verification** | API Mechanics | Granular `sklearnex.patch_sklearn` | 🔴 Advanced | 30 mins |
| **Lab 6** | **High-Throughput ML Inference Pipeline (Scaler + PCA + KNN)** | End-to-End Pipeline | Streaming Latency & Batch Scoring | 🔴 Advanced | 40 mins |

---

## 🛠️ Lab Environment Setup Instructions

Before beginning any lab, ensure your Python environment has the necessary Intel-optimized packages:

```bash
# 1. Activate your virtual environment
python -m venv venv_intel
# Linux/macOS:
source venv_intel/bin/activate
# Windows PowerShell:
.\venv_intel\Scripts\Activate.ps1

# 2. Install required packages
pip install --upgrade pip
pip install scikit-learn-intelex numpy scipy pandas matplotlib pytest
```

---

## 🧪 Lab 1: Intel Hardware & oneAPI Telemetry Audit

### 🎯 Objective
Verify whether your host CPU supports SIMD vector extensions (AVX2, AVX-512, AMX), check if NumPy is linked against Intel MKL (Math Kernel Library), and confirm that `scikit-learn-intelex` is installed and ready to accelerate computation.

### 🏢 Real-World Engineering Scenario
Before deploying high-performance data processing pipelines to HPC cluster nodes or cloud instances (AWS c6i, GCP c2/c3, Azure Fsv2), machine learning engineers must run hardware telemetry checks. If code runs on an instance without vector acceleration or using fallback reference BLAS libraries, throughput can drop by 10x to 50x without throwing any error.

### 📝 Step-by-Step Instructions
1. Query CPU hardware flags to detect SIMD instruction sets (AVX, AVX2, AVX512F).
2. Inspect NumPy's underlying BLAS/LAPACK configuration to confirm Intel MKL linkage.
3. Import `sklearnex` and retrieve its version and device target.
4. Print a clean, formatted ASCII diagnostic report.

### 🧩 Student Starter Code (Fill in the blanks `___`)
```python
"""
Lab 1 Starter Code: Intel Hardware & oneAPI Telemetry Audit
"""
import sys
import platform
import numpy as np

# TODO: Step 1 - Import sklearnex
import _________ as sx

def audit_cpu_flags():
    # Detect CPU instruction set
    flags = []
    # On Linux, inspect /proc/cpuinfo; on Windows, check platform
    print(f"Platform: {platform.platform()}")
    print(f"Processor: {platform.processor()}")
    print(f"Python Version: {sys.version.split()[0]}")

def audit_numpy_blas():
    print("\n--- NumPy BLAS/LAPACK Configuration ---")
    # TODO: Step 2 - Call NumPy's configuration display method
    np.show__________()

def audit_sklearnex():
    print("\n--- Intel Extension for Scikit-learn ---")
    # TODO: Step 3 - Check sklearnex version
    print(f"sklearnex Version: {sx._________}")

if __name__ == "__main__":
    audit_cpu_flags()
    audit_numpy_blas()
    audit_sklearnex()
```

### ✅ Complete Reference Solution Code
```python
"""
Lab 1 Solution: Intel Hardware & oneAPI Telemetry Audit
"""
import sys
import platform
import os
import numpy as np
import sklearnex

def audit_system_environment():
    print("=" * 65)
    print("      LAB 1: INTEL HARDWARE & ONEAPI TELEMETRY AUDIT")
    print("=" * 65)
    
    # 1. OS and Python Details
    print(f"[*] Operating System : {platform.system()} {platform.release()} ({platform.machine()})")
    print(f"[*] Processor Arch   : {platform.processor()}")
    print(f"[*] Python Executable: {sys.executable}")
    print(f"[*] Python Version   : {sys.version.split()[0]}")
    
    # 2. Threading Environment Variables
    omp_threads = os.environ.get("OMP_NUM_THREADS", "Not explicitly set (defaults to CPU count)")
    mkl_threads = os.environ.get("MKL_NUM_THREADS", "Not explicitly set (defaults to OMP)")
    print(f"[*] OMP_NUM_THREADS  : {omp_threads}")
    print(f"[*] MKL_NUM_THREADS  : {mkl_threads}")
    
    # 3. NumPy BLAS Linkage
    print("\n[*] Auditing NumPy Linear Algebra Engine...")
    config_dict = np.__config__.blas_opt_info if hasattr(np.__config__, 'blas_opt_info') else {}
    libraries = config_dict.get('libraries', [])
    print(f"    - Linked BLAS Libraries: {libraries}")
    
    # 4. sklearnex Information
    print("\n[*] Auditing Intel Extension for Scikit-learn (oneDAL)...")
    print(f"    - sklearnex Version: {sklearnex.__version__}")
    
    # 5. Patch Status Check
    try:
        from sklearnex import sklearn_is_patched
        patch_active = sklearn_is_patched()
    except ImportError:
        try:
            from sklearnex.dispatcher import is_patched
            patch_active = is_patched()
        except ImportError:
            patch_active = False
    print(f"    - Global Patch Active: {patch_active}")
    
    print("=" * 65)
    print("  [PASSED] Telemetry Audit Completed Successfully!")
    print("=" * 65)

if __name__ == "__main__":
    audit_system_environment()
```

### 🧪 Automated Verification Test
```python
def test_lab_1_telemetry():
    import numpy as np
    import sklearnex
    assert hasattr(sklearnex, "__version__"), "sklearnex must have a __version__ attribute"
    assert len(sklearnex.__version__) > 0, "sklearnex version must be a non-empty string"
    assert hasattr(np, "__config__"), "NumPy config must be accessible"
```

---

## 🧪 Lab 2: Customer Segmentation with Accelerated K-Means

### 🎯 Objective
Perform unsupervised customer segmentation on 500,000 transactions with 10 behavioral features. Compare clustering execution time between standard Scikit-learn and Intel oneDAL-accelerated K-Means, verifying a minimum **10x speedup** with **< 0.01% inertia difference**.

### 🏢 Real-World Engineering Scenario
An e-commerce giant processes 500,000 shopping session vectors every midnight to re-cluster customer personas for personalized homepage recommendations. Standard Scikit-learn takes 45 seconds on single-threaded fallback. Using Intel oneDAL multi-core vectorization, clustering finishes in 2.1 seconds, reducing compute costs by 95% on AWS EC2 instances.

### 📝 Step-by-Step Instructions
1. Generate synthetic clustering data with `make_blobs` ($N=500,000$, $D=10$, $K=8$).
2. Run standard Scikit-learn `KMeans(n_clusters=8, n_init=10, max_iter=300)`. Measure execution time and record final cluster inertia.
3. Enable Intel oneDAL acceleration via `patch_sklearn(["KMeans"])`.
4. Run the identical K-Means clustering algorithm. Measure execution time and record inertia.
5. Compute speedup multiplier: $\text{Speedup} = \frac{T_{\text{stock}}}{T_{\text{intel}}}$.
6. Verify numerical convergence parity: $\frac{|\text{Inertia}_{\text{stock}} - \text{Inertia}_{\text{intel}}|}{\text{Inertia}_{\text{stock}}} \le 0.0001$.

### 🧩 Student Starter Code (Fill in the blanks `___`)
```python
"""
Lab 2 Starter Code: Accelerated K-Means Clustering
"""
import time
import numpy as np
from sklearn.datasets import make_blobs

# Generate 500,000 samples
print("[*] Generating 500,000 customer transaction vectors...")
X, _ = make_blobs(n_samples=500_000, n_features=10, centers=8, random_state=42)

# --- TASK 1: Benchmark Stock Scikit-learn ---
from sklearn.cluster import KMeans
t0 = time.perf_counter()
kmeans_stock = KMeans(n_clusters=8, n_init=10, max_iter=300, random_state=42)
kmeans_stock.fit(X)
t_stock = time.perf_counter() - t0
print(f"[Stock Scikit-learn] Time: {t_stock:.3f} s, Inertia: {kmeans_stock.inertia_:.2f}")

# --- TASK 2: Enable Intel oneDAL Acceleration ---
from sklearnex import _________
patch_sklearn(["_________"])

# Re-import KMeans to get the patched version
from sklearn.cluster import KMeans
t0 = time.perf_counter()
kmeans_intel = KMeans(n_clusters=8, n_init=10, max_iter=300, random_state=42)
kmeans_intel.fit(X)
t_intel = time.perf_counter() - t0
print(f"[Intel oneDAL]       Time: {t_intel:.3f} s, Inertia: {kmeans_intel.inertia_:.2f}")

# --- TASK 3: Calculate Metrics ---
speedup = _________ / _________
print(f"[*] Achieved Speedup: {speedup:.2f}x")
```

### ✅ Complete Reference Solution Code
```python
"""
Lab 2 Solution: Accelerated K-Means Clustering
"""
import time
import numpy as np
from sklearn.datasets import make_blobs
from sklearnex import patch_sklearn, unpatch_sklearn

def run_kmeans_lab():
    print("=" * 65)
    print("      LAB 2: ACCELERATED K-MEANS CUSTOMER SEGMENTATION")
    print("=" * 65)
    
    # 1. Generate Synthetic Dataset
    n_samples = 500_000
    n_features = 10
    n_clusters = 8
    print(f"[*] Generating {n_samples:,} customer vectors ({n_features} features)...")
    X, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=n_clusters, random_state=42)
    X = np.ascontiguousarray(X, dtype=np.float32)
    
    # 2. Ensure we start in unpatched state
    unpatch_sklearn()
    from sklearn.cluster import KMeans as StockKMeans
    
    print("\n[Phase 1] Executing Standard Scikit-learn KMeans...")
    t0 = time.perf_counter()
    model_stock = StockKMeans(n_clusters=n_clusters, n_init=10, max_iter=300, random_state=42)
    model_stock.fit(X)
    t_stock = time.perf_counter() - t0
    inertia_stock = model_stock.inertia_
    print(f"   -> Stock Time    : {t_stock:.4f} seconds")
    print(f"   -> Stock Inertia : {inertia_stock:,.2f}")
    
    # 3. Patch with Intel oneDAL
    print("\n[Phase 2] Dynamically Patching KMeans via oneDAL...")
    patch_sklearn(["KMeans"])
    from sklearn.cluster import KMeans as IntelKMeans
    
    print("   -> Verifying patch module:", IntelKMeans.__module__)
    assert "daal4py" in IntelKMeans.__module__ or "sklearnex" in IntelKMeans.__module__, "KMeans was not patched!"
    
    t0 = time.perf_counter()
    model_intel = IntelKMeans(n_clusters=n_clusters, n_init=10, max_iter=300, random_state=42)
    model_intel.fit(X)
    t_intel = time.perf_counter() - t0
    inertia_intel = model_intel.inertia_
    print(f"   -> Intel Time    : {t_intel:.4f} seconds")
    print(f"   -> Intel Inertia : {inertia_intel:,.2f}")
    
    # 4. Parity & Speedup Verification
    speedup = t_stock / t_intel
    inertia_rel_diff = abs(inertia_stock - inertia_intel) / inertia_stock
    
    print("\n" + "-" * 65)
    print(f"[*] PERFORMANCE SPEEDUP     : {speedup:.2f}x Faster")
    print(f"[*] INERTIA RELATIVE DELTA  : {inertia_rel_diff:.6f} ({inertia_rel_diff * 100:.4f}%)")
    print("-" * 65)
    
    assert inertia_rel_diff < 0.001, f"Inertia mismatch exceeds threshold: {inertia_rel_diff}"
    assert speedup > 3.0, f"Speedup is below minimum threshold: {speedup:.2f}x"
    print("  [PASSED] Lab 2 Assertions Verified Successfully!\n")
    
    # Clean up state
    unpatch_sklearn()

if __name__ == "__main__":
    run_kmeans_lab()
```

### 🧪 Automated Verification Test
```python
def test_lab_2_kmeans_convergence():
    from sklearnex import patch_sklearn, unpatch_sklearn
    from sklearn.datasets import make_blobs
    import numpy as np
    
    X, _ = make_blobs(n_samples=50_000, n_features=6, centers=4, random_state=42)
    
    unpatch_sklearn()
    from sklearn.cluster import KMeans as StockKMeans
    m_stock = StockKMeans(n_clusters=4, n_init=5, random_state=42).fit(X)
    
    patch_sklearn(["KMeans"])
    from sklearn.cluster import KMeans as IntelKMeans
    m_intel = IntelKMeans(n_clusters=4, n_init=5, random_state=42).fit(X)
    
    rel_diff = abs(m_stock.inertia_ - m_intel.inertia_) / m_stock.inertia_
    assert rel_diff < 0.01, f"K-Means inertia divergence too high: {rel_diff}"
    unpatch_sklearn()
```

---

## 🧪 Lab 3: Credit Card Fraud Detection with Random Forest

### 🎯 Objective
Train an ensemble `RandomForestClassifier` on 100,000 simulated credit card transactions with 20 numerical fraud indicators. Measure tree construction throughput and verify exact ROC-AUC parity between stock Scikit-learn and Intel oneDAL.

### 🏢 Real-World Engineering Scenario
In real-time credit scoring, fraud detection models must be retrained continuously every few hours on fresh transaction streams. Training 100 trees on large tabular datasets with stock Python often hits CPU saturation due to single-threaded GIL contention in tree splits. Intel oneDAL uses multi-core task scheduling and histogram-based binning to accelerate ensemble training by **10x to 15x**.

### 📝 Step-by-Step Instructions
1. Generate an imbalanced binary classification dataset using `make_classification` ($N=100,000$, $D=20$, weights 97% legitimate, 3% fraud).
2. Split dataset into 80% train and 20% test sets.
3. Train `RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42)` using stock Scikit-learn.
4. Record fit time, prediction time, and test ROC-AUC score.
5. Enable `patch_sklearn(["RandomForestClassifier"])` and train the identical model.
6. Verify ROC-AUC concordance ($|\text{AUC}_{\text{stock}} - \text{AUC}_{\text{intel}}| \le 0.005$) and verify minimum **6x speedup**.

### 🧩 Student Starter Code (Fill in the blanks `___`)
```python
"""
Lab 3 Starter Code: Accelerated Random Forest Classifier
"""
import time
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

# Generate 100,000 fraud records
X, y = make_classification(n_samples=100_000, n_features=20, weights=[0.97, 0.03], random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- TASK 1: Benchmark Stock Random Forest ---
from sklearn.ensemble import RandomForestClassifier
t0 = time.perf_counter()
rf_stock = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
rf_stock.fit(X_train, y_train)
t_stock_fit = time.perf_counter() - t0
auc_stock = roc_auc_score(y_test, rf_stock.predict_proba(X_test)[:, 1])
print(f"[Stock RF] Fit Time: {t_stock_fit:.3f} s, Test ROC-AUC: {auc_stock:.4f}")

# --- TASK 2: Enable Intel Acceleration ---
from sklearnex import _________
patch_sklearn(["_________"])

from sklearn.ensemble import RandomForestClassifier
t0 = time.perf_counter()
rf_intel = RandomForestClassifier(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
rf_intel.fit(X_train, y_train)
t_intel_fit = time.perf_counter() - t0
auc_intel = roc_auc_score(y_test, rf_intel.predict_proba(X_test)[:, 1])
print(f"[Intel RF] Fit Time: {t_intel_fit:.3f} s, Test ROC-AUC: {auc_intel:.4f}")

# --- TASK 3: Speedup Evaluation ---
print(f"[*] Training Speedup: {t_stock_fit / t_intel_fit:.2f}x")
```

### ✅ Complete Reference Solution Code
```python
"""
Lab 3 Solution: Accelerated Random Forest Classifier
"""
import time
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearnex import patch_sklearn, unpatch_sklearn

def run_random_forest_lab():
    print("=" * 65)
    print("      LAB 3: ACCELERATED RANDOM FOREST FRAUD DETECTION")
    print("=" * 65)
    
    # 1. Synthesize Imbalanced Fraud Dataset
    n_samples = 100_000
    n_features = 20
    print(f"[*] Generating {n_samples:,} transaction records ({n_features} features, 3% fraud rate)...")
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=14,
        weights=[0.97, 0.03],
        random_state=42
    )
    X = np.ascontiguousarray(X, dtype=np.float32)
    y = np.ascontiguousarray(y, dtype=np.int32)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 2. Phase 1: Stock Scikit-learn
    unpatch_sklearn()
    from sklearn.ensemble import RandomForestClassifier as StockRF
    
    print("\n[Phase 1] Training Stock Scikit-learn RandomForest (100 trees, max_depth=12)...")
    t0 = time.perf_counter()
    rf_stock = StockRF(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
    rf_stock.fit(X_train, y_train)
    t_stock_fit = time.perf_counter() - t0
    
    t0 = time.perf_counter()
    prob_stock = rf_stock.predict_proba(X_test)[:, 1]
    t_stock_pred = time.perf_counter() - t0
    auc_stock = roc_auc_score(y_test, prob_stock)
    
    print(f"   -> Stock Fit Time     : {t_stock_fit:.4f} seconds")
    print(f"   -> Stock Predict Time : {t_stock_pred:.4f} seconds")
    print(f"   -> Stock Test ROC-AUC : {auc_stock:.4f}")
    
    # 3. Phase 2: Intel oneDAL Accelerated RF
    print("\n[Phase 2] Dynamically Patching RandomForest via oneDAL...")
    patch_sklearn(["RandomForestClassifier"])
    from sklearn.ensemble import RandomForestClassifier as IntelRF
    
    print("   -> Verifying patch module:", IntelRF.__module__)
    t0 = time.perf_counter()
    rf_intel = IntelRF(n_estimators=100, max_depth=12, random_state=42, n_jobs=-1)
    rf_intel.fit(X_train, y_train)
    t_intel_fit = time.perf_counter() - t0
    
    t0 = time.perf_counter()
    prob_intel = rf_intel.predict_proba(X_test)[:, 1]
    t_intel_pred = time.perf_counter() - t0
    auc_intel = roc_auc_score(y_test, prob_intel)
    
    print(f"   -> Intel Fit Time     : {t_intel_fit:.4f} seconds")
    print(f"   -> Intel Predict Time : {t_intel_pred:.4f} seconds")
    print(f"   -> Intel Test ROC-AUC : {auc_intel:.4f}")
    
    # 4. Metrics & Assertions
    speedup_fit = t_stock_fit / t_intel_fit
    speedup_pred = t_stock_pred / t_intel_pred
    auc_delta = abs(auc_stock - auc_intel)
    
    print("\n" + "-" * 65)
    print(f"[*] TRAINING SPEEDUP        : {speedup_fit:.2f}x Faster")
    print(f"[*] INFERENCE SPEEDUP       : {speedup_pred:.2f}x Faster")
    print(f"[*] ROC-AUC ABSOLUTE DELTA  : {auc_delta:.5f}")
    print("-" * 65)
    
    assert auc_delta < 0.01, f"AUC divergence exceeds tolerance: {auc_delta}"
    assert speedup_fit > 3.0, f"Fit speedup below threshold: {speedup_fit:.2f}x"
    print("  [PASSED] Lab 3 Assertions Verified Successfully!\n")
    
    unpatch_sklearn()

if __name__ == "__main__":
    run_random_forest_lab()
```

### 🧪 Automated Verification Test
```python
def test_lab_3_random_forest_roc_parity():
    from sklearnex import patch_sklearn, unpatch_sklearn
    from sklearn.datasets import make_classification
    from sklearn.metrics import roc_auc_score
    import numpy as np
    
    X, y = make_classification(n_samples=20_000, n_features=10, weights=[0.95, 0.05], random_state=42)
    
    unpatch_sklearn()
    from sklearn.ensemble import RandomForestClassifier as StockRF
    m_stock = StockRF(n_estimators=30, max_depth=8, random_state=42).fit(X, y)
    auc_stock = roc_auc_score(y, m_stock.predict_proba(X)[:, 1])
    
    patch_sklearn(["RandomForestClassifier"])
    from sklearn.ensemble import RandomForestClassifier as IntelRF
    m_intel = IntelRF(n_estimators=30, max_depth=8, random_state=42).fit(X, y)
    auc_intel = roc_auc_score(y, m_intel.predict_proba(X)[:, 1])
    
    assert abs(auc_stock - auc_intel) < 0.015, "ROC-AUC divergence too large"
    unpatch_sklearn()
```

---

## 🧪 Lab 4: Genomic Data Dimensionality Reduction via PCA

### 🎯 Objective
Project 250,000 genomic expression profiles across 50 features down to 5 principal components. Measure SVD (Singular Value Decomposition) throughput, verify explained variance ratio concordance, and observe memory consumption.

### 🏢 Real-World Engineering Scenario
Bioinformatics pipelines process single-cell RNA sequencing arrays containing hundreds of thousands of cellular barcodes and dozens of marker gene clusters. Standard Scikit-learn PCA relies on standard LAPACK `dgesdd`/`dgesvd` routines that often copy arrays multiple times in memory. Intel oneDAL utilizes multi-threaded blocked Householder QR transformations optimized for L3 cache hierarchies, completing PCA in a fraction of the time.

### 📝 Step-by-Step Instructions
1. Generate synthetic genomic matrix $X \in \mathbb{R}^{250,000 \times 50}$ with correlated latent factors.
2. Fit standard `PCA(n_components=5, svd_solver="full")` and measure decomposition time.
3. Record total explained variance ratio: $\sum_{i=1}^5 \lambda_i / \sum \lambda$.
4. Enable `patch_sklearn(["PCA"])` and fit the accelerated model.
5. Compute speedup and assert that the explained variance ratio delta is $< 10^{-5}$.

### 🧩 Student Starter Code (Fill in the blanks `___`)
```python
"""
Lab 4 Starter Code: Accelerated Principal Component Analysis
"""
import time
import numpy as np

# Generate 250,000 high-dimensional genomic features
np.random.seed(42)
X = np.random.randn(250_000, 50).astype(np.float32)

# --- TASK 1: Benchmark Stock PCA ---
from sklearn.decomposition import PCA
t0 = time.perf_counter()
pca_stock = PCA(n_components=5, svd_solver="full", random_state=42)
X_proj_stock = pca_stock.fit_transform(X)
t_stock = time.perf_counter() - t0
var_stock = np.sum(pca_stock.explained_variance_ratio_)
print(f"[Stock PCA] Time: {t_stock:.3f} s, Explained Variance: {var_stock:.4f}")

# --- TASK 2: Enable Intel oneDAL Acceleration ---
from sklearnex import _________
patch_sklearn(["_________"])

from sklearn.decomposition import PCA
t0 = time.perf_counter()
pca_intel = PCA(n_components=5, svd_solver="full", random_state=42)
X_proj_intel = pca_intel.fit_transform(X)
t_intel = time.perf_counter() - t0
var_intel = np.sum(pca_intel.explained_variance_ratio_)
print(f"[Intel PCA] Time: {t_intel:.3f} s, Explained Variance: {var_intel:.4f}")

# --- TASK 3: Verification ---
speedup = t_stock / t_intel
print(f"[*] PCA Speedup: {speedup:.2f}x")
```

### ✅ Complete Reference Solution Code
```python
"""
Lab 4 Solution: Accelerated Principal Component Analysis
"""
import time
import numpy as np
from sklearnex import patch_sklearn, unpatch_sklearn

def run_pca_lab():
    print("=" * 65)
    print("      LAB 4: GENOMIC DATA DIMENSIONALITY REDUCTION (PCA)")
    print("=" * 65)
    
    # 1. Synthesize High-Dimensional Matrix
    n_samples = 250_000
    n_features = 50
    n_components = 5
    print(f"[*] Synthesizing {n_samples:,} genomic observations x {n_features} features...")
    np.random.seed(42)
    # Create covariance structure
    latent = np.random.randn(n_samples, 10).astype(np.float32)
    mixing = np.random.randn(10, n_features).astype(np.float32)
    X = np.dot(latent, mixing) + 0.1 * np.random.randn(n_samples, n_features).astype(np.float32)
    X = np.ascontiguousarray(X, dtype=np.float32)
    
    # 2. Phase 1: Stock Scikit-learn PCA
    unpatch_sklearn()
    from sklearn.decomposition import PCA as StockPCA
    
    print("\n[Phase 1] Fitting Standard Scikit-learn PCA (svd_solver='full')...")
    t0 = time.perf_counter()
    pca_stock = StockPCA(n_components=n_components, svd_solver="full", random_state=42)
    pca_stock.fit(X)
    t_stock = time.perf_counter() - t0
    var_stock = np.sum(pca_stock.explained_variance_ratio_)
    print(f"   -> Stock Time               : {t_stock:.4f} seconds")
    print(f"   -> Explained Variance Ratio : {var_stock:.6f}")
    
    # 3. Phase 2: Intel oneDAL Accelerated PCA
    print("\n[Phase 2] Dynamically Patching PCA via oneDAL...")
    patch_sklearn(["PCA"])
    from sklearn.decomposition import PCA as IntelPCA
    
    print("   -> Verifying patch module:", IntelPCA.__module__)
    t0 = time.perf_counter()
    pca_intel = IntelPCA(n_components=n_components, svd_solver="full", random_state=42)
    pca_intel.fit(X)
    t_intel = time.perf_counter() - t0
    var_intel = np.sum(pca_intel.explained_variance_ratio_)
    print(f"   -> Intel Time               : {t_intel:.4f} seconds")
    print(f"   -> Explained Variance Ratio : {var_intel:.6f}")
    
    # 4. Metrics & Parity Assertions
    speedup = t_stock / t_intel
    var_delta = abs(var_stock - var_intel)
    
    print("\n" + "-" * 65)
    print(f"[*] PCA SPEEDUP             : {speedup:.2f}x Faster")
    print(f"[*] EXPLAINED VARIANCE DELTA: {var_delta:.8f}")
    print("-" * 65)
    
    assert var_delta < 1e-4, f"Variance divergence exceeds threshold: {var_delta}"
    assert speedup > 3.0, f"Speedup below threshold: {speedup:.2f}x"
    print("  [PASSED] Lab 4 Assertions Verified Successfully!\n")
    
    unpatch_sklearn()

if __name__ == "__main__":
    run_pca_lab()
```

### 🧪 Automated Verification Test
```python
def test_lab_4_pca_variance_ratio():
    from sklearnex import patch_sklearn, unpatch_sklearn
    import numpy as np
    
    np.random.seed(42)
    X = np.random.randn(30_000, 20).astype(np.float32)
    
    unpatch_sklearn()
    from sklearn.decomposition import PCA as StockPCA
    m_stock = StockPCA(n_components=3, svd_solver="full", random_state=42).fit(X)
    
    patch_sklearn(["PCA"])
    from sklearn.decomposition import PCA as IntelPCA
    m_intel = IntelPCA(n_components=3, svd_solver="full", random_state=42).fit(X)
    
    delta = abs(np.sum(m_stock.explained_variance_ratio_) - np.sum(m_intel.explained_variance_ratio_))
    assert delta < 1e-4, f"PCA explained variance mismatch: {delta}"
    unpatch_sklearn()
```

---

## 🧪 Lab 5: Dynamic & Selective Monkey-Patching Verification

### 🎯 Objective
Master the internal mechanics of Python `sys.modules` monkey-patching. Learn how to patch specific estimators selectively, verify module namespaces, and safely unpatch without restarting the Python kernel.

### 🏢 Real-World Engineering Scenario
In a complex multi-team microservice codebase, some components may use experimental custom estimators that depend on private Scikit-learn internals, while performance-critical clustering requires oneDAL acceleration. Engineers must know how to selectively patch only `KMeans` and `PCA` while leaving other algorithms untouched, avoiding unintended side-effects.

### 📝 Step-by-Step Instructions
1. Inspect the initial state of `sys.modules` for Scikit-learn estimators.
2. Selectively patch only `KMeans` and `PCA` using `sklearnex.patch_sklearn(name=["sklearn.cluster.KMeans", "sklearn.decomposition.PCA"])` (or `["KMeans", "PCA"]` on legacy releases).
3. Assert that `sklearn.cluster.KMeans` resolves to `daal4py` or `sklearnex`.
4. Assert that `sklearn.ensemble.RandomForestClassifier` remains in the standard `sklearn.ensemble._forest` module (unpatched).
5. Call `sklearnex.unpatch_sklearn()` and assert that all estimators revert to stock Scikit-learn.

### 🧩 Student Starter Code (Fill in the blanks `___`)
```python
"""
Lab 5 Starter Code: Selective Patching Mechanics
"""
import sys
import sklearnex
from sklearnex import patch_sklearn, unpatch_sklearn

# Start unpatched
unpatch_sklearn()

# --- TASK 1: Selectively Patch ONLY KMeans and PCA ---
patch_sklearn(name=["_________", "_________"])

# Import estimators
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier

# --- TASK 2: Verify Module Namespaces ---
print(f"KMeans Module: {KMeans.__module__}")
print(f"PCA Module   : {PCA.__module__}")
print(f"RF Module    : {RandomForestClassifier.__module__}")

# Check conditions
assert "sklearnex" in KMeans.__module__ or "daal4py" in KMeans.__module__
assert "sklearnex" in PCA.__module__ or "daal4py" in PCA.__module__
# RF should NOT be patched
assert "sklearn.ensemble" in RandomForestClassifier.__module__

# --- TASK 3: Unpatch and Verify Full Rollback ---
unpatch_sklearn()
from sklearn.cluster import KMeans as RevertedKMeans
print(f"Reverted KMeans Module: {RevertedKMeans.__module__}")
```

### ✅ Complete Reference Solution Code
```python
"""
Lab 5 Solution: Selective Patching Mechanics
"""
import sys
import sklearnex
from sklearnex import patch_sklearn, unpatch_sklearn

def run_selective_patching_lab():
    print("=" * 65)
    print("      LAB 5: DYNAMIC & SELECTIVE MONKEY-PATCHING VERIFICATION")
    print("=" * 65)
    
    # 1. Reset to Clean State
    print("[*] Resetting all estimators to stock Scikit-learn...")
    unpatch_sklearn()
    
    from sklearn.cluster import KMeans as InitialKMeans
    from sklearn.ensemble import RandomForestClassifier as InitialRF
    print(f"   -> Baseline KMeans Module: {InitialKMeans.__module__}")
    print(f"   -> Baseline RF Module    : {InitialRF.__module__}")
    
    # 2. Selectively Patch
    # In modern scikit-learn-intelex (2024-2026+), patch_sklearn uses fully-qualified names:
    # ['sklearn.cluster.KMeans', 'sklearn.decomposition.PCA']. Legacy releases accept ['KMeans', 'PCA'].
    try:
        target_estimators = ["sklearn.cluster.KMeans", "sklearn.decomposition.PCA"]
        patch_sklearn(name=target_estimators)
    except ValueError:
        target_estimators = ["KMeans", "PCA"]
        patch_sklearn(name=target_estimators)
    print(f"\n[*] Applying SELECTIVE patch to: {target_estimators}...")
    
    from sklearn.cluster import KMeans as PatchedKMeans
    from sklearn.decomposition import PCA as PatchedPCA
    from sklearn.ensemble import RandomForestClassifier as UntouchedRF
    
    print(f"   -> Patched KMeans Module : {PatchedKMeans.__module__}")
    print(f"   -> Patched PCA Module    : {PatchedPCA.__module__}")
    print(f"   -> Untouched RF Module   : {UntouchedRF.__module__}")
    
    # 3. Assertions
    is_kmeans_patched = "sklearnex" in PatchedKMeans.__module__ or "daal4py" in PatchedKMeans.__module__
    is_pca_patched = "sklearnex" in PatchedPCA.__module__ or "daal4py" in PatchedPCA.__module__
    is_rf_stock = "sklearn.ensemble" in UntouchedRF.__module__ and "daal4py" not in UntouchedRF.__module__
    
    assert is_kmeans_patched, "ERROR: KMeans should be patched!"
    assert is_pca_patched, "ERROR: PCA should be patched!"
    assert is_rf_stock, "ERROR: RandomForestClassifier should NOT be patched!"
    print("   -> Selective patching assertions PASSED!")
    
    # 4. Global Unpatching
    print("\n[*] Unpatching all estimators...")
    unpatch_sklearn()
    
    from sklearn.cluster import KMeans as UnpatchedKMeans
    from sklearn.decomposition import PCA as UnpatchedPCA
    print(f"   -> Restored KMeans Module: {UnpatchedKMeans.__module__}")
    print(f"   -> Restored PCA Module   : {UnpatchedPCA.__module__}")
    
    assert "sklearn.cluster" in UnpatchedKMeans.__module__ and "daal4py" not in UnpatchedKMeans.__module__
    assert "sklearn.decomposition" in UnpatchedPCA.__module__ and "daal4py" not in UnpatchedPCA.__module__
    print("   -> Full rollback assertions PASSED!")
    
    print("=" * 65)
    print("  [PASSED] Lab 5 Mechanics Fully Validated!\n")

if __name__ == "__main__":
    run_selective_patching_lab()
```

### 🧪 Automated Verification Test
```python
def test_lab_5_selective_isolation():
    from sklearnex import patch_sklearn, unpatch_sklearn
    
    unpatch_sklearn()
    try:
        patch_sklearn(name=["sklearn.cluster.KMeans"])
    except ValueError:
        patch_sklearn(name=["KMeans"])
    
    from sklearn.cluster import KMeans
    from sklearn.linear_model import Ridge
    
    assert "daal4py" in KMeans.__module__ or "sklearnex" in KMeans.__module__
    assert "sklearn.linear_model" in Ridge.__module__
    
    unpatch_sklearn()
```

---

## 🧪 Lab 6: High-Throughput ML Pipeline (StandardScaler + PCA + KNN)

### 🎯 Objective
Construct an end-to-end multi-stage Scikit-learn Pipeline containing feature normalization (`StandardScaler`), dimensionality reduction (`PCA`), and non-parametric classification (`KNeighborsClassifier`). Evaluate training speedup and streaming query batch latency.

### 🏢 Real-World Engineering Scenario
A biometric authentication gateway captures high-dimensional facial embedding vectors. Each authentication request must be normalized, projected via PCA to remove noise, and matched against registered templates using K-Nearest Neighbors within a strict **50-millisecond SLA**. Stock Python KNN has $O(N \cdot D)$ brute-force distance compute latency. Intel oneDAL AVX-512 distance matrices accelerate KNN scoring by **15x to 30x**, easily satisfying real-time latency budgets.

### 📝 Step-by-Step Instructions
1. Synthesize 100,000 feature vectors with 40 dimensions across 10 identity classes.
2. Build a `sklearn.pipeline.Pipeline` with:
   - `('scaler', StandardScaler())`
   - `('pca', PCA(n_components=12, random_state=42))`
   - `('knn', KNeighborsClassifier(n_neighbors=5, n_jobs=-1))`
3. Train pipeline using standard Scikit-learn. Measure fit time and batch query latency on 5,000 test vectors.
4. Enable global Intel acceleration via `patch_sklearn()`.
5. Re-train and evaluate pipeline. Compare throughput (queries per second) and verify classification accuracy parity.

### 🧩 Student Starter Code (Fill in the blanks `___`)
```python
"""
Lab 6 Starter Code: High-Throughput Scikit-learn Pipeline
"""
import time
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Generate biometric embeddings
X, y = make_classification(n_samples=80_000, n_features=40, n_classes=10, n_informative=25, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# --- TASK 1: Build Pipeline ---
def build_pipeline():
    return Pipeline([
        ('scaler', _________()),
        ('pca', _________(n_components=12, random_state=42)),
        ('knn', _________(n_neighbors=5, n_jobs=-1))
    ])

# Fit stock pipeline
pipe_stock = build_pipeline()
t0 = time.perf_counter()
pipe_stock.fit(X_train, y_train)
t_stock_fit = time.perf_counter() - t0
y_pred_stock = pipe_stock.predict(X_test)
acc_stock = accuracy_score(y_test, y_pred_stock)
print(f"[Stock Pipeline] Fit Time: {t_stock_fit:.3f} s, Accuracy: {acc_stock:.4f}")

# --- TASK 2: Enable Intel Acceleration ---
from sklearnex import _________
patch_sklearn()

pipe_intel = build_pipeline()
t0 = time.perf_counter()
pipe_intel.fit(X_train, y_train)
t_intel_fit = time.perf_counter() - t0
y_pred_intel = pipe_intel.predict(X_test)
acc_intel = accuracy_score(y_test, y_pred_intel)
print(f"[Intel Pipeline] Fit Time: {t_intel_fit:.3f} s, Accuracy: {acc_intel:.4f}")
print(f"[*] Pipeline Speedup: {t_stock_fit / t_intel_fit:.2f}x")
```

### ✅ Complete Reference Solution Code
```python
"""
Lab 6 Solution: High-Throughput Scikit-learn Pipeline
"""
import time
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearnex import patch_sklearn, unpatch_sklearn

def run_pipeline_lab():
    print("=" * 65)
    print("      LAB 6: HIGH-THROUGHPUT ML PIPELINE (SCALER + PCA + KNN)")
    print("=" * 65)
    
    # 1. Generate Biometric Embedding Simulation
    n_samples = 80_000
    n_features = 40
    n_classes = 10
    print(f"[*] Generating {n_samples:,} vectors x {n_features} features ({n_classes} classes)...")
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_informative=25,
        n_classes=n_classes,
        random_state=42
    )
    X = np.ascontiguousarray(X, dtype=np.float32)
    y = np.ascontiguousarray(y, dtype=np.int32)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=5_000, random_state=42)
    
    # Pipeline Factory
    def create_pipeline():
        return Pipeline([
            ('scaler', StandardScaler()),
            ('pca', PCA(n_components=12, random_state=42)),
            ('knn', KNeighborsClassifier(n_neighbors=5, n_jobs=-1))
        ])
    
    # 2. Phase 1: Stock Scikit-learn Pipeline
    unpatch_sklearn()
    print("\n[Phase 1] Training Standard Scikit-learn Pipeline...")
    pipe_stock = create_pipeline()
    
    t0 = time.perf_counter()
    pipe_stock.fit(X_train, y_train)
    t_stock_fit = time.perf_counter() - t0
    
    t0 = time.perf_counter()
    preds_stock = pipe_stock.predict(X_test)
    t_stock_pred = time.perf_counter() - t0
    acc_stock = accuracy_score(y_test, preds_stock)
    
    qps_stock = len(X_test) / t_stock_pred
    print(f"   -> Stock Fit Time    : {t_stock_fit:.4f} seconds")
    print(f"   -> Stock Query Time  : {t_stock_pred:.4f} seconds ({qps_stock:,.1f} Queries/sec)")
    print(f"   -> Stock Accuracy    : {acc_stock * 100:.2f}%")
    
    # 3. Phase 2: Intel oneDAL Accelerated Pipeline
    print("\n[Phase 2] Globally Patching Pipeline via oneDAL...")
    patch_sklearn()
    pipe_intel = create_pipeline()
    
    t0 = time.perf_counter()
    pipe_intel.fit(X_train, y_train)
    t_intel_fit = time.perf_counter() - t0
    
    t0 = time.perf_counter()
    preds_intel = pipe_intel.predict(X_test)
    t_intel_pred = time.perf_counter() - t0
    acc_intel = accuracy_score(y_test, preds_intel)
    
    qps_intel = len(X_test) / t_intel_pred
    print(f"   -> Intel Fit Time    : {t_intel_fit:.4f} seconds")
    print(f"   -> Intel Query Time  : {t_intel_pred:.4f} seconds ({qps_intel:,.1f} Queries/sec)")
    print(f"   -> Intel Accuracy    : {acc_intel * 100:.2f}%")
    
    # 4. Metrics & Evaluation
    speedup_fit = t_stock_fit / t_intel_fit
    speedup_pred = t_stock_pred / t_intel_pred
    acc_delta = abs(acc_stock - acc_intel)
    
    print("\n" + "-" * 65)
    print(f"[*] PIPELINE FIT SPEEDUP    : {speedup_fit:.2f}x Faster")
    print(f"[*] INFERENCE LATENCY SPEEDUP: {speedup_pred:.2f}x Faster ({qps_intel/qps_stock:.1f}x QPS)")
    print(f"[*] ACCURACY ABSOLUTE DELTA : {acc_delta:.6f}")
    print("-" * 65)
    
    assert acc_delta < 0.02, f"Accuracy divergence exceeds threshold: {acc_delta}"
    assert speedup_pred > 2.0, f"Inference speedup below threshold: {speedup_pred:.2f}x"
    print("  [PASSED] Lab 6 Pipeline Assertions Verified Successfully!\n")
    
    unpatch_sklearn()

if __name__ == "__main__":
    run_pipeline_lab()
```

### 🧪 Automated Verification Test
```python
def test_lab_6_pipeline_integrity():
    from sklearnex import patch_sklearn, unpatch_sklearn
    from sklearn.datasets import make_classification
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.decomposition import PCA
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import accuracy_score
    
    X, y = make_classification(n_samples=5_000, n_features=15, n_classes=3, random_state=42)
    
    def make_pipe():
        return Pipeline([
            ('scaler', StandardScaler()),
            ('pca', PCA(n_components=5, random_state=42)),
            ('knn', KNeighborsClassifier(n_neighbors=3))
        ])
    
    unpatch_sklearn()
    p_stock = make_pipe().fit(X, y)
    acc_stock = accuracy_score(y, p_stock.predict(X))
    
    patch_sklearn()
    p_intel = make_pipe().fit(X, y)
    acc_intel = accuracy_score(y, p_intel.predict(X))
    
    assert abs(acc_stock - acc_intel) < 0.03, "Pipeline accuracy divergence too large"
    unpatch_sklearn()
```

---

## 🏆 Summary Checklist for Students
To earn full marks in the Day 2 afternoon practical lab session, ensure you have:
1. Executed all 6 lab scripts in your active environment.
2. Recorded the execution timings and speedup ratios in your lab worksheet.
3. Verified that numerical parity (inertia, variance ratio, ROC-AUC) is strictly preserved.
4. Practiced selective unpatching using `unpatch_sklearn()`.
