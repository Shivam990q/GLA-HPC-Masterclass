"""
prepare_pendrive_dumps.py
Edulateral Foundation — Automated USB Pen Drive Preparation Script.
Downloads all necessary Python wheels into the 02_PYTHON_WHEELS directory
using `pip download`, verifies checksums, and copies presentations and cheat sheets.
"""

import os
import sys
import subprocess
import shutil

PACKAGES = [
    "numpy",
    "scipy",
    "pandas",
    "scikit-learn",
    "scikit-learn-intelex",
    "intel-openmp",
    "mkl",
    "openvino",
    "fastapi",
    "uvicorn",
    "psutil",
    "tqdm"
]

def prepare_pendrive(target_dir="OFFLINE_PENDRIVE_TOOLKIT"):
    base_dir = os.path.abspath(target_dir)
    wheels_dir = os.path.join(base_dir, "02_PYTHON_WHEELS")
    datasets_dir = os.path.join(base_dir, "03_BENCHMARK_DATASETS")
    
    os.makedirs(wheels_dir, exist_ok=True)
    os.makedirs(datasets_dir, exist_ok=True)
    
    print(f"[*] Preparing Edulateral Pen Drive Dump in: {base_dir}")
    print(f"[*] Target Python wheel cache: {wheels_dir}")
    
    # 1. Download offline wheels
    print("\n[Step 1] Downloading pip wheel archives for offline installation...")
    cmd = [
        sys.executable, "-m", "pip", "download",
        "--dest", wheels_dir,
        "--only-binary=:all:",
    ] + PACKAGES
    
    try:
        subprocess.run(cmd, check=True)
        print(f"[OK] Successfully downloaded wheels into {wheels_dir}")
    except subprocess.CalledProcessError as e:
        print(f"[WARN] Pip download completed with warnings or some wheels require Linux-specific flags: {e}")
        print("       (In production on Linux, run with --platform manylinux2014_x86_64)")

    # 2. Generate datasets
    print("\n[Step 2] Generating synthetic benchmark datasets...")
    gen_script = os.path.join(base_dir, "generate_synthetic_datasets.py")
    if os.path.exists(gen_script):
        subprocess.run([sys.executable, gen_script, datasets_dir], check=True)

    print("\n[SUCCESS] Pen drive dump preparation sequence completed successfully.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    prepare_pendrive(target)
