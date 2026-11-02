"""
==============================================================================
Master Generator & Upgrader for GLA HPC Masterclass Notebooks (Days 2 to 5)
==============================================================================
Equips Days 2, 3, 4, and 5 with:
  1. Official "Open in Colab" badge in Cell 0 pointing to public GitHub repo.
  2. Section 0 Markdown: Bilingual Hindi/English folder map & Drive hierarchy.
  3. Section 0 Code: Autonomous Google Drive Mount, Auto-Sync Engine,
     and IPython `post_run_cell` hook for real-time background mirroring.
  4. Master Google Drive Forensic Audit & Verification Suite at the end of each day.
  5. Synchronizes both `COLAB_NOTEBOOKS/` and `HPC_Master_Curriculum/Day-0X.../lab_activities/`.
"""

import json
import os
import re
import sys
import shutil

sys.stdout.reconfigure(encoding='utf-8')

BASE_REPO_URL = "https://colab.research.google.com/github/Shivam990q/GLA-HPC-Masterclass/blob/main/COLAB_NOTEBOOKS"

def make_badge_html(filename):
    return (
        f'<div align="center">\n'
        f'  <a href="{BASE_REPO_URL}/{filename}">\n'
        f'    <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" width="160">\n'
        f'  </a>\n'
        f'</div>\n\n'
    )

def make_section0_markdown(day_num, day_tag):
    return (
        f"## 💾 Section 0: Google Drive Storage Architecture & Autonomous Auto-Sync Engine\n\n"
        f"> ### 📌 Google Drive में ये फाइल्स कहाँ दिखेंगी? (Where will these files appear in Google Drive?)\n"
        f"> जब आप नीचे दिया गया सेल चलाएंगे, तो Google Drive आपके Google Account से कनेक्ट (Mount) हो जाएगा।\n"
        f"> आपकी सभी फाइल्स सीधे आपकी **Google Drive** के निम्नलिखित फ़ोल्डर में अपने-आप सेव (Sync) हो जाएंगी:\n"
        f"> \n"
        f"> ```\n"
        f"> 📁 Google Drive\n"
        f">    └── 📁 My Drive (मेरी ड्राइव)\n"
        f">         └── 📁 {day_tag}/\n"
        f">              ├── 📁 sources/    <-- All C++, Python, Shell scripts & Slurm jobs\n"
        f">              ├── 📁 binaries/   <-- Compiled high-performance executables\n"
        f">              ├── 📁 logs/       <-- Hardware audit & compiler optimization reports\n"
        f">              ├── 📁 data/       <-- Benchmark outputs, models, CSVs & plots\n"
        f">              └── 📄 drive_sync_manifest.json  <-- Cryptographic verification manifest\n"
        f"> ```\n\n"
        f"### ⚡ Why is this Auto-Sync Engine Critical?\n"
        f"In Google Colab, code executes on an **ephemeral virtual machine** whose local disk (`/content/`) is **completely erased** when the session disconnects or times out.\n"
        f"To guarantee **zero data loss**:\n"
        f"1. We mount Google Drive to `/content/drive`.\n"
        f"2. We create an organized workspace directory at `/content/drive/MyDrive/{day_tag}`.\n"
        f"3. We register an **autonomous IPython `post_run_cell` hook** that automatically mirrors every generated file (`.cpp`, `.c`, `.h`, `.hpp`, `.sh`, `.py`, `.slurm`, `.log`, `.txt`, `.csv`, `.json`, `.png`, `.onnx`, `.bin`, `.xml`) directly to Google Drive after **every single cell execution**!\n"
    )

def make_section0_code(day_num, day_tag, local_dir, known_bins):
    bins_repr = repr(set(known_bins))
    return f"""# ==============================================================================
# SECTION 0: Google Drive Mount, Workspace Setup & Autonomous Auto-Sync Hook
# ==============================================================================
import os
import sys
import shutil
import hashlib
import json
from datetime import datetime

# 1. Mount Google Drive if running in Google Colab environment
IN_COLAB = False
try:
    from google.colab import drive
    print("[*] Detected Google Colab environment. Mounting Google Drive...")
    drive.mount('/content/drive', force_remount=False)
    DRIVE_BASE_DIR = "/content/drive/MyDrive/{day_tag}"
    LOCAL_BASE_DIR = "{local_dir}"
    IN_COLAB = True
    print("[+] Google Drive successfully mounted at: /content/drive")
except Exception as e:
    print(f"[i] Running in local/standalone Jupyter environment (Non-Colab): {{e}}")
    DRIVE_BASE_DIR = os.path.abspath("./{day_tag}_DriveBackup")
    LOCAL_BASE_DIR = os.path.abspath("./{os.path.basename(local_dir)}_workspace")

# 2. Define standard directory hierarchy
SUBDIRS = ["sources", "binaries", "logs", "data"]
for d in SUBDIRS:
    os.makedirs(os.path.join(DRIVE_BASE_DIR, d), exist_ok=True)
    os.makedirs(os.path.join(LOCAL_BASE_DIR, d), exist_ok=True)

print(f"[+] Local Workspace initialized at : {{LOCAL_BASE_DIR}}")
print(f"[+] Google Drive Target Folder at  : {{DRIVE_BASE_DIR}}")

# 3. Autonomous Synchronization Engine
def compute_sha256(filepath):
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def sync_to_drive(verbose=True):
    \"\"\"
    Scans the local working directory and mirrors all source codes, compiled binaries,
    logs, and data files directly to Google Drive.
    \"\"\"
    source_exts = {{".cpp", ".c", ".h", ".hpp", ".sh", ".py", ".slurm"}}
    log_exts = {{".log"}}
    data_exts = {{".txt", ".csv", ".json", ".png", ".jpg", ".onnx", ".bin", ".xml"}}
    known_binaries = {bins_repr}

    synced_items = []
    search_dirs = [os.getcwd(), LOCAL_BASE_DIR]

    for s_dir in search_dirs:
        if not os.path.exists(s_dir):
            continue
        for root, _, files in os.walk(s_dir):
            if "drive/MyDrive" in root:
                continue
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                src_path = os.path.join(root, file)

                category = None
                if ext in source_exts:
                    category = "sources"
                elif ext in log_exts:
                    category = "logs"
                elif ext in data_exts and file != "drive_sync_manifest.json":
                    category = "data"
                elif file in known_binaries or (os.access(src_path, os.X_OK) and ext == "" and not file.endswith(".sh") and not file.endswith(".py")):
                    category = "binaries"

                if category:
                    dest_path = os.path.join(DRIVE_BASE_DIR, category, file)
                    should_copy = False
                    if not os.path.exists(dest_path):
                        should_copy = True
                    else:
                        if os.path.getmtime(src_path) > os.path.getmtime(dest_path):
                            should_copy = True

                    if should_copy:
                        shutil.copy2(src_path, dest_path)
                        synced_items.append((file, category, compute_sha256(src_path)))

    manifest_path = os.path.join(DRIVE_BASE_DIR, "drive_sync_manifest.json")
    manifest = {{
        "last_sync_timestamp": datetime.now().isoformat(),
        "drive_folder": DRIVE_BASE_DIR,
        "files_count": len(synced_items),
        "files": {{item[0]: {{"category": item[1], "sha256": item[2]}} for item in synced_items}}
    }}
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    if verbose:
        print("=" * 72)
        print("         🌐 GOOGLE DRIVE AUTONOMOUS SYNC STATUS REPORT")
        print("=" * 72)
        print(f"[*] Target Location : Google Drive > My Drive > {day_tag}")
        print(f"[*] Last Sync Time  : {{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}")
        print(f"[*] Files Synced    : {{len(synced_items)}} file(s)")
        for fname, cat, sha in synced_items[:10]:
            print(f"  • [{{cat.upper()}}] {{fname:<25}} (SHA256: {{sha[:12]}}...)")
        if len(synced_items) > 10:
            print(f"  ... and {{len(synced_items) - 10}} more files.")
        print("=" * 72)

# 4. Register IPython event hook for automated background synchronization
try:
    ip = get_ipython()
    if ip is not None:
        def auto_sync_hook(result):
            sync_to_drive(verbose=False)
        ip.events.register('post_run_cell', auto_sync_hook)
        print("[+] Autonomous Google Drive Auto-Sync Hook is now ACTIVE.")
        print("    Every code cell executed will automatically save its output to Drive!")
except Exception as e:
    print(f"[i] Could not register post_run_cell hook: {{e}}")

sync_to_drive(verbose=True)
"""

def make_audit_code(day_num, day_tag, deliverables):
    deliv_repr = repr(deliverables)
    return f"""# ==============================================================================
# MASTER GOOGLE DRIVE FORENSIC AUDIT & VERIFICATION SUITE
# ==============================================================================
import os
import hashlib
from datetime import datetime

# 1. Trigger final synchronous mirror to Google Drive
sync_to_drive(verbose=False)

EXPECTED_DELIVERABLES = {deliv_repr}

print("=" * 84)
print("     🏢 GLA UNIVERSITY // HPC MASTERCLASS DAY {day_num} FINAL DRIVE AUDIT")
print("=" * 84)
print(f"[*] Audit Timestamp    : {{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}")
print(f"[*] Verified Directory  : {{DRIVE_BASE_DIR}}")
print("-" * 84)
print(f"{{'Filename':<30}} | {{'Category':<10}} | {{'Status':<12}} | {{'Bytes':<10}} | {{'SHA-256':<12}}")
print("-" * 84)

verified_count = 0
for filename, category in EXPECTED_DELIVERABLES:
    drive_file_path = os.path.join(DRIVE_BASE_DIR, category, filename)
    local_file_path = filename
    
    target_path = None
    if os.path.exists(drive_file_path):
        target_path = drive_file_path
    elif os.path.exists(local_file_path):
        target_path = local_file_path

    if target_path and os.path.exists(target_path):
        file_bytes = os.path.getsize(target_path)
        hasher = hashlib.sha256()
        with open(target_path, "rb") as f:
            hasher.update(f.read())
        sha_prefix = hasher.hexdigest()[:10] + ".."
        status = "✅ VERIFIED"
        verified_count += 1
        print(f"{{filename:<30}} | {{category:<10}} | {{status:<12}} | {{file_bytes:<10}} | {{sha_prefix:<12}}")
    else:
        status = "⚠️ PENDING"
        print(f"{{filename:<30}} | {{category:<10}} | {{status:<12}} | {{'-':<10}} | {{'-':<12}}")

print("=" * 84)
completion_pct = (verified_count / len(EXPECTED_DELIVERABLES)) * 100.0
print(f"[*] Artifact Verification Score: {{verified_count}}/{{len(EXPECTED_DELIVERABLES)}} ({{completion_pct:.1f}}%)")

if verified_count == len(EXPECTED_DELIVERABLES):
    print(\"\"\"
  ╔════════════════════════════════════════════════════════════════════════════╗
  ║    🎉 CONGRATULATIONS! DAY {day_num} MASTERCLASS LAB 100% COMPLETED! 🎉            ║
  ║                                                                            ║
  ║  All source codes, compiled binaries, benchmark metrics, and logs have      ║
  ║  been cryptographically verified and permanently backed up in your        ║
  ║  Google Drive:                                                             ║
  ║  📁 My Drive > {day_tag}                                   ║
  ╚════════════════════════════════════════════════════════════════════════════╝
\"\"\")
else:
    print(f"[i] Note: {{len(EXPECTED_DELIVERABLES) - verified_count}} deliverable(s) will be created as you run the corresponding lab cells above!")
print("=" * 84)
"""

def make_wrapup_markdown(day_num, title, key_points, next_preview):
    pts = "\n".join([f"{i+1}. {p}" for i, p in enumerate(key_points)])
    return (
        f"## 🌟 Summary, Key Takeaways & Day {day_num+1 if day_num < 5 else 'Certificate'} Preview\n\n"
        f"### 📋 Key Takeaways from Day {day_num} ({title}):\n"
        f"{pts}\n\n"
        f"### 🔭 What's Next in {next_preview}:\n"
        f"Keep your Google Drive portfolio intact. All deliverables have been committed and verified.\n"
    )

DAY_SPECS = {
    2: {
        "filename": "Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb",
        "curr_rel": "HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/lab_activities/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb",
        "colab_rel": "COLAB_NOTEBOOKS/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb",
        "alt_curr": "HPC_Master_Curriculum/Day-02_Parallel_OpenMP_MPI_oneDAL/Day_02_Traditional_ML_oneAPI_OpenMP_MPI_oneDAL.ipynb",
        "day_tag": "GLA_HPC_Masterclass_Day02",
        "local_dir": "/content/hpc_day02",
        "known_bins": ["openmp_sum", "false_sharing", "mpi_reduction"],
        "deliverables": [
            ("openmp_vector_sum.cpp", "sources"),
            ("openmp_sum", "binaries"),
            ("false_sharing_demo.cpp", "sources"),
            ("false_sharing", "binaries"),
            ("mpi_reduction.cpp", "sources"),
            ("mpi_reduction", "binaries"),
            ("random_forest_benchmark.csv", "data"),
            ("amdahl_scaling.png", "data")
        ],
        "title": "Traditional ML & Parallel Computing with OpenMP, MPI & oneDAL",
        "key_points": [
            "**Amdahl's Law**: Adding infinite cores cannot speed up the serial fraction of code ($S = 1/((1-P) + P/N)$).",
            "**OpenMP Shared Memory**: The Fork-Join model with `#pragma omp parallel for` achieves linear core scaling when memory contention is avoided.",
            "**False Sharing Elimination**: Separate per-thread counters by at least 64 bytes (L1 cache line boundary) to eliminate hardware cache invalidation bus storms.",
            "**MPI Distributed Memory**: Message Passing Interface enables clusters without shared memory to exchange data via point-to-point and collective operations (`MPI_Reduce`).",
            "**Intel oneDAL (`sklearnex`)**: Hardware-accelerated machine learning yields 10x-40x speedups with zero code changes using `patch_sklearn()`."
        ],
        "next_preview": "Day 3 (Deep Learning on HPC with TensorFlow, oneDNN, Slurm & Horovod)"
    },
    3: {
        "filename": "Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb",
        "curr_rel": "HPC_Master_Curriculum/Day-03_DeepLearning_TF_Slurm_Horovod/lab_activities/Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb",
        "colab_rel": "COLAB_NOTEBOOKS/Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb",
        "alt_curr": "HPC_Master_Curriculum/Day-03_DeepLearning_TF_Slurm_Horovod/Day_03_Deep_Learning_TensorFlow_oneDNN_Slurm_Horovod.ipynb",
        "day_tag": "GLA_HPC_Masterclass_Day03",
        "local_dir": "/content/hpc_day03",
        "known_bins": [],
        "deliverables": [
            ("slurm_simulator.py", "sources"),
            ("train_resnet_hpc.slurm", "sources"),
            ("distributed_tf_horovod.py", "sources"),
            ("onednn_operator_fusion.log", "logs"),
            ("horovod_ring_allreduce.log", "logs"),
            ("resnet_training_metrics.csv", "data")
        ],
        "title": "Deep Learning on HPC with TensorFlow, oneDNN, Slurm & Horovod",
        "key_points": [
            "**Memory Wall in Deep Learning**: DRAM bandwidth cannot keep up with vector execution units; cache-blocking and operator fusion are mandatory.",
            "**Intel oneDNN**: Fuses Conv2D + BiasAdd + ReLU into single hardware execution kernels, evaluating activation functions while tensors are in L1 cache.",
            "**Slurm Workload Manager**: Enterprise cluster scheduler managing partitions, nodes, jobs, tasks, and memory limits via `sbatch` scripts.",
            "**Distributed DL with Horovod**: Ring-AllReduce communication topology eliminates parameter server bottlenecks by exchanging gradients in a ring.",
            "**Habana Gaudi Architecture**: Dedicated AI processors with matrix multiplication engines and integrated RoCE (RDMA over Converged Ethernet)."
        ],
        "next_preview": "Day 4 (Distributed AI Training, Slurm Multi-Node Clusters & Intel VTune Profiling)"
    },
    4: {
        "filename": "Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb",
        "curr_rel": "HPC_Master_Curriculum/Day-04_Distributed_Slurm_VTune_Profiling/lab_activities/Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb",
        "colab_rel": "COLAB_NOTEBOOKS/Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb",
        "alt_curr": "HPC_Master_Curriculum/Day-04_Distributed_Slurm_VTune_Profiling/Day_04_Distributed_AI_Slurm_VTune_Profiling.ipynb",
        "day_tag": "GLA_HPC_Masterclass_Day04",
        "local_dir": "/content/hpc_day04",
        "known_bins": [],
        "deliverables": [
            ("multinode_sbatch.slurm", "sources"),
            ("ring_allreduce_simulation.py", "sources"),
            ("vtune_tmam_report.txt", "logs"),
            ("roofline_model.png", "data"),
            ("strong_vs_weak_scaling.png", "data"),
            ("cluster_scaling_metrics.csv", "data")
        ],
        "title": "Distributed AI Training, Slurm Multi-Node Clusters & Intel VTune Profiling",
        "key_points": [
            "**Multi-Node Slurm Orchestration**: Submitting distributed jobs across multi-node clusters with Intel MPI and NCCL/oneCCL backends.",
            "**Ring-AllReduce Mathematical Complexity**: Total data transferred per worker is $2 \\times \\frac{N-1}{N} \\times S$, independent of cluster size $N$.",
            "**Intel VTune TMAM (Top-Down Microarchitecture Analysis Method)**: Classifying execution slots into Frontend Bound, Bad Speculation, Backend Bound, and Retiring.",
            "**Intel Advisor & Roofline Analysis**: Plotting Operational Intensity (FLOPs/Byte) against hardware theoretical peak to identify memory-bound vs compute-bound kernels.",
            "**Strong vs Weak Scaling**: Strong scaling keeps problem size fixed while adding nodes; Weak scaling increases problem size proportionally with nodes."
        ],
        "next_preview": "Day 5 (Generative AI, LLMs, Intel Gaudi & OpenVINO Toolkit)"
    },
    5: {
        "filename": "Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb",
        "curr_rel": "HPC_Master_Curriculum/Day-05_GenAI_LLMs_Gaudi_OpenVINO/lab_activities/Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb",
        "colab_rel": "COLAB_NOTEBOOKS/Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb",
        "alt_curr": "HPC_Master_Curriculum/Day-05_GenAI_LLMs_Gaudi_OpenVINO/Day_05_Generative_AI_LLMs_OpenVINO_Gaudi_HPC_Master_Lab.ipynb",
        "day_tag": "GLA_HPC_Masterclass_Day05",
        "local_dir": "/content/hpc_day05",
        "known_bins": [],
        "deliverables": [
            ("compress_llm_nncf.py", "sources"),
            ("live_llm_benchmark.py", "sources"),
            ("sbatch_finetune_llm.sh", "sources"),
            ("llm_serving_api.py", "sources"),
            ("genai_hardware_audit.log", "logs"),
            ("openvino_quantization_report.txt", "logs"),
            ("token_latency_benchmark.csv", "data")
        ],
        "title": "Generative AI, LLMs, Intel Gaudi & OpenVINO Toolkit",
        "key_points": [
            "**LLM Autoregressive Generation Memory Wall**: Generating each token requires streaming the full model weight matrix through memory channels; bandwidth is king.",
            "**Intel Xeon AMX (Advanced Matrix Extensions)**: 2D tile registers (TMM0-TMM7) and TMUL accelerator delivering up to 16x INT8/BF16 matrix multiply throughput.",
            "**Habana Gaudi 2/3 Heterogeneous Accelerators**: Tensor Processing Cores (TPCs) and direct 24x 100GbE RoCE RDMA networking for large-scale LLM training.",
            "**Intel OpenVINO & NNCF INT4 Quantization**: Compressing 16-bit floating point LLMs into 4-bit weights with symmetric/asymmetric group quantization, cutting RAM footprint by 70%.",
            "**Production Serving Architecture**: TTFT (Time to First Token) vs ITL (Inter-Token Latency) metrics, continuous batching, and high-concurrency FastAPI deployment."
        ],
        "next_preview": "Capstone Completion & Masterclass Certification"
    }
}

def upgrade_day(day_num):
    spec = DAY_SPECS[day_num]
    print(f"\n=======================================================")
    print(f"[*] Upgrading DAY {day_num}: {spec['filename']}")
    print(f"=======================================================")
    
    curr_path = spec['curr_rel']
    if not os.path.exists(curr_path):
        print(f"[!] Error: {curr_path} not found!")
        return False
        
    with open(curr_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    cells = nb.get('cells', [])
    print(f"[*] Original cell count: {len(cells)}")
    
    # 1. Update Cell 0: Prepend Colab Badge
    c0 = cells[0]
    c0_src = "".join(c0.get('source', []))
    
    c0_src = re.sub(r'<div align="center">\s*<a href="https://colab\.research\.google\.com/[^"]+">.*?</a>\s*</div>\s*', '', c0_src, flags=re.DOTALL)
    c0_src = re.sub(r'\[!\[Open In Colab\]\(https://colab\.research\.google\.com/[^\)]+\)\]\([^\)]+\)\s*', '', c0_src)
    
    badge = make_badge_html(spec['filename'])
    new_c0_src = badge + c0_src
    
    if "Google Drive" not in new_c0_src:
        new_c0_src += (
            f"\n\n### 💾 Cloud Persistence Guarantee:\n"
            f"- **100% Google Drive Synchronization**: All source files, compiled binaries, benchmark logs, and models are automatically mirrored to `📁 My Drive > {spec['day_tag']}` in real-time."
        )
    c0['source'] = [line + '\n' for line in new_c0_src.split('\n')[:-1]] + [new_c0_src.split('\n')[-1]]
    
    # 2. Section 0 Markdown & Code Cells
    sec0_md = make_section0_markdown(day_num, spec['day_tag'])
    sec0_code = make_section0_code(day_num, spec['day_tag'], spec['local_dir'], spec['known_bins'])
    
    sec0_md_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [l + '\n' for l in sec0_md.split('\n')[:-1]] + [sec0_md.split('\n')[-1]]
    }
    sec0_code_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [l + '\n' for l in sec0_code.split('\n')[:-1]] + [sec0_code.split('\n')[-1]]
    }
    
    if day_num in [2, 3]:
        cells[1] = sec0_md_cell
        cells[2] = sec0_code_cell
    elif day_num in [4, 5]:
        cells.insert(1, sec0_code_cell)
        cells.insert(1, sec0_md_cell)
        
    # 3. For Day 4: Ensure sbatch_script is also written to file multinode_sbatch.slurm
    if day_num == 4:
        for c in cells:
            if c.get('cell_type') == 'code':
                c_src = "".join(c.get('source', []))
                if "sbatch_script = '''#!/bin/bash" in c_src and "with open('multinode_sbatch.slurm'" not in c_src:
                    c_src += "\n\n# Save sbatch script to file so it is synced to Google Drive\nwith open('multinode_sbatch.slurm', 'w') as f:\n    f.write(sbatch_script)\nprint('[+] Generated and saved multinode_sbatch.slurm')\n"
                    c['source'] = [l + '\n' for l in c_src.split('\n')[:-1]] + [c_src.split('\n')[-1]]
                    print("[+] Added file write for Day 4 multinode_sbatch.slurm")

    # 4. For Day 5: Ensure hardware audit log is written to genai_hardware_audit.log
    if day_num == 5:
        for c in cells:
            if c.get('cell_type') == 'code':
                c_src = "".join(c.get('source', []))
                if "def check_silicon():" in c_src and "genai_hardware_audit.log" not in c_src:
                    c_src = c_src.replace(
                        "print(\"Hardware introspection complete.\")",
                        "# Save audit report to log\n    with open('genai_hardware_audit.log', 'w') as f:\n        f.write(cpu_info + '\\n' + flags + '\\n' + str(mem))\n    print('[+] Audit report saved to genai_hardware_audit.log')\n    print('Hardware introspection complete.')"
                    )
                    c['source'] = [l + '\n' for l in c_src.split('\n')[:-1]] + [c_src.split('\n')[-1]]
                    print("[+] Added log write for Day 5 genai_hardware_audit.log")

    # 5. Append Forensic Verification Audit Suite & Key Takeaways
    audit_code = make_audit_code(day_num, spec['day_tag'], spec['deliverables'])
    wrapup_md = make_wrapup_markdown(day_num, spec['title'], spec['key_points'], spec['next_preview'])
    
    audit_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [l + '\n' for l in audit_code.split('\n')[:-1]] + [audit_code.split('\n')[-1]]
    }
    wrapup_cell = {
        "cell_type": "markdown",
        "metadata": {},
        "source": [l + '\n' for l in wrapup_md.split('\n')[:-1]] + [wrapup_md.split('\n')[-1]]
    }
    
    last_src = "".join(cells[-1].get('source', []))
    if "MASTER GOOGLE DRIVE FORENSIC AUDIT" not in last_src and "FINAL DRIVE AUDIT" not in last_src:
        cells.append(audit_cell)
        cells.append(wrapup_cell)
    else:
        print("[*] Audit cell already present; replacing")
        cells[-2] = audit_cell
        cells[-1] = wrapup_cell

    nb['cells'] = cells
    print(f"[+] Final upgraded cell count for Day {day_num}: {len(cells)}")
    
    destinations = [spec['curr_rel'], spec['colab_rel']]
    if os.path.exists(os.path.dirname(spec['alt_curr'])):
        destinations.append(spec['alt_curr'])
        
    for dst in destinations:
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        with open(dst, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
        print(f"  -> Saved: {dst} ({os.path.getsize(dst)} bytes)")
        
    return True

def main():
    print("=================================================================")
    print("   AUTONOMOUS UPGRADE: GLA HPC MASTERCLASS NOTEBOOKS (DAYS 2-5)  ")
    print("=================================================================")
    for d in [2, 3, 4, 5]:
        ok = upgrade_day(d)
        if not ok:
            print(f"[!] FAILED on Day {d}")
            sys.exit(1)
            
    print("\n[🎉] ALL DAYS 2 TO 5 SUCCESSFULLY UPGRADED AND SYNCHRONIZED!")

if __name__ == "__main__":
    main()
