import os, csv, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from pathlib import Path

# ==============================================================================
# 1. DEFINE IN-CLASS CHECKPOINT 25 MCQS (Modules 1 - 7)
# ==============================================================================
inclass_data = [
    # Module 1: Intro to HPC (3 Qs)
    {
        "sl": 1,
        "module": "Module 1: Introduction to HPC & Scientific Parallelism",
        "category": "Foundational", "difficulty": "Easy", "topic": "Memory Wall & HPC Constraint",
        "q": "Why do large AI models (e.g., 70-Billion parameter LLMs) fail to train efficiently on high-end consumer laptops despite having fast CPUs?",
        "options": {"a": "Laptops lack sufficient DDR memory channels and bandwidth (choked by the Memory Wall)", "b": "Laptops do not support floating-point arithmetic", "c": "Windows OS permanently limits memory allocation to 4 GB", "d": "Laptop CPUs cannot execute C++ code"},
        "ans": "a", "exp": "Consumer laptops typically have 2 memory channels providing 50-80 GB/s bandwidth, creating a massive Memory Wall bottleneck. Dual-socket enterprise HPC nodes provide 16 DDR5 channels delivering over 600 GB/s bandwidth."
    },
    {
        "sl": 2,
        "module": "Module 1: Introduction to HPC & Scientific Parallelism",
        "category": "Conceptual", "difficulty": "Medium", "topic": "Flynn's Taxonomy",
        "q": "Under Flynn's classical computer architecture taxonomy, which architectural model best describes modern GPUs and CPU vector execution units (AVX-512)?",
        "options": {"a": "SISD (Single Instruction, Single Data)", "b": "SIMD (Single Instruction, Multiple Data)", "c": "MISD (Multiple Instruction, Single Data)", "d": "MIMD (Multiple Instruction, Multiple Data)"},
        "ans": "b", "exp": "SIMD describes hardware where a single machine instruction controls multiple execution units simultaneously processing a vector of distinct data points (e.g., eight 64-bit doubles in a single AVX-512 clock cycle)."
    },
    {
        "sl": 3,
        "module": "Module 1: Introduction to HPC & Scientific Parallelism",
        "category": "Numerical", "difficulty": "Medium", "topic": "Amdahl's Law Speedup Limit",
        "q": "An HPC simulation contains a sequential fraction of 10% that cannot be parallelized. According to Amdahl's Law, what is the theoretical maximum speedup limit, even with an infinite number of processor cores?",
        "options": {"a": "100x speedup", "b": "10x speedup", "c": "50x speedup", "d": "Infinite speedup"},
        "ans": "b", "exp": "By Amdahl's Law: Speedup_max = 1 / (1 - P) = 1 / S. Here sequential fraction S = 0.10, so Speedup_max = 1 / 0.10 = 10x maximum speedup regardless of core count."
    },

    # Module 2: Intel HPC Hardware & Accelerators (4 Qs)
    {
        "sl": 4,
        "module": "Module 2: Intel HPC Architecture & Hardware Accelerators",
        "category": "Technical", "difficulty": "Medium", "topic": "Intel Xeon Role in Heterogeneous Clusters",
        "q": "In an enterprise heterogeneous supercomputing cluster, what is the primary architectural responsibility of Intel Xeon Scalable processors?",
        "options": {"a": "High-latency batch graphics rendering only", "b": "Orchestrating workflows, managing OS scheduling, preprocessing tensors, and handling irregular sequential logic", "c": "Replacing all network switches in the datacenter", "d": "Acting exclusively as passive memory controllers"},
        "ans": "b", "exp": "Intel Xeon CPUs excel at low-latency sequential execution, kernel memory management, I/O dispatch, and data orchestration, feeding structured tensor batches to parallel accelerators."
    },
    {
        "sl": 5,
        "module": "Module 2: Intel HPC Architecture & Hardware Accelerators",
        "category": "Technical", "difficulty": "Medium", "topic": "Intel AMX Hardware Function",
        "q": "What specific hardware capability is introduced on 4th Gen Intel Xeon Scalable processors (Sapphire Rapids) via Intel AMX (Advanced Matrix Extensions)?",
        "options": {"a": "Integrated liquid nitrogen cooling controllers", "b": "Dedicated 2D tile registers (TMM0-TMM7) and matrix multiplication units (TMUL) accelerating deep learning on the CPU die", "c": "Hardware emulation of 8-bit retro video game graphics", "d": "Direct connection to SATA-1 mechanical hard drives"},
        "ans": "b", "exp": "Intel AMX integrates eight 1KB 2D tile registers (8 KB total) and Tile Matrix Multiply (TMUL) accelerators, performing up to 2048 INT8 operations per cycle per core directly on the CPU."
    },
    {
        "sl": 6,
        "module": "Module 2: Intel HPC Architecture & Hardware Accelerators",
        "category": "Technical", "difficulty": "Medium", "topic": "Intel Data Center GPU Max Architecture",
        "q": "Which computational workload is the Intel Data Center GPU Max Series (formerly code-named Ponte Vecchio) primarily architected to accelerate?",
        "options": {"a": "Massive parallel floating-point vector/matrix simulations and high-density FP64/FP32 scientific computing", "b": "Single-threaded shell script execution", "c": "Low-speed serial ASCII text parsing", "d": "Managing Linux user account passwords"},
        "ans": "a", "exp": "Intel Data Center GPU Max Series features up to 128 Xe cores with integrated high-bandwidth memory (HBM2e) providing massive throughput for parallel FP64, FP32, and matrix workloads."
    },
    {
        "sl": 7,
        "module": "Module 2: Intel HPC Architecture & Hardware Accelerators",
        "category": "Technical", "difficulty": "Hard", "topic": "Habana Gaudi 2 Interconnect Fabric",
        "q": "How does the Habana Gaudi 2 AI accelerator achieve scale-out multi-node cluster training without requiring external discrete InfiniBand PCIe host channel adapters (HCAs)?",
        "options": {"a": "By transmitting data across standard USB 2.0 cables", "b": "By integrating 24x 100GbE RoCE (RDMA over Converged Ethernet) ports directly onto each Gaudi silicon die", "c": "By compressing all neural weights into local CPU L1 cache", "d": "By running software emulated WiFi bridges"},
        "ans": "b", "exp": "Gaudi 2 integrates twenty-four 100 Gigabit Ethernet RoCE RDMA interfaces directly on the processor die, providing 2.4 Tbps (300 GB/s) bi-directional network fabric throughput natively."
    },

    # Module 3: Linux OS Architecture & Filesystem (4 Qs)
    {
        "sl": 8,
        "module": "Module 3: Linux OS Architecture & Filesystem Internals",
        "category": "Foundational", "difficulty": "Easy", "topic": "UNIX File System Philosophy",
        "q": "Which fundamental design philosophy of the Linux operating system enables hardware devices, running processes, and network sockets to be manipulated using standard file commands (cat, read, write)?",
        "options": {"a": "Everything is an executable script", "b": "Everything is a file (Virtual File System abstraction)", "c": "Everything is a Windows registry entry", "d": "Everything is a shared cloud database"},
        "ans": "b", "exp": "In UNIX/Linux, 'everything is a file' allows the VFS to represent hardware devices (/dev), kernel status tables (/proc), and system properties (/sys) as accessible file streams."
    },
    {
        "sl": 9,
        "module": "Module 3: Linux OS Architecture & Filesystem Internals",
        "category": "Technical", "difficulty": "Medium", "topic": "Octal Permission Bitmask",
        "q": "An HPC cluster administrator runs 'chmod 750 run_simulation.sh'. What exact permissions are granted to Owner, Group, and Others?",
        "options": {"a": "Owner: rwx, Group: r-x, Others: ---", "b": "Owner: rw-, Group: r--, Others: r--", "c": "Owner: rwx, Group: rwx, Others: rwx", "d": "Owner: r-x, Group: ---, Others: ---"},
        "ans": "a", "exp": "In octal: 7 = 4+2+1 (read, write, execute for Owner); 5 = 4+0+1 (read, execute for Group); 0 = no permissions for Others (secure cluster practice)."
    },
    {
        "sl": 10,
        "module": "Module 3: Linux OS Architecture & Filesystem Internals",
        "category": "Numerical", "difficulty": "Medium", "topic": "Dual umask Calculation",
        "q": "If an HPC user's shell profile sets 'umask 027', what default octal permissions will be assigned to newly created directories and text files respectively?",
        "options": {"a": "Directory: 750 (rwxr-x---), File: 640 (rw-r-----)", "b": "Directory: 777 (rwxrwxrwx), File: 666 (rw-rw-rw-)", "c": "Directory: 755 (rwxr-xr-x), File: 644 (rw-r--r--)", "d": "Directory: 700 (rwx------), File: 600 (rw-------)"},
        "ans": "a", "exp": "Base directory mode is 777; subtracting 027 yields 750 (rwxr-x---). Base file mode is 666; subtracting 027 (and stripping execute) yields 640 (rw-r-----)."
    },
    {
        "sl": 11,
        "module": "Module 3: Linux OS Architecture & Filesystem Internals",
        "category": "Foundational", "difficulty": "Easy", "topic": "Path Navigation",
        "q": "In Linux cluster navigation, what does the command 'cd ../../data' instruct the shell to do?",
        "options": {"a": "Search for the word 'data' across all files in the system", "b": "Move up two directory levels from the current location, then enter the 'data' directory", "c": "Delete two parent folders and format the disk", "d": "Open a graphical file manager window"},
        "ans": "b", "exp": "In relative path syntax, '..' refers to the parent directory. Doing '../../' navigates two levels up the directory tree before descending into 'data'."
    },

    # Module 4: Shell Scripting & Automation (4 Qs)
    {
        "sl": 12,
        "module": "Module 4: Linux Shell Scripting & HPC Workflows",
        "category": "Technical", "difficulty": "Easy", "topic": "Shebang Portability",
        "q": "Why is '#!/usr/bin/env bash' widely considered a best practice over hardcoded '#!/bin/bash' on enterprise HPC clusters?",
        "options": {"a": "It compiles the bash script into machine code before running", "b": "It dynamically searches the user's $PATH to locate the bash binary across diverse Linux distributions", "c": "It forces bash to run with superuser (root) privileges", "d": "It automatically translates bash code into Python"},
        "ans": "b", "exp": "On heterogeneous clusters and custom operating environments, bash may be located in /bin, /usr/bin, or a custom environment module; 'env' dynamically resolves the active interpreter."
    },
    {
        "sl": 13,
        "module": "Module 4: Linux Shell Scripting & HPC Workflows",
        "category": "Technical", "difficulty": "Medium", "topic": "Defensive Bash set Flags",
        "q": "What is the critical defensive engineering purpose of placing 'set -euo pipefail' at the beginning of an automated cluster orchestration script?",
        "options": {"a": "It increases CPU clock frequency by 15%", "b": "It causes the script to abort immediately if any command errors (-e), any unset variable is used (-u), or any pipe step fails (pipefail)", "c": "It ignores all syntax errors and suppresses terminal logging", "d": "It encrypts the script using AES-256"},
        "ans": "b", "exp": "In batch supercomputing workflows, silent failures cause corrupted data or wasted cluster node-hours. 'set -euo pipefail' guarantees fail-fast deterministic execution."
    },
    {
        "sl": 14,
        "module": "Module 4: Linux Shell Scripting & HPC Workflows",
        "category": "Technical", "difficulty": "Easy", "topic": "Bash Variable Assignment Syntax",
        "q": "Why will the shell command 'BATCH_SIZE = 64' produce a 'command not found' error in Bash?",
        "options": {"a": "Bash does not support numbers larger than 32", "b": "Bash treats spaces around '=' as argument delimiters, interpreting 'BATCH_SIZE' as a command name", "c": "Variable names in bash must start with a dollar sign ($)", "d": "Variables can only be declared inside compiled C++ code"},
        "ans": "b", "exp": "In Bash, assignment syntax must have zero spaces around the '=' operator: 'BATCH_SIZE=64'. Spaces cause Bash to parse 'BATCH_SIZE' as an executable command."
    },
    {
        "sl": 15,
        "module": "Module 4: Linux Shell Scripting & HPC Workflows",
        "category": "Technical", "difficulty": "Medium", "topic": "Standard Stream Redirection",
        "q": "In the command './hpc_node_audit.sh > audit.log 2>&1', what is the exact effect of '2>&1'?",
        "options": {"a": "It multiplies the output volume by 2", "b": "It redirects standard error (file descriptor 2) to the same destination as standard output (file descriptor 1)", "c": "It runs the script twice on core 1", "d": "It delays script execution by 2 seconds"},
        "ans": "b", "exp": "File descriptor 1 is stdout and 2 is stderr. '2>&1' merges the stderr stream into stdout, ensuring that both normal logs and runtime error messages are written into 'audit.log'."
    },

    # Module 5: Secured Shell (SSH) (3 Qs)
    {
        "sl": 16,
        "module": "Module 5: Secure Remote Access & Cluster Environments",
        "category": "Technical", "difficulty": "Medium", "topic": "SSH Cryptographic Algorithms",
        "q": "When generating cluster access credentials via 'ssh-keygen -t ed25519', why is the Ed25519 algorithm preferred over standard RSA 2048/4096?",
        "options": {"a": "Ed25519 uses shorter 256-bit elliptic-curve keys, achieves faster handshakes, and provides superior resistance to side-channel attacks", "b": "RSA is incompatible with Linux operating systems", "c": "Ed25519 does not require a private key", "d": "Ed25519 allows passwords to be transmitted in plain text"},
        "ans": "a", "exp": "Ed25519 uses the Edwards-curve Digital Signature Algorithm (EdDSA) over Curve25519. It offers equivalent security to 3072-bit RSA with only 256-bit key length and faster execution."
    },
    {
        "sl": 17,
        "module": "Module 5: Secure Remote Access & Cluster Environments",
        "category": "Technical", "difficulty": "Easy", "topic": "SSH Remote Key Storage",
        "q": "To enable passwordless automated job submission from a local machine to a remote cluster node, into which remote file must your client's public key (~/.ssh/id_ed25519.pub) be appended?",
        "options": {"a": "/etc/passwd", "b": "~/.ssh/authorized_keys", "c": "~/.ssh/known_hosts", "d": "/tmp/public_keys.txt"},
        "ans": "b", "exp": "The SSH server inspects ~/.ssh/authorized_keys on the remote host to match incoming signature challenges against authorized client public keys."
    },
    {
        "sl": 18,
        "module": "Module 5: Secure Remote Access & Cluster Environments",
        "category": "Technical", "difficulty": "Medium", "topic": "SSH Private Key Permissions",
        "q": "A student attempts to connect to an HPC node and receives: 'Permissions 0644 for id_ed25519 are too open. It is required that your private key files are NOT accessible by others.' What command resolves this?",
        "options": {"a": "chmod 777 ~/.ssh/id_ed25519", "b": "chmod 600 ~/.ssh/id_ed25519", "c": "rm -rf ~/.ssh", "d": "chmod 000 ~/.ssh/id_ed25519"},
        "ans": "b", "exp": "SSH enforces strict security: private keys must be accessible only by the owner (read/write = 600). Group and others must have 0 access, or the SSH client refuses to use the key."
    },

    # Module 6: Intel oneAPI Ecosystem (4 Qs)
    {
        "sl": 19,
        "module": "Module 6: Intel oneAPI Ecosystem & oneAPI HPC Toolkit",
        "category": "Conceptual", "difficulty": "Easy", "topic": "oneAPI Unified Architecture Purpose",
        "q": "What is the primary industry objective of the Intel oneAPI software ecosystem?",
        "options": {"a": "To replace the Linux kernel with a custom proprietary operating system", "b": "To provide an open, standards-based unified programming model across heterogeneous architectures (CPUs, GPUs, FPGAs) without vendor lock-in", "c": "To convert Python scripts directly into hardware circuits", "d": "To eliminate the need for computer RAM"},
        "ans": "b", "exp": "oneAPI provides cross-architecture developer freedom through the open Khronos SYCL standard, enabling a single codebase to compile across diverse compute targets."
    },
    {
        "sl": 20,
        "module": "Module 6: Intel oneAPI Ecosystem & oneAPI HPC Toolkit",
        "category": "Technical", "difficulty": "Medium", "topic": "SYCL Language Standard",
        "q": "What is SYCL (pronounced 'sickle') in the context of high performance computing with Intel oneAPI?",
        "options": {"a": "A high-level Khronos standard C++ programming model for single-source heterogeneous programming", "b": "A relational database query engine", "c": "An alternative to the Linux Bash shell", "d": "A network cabling standard for InfiniBand"},
        "ans": "a", "exp": "SYCL is a modern C++ template library standard defined by the Khronos Group, allowing developers to write both host orchestration code and accelerator device kernels in standard C++."
    },
    {
        "sl": 21,
        "module": "Module 6: Intel oneAPI Ecosystem & oneAPI HPC Toolkit",
        "category": "Technical", "difficulty": "Medium", "topic": "Unified Shared Memory (USM)",
        "q": "In SYCL/DPC++, what is the principal architectural advantage of allocating memory via 'sycl::malloc_shared' (Unified Shared Memory)?",
        "options": {"a": "It doubles the available storage capacity of hard disks", "b": "It provides a single virtual pointer accessible by both CPU (Host) and GPU/Accelerator (Device) with automatic page migration", "c": "It permanently disables CPU cache coherence", "d": "It translates floating point numbers into integers"},
        "ans": "b", "exp": "USM shared allocations provide a pointer valid on both host and device; the SYCL runtime and OS driver automatically handle page fault migration between system RAM and device memory."
    },
    {
        "sl": 22,
        "module": "Module 6: Intel oneAPI Ecosystem & oneAPI HPC Toolkit",
        "category": "Technical", "difficulty": "Easy", "topic": "oneAPI Environment Sourcing",
        "q": "Which shell command initializes the Intel oneAPI development environment, populating $PATH, $LD_LIBRARY_PATH, and compiler binaries (icpx, ifx)?",
        "options": {"a": "source /opt/intel/oneapi/setvars.sh", "b": "python3 /opt/intel/install.py", "c": "systemctl restart oneapi", "d": "apt install oneapi-now"},
        "ans": "a", "exp": "Executing 'source /opt/intel/oneapi/setvars.sh' (or 'oneapi-vars.sh') dynamically updates environment paths to make oneAPI compilers and libraries accessible in the active terminal session."
    },

    # Module 7: Intel HPC Toolkit & Diagnostics (3 Qs)
    {
        "sl": 23,
        "module": "Module 7: Hands-on Lab Environment & Diagnostics",
        "category": "Foundational", "difficulty": "Easy", "topic": "Base Toolkit vs HPC Toolkit",
        "q": "What is the defining distinction between the Intel oneAPI Base Toolkit and the Intel HPC Toolkit?",
        "options": {"a": "Base Toolkit is for single-node development (SYCL, MKL, DAL); HPC Toolkit adds multi-node cluster tools (Intel MPI, Fortran ifx, Inspector, ITAC)", "b": "Base Toolkit is paid commercial software; HPC Toolkit is open-source", "c": "Base Toolkit is for Python; HPC Toolkit is for Java", "d": "There is no difference; they are exact duplicates"},
        "ans": "a", "exp": "The Base Toolkit provides foundational single-node compilers and domain libraries. The HPC Toolkit layers on cluster-scale supercomputing components: Intel MPI, Classic/LLVM Compilers, and debuggers."
    },
    {
        "sl": 24,
        "module": "Module 7: Hands-on Lab Environment & Diagnostics",
        "category": "Technical", "difficulty": "Easy", "topic": "Hardware Introspection CLI",
        "q": "Which Linux terminal utility provides immediate introspection of CPU architecture, hardware thread count, cache hierarchy (L1/L2/L3), and NUMA topology?",
        "options": {"a": "lscpu", "b": "ping", "c": "chmod", "d": "grep"},
        "ans": "a", "exp": "'lscpu' parses sysfs and /proc/cpuinfo to display processor architecture, socket count, threads per core, NUMA nodes, and vector instruction flags."
    },
    {
        "sl": 25,
        "module": "Module 7: Hands-on Lab Environment & Diagnostics",
        "category": "Technical", "difficulty": "Medium", "topic": "Intel Compiler Host Optimization Flag",
        "q": "When compiling an HPC benchmark with the Intel oneAPI C++ Compiler (icpx), which optimization flag instructs the compiler to generate instructions matching the host processor's highest SIMD capability (e.g., AVX-512)?",
        "options": {"a": "-xHost", "b": "-O0", "c": "-w", "d": "-g"},
        "ans": "a", "exp": "The '-xHost' flag tells the Intel compiler to interrogate the compilation machine's microarchitecture and enable all supported SIMD vector extensions (AVX-512, AMX, AVX2) for maximum throughput."
    }
]

print(f"Total In-Class Questions: {len(inclass_data)}")

# Output directories
base_dir = Path("HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/quizzes_and_assessments")
inclass_dir = base_dir / "in_class_assessment"
inclass_excel_dir = inclass_dir / "excel"
inclass_excel_dir.mkdir(parents=True, exist_ok=True)

# Generate Excel and CSV for In-Class Checkpoint
xlsx_path = inclass_excel_dir / "GLA_University_Day_01_In_Class_Checkpoint_25_MCQs.xlsx"
csv_path = inclass_excel_dir / "GLA_University_Day_01_In_Class_Checkpoint_25_MCQs.csv"
md_official_path = inclass_dir / "GLA_UNIVERSITY_DAY_01_IN_CLASS_CHECKPOINT_MCQS_OFFICIAL.md"
md_student_path = inclass_dir / "GLA_UNIVERSITY_DAY_01_IN_CLASS_CHECKPOINT_STUDENT_PAPER.md"
readme_path = inclass_dir / "README.md"

wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = "Day 1 In-Class Checkpoint"
ws1.views.sheetView[0].showGridLines = True

headers_sreeja = ["Sl no", "Questions", "Option a", "Option b", "Option c", "Option d", "Answer ( only mention option a,b,c,d)"]
ws1.append(headers_sreeja)

header_fill = PatternFill(start_color="003366", end_color="003366", fill_type="solid")
header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
thin_border = Border(left=Side(style='thin', color='D3D3D3'), right=Side(style='thin', color='D3D3D3'), top=Side(style='thin', color='D3D3D3'), bottom=Side(style='thin', color='D3D3D3'))

for col_num in range(1, len(headers_sreeja) + 1):
    cell = ws1.cell(row=1, column=col_num)
    cell.fill = header_fill
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

csv_rows = [headers_sreeja]
for idx, q in enumerate(inclass_data, start=1):
    row_data = [idx, q["q"], q["options"]["a"], q["options"]["b"], q["options"]["c"], q["options"]["d"], q["ans"]]
    ws1.append(row_data)
    csv_rows.append(row_data)

ws2 = wb.create_sheet(title="Evaluation Key & Explanations")
ws2.views.sheetView[0].showGridLines = True
headers_eval = ["Sl no", "Module", "Topic", "Category", "Difficulty", "Question", "Correct Answer", "Full Answer Text", "Technical Explanation"]
ws2.append(headers_eval)
for col_num in range(1, len(headers_eval) + 1):
    cell = ws2.cell(row=1, column=col_num)
    cell.fill = PatternFill(start_color="004080", end_color="004080", fill_type="solid")
    cell.font = header_font
    cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

for idx, q in enumerate(inclass_data, start=1):
    eval_row = [idx, q["module"], q["topic"], q["category"], q["difficulty"], q["q"], q["ans"], q["options"][q["ans"]], q["exp"]]
    ws2.append(eval_row)

ws1.column_dimensions['A'].width = 8
ws1.column_dimensions['B'].width = 50
ws1.column_dimensions['C'].width = 35
ws1.column_dimensions['D'].width = 35
ws1.column_dimensions['E'].width = 35
ws1.column_dimensions['F'].width = 35
ws1.column_dimensions['G'].width = 15

wb.save(xlsx_path)
print(f"[+] Saved In-Class Excel: {xlsx_path}")

with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.writer(f)
    writer.writerows(csv_rows)
print(f"[+] Saved In-Class CSV: {csv_path}")

# Write Markdown Official
md_official_content = f"""# 🎯 GLA UNIVERSITY — DAY 1 IN-CLASS SOCRATIC CHECKPOINT MCQS (OFFICIAL INSTRUCTOR KEY)
## High Performance Computing & Heterogeneous AI Systems (`GLA-HPC-BCSG701`)
**Lead Trainer:** Shivam Gupta | **Target Session:** Day 1 Lectures & Labs (Interactive In-Class Checkpoints)  
**Total Questions:** 25 Multi-Choice Questions | **Modules Covered:** 1 through 7  

---

## 📌 Pedagogical Delivery Strategy (Socratic In-Class Checkpointing)
Do NOT administer these 25 questions as a single sit-down exam!
Instead, weave 3-4 questions into each module as you teach. When you finish explaining a concept (e.g., Amdahl's Law, `chmod 750`, or Intel AMX), project the corresponding question, give students 30 seconds to commit to an answer, and use the explanation to **connect the dots** to the next architectural concept!

---

"""
for q in inclass_data:
    md_official_content += f"""### Question {q['sl']:02d} [{q['module']} | {q['difficulty']} | {q['category']}]
**Topic:** {q['topic']}  
**Question:** {q['q']}

- **a)** {q['options']['a']}
- **b)** {q['options']['b']}
- **c)** {q['options']['c']}
- **d)** {q['options']['d']}

> [!TIP]
> **Correct Answer: [{q['ans']}]** — {q['options'][q['ans']]}  
> **Technical Explanation:** {q['exp']}

---

"""

with open(md_official_path, 'w', encoding='utf-8') as f:
    f.write(md_official_content)
print(f"[+] Saved In-Class Official MD: {md_official_path}")

# Write Markdown Student Paper
md_student_content = f"""# 📝 GLA UNIVERSITY // DAY 1 IN-CLASS CONCEPT CHECKPOINT (STUDENT QUESTION PAPER)
## High Performance Computing & Heterogeneous AI Systems (`GLA-HPC-BCSG701`)
**Date:** Day 1 Masterclass | **Duration:** Active Lecture Checkpoints | **Total Marks:** 25 Marks  

**Instructions for Students:**
1. Select the single best answer (a, b, c, or d) for each question as presented during the lecture.
2. Note your reasoning before the instructor reveals the architectural mechanism.

---

"""
for q in inclass_data:
    md_student_content += f"""#### Question {q['sl']:02d}: {q['q']}
- **a)** {q['options']['a']}
- **b)** {q['options']['b']}
- **c)** {q['options']['c']}
- **d)** {q['options']['d']}

---

"""

with open(md_student_path, 'w', encoding='utf-8') as f:
    f.write(md_student_content)
print(f"[+] Saved In-Class Student MD: {md_student_path}")

# Write In-Class README
readme_content = """# 🎯 DAY 1: IN-CLASS SOCRATIC CHECKPOINTS (25 MCQS)
## Active Real-Time Comprehension Verification During Lectures
**Course Code:** `GLA-HPC-BCSG701` | **Lead Trainer:** Shivam Gupta  
**Pedagogical Purpose:** Interactive Socratic checkpoint questions woven directly into the 6-hour training schedule.

---

## 📁 Artifacts Structure in `in_class_assessment/`

| File | Format | Target Audience & Purpose |
| :--- | :---: | :--- |
| [`excel/GLA_University_Day_01_In_Class_Checkpoint_25_MCQs.xlsx`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/quizzes_and_assessments/in_class_assessment/excel/GLA_University_Day_01_In_Class_Checkpoint_25_MCQs.xlsx) | Excel `.xlsx` | Official 7-column spreadsheet + Sheet 2 Instructor Evaluation Key. |
| [`excel/GLA_University_Day_01_In_Class_Checkpoint_25_MCQs.csv`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/quizzes_and_assessments/in_class_assessment/excel/GLA_University_Day_01_In_Class_Checkpoint_25_MCQs.csv) | CSV `.csv` | UTF-8-BOM synchronized flat file. |
| [`GLA_UNIVERSITY_DAY_01_IN_CLASS_CHECKPOINT_MCQS_OFFICIAL.md`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/quizzes_and_assessments/in_class_assessment/GLA_UNIVERSITY_DAY_01_IN_CLASS_CHECKPOINT_MCQS_OFFICIAL.md) | Markdown `.md` | Complete instructor guide with module tags, answers, and dot-connecting explanations. |
| [`GLA_UNIVERSITY_DAY_01_IN_CLASS_CHECKPOINT_STUDENT_PAPER.md`](file:///c:/Users/Rose/Videos/GLA%20Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/quizzes_and_assessments/in_class_assessment/GLA_UNIVERSITY_DAY_01_IN_CLASS_CHECKPOINT_STUDENT_PAPER.md) | Markdown `.md` | Clean student quiz paper. |

---

## ⏱️ Lecture Integration Timetable (When to Ask During Class)
* **09:30 - 10:30 (Module 1 & 2):** Questions 01 to 07 (HPC basics, Flynn, Amdahl's Law, Xeon, AMX, Gaudi 2)
* **10:30 - 12:00 (Module 3 & 4):** Questions 08 to 15 (Linux VFS, chmod 750, umask 027, shebang, set -euo pipefail)
* **01:00 - 02:15 (Module 5 & 6):** Questions 16 to 22 (SSH keypairs, Ed25519, authorized_keys, oneAPI, SYCL, USM)
* **02:15 - 03:30 (Module 7 Lab):** Questions 23 to 25 (HPC Toolkit vs Base, lscpu introspection, -xHost flag)
"""

with open(readme_path, 'w', encoding='utf-8') as f:
    f.write(readme_content)
print(f"[+] Saved In-Class README: {readme_path}")
print("[+] In-Class Checkpoint Assessment generated 100% successfully!")
