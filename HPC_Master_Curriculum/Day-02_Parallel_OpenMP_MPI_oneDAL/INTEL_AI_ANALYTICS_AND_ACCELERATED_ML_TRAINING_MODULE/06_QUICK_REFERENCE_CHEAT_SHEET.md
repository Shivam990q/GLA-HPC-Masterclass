# ⚡ INTEL AI ANALYTICS & ONEDAL QUICK REFERENCE CHEAT SHEET
## High-Performance Classical Machine Learning Acceleration with `sklearnex` & NumPy MKL
**GLA University — HPC & Intel oneAPI Masterclass | Day 02 (Afternoon Applied Session)**

---

## 🚀 1. The 2-Line Dynamic Patching Formula

Accelerate existing Scikit-learn code up to **10x–35x** on CPU with zero algorithmic changes.

### A. Global Dynamic Monkey-Patch (Recommended for Scripts & Notebooks)
*Rule: Always execute patching **before** importing any Scikit-learn estimators!*
```python
# MUST BE AT THE VERY TOP OF YOUR SCRIPT OR FIRST NOTEBOOK CELL
from sklearnex import patch_sklearn
patch_sklearn()

# Normal Scikit-learn imports now load oneDAL C++ kernels automatically
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.neighbors import NearestNeighbors
from sklearn.svm import SVC
```

### B. Command-Line Patching (Zero Code Changes)
Accelerate third-party or legacy Python scripts without editing a single line of code:
```bash
# Invoking through python -m sklearnex monkey-patches sys.modules prior to script execution
python -m sklearnex train_pipeline.py --dataset massive_matrix.csv
```

### C. Selective Estimator Patching
Target specific compute-heavy estimators while leaving others on vanilla scikit-learn:
```python
from sklearnex import patch_sklearn

# Patch ONLY KMeans and PCA:
patch_sklearn(name=["KMeans", "PCA"])

# Or patch an entire algorithm family:
patch_sklearn(name=["svm", "cluster"])
```

### D. Reverting to Vanilla Scikit-learn (Runtime Unpatching)
Revert estimators back to vanilla scikit-learn in the same Python process:
```python
from sklearnex import unpatch_sklearn
unpatch_sklearn()

# Verify that the unpatch succeeded:
from sklearn.cluster import KMeans
print(KMeans.__module__)  # Outputs: 'sklearn.cluster._kmeans' (Stock)
```

---

## 🛠️ 2. Core Environment Variables & Hardware Tuning

Intel oneDAL uses OpenMP and Intel MKL underneath. Control threading, memory affinity, and telemetry via environment variables:

| Environment Variable | Recommended Value | Architectural Mechanism & Impact |
|:---------------------|:-----------------:|:---------------------------------|
| `OMP_NUM_THREADS` | `$(nproc)` / Physical Cores | Sets the OpenMP thread team size. Optimal when set to **physical cores** (ignoring Hyper-Threading / SMT logical virtual threads). |
| `MKL_NUM_THREADS` | Physical Cores | Thread pool budget specifically for NumPy MKL BLAS / LAPACK matrix operations. |
| `KMP_AFFINITY` | `granularity=fine,compact,1,0` | Binds OpenMP worker threads to adjacent CPU cores, maximizing shared L2/L3 cache line reuse and eliminating thread migration across sockets. |
| `SKLEARNEX_VERBOSE` | `INFO` or `DEBUG` | Prints real-time acceleration logs to stderr when oneDAL C++ kernels are dispatched. |
| `MKL_DEBUG_CPU_TYPE` | `5` | Forces Intel MKL to utilize AVX2 SIMD dispatch pathways even on compatible non-Intel x86_64 host processors (e.g. AMD Zen). |

### Setting Environment Variables in Bash / Linux:
```bash
export OMP_NUM_THREADS=$(lscpu -p | egrep -v '^#' | sort -u -k 2 -n | wc -l) # Physical cores
export KMP_AFFINITY="granularity=fine,compact,1,0"
export SKLEARNEX_VERBOSE="INFO"
python train_model.py
```

### Setting Environment Variables in Python / Jupyter:
```python
import os
os.environ["OMP_NUM_THREADS"] = "8"
os.environ["KMP_AFFINITY"] = "granularity=fine,compact,1,0"
os.environ["SKLEARNEX_VERBOSE"] = "INFO"

from sklearnex import patch_sklearn
patch_sklearn()
```

---

## 📊 3. Supported Estimators & Expected Acceleration Matrix

| Estimator / Algorithm | Module Origin | Typical Speedup | Key Accelerating Features |
|:----------------------|:--------------|:---------------:|:--------------------------|
| **KMeans** | `daal4py.sklearn.cluster` | **15x – 30x** | Lloyd's algorithm vectorized via AVX-512; parallel distance matrix calculations. |
| **PCA** | `daal4py.sklearn.decomposition` | **10x – 25x** | MKL LAPACK SVD decomposition; correlation matrix computed in parallel C++ buffers. |
| **RandomForestClassifier** | `daal4py.sklearn.ensemble` | **10x – 20x** | Multi-threaded tree construction; SIMD histogram binning; cache-friendly feature evaluation. |
| **RandomForestRegressor** | `daal4py.sklearn.ensemble` | **8x – 18x** | Parallel variance reduction; SIMD split finding. |
| **LinearRegression** | `daal4py.sklearn.linear_model` | **5x – 15x** | Fast normal equations via Intel MKL Cholesky / QR solver. |
| **LogisticRegression** | `daal4py.sklearn.linear_model` | **4x – 12x** | L-BFGS & Newton-CG solvers accelerated via MKL matrix-vector kernels. |
| **SVC / SVR** | `daal4py.sklearn.svm` | **10x – 35x** | Replaces standard sequential LibSVM with Intel oneDAL SMO solver. |
| **NearestNeighbors / KNN** | `daal4py.sklearn.neighbors` | **8x – 22x** | Vectorized Euclidean distance metrics; parallel KD-tree / brute-force queries. |
| **DBSCAN** | `daal4py.sklearn.cluster` | **12x – 28x** | Fast spatial neighborhood indexing with multi-threaded cluster expansion. |
| **t-SNE** | `daal4py.sklearn.manifold` | **15x – 40x** | Barnes-Hut quadtree / octree evaluation optimized for AVX-512 CPU registers. |

---

## 🧠 4. The Memory & Architecture Mental Model

### CPython Vanilla vs Intel oneDAL Execution Flow
```
Vanilla Scikit-Learn:
[Python Script] ──► [CPython GIL Locked] ──► [Boxed PyObject Pointers] ──► [Sequential Cython/C] ──► Cache Misses (80ns)

Intel Extension for Scikit-learn (oneDAL):
[Python Script] ──► [patch_sklearn()] ──► [Zero-Copy PyArray Ptr] ──► [GIL RELEASED] ──► [C++ oneDAL / AVX-512 / OpenMP]
                                                                                               │
                                                                                               ▼
                                                                                   L1 Cache Burst (<1ns)
```

### The 3 Core Rules for Peak Throughput:
1. **Contiguous Memory**: Always ensure input data is contiguous float64 or float32. Discontinuous arrays force memory reallocation before C++ dispatch:
   ```python
   X = np.ascontiguousarray(X, dtype=np.float32) # float32 yields 2x AVX vector density!
   ```
2. **Release the GIL**: oneDAL drops the Python Global Interpreter Lock during computation, allowing all CPU cores to compute in parallel.
3. **Double vs Single Precision**: If mathematical precision permits, `np.float32` fits **16 floats** in an AVX-512 register versus **8 floats** for `np.float64`, doubling theoretical arithmetic throughput.

---

## 🔍 5. Runtime Verification & Integrity Assertion

Copy-paste this snippet into any script to verify whether oneDAL acceleration is actively engaged:

```python
import sklearn
import sklearnex

def verify_onedal_status():
    from sklearn.cluster import KMeans
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.decomposition import PCA
    
    is_km_patched = "daal4py" in KMeans.__module__ or "sklearnex" in KMeans.__module__
    is_rf_patched = "daal4py" in RandomForestClassifier.__module__ or "sklearnex" in RandomForestClassifier.__module__
    is_pca_patched = "daal4py" in PCA.__module__ or "sklearnex" in PCA.__module__
    
    print("=" * 60)
    print("⚡ INTEL ONEDAL ACCELERATION AUDIT")
    print(f"  • KMeans Patched:          {'✅ YES (' + KMeans.__module__ + ')' if is_km_patched else '❌ NO (Stock)'}")
    print(f"  • RandomForest Patched:    {'✅ YES (' + RandomForestClassifier.__module__ + ')' if is_rf_patched else '❌ NO (Stock)'}")
    print(f"  • PCA Patched:             {'✅ YES (' + PCA.__module__ + ')' if is_pca_patched else '❌ NO (Stock)'}")
    print("=" * 60)
    return is_km_patched and is_rf_patched and is_pca_patched

# Test:
verify_onedal_status()
```

---

## 🚨 6. Troubleshooting & Common Gotchas

### ⚠️ Gotcha 1: "I called patch_sklearn() but speedup is 1.0x!"
* **Cause**: `from sklearn.cluster import KMeans` was imported **before** `patch_sklearn()`.
* **Fix**: Move `patch_sklearn()` to line 1 of the file, before ANY `sklearn` import.

### ⚠️ Gotcha 2: "Dataset has string or categorical columns"
* **Cause**: oneDAL operates on raw numerical matrices (float32/float64).
* **Fix**: Encode categories via `OneHotEncoder` or `OrdinalEncoder`, and pass pure numeric NumPy arrays into `.fit()`.

### ⚠️ Gotcha 3: "Thread oversubscription on small datasets (< 10,000 rows)"
* **Cause**: On tiny datasets, thread creation and synchronization overhead exceeds the computation time.
* **Fix**: oneDAL has built-in heuristics to fall back to serial execution on small inputs. For maximum speedup, train on $N \ge 50,000$ rows.

### ⚠️ Gotcha 4: "Multi-socket NUMA remote memory latency"
* **Cause**: On 2-socket Xeon servers, OpenMP threads accessing RAM attached to the remote CPU socket incur 140ns latency penalties.
* **Fix**: Run using `numactl --interleave=all python script.py` or bind to a single socket with `numactl --cpunodebind=0 --membind=0 python script.py`.
