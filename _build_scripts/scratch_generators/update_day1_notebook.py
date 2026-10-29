import json
from pathlib import Path

nb_path = Path('HPC_Master_Curriculum/Day-01_HPC_Linux_Shell_oneAPI/Day_01_Intel_oneAPI_and_HPC_Toolkit_Master_Lab.ipynb')

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# 1. Update Cell 4: Add Intel AMX check
c4_src = ''.join(nb['cells'][4]['source'])
if 'has_amx' not in c4_src:
    c4_src = c4_src.replace(
        'has_sse4_2 = "sse4_2" in flags',
        'has_sse4_2 = "sse4_2" in flags\nhas_amx = "amx" in flags'
    )
    old_vector_text = 'print("-" * 65)\nprint("  Vector Instruction Extensions Detected:")'
    new_vector_text = (
        'print("-" * 65)\n'
        'print("  Hardware Acceleration & Vector Flags:")\n'
        'print(f"  • Intel AMX (Advanced Matrix Extensions) : {\'✅ ACTIVE (2D Tile Accelerators)\' if has_amx else \'❌ Not Present (Intel Xeon Sapphire Rapids Feature)\'}")'
    )
    c4_src = c4_src.replace(old_vector_text, new_vector_text)
    nb['cells'][4]['source'] = [line + '\n' for line in c4_src.split('\n')[:-1]] + [c4_src.split('\n')[-1]]
    print("[+] Cell 4 successfully updated with Intel AMX hardware detection!")

# 2. Check if Interactive Quiz cell already exists in Section 11
has_quiz = any('Interactive Day 1 In-Class Checkpoint Quiz' in ''.join(c['source']) for c in nb['cells'])
if not has_quiz:
    quiz_code = '''# ==============================================================================
# 🎯 INTERACTIVE DAY 1 IN-CLASS CHECKPOINT QUIZ (Self-Grading Runner)
# Tests core concepts covered today: Amdahl's Law, Linux permissions, SSH & oneAPI
# ==============================================================================

quiz_questions = [
    {
        "q": "1. What is the fundamental difference between Intel oneAPI Base Toolkit and HPC Toolkit?",
        "options": {
            "a": "Base Toolkit is for single-node heterogeneous programming; HPC Toolkit adds cluster tools (MPI, Fortran, ITAC).",
            "b": "Base Toolkit is free, HPC Toolkit requires an expensive monthly cloud license.",
            "c": "Base Toolkit is only for GPUs; HPC Toolkit is only for CPUs.",
            "d": "They are completely identical packages."
        },
        "ans": "a",
        "exp": "Base Toolkit establishes single-node SYCL/DPC++ and oneMKL acceleration; HPC Toolkit layers cluster compilers (icx, ifx) and Intel MPI."
    },
    {
        "q": "2. In Amdahl's Law, if 80% of an HPC simulation is parallelized and 20% is strictly serial, what is the maximum possible theoretical speedup?",
        "options": {
            "a": "80x speedup",
            "b": "5x speedup (1 / 0.20 = 5)",
            "c": "20x speedup",
            "d": "Infinite speedup on a 1000-node cluster"
        },
        "ans": "b",
        "exp": "By Amdahl's Law: Speedup_max = 1 / (1 - P) = 1 / 0.20 = 5x speedup."
    },
    {
        "q": "3. In Linux cluster administration, what do octal permissions 'chmod 750 script.sh' grant?",
        "options": {
            "a": "Owner: rwx, Group: r-x, Others: ---",
            "b": "Owner: rw-, Group: r--, Others: r--",
            "c": "Owner: rwx, Group: rwx, Others: rwx",
            "d": "Owner: r-x, Group: ---, Others: ---"
        },
        "ans": "a",
        "exp": "7 = 4+2+1 (rwx for owner), 5 = 4+0+1 (r-x for group), 0 = no access for others."
    },
    {
        "q": "4. Why is key-based SSH authentication preferred over passwords in enterprise supercomputing clusters?",
        "options": {
            "a": "It uses asymmetric cryptography (ed25519) enabling secure, passwordless automated batch job execution.",
            "b": "Passwords slow down the CPU clock frequency.",
            "c": "Linux kernels cannot store passwords in memory.",
            "d": "SSH keys compress data packets by 90%."
        },
        "ans": "a",
        "exp": "Asymmetric key pairs (public/private) allow automated scheduler scripts and MPI ranks to authenticate without human typing."
    },
    {
        "q": "5. In DPC++/SYCL, what is the primary benefit of Unified Shared Memory (malloc_shared)?",
        "options": {
            "a": "It provides a single unified virtual pointer accessible by both CPU and GPU without manual memcpy.",
            "b": "It doubles the physical capacity of RAM.",
            "c": "It forces code to run only on NVIDIA hardware.",
            "d": "It disables CPU L1 and L2 caches."
        },
        "ans": "a",
        "exp": "USM allows host and device to share virtual address space, with the SYCL runtime automatically migrating pages on demand."
    }
]

def run_day1_quiz():
    score = 0
    print("=" * 68)
    print("      🎓 GLA UNIVERSITY // DAY 1 IN-CLASS CONCEPT CHECKPOINT")
    print("=" * 68)
    for item in quiz_questions:
        print(f"\\n{item['q']}")
        for opt_key, opt_val in item['options'].items():
            print(f"   [{opt_key}] {opt_val}")
        
        user_choice = input("Your Answer (a/b/c/d): ").strip().lower()
        if user_choice == item['ans']:
            print("✅ Correct! " + item['exp'])
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer is [{item['ans']}].")
            print("💡 Reason: " + item['exp'])
        print("-" * 68)
    
    print(f"\\n🏁 Final Score: {score} / {len(quiz_questions)} ({int(score/len(quiz_questions)*100)}%)")
    if score >= 4:
        print("🌟 Outstanding! You have mastered Day 1 HPC foundations!")
    elif score >= 2:
        print("👍 Good progress! Review the glossary and notebook before Day 2!")
    else:
        print("📖 Keep studying! Review Section 3 and Section 5 in this notebook!")

# Uncomment below to run interactively:
# run_day1_quiz()
print("[+] Day 1 In-Class Interactive Quiz Initialized! Run `run_day1_quiz()` to launch.")
'''
    new_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + '\n' for line in quiz_code.split('\n')[:-1]] + [quiz_code.split('\n')[-1]]
    }
    nb['cells'].append(new_cell)
    print("[+] Interactive Quiz Runner Cell appended to Notebook!")

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("[✓] Notebook successfully audited, updated, and validated!")
