# compute_engine.py
import sys
import time
import os

mode = sys.argv[1] if len(sys.argv) > 1 else "standard"
SIZE = 5000000

if mode == "standard":
    print("[-] Running STANDARD (Single-threaded Python) Mode...")
    t0 = time.time()
    data = list(range(SIZE))
    result = [x * 1.00001 for x in data]
    total = sum(result)
    elapsed = time.time() - t0
    print(f"[-] Standard Execution Time : {elapsed:.3f}s | Sum: {total:.2f}")

elif mode == "accelerated":
    print("[+] Running HPC ACCELERATED (Intel Vectorized) Mode...")
    import numpy as np
    t0 = time.time()
    data = np.arange(SIZE, dtype=np.float64)
    result = data * 1.00001
    total = np.sum(result)
    elapsed = time.time() - t0
    print(f"[+] HPC Vectorized Time     : {elapsed:.3f}s | Sum: {total:.2f}")
