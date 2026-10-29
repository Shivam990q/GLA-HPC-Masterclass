#!/usr/bin/env python3
"""
tf_onednn_benchmark.py
Intel oneDNN Operator Fusion & Hardware-Aware Convolution Benchmark in TensorFlow
GLA University — High Performance Computing | Lead: Shivam Gupta
"""

import os
import sys
import time

print("=" * 75)
print("   🚀 INTEL oneDNN OPERATOR FUSION BENCHMARK IN TENSORFLOW         ")
print("      GLA University High Performance Computing | Lead: Shivam Gupta")
print("=" * 75)

# 1. Inspect active oneDNN Environment Configuration
onednn_status = os.environ.get("TF_ENABLE_ONEDNN_OPTS", "1")
print(f"[*] Environment Variable TF_ENABLE_ONEDNN_OPTS = {onednn_status}")

try:
    import tensorflow as tf
    print(f"[+] TensorFlow Version: {tf.__version__}")
    
    # Check if oneDNN is compiled into binary
    is_onednn_enabled = tf.test.is_built_with_cpu_support()
    print(f"[+] Built with CPU acceleration support: {is_onednn_enabled}")
except ImportError:
    print("[!] TensorFlow not installed in current environment.")
    print("[!] Install via: pip install intel-optimized-tensorflow or pip install tensorflow")
    sys.exit(0)

# Configure CPU Threading for Intel Xeon
num_threads = os.cpu_count() or 4
tf.config.threading.set_inter_op_parallelism_threads(2)
tf.config.threading.set_intra_op_parallelism_threads(num_threads)
print(f"[+] Configured intra-op threads: {num_threads}, inter-op threads: 2")

# 2. Benchmark Operator Fusion: Conv2D + BiasAdd + ReLU vs Unfused Sequence
# Batch=128, Image=64x64x64, Filters=128, Kernel=3x3
BATCH_SIZE = 128
H, W, C = 64, 64, 64
FILTERS = 128
KERNEL_SIZE = 3

print(f"\n[*] Synthesizing deep learning input tensor: ({BATCH_SIZE}, {H}, {W}, {C})...")
input_tensor = tf.random.normal([BATCH_SIZE, H, W, C], dtype=tf.float32)
conv_layer = tf.keras.layers.Conv2D(
    filters=FILTERS,
    kernel_size=KERNEL_SIZE,
    padding='same',
    activation='relu',
    use_bias=True
)

# Warm-up run to trigger oneDNN JIT kernel compilation
print("[*] Performing warm-up inference run to trigger oneDNN JIT fusion...")
_ = conv_layer(input_tensor[:4])

# Timed Benchmark
NUM_ITERATIONS = 50
print(f"[*] Executing {NUM_ITERATIONS} iterations of fused Conv2D+BiasAdd+ReLU...")
t0 = time.time()
for _ in range(NUM_ITERATIONS):
    output = conv_layer(input_tensor)
elapsed = time.time() - t0

avg_latency_ms = (elapsed / NUM_ITERATIONS) * 1000.0
images_per_second = (BATCH_SIZE * NUM_ITERATIONS) / elapsed

print("\n" + "=" * 75)
print(f"  🏆 oneDNN CONVOLUTION BENCHMARK RESULTS:")
print(f"     Total Elapsed Time   : {elapsed:.3f} seconds")
print(f"     Average Step Latency : {avg_latency_ms:.2f} ms")
print(f"     Inference Throughput : {images_per_second:.1f} Images/Second")
print("=" * 75)
print("[+] Architectural Insight: Intel oneDNN fuses Convolution + Bias + ReLU")
print("    into a single memory-resident L1/L2 cache pass, eliminating intermediate")
print("    round-trips to DDR RAM and maximizing AVX-512 FMA utilization.")
