import re
import json

with open('c:/Users/Rose/Videos/GLA Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/03_DAY_01_STUDENT_CHEATSHEET_AND_MCQS.md', 'r', encoding='utf-8') as f:
    text_cheatsheet = f.read()

with open('c:/Users/Rose/Videos/GLA Trainings/HPC_Master_Curriculum/EDULATERAL_OFFICIAL_MCQ_BANK/Day-01_HPC_Linux_Shell_oneAPI_MCQs.md', 'r', encoding='utf-8') as f:
    text_edulateral = f.read()

pattern_cs = re.compile(
    r'#### Q(\d+)\.\s*(.*?)\n'
    r'-\s*A\)\s*(.*?)\n'
    r'-\s*B\)\s*(.*?)\n'
    r'-\s*C\)\s*(.*?)\n'
    r'-\s*D\)\s*(.*?)\s*\n'
    r'\*\*Answer:\s*([A-D])\*\*\s*\|\s*\*Explanation:\s*(.*?)\*',
    re.DOTALL
)
matches_cs = pattern_cs.findall(text_cheatsheet)

pattern_edu = re.compile(
    r'### Question \d+:\s*(D1-Q\d+)\s*\n'
    r'\*\*(.*?)\*\*\s*\n\s*'
    r'-\s*\*\*\(A\)\*\*\s*(.*?)\n'
    r'-\s*\*\*\(B\)\*\*\s*(.*?)\n'
    r'-\s*\*\*\(C\)\*\*\s*(.*?)\n'
    r'-\s*\*\*\(D\)\*\*\s*(.*?)\s*\n\s*'
    r'>\s*\*\*Correct Answer\*\*:\s*\*\*\(?([A-D])\)?\*\*\s*\n'
    r'>\s*\*\*Technical Explanation\*\*:\s*(.*?)(?=\n---|### Question|\Z)',
    re.DOTALL
)
matches_edu = pattern_edu.findall(text_edulateral)

print(f"Loaded {len(matches_cs)} CS questions and {len(matches_edu)} EDU questions.")

# Standardize into a unified list of 50 questions
questions = []

# Questions 1 to 25: Foundational Concepts & Operational Linux
for num, q_text, opt_a, opt_b, opt_c, opt_d, ans, exp in matches_cs:
    questions.append({
        "id": f"D1-Q{int(num):02d}",
        "section": "Section A: Foundational Concepts & Operational Linux (Q01 - Q25)",
        "question": q_text.strip(),
        "options": {
            "A": opt_a.strip(),
            "B": opt_b.strip(),
            "C": opt_c.strip(),
            "D": opt_d.strip(),
        },
        "answer": ans.strip(),
        "explanation": exp.strip()
    })

# Questions 26 to 50: Advanced Supercomputer & Silicon Architecture
for idx, (code, q_text, opt_a, opt_b, opt_c, opt_d, ans, exp) in enumerate(matches_edu, 26):
    questions.append({
        "id": f"D1-Q{idx:02d}",
        "section": "Section B: Advanced Supercomputer & Silicon Architecture (Q26 - Q50)",
        "question": q_text.strip(),
        "options": {
            "A": opt_a.strip(),
            "B": opt_b.strip(),
            "C": opt_c.strip(),
            "D": opt_d.strip(),
        },
        "answer": ans.strip(),
        "explanation": exp.strip()
    })

print(f"Total unified questions: {len(questions)}")

# 1. Build the Official GLA 50-MCQ Pre-Assessment Document
md_output = []
md_output.append("# 🏢 GLA UNIVERSITY — OFFICIAL 50-MCQ PRE-ASSESSMENT BANK")
md_output.append("## High Performance Computing & Heterogeneous AI Systems (GLA-HPC-BCSG701)")
md_output.append("### Day 1 Workshop Entrance & Diagnostic Pre-Assessment")
md_output.append("**Course Code:** GLA-HPC-BCSG701 | **Track:** Intel & NEC Supercomputing Alliance × Edulateral Foundation")
md_output.append("**Target Audience:** 7th-Semester B.Tech Computer Science & IT Students (60 Students)")
md_output.append("**Lead Trainer:** Shivam Gupta | **Assessment Coordinator:** Pedina Sreeja (GLA University)")
md_output.append("**Total Questions:** Exactly 50 Multiple Choice Questions | **Duration:** 60 Minutes | **Evaluation:** +1 Mark for Correct, 0 for Unattempted")
md_output.append("**Official Reference:** `Intel & NEC - High Performance Computing.pdf` (Page 2)")
md_output.append("")
md_output.append("---")
md_output.append("")
md_output.append("## 📌 Structure of the 50-MCQ Pre-Assessment")
md_output.append("- **Section A (Questions 01 – 25):** Core HPC Principles, Intel Silicon Triad (Xeon/GPU/Gaudi), Linux VFS Navigation, Shell Automation & SSH Security.")
md_output.append("- **Section B (Questions 26 – 50):** Advanced Supercomputing Architecture, Dennard Scaling & Amdahl's Law, NUMA Topology, Cache Coherence, InfiniBand Fabric & Intel oneAPI/SYCL Compilers.")
md_output.append("")
md_output.append("---")
md_output.append("")

current_section = ""
for i, q in enumerate(questions, 1):
    if q["section"] != current_section:
        current_section = q["section"]
        md_output.append(f"## 🔷 {current_section}\n")
    
    md_output.append(f"### Question {i:02d} ({q['id']})")
    md_output.append(f"**{q['question']}**\n")
    md_output.append(f"- **(A)** {q['options']['A']}")
    md_output.append(f"- **(B)** {q['options']['B']}")
    md_output.append(f"- **(C)** {q['options']['C']}")
    md_output.append(f"- **(D)** {q['options']['D']}\n")
    md_output.append(f"> **Correct Answer**: **({q['answer']})**  ")
    md_output.append(f"> **Technical Explanation**: {q['explanation']}\n")
    md_output.append("---\n")

# Add Master Answer Key Table
md_output.append("## 📊 MASTER 50-QUESTION EVALUATION & ANSWER KEY GRID\n")
md_output.append("| Q# | Key | Question Topic | Q# | Key | Question Topic |")
md_output.append("|:---:|:---:|:---|:---:|:---:|:---|")

topic_summaries = [
    "HPC Definition & Fundamentals",
    "Memory Wall & LLM Laptop Bottlenecks",
    "Head / Login Node Role vs Compute Nodes",
    "Habana Gaudi On-Die RoCE Architecture",
    "Intel Xeon Sapphire Rapids AMX Acceleration",
    "Linux VFS Root Directory & Paths",
    "Linux `ls -la` Hidden Dotfiles & Permissions",
    "Linux `rm` Permanent Deletion Semantics",
    "Bash Variable Assignment Syntax",
    "Bash Script Shebang (`#!/bin/bash`)",
    "Linux `chmod +x` Script Execution Rights",
    "Shell Redirection (`>` vs `>>`)",
    "SSH Port 22 & Protocol Architecture",
    "Asymmetric SSH Keys (`ed25519` vs RSA)",
    "Remote Server `~/.ssh/authorized_keys`",
    "Intel oneAPI Cross-Architecture Vision",
    "Khronos SYCL Single-Source C++ Standard",
    "oneAPI Environment Sourcing (`setvars.sh`)",
    "Intel oneAPI DPC++/C++ Compiler (`icpx`)",
    "Intel oneMKL High-Performance Math Kernels",
    "Intel Inspector Memory/Thread Debugger",
    "Intel MPI Multi-Node Message Passing",
    "Shell Exit Status Check (`$?`)",
    "Linux Environment `$PATH` Resolution",
    "Curriculum Scope Boundary Discipline",
    "Dennard Scaling Breakdown & Power Wall",
    "Amdahl's Law Speedup Boundary Calculation",
    "Gustafson's Law Scaled Speedup Model",
    "Xeon Dual-Socket UPI Bus & Memory Channels",
    "AVX-512 Register Width & FLOPS Throughput",
    "Intel AMX Hardware Tile Registers (`tmm0-7`)",
    "NEC SX-Aurora TSUBASA Vector Engine",
    "NEC SX-Aurora HBM2 Memory Bandwidth",
    "Linux `/home` vs High-Throughput `/scratch`",
    "Defensive Shell Scripting (`set -euo pipefail`)",
    "Ed25519 Elliptic-Curve SSH Security",
    "SSH Multiplexing (`ControlMaster`)",
    "Lmod / Environment Modules Management",
    "oneAPI Base Toolkit vs HPC Toolkit",
    "Linux NUMA Architecture Inspection (`numactl`)",
    "NUMA Distance Matrix & Interconnect Latency",
    "Intel `icx -xHost` Architectural Vectorization",
    "Linux `/proc` Virtual Kernel Telemetry",
    "Hardware Core Topology Inspection (`lscpu -C`)",
    "Intel Level Zero Direct Hardware Driver API",
    "InfiniBand NDR 400Gb/s Interconnect Fabrics",
    "Supercomputer Fat-Tree Network Topology",
    "Hardware Thread Pinning (`numactl --membind`)",
    "Khronos SYCL Standard Governance",
    "SSH Security Permission Discipline (`700`/`600`)"
]

for row in range(25):
    q1_idx = row
    q2_idx = row + 25
    q1 = questions[q1_idx]
    q2 = questions[q2_idx]
    t1 = topic_summaries[q1_idx]
    t2 = topic_summaries[q2_idx]
    md_output.append(f"| **Q{q1_idx+1:02d}** | **{q1['answer']}** | {t1} | **Q{q2_idx+1:02d}** | **{q2['answer']}** | {t2} |")

md_content = "\n".join(md_output)

# Write to GLA_UNIVERSITY_DAY_01_50_MCQ_PRE_ASSESSMENT_OFFICIAL.md
dest_path = 'c:/Users/Rose/Videos/GLA Trainings/HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/GLA_UNIVERSITY_DAY_01_50_MCQ_PRE_ASSESSMENT_OFFICIAL.md'
with open(dest_path, 'w', encoding='utf-8') as f:
    f.write(md_content)
print(f"Wrote 50 MCQs to {dest_path}")

# Also write to EDULATERAL_OFFICIAL_MCQ_BANK/Day-01_HPC_Linux_Shell_oneAPI_MCQs.md
bank_path = 'c:/Users/Rose/Videos/GLA Trainings/HPC_Master_Curriculum/EDULATERAL_OFFICIAL_MCQ_BANK/Day-01_HPC_Linux_Shell_oneAPI_MCQs.md'
with open(bank_path, 'w', encoding='utf-8') as f:
    f.write(md_content)
print(f"Updated {bank_path}")

# Update official_mcq_evaluation_dataset.json
json_dataset_path = 'c:/Users/Rose/Videos/GLA Trainings/HPC_Master_Curriculum/EDULATERAL_OFFICIAL_MCQ_BANK/official_mcq_evaluation_dataset.json'
with open(json_dataset_path, 'r', encoding='utf-8') as f:
    json_data = json.load(f)

json_data['Day-01_HPC_Linux_Shell_oneAPI_MCQs.md'] = [
    {
        "id": q["id"],
        "question": q["question"],
        "options": [
            f"(A) {q['options']['A']}",
            f"(B) {q['options']['B']}",
            f"(C) {q['options']['C']}",
            f"(D) {q['options']['D']}"
        ],
        "answer": q["answer"],
        "explanation": q["explanation"]
    }
    for q in questions
]

with open(json_dataset_path, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2)
print(f"Updated {json_dataset_path} with 50 questions for Day 1!")
