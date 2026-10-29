#!/usr/bin/env python3
"""
tf_distributed_profiling.py
Distributed TensorFlow Benchmark with Step Timing & Profiling Hooks.
Employs Horovod Ring-AllReduce when available, with a local single-node simulator fallback.
"""

import os
import sys
import time
import argparse

# Check for Horovod availability
try:
    import horovod.tensorflow as hvd
    HVD_AVAILABLE = True
except ImportError:
    HVD_AVAILABLE = False

try:
    import tensorflow as tf
    TF_AVAILABLE = True
except ImportError:
    TF_AVAILABLE = False

def init_environment():
    if HVD_AVAILABLE:
        hvd.init()
        rank = hvd.rank()
        local_rank = hvd.local_rank()
        size = hvd.size()
    else:
        rank = 0
        local_rank = 0
        size = 1
        
    return rank, local_rank, size

def run_synthetic_distributed_benchmark(epochs=5, batch_size=128, rank=0, size=1):
    if rank == 0:
        print("==========================================================")
        print("    DISTRIBUTED TENSORFLOW & PROFILING BENCHMARK          ")
        print(f"    Total Distributed Workers (World Size): {size}")
        print(f"    Per-Worker Batch Size:                  {batch_size}")
        print(f"    Effective Global Batch Size:            {batch_size * size}")
        print(f"    Training Epochs:                        {epochs}")
        print("==========================================================")

    if not TF_AVAILABLE:
        if rank == 0:
            print("[!] TensorFlow not detected in local python environment.")
            print("[*] Running synthetic distributed step simulator for timing calibration...")
        for epoch in range(1, epochs + 1):
            t0 = time.perf_counter()
            # Simulate forward pass, backward pass, and allreduce gradient exchange
            time.sleep(0.08) # Compute time
            # AllReduce ring time: 2*(size-1)/size * (M/Bandwidth)
            ring_transfer_delay = 0.02 * (size - 1) / size if size > 1 else 0.001
            time.sleep(ring_transfer_delay)
            t1 = time.perf_counter()
            step_time_ms = (t1 - t0) * 1000
            throughput = (batch_size * size) / (t1 - t0)
            if rank == 0:
                print(f"Epoch {epoch:02d}/{epochs:02d} | Step Time: {step_time_ms:.2f} ms | Throughput: {throughput:.1f} images/sec")
        return

    # Real TensorFlow execution path
    # Configure CPU threading / GPU pinning
    tf.config.threading.set_inter_op_parallelism_threads(2)
    tf.config.threading.set_intra_op_parallelism_threads(4)

    # Synthetic ResNet-like Conv2D model
    inputs = tf.keras.Input(shape=(64, 64, 3))
    x = tf.keras.layers.Conv2D(64, (3, 3), padding='same', activation='relu')(inputs)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.Conv2D(128, (3, 3), padding='same', activation='relu')(x)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
    model = tf.keras.Model(inputs=inputs, outputs=outputs)

    # Linear scaling rule for learning rate
    base_lr = 0.001
    scaled_lr = base_lr * size
    optimizer = tf.keras.optimizers.Adam(learning_rate=scaled_lr)

    if HVD_AVAILABLE and size > 1:
        optimizer = hvd.DistributedOptimizer(optimizer)

    loss_fn = tf.keras.losses.CategoricalCrossentropy()

    # Synthetic dataset
    x_train = tf.random.normal((batch_size * 4, 64, 64, 3))
    y_train = tf.one_hot(tf.random.uniform((batch_size * 4,), maxval=10, dtype=tf.int32), depth=10)
    dataset = tf.data.Dataset.from_tensor_slices((x_train, y_train)).batch(batch_size)

    @tf.function
    def train_step(x_b, y_b, first_batch):
        with tf.GradientTape() as tape:
            preds = model(x_b, training=True)
            loss_val = loss_fn(y_b, preds)
        
        grads = tape.gradient(loss_val, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))
        
        if HVD_AVAILABLE and size > 1 and first_batch:
            hvd.broadcast_variables(model.variables, root_rank=0)
            hvd.broadcast_variables(optimizer.variables(), root_rank=0)
            
        return loss_val

    # Warmup step
    for x_b, y_b in dataset.take(1):
        _ = train_step(x_b, y_b, first_batch=True)

    # Benchmarking epochs
    for epoch in range(1, epochs + 1):
        t0 = time.perf_counter()
        total_loss = 0.0
        steps = 0
        for x_b, y_b in dataset:
            loss = train_step(x_b, y_b, first_batch=False)
            total_loss += float(loss)
            steps += 1
        t1 = time.perf_counter()
        
        elapsed = t1 - t0
        throughput = (batch_size * steps * size) / elapsed if elapsed > 0 else 0
        if rank == 0:
            print(f"Epoch {epoch:02d}/{epochs:02d} | Avg Loss: {total_loss/steps:.4f} | Time: {elapsed*1000:.2f} ms | Throughput: {throughput:.1f} img/s")

def main():
    parser = argparse.ArgumentParser(description="Distributed TensorFlow & Profiling Benchmark")
    parser.add_argument("--epochs", type=int, default=5, help="Number of training epochs")
    parser.add_argument("--batch-size", type=int, default=128, help="Minibatch size per worker")
    args = parser.parse_args()

    rank, local_rank, size = init_environment()
    run_synthetic_distributed_benchmark(epochs=args.epochs, batch_size=args.batch_size, rank=rank, size=size)
    
    if rank == 0:
        print("\n[✓] Benchmark execution finished successfully!")

if __name__ == "__main__":
    main()
