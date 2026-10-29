import re

cheatsheet_path = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\Day-01_HPC_Linux_Shell_oneAPI\03_DAY_01_STUDENT_CHEATSHEET_AND_MCQS.md"
with open(cheatsheet_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Keep everything up to Part 3
split_marker = "## 📝 PART 3: 50 Official Evaluated Pre-Assessment Questions"
if split_marker in content:
    pre_part3 = content.split(split_marker)[0]
else:
    # fallback
    pre_part3 = content[:content.find("## 📝 PART 3:")]

from generate_gla_day1_50_mcqs_excel import questions_data

part3_lines = [
    "## 📝 PART 3: 50 Official Evaluated Pre-Assessment Questions (With Answers & Explanations)\n",
    "> **Official 50-Question Diagnostic Bank for Day 1 Pre-Assessment (GLA University BCSG701)**  ",
    "> **Track:** Intel & NEC Supercomputing Alliance × Edulateral Foundation  ",
    "> **Gradation:** Easy (14) | Medium (21) | Hard (15) — Strictly structured across Day 1 Syllabus Modules 1 to 7.\n",
    "---\n"
]

current_mod = ""
for q in questions_data:
    if q["module"] != current_mod:
        current_mod = q["module"]
        part3_lines.append(f"### 🔷 {current_mod}\n")
    
    part3_lines.append(f"#### Q{q['sl_no']:02d}. [{q['difficulty']}] {q['question']}")
    part3_lines.append(f"- A) {q['options']['a']}")
    part3_lines.append(f"- B) {q['options']['b']}")
    part3_lines.append(f"- C) {q['options']['c']}")
    part3_lines.append(f"- D) {q['options']['d']}")
    part3_lines.append(f"**Answer: {q['answer'].upper()}** | *Explanation: {q['explanation']}*\n")

new_content = pre_part3 + "\n".join(part3_lines)

with open(cheatsheet_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Updated {cheatsheet_path} with 50 questions!")
