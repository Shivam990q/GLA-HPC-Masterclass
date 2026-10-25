# cpu_bottleneck_demo.py
# Designed to demonstrate Memory-Bound vs Compute-Bound profiles in VTune
import time
import numpy as np

SIZE = 50000000

print("[*] Running Cache-Thrashing Memory Access (Inefficient)...")
t0 = time.time()
# Stride access causes L1/L2/L3 cache misses
arr = np.ones(SIZE, dtype=np.int32)
stride_sum = np.sum(arr[::64])
print(f"[-] Stride Sum: {stride_sum} in {time.time() - t0:.3f}s")

print("[*] Running Memory-Contiguous Vectorized Access (Optimized)...")
t0 = time.time()
contiguous_sum = np.sum(arr[:SIZE//64])
print(f"[+] Contiguous Sum: {contiguous_sum} in {time.time() - t0:.3f}s")
