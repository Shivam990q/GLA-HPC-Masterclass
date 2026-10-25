# 💻 DAY 2: HANDS-ON LAB & COMMANDS PLAYBOOK
## Practical Execution for OpenMP Multithreading & Scikit-Learn Acceleration
**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance  
**Primary Reference:** `Intel & NEC - High Performance Computing.pdf`

---

## 📋 LAB SECTION 1: OpenMP Multithreading in C++

```cpp
// Save as openmp_vector_sum.cpp
#include <iostream>
#include <vector>
#include <omp.h>

int main() {
    const size_t N = 50000000; // 50 Million elements
    std::vector<double> data(N, 1.0);
    double total_sum = 0.0;

    std::cout << "[INFO] Available OpenMP Threads: " << omp_get_max_threads() << std::endl;

    double start = omp_get_wtime();

    #pragma omp parallel for reduction(+:total_sum)
    for (size_t i = 0; i < N; ++i) {
        total_sum += data[i];
    }

    double end = omp_get_wtime();

    std::cout << "[SUCCESS] Computed sum = " << total_sum << " in " << (end - start) * 1000.0 << " ms" << std::endl;
    return 0;
}
```

```bash
# Compilation with Intel oneAPI Compiler:
icpx -O3 -qopenmp openmp_vector_sum.cpp -o openmp_sum 2>/dev/null || g++ -O3 -fopenmp openmp_vector_sum.cpp -o openmp_sum
./openmp_sum
```

---

## 📋 LAB SECTION 2: Scikit-learn Acceleration with Intel oneDAL (`sklearnex`)

```python
# Save as benchmark_sklearnex.py
import time
import numpy as np
from sklearn.datasets import make_blobs

# Generate 500,000 samples with 32 features
print("[INFO] Generating synthetic clustering dataset (500,000 samples, 32 features)...")
X, _ = make_blobs(n_samples=500000, n_features=32, centers=10, random_state=42)

# --- 1. Stock Scikit-Learn Run ---
from sklearn.cluster import KMeans
print("[RUN 1] Running Stock Scikit-learn k-Means...")
start = time.time()
kmeans_stock = KMeans(n_clusters=10, max_iter=20, n_init=1, random_state=42)
kmeans_stock.fit(X)
stock_time = time.time() - start
print(f"Stock Scikit-learn Time: {stock_time:.3f} seconds")

# --- 2. Intel oneDAL Accelerated Run ---
print("\n[RUN 2] Applying Intel oneDAL Acceleration (patch_sklearn)...")
from sklearnex import patch_sklearn
patch_sklearn()
from sklearn.cluster import KMeans as AcceleratedKMeans

start = time.time()
kmeans_intel = AcceleratedKMeans(n_clusters=10, max_iter=20, n_init=1, random_state=42)
kmeans_intel.fit(X)
intel_time = time.time() - start
print(f"Intel oneDAL Time:        {intel_time:.3f} seconds")

speedup = stock_time / intel_time if intel_time > 0 else 1.0
print("==========================================================")
print(f"MEASURED SPEEDUP:        {speedup:.2f}x FASTER!")
print("==========================================================")
```

```bash
python3 benchmark_sklearnex.py
```
