"""
generate_synthetic_datasets.py
Edulateral Foundation — Offline Synthetic Dataset Generator for HPC Workshops.
Generates deterministic, zero-network benchmark datasets for:
- Day 2: Intel oneDAL / Scikit-learn speedup benchmarks (500,000 samples, 20 features)
- Day 2: High-dimensional regression benchmarks (1,000,000 samples, 30 features)
- Day 3: Image classification tensors (10,000 samples, 28x28 normalized floats)
- Day 5: Offline text corpus for LLM prompt benchmarking

Run this script locally to populate the pen drive before deploying to GLA University labs.
"""

import os
import sys
import numpy as np

def generate_datasets(output_dir="03_BENCHMARK_DATASETS"):
    os.makedirs(output_dir, exist_ok=True)
    print(f"[*] Initializing synthetic dataset generator in: {output_dir}")
    np.random.seed(42)

    # 1. Classification Dataset (500,000 samples, 20 features)
    cls_path = os.path.join(output_dir, "classification_500k_20feat.npz")
    if not os.path.exists(cls_path):
        print("  -> Generating 500k classification dataset (float32)...")
        n_samples = 500_000
        n_features = 20
        X = np.random.randn(n_samples, n_features).astype(np.float32)
        # Create a non-linear separable boundary
        weights = np.random.randn(n_features).astype(np.float32)
        logits = np.dot(X, weights) + 0.5 * (X[:, 0] ** 2)
        y = (logits > 0).astype(np.int32)
        np.savez_compressed(cls_path, X=X, y=y)
        print(f"     [OK] Saved {cls_path} ({os.path.getsize(cls_path) / (1024*1024):.2f} MB)")
    else:
        print(f"     [EXISTS] {cls_path}")

    # 2. Regression Dataset (1,000,000 samples, 30 features)
    reg_path = os.path.join(output_dir, "regression_1m_30feat.npz")
    if not os.path.exists(reg_path):
        print("  -> Generating 1M regression dataset (float32)...")
        n_samples = 1_000_000
        n_features = 30
        X_reg = np.random.uniform(-5.0, 5.0, size=(n_samples, n_features)).astype(np.float32)
        true_w = np.linspace(0.1, 2.0, n_features, dtype=np.float32)
        noise = np.random.normal(0, 0.1, size=n_samples).astype(np.float32)
        y_reg = np.dot(X_reg, true_w) + noise
        np.savez_compressed(reg_path, X=X_reg, y=y_reg)
        print(f"     [OK] Saved {reg_path} ({os.path.getsize(reg_path) / (1024*1024):.2f} MB)")
    else:
        print(f"     [EXISTS] {reg_path}")

    # 3. Vision Tensor Dataset (10,000 samples, 28x28 normalized)
    img_path = os.path.join(output_dir, "mnist_offline_arrays.npz")
    if not os.path.exists(img_path):
        print("  -> Generating synthetic image arrays for TF-MKL / Horovod (10k images)...")
        n_images = 10_000
        X_img = np.random.uniform(0.0, 1.0, size=(n_images, 28, 28, 1)).astype(np.float32)
        y_img = np.random.randint(0, 10, size=n_images, dtype=np.int32)
        np.savez_compressed(img_path, X_train=X_img, y_train=y_img)
        print(f"     [OK] Saved {img_path} ({os.path.getsize(img_path) / (1024*1024):.2f} MB)")
    else:
        print(f"     [EXISTS] {img_path}")

    # 4. Offline Text Corpus for LLM Prompt Benchmarking
    txt_path = os.path.join(output_dir, "synthetic_text_corpus.txt")
    if not os.path.exists(txt_path):
        print("  -> Generating offline text corpus for LLM prompt processing...")
        prompts = [
            "Explain the difference between Amdahl's Law and Gustafson's Law in HPC clusters.",
            "How does Intel Advanced Matrix Extensions (AMX) accelerate bfloat16 matrix multiplication?",
            "Detail the Ring-AllReduce communication volume formula and why it avoids parameter server bottlenecks.",
            "Describe the architecture of the NEC SX-Aurora TSUBASA Vector Engine and its 1.53 TB/s memory bandwidth.",
            "Compare the Prefill phase versus the Decode phase in large language model inference on Intel Xeon CPUs.",
            "Explain how OpenVINO INT4 Weight-Only Quantization (WOQ) reduces memory bandwidth consumption."
        ]
        with open(txt_path, "w", encoding="utf-8") as f:
            for i, p in enumerate(prompts * 50): # 300 test prompts
                f.write(f"PROMPT_{i:04d}: {p}\n")
        print(f"     [OK] Saved {txt_path} ({os.path.getsize(txt_path) / 1024:.2f} KB)")
    else:
        print(f"     [EXISTS] {txt_path}")

    print("[SUCCESS] All offline synthetic benchmark datasets ready for pen drive deployment!")

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "03_BENCHMARK_DATASETS"
    generate_datasets(out)
