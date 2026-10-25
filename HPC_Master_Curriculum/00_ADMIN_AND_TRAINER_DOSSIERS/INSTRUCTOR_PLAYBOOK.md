# 🎙️ Shivam Gupta's Master Instructor Playbook
### The Definitive Guide to Delivering World-Class HPC Training @ GLA University
**Program**: GLA University Block Teaching | High Performance Computing (Intel & NEC Edition)  
**Dates**: November 16th – November 20th, 2026 (5 Full Days)  
**Lead Trainer**: Shivam Gupta (~Shivam 🌱SEED🐍) | **Co-Trainer / Counterpart**: Mr. Nikhil / Designated Co-Trainer  
**Institutional Partner**: GLA University Mathura | **Organizing Partner**: Edulateral Foundation  
**Key Contacts**:
- Pedina Sreeja, Program Operations Executive, Edulateral (Mob: +91 9861773390 | Email: sreeja@edulateral.com)
- Dilip Kumar, Senior Management, Edulateral (Email: dilip@edulateral.com)
- Rajat Garg, Academic & Operations Coordinator (Email: rajatgarg.iitr@gmail.com)

---

## 🏛️ Part 1: Operational & Legal Compliance Charter

### 1. Financial & Tax Terms
- **Gross Honorarium**: ₹18,000 INR for the 5-day block training commitment.
- **Disbursement Milestones**:
  - **Milestone 1**: 50% advance (₹9,000 INR gross) on Day 1 (Monday, Nov 16). Net after 10% TDS = **₹8,100 INR**.
  - **Milestone 2**: Remaining 50% (₹9,000 INR gross) within 15 working days post-completion. Net after 10% TDS = **₹8,100 INR**.
  - **Total Net Realized**: **₹16,200 INR**.
- **Taxation (Section 194J)**: 10% TDS deducted against PAN. PAN details must be submitted to Sreeja prior to Day 1 to avoid statutory 20% deduction under Section 206AA.

### 2. Intellectual Property & Media Protocol (Strict Clause)
- All slides, materials, code, photos, and recordings are the **exclusive Intellectual Property of Edulateral Foundation**.
- **Social Media Embargo**: Trainers are strictly prohibited from posting photos, videos, student snapshots, reels, or materials on personal social media (LinkedIn, Instagram, YouTube, X/Twitter, personal blogs) without prior written consent from Edulateral Foundation.
- All presentation slides and student handouts must carry the official **Edulateral Foundation banner and logo**.

### 3. Strict Anti-Competitor / No External Sites Rule
- **Mandate**: No external support like ChatGPT, GeeksforGeeks, or competitor platforms should be used or promoted during Block Teaching.
- **Strategy**: Flawless whiteboard derivations, self-contained student cheat sheets, and complete offline code running directly in Linux terminals. Zero dependency on web search.

---

## 🧠 Part 2: Classroom Psychology & Student Engagement

### 1. The 7th-Semester Student Mindset:
- 7th-semester B.Tech CSE students consider themselves senior engineers. They are skeptical of generic slide reading.
- Their urgent priorities:
  1. **Tier-1 Technical Placement Drives** (Systems architecture, low-latency coding, distributed systems interviews).
  2. **Final Year Capstone Projects** (Major projects deciding academic honors).
  3. **Industry Credibility** (Does this syllabus map to real enterprise cloud architectures?).

### 2. The Golden Rule of Credibility:
> **"Never read a slide. Draw the architecture on the whiteboard, open the Linux terminal, and let the code fail and succeed live in front of their eyes."**

---

## ⚡ Part 3: Minute-by-Minute Room Management Rules

1. **The 20-Minute Theory Cap**:
   - Never lecture on theoretical concepts for more than 20 consecutive minutes.
   - Every 20-minute conceptual block MUST be punctuated by a live terminal command, a hardware flag inspection, or a live benchmark showdown.
2. **The "Before vs After" Shock Value**:
   - Always run the unoptimized, stock code first (e.g. unpatched Scikit-learn KMeans taking 15 seconds).
   - Then apply the Intel oneAPI / oneDAL optimization live (`patch_sklearn()`) and watch the terminal complete in 0.5 seconds.
   - Point directly at the terminal execution time and state: *"This is the difference between an amateur developer and a High-Performance Systems Engineer."*
3. **Handling the "Oversmart" Student**:
   - If a student asks: *"Sir, isn't CUDA better than oneAPI? Why not just buy Nvidia H100s?"*
   - **Do NOT dismiss them.** Validate them: *"Brilliant question! You are thinking like an enterprise systems architect."*
   - Deliver the corporate answer: *"CUDA is proprietary vendor lock-in. If your company spends $10M on Nvidia hardware, you are trapped. Intel oneAPI is based on open standard SYCL—it compiles across Intel CPUs, GPUs, AMD chips, and FPGAs. Furthermore, 70% of enterprise servers already have Intel Xeon CPUs. Repurposing existing hardware saves companies millions."*
4. **Co-Trainer Synergy (Shivam + Nikhil)**:
   - **Lead Trainer (Shivam)**: Drives podium projector, master slides, whiteboard diagrams, live coding, and placement Q&A.
   - **Floor Support (Nikhil)**: Constantly roams aisles, fixing syntax typos, path issues, and SSH timeouts within 30 seconds so Shivam never pauses the lecture.
   - **Dual Redundancy**: In the event of an emergency, both trainers are 100% prepared to deliver all 40 hours solo.

---

## 🛠️ Part 4: Emergency Lab Fail-Safes & Offline Pen Drive Kit

- **If Campus Internet Drops**:
  - The master USB 3.2 pen drive is pre-loaded with `HPC_Master_Curriculum/OFFLINE_PENDRIVE_TOOLKIT/`.
  - Execute `bash setup_offline_lab.sh` to install all offline wheels, Miniconda environments, and synthetic datasets in 60 seconds with zero internet.
- **If a Student PC Has Restricted Permissions**:
  - Use local user virtual environments in `$HOME/hpc_env`.
- **Daily MCQ Evaluation**:
  - Administer the 25-question daily evaluative quiz from `EDULATERAL_OFFICIAL_MCQ_BANK/` at 04:15 PM daily.
  - Coordinate results with Pedina Sreeja and GLA faculty coordinators.
