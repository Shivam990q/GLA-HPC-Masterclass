"""
build_institutional_intelligence.py
Phase 1: Generates exhaustive institutional, corporate, and personnel dossiers:
- 00_INSTITUTIONAL_AND_CORPORATE_INTELLIGENCE/
  - 01_GLA_University_Deep_Profile/
  - 02_Edulateral_Foundation_Intelligence/
  - 03_ManasAI_Technology_Deep_Dossier/
  - 04_Krishnayan_AI_Deep_Dossier/
  - 05_Key_Personnel_Profiles/
"""

import os

base_dir = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\00_INSTITUTIONAL_AND_CORPORATE_INTELLIGENCE"

def write_f(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")
    print(f"[OK] Wrote: {rel_path}")

# ==============================================================================
# 01 GLA UNIVERSITY DEEP PROFILE
# ==============================================================================

write_f("01_GLA_University_Deep_Profile/gla_university_institutional_profile.md", """# 🏛️ GLA University Mathura: Complete Institutional & Academic Dossier
**Target Institution**: GLA University, Mathura, Uttar Pradesh, India  
**Audience**: 7th Semester B.Tech Computer Science & Engineering (Senior Undergraduates)  
**Campus Location**: 17km Stone, NH-19 (Delhi-Mathura Highway), P.O. Chaumuhan, Mathura, UP – 281406  

---

## 1. History, Heritage & Governance Structure

### 1.1 Founding Vision & Leadership
* **Origins**: Founded in 1998 by **Shri Narayan Das Agrawal** in memory of his late father, **Shri Ganeshi Lal Agrawal (GLA)**. Established initially as GLA Institute of Technology and Management (GLAITM) and upgraded to a full State Private University by the UP State Legislature in 2010.
* **Chancellor**: **Shri Narayan Das Agrawal** — Industrialist and educationist; maintains strong ties with industry leaders across North India.
* **Vice-Chancellor**: **Prof. Phalguni Gupta** — World-renowned computer scientist, former Professor at **IIT Kanpur** for over three decades, former Director of NITTTR Kolkata. His presence means the university administration has deep respect for rigorous, first-principles computer science.
* **Dean, Academic Affairs & IET**: **Prof. Ashish Sharma** — Oversees undergraduate engineering pedagogy, academic timetables, and external training accreditations.
* **Department of Computer Engineering & Applications (CEA)**:
  - Largest department in the university with over 2,500 active B.Tech students across years.
  - Specializations: Core CSE, Artificial Intelligence & Machine Learning (AI-ML), Data Analytics, Cyber Security, Cloud Computing & IoT.
  - Faculty Profile: A mix of experienced senior professors and young assistant professors. Many faculty members are actively pursuing Ph.D. publications in deep learning, cloud scheduling, and wireless networks.

---

## 2. Student Demographics & Placement Psychology (7th Semester)

### 2.1 The November Placement Pressure Cooker
You are addressing students in the **middle of their 7th semester (mid-November 2026)**. In Indian engineering colleges, this is the most emotionally charged and tense period of their degree:
1. **The Placed Elite (Top 10-15%)**:
   - Have secured 10 LPA to 25+ LPA offers or early startup internships.
   - Ego Profile: Highly confident, sometimes arrogant. They have spent months doing LeetCode, system design, and prompt engineering. They will sit in the front rows or corners, listening with a critical ear, ready to ask complex edge-case questions to test whether the trainer is "legit" or just another college guest lecturer.
2. **The Mass Recruited (40-50%)**:
   - Have offers from IT service giants (TCS Digital/Ninja, Infosys, Capgemini, Accenture, Wipro) in the ₹3.5 LPA to ₹7 LPA range.
   - Psychological State: Satisfied that they have a safety net, but desperately hungry for product-company skills (HPC, distributed AI, low-latency C++, systems engineering) that can unlock 12 LPA to 30 LPA off-campus or super-dream offers.
3. **The Unplaced / Panicked (30-40%)**:
   - High anxiety. They worry about graduating without a job.
   - Psychological State: Intimidated by complex mathematics, but immensely grateful if the trainer breaks concepts down into intuitive, visual, dead-simple logic that demystifies real technology.

### 2.2 GLA University Placement Statistics
* **Peak Highest Package**: ₹55 LPA (secured at Microsoft), ₹44 LPA (Amazon).
* **Average Package**: ₹6.50 LPA to ₹8.00 LPA for CSE / AIML streams.
* **Median Package**: ~₹6.00 LPA.
* **Top Regular Recruiters**: Microsoft, Amazon, VMware, Adobe, Samsung, TCS, Infosys, Capgemini, Cognizant, IBM, Deloitte, Tech Mahindra.

---

## 3. Campus Infrastructure, Lab Environment & Potential Bottlenecks

### 3.1 Computer Science Lab Setup
* **Lab Configuration**: High-density labs with 60 to 90 desktop PCs per lab room.
* **Operating Systems**: Dual-boot systems (Ubuntu 20.04/22.04 LTS and Windows 10/11 Enterprise).
* **Hardware Specs**: Typical student lab desktop: Intel Core i5 / i7 (8th to 12th Gen), 8 GB to 16 GB RAM, integrated graphics or entry-level Nvidia GPUs (GTX 1650 / RTX 3050). No local high-end server clusters inside student desktop labs.
* **Network Infrastructure**: High-speed campus LAN, but heavily restricted by central proxy firewalls, content filters, and blocked peer-to-peer / SSH ports.

### 3.2 The Golden Threat Model: Potential Lab Failure Modes
1. **Campus Wi-Fi / Proxy Collapse**:
   - If 60 students simultaneously attempt `pip install tensorflow` or `git clone` during a lab, the campus proxy throttles or drops connections.
   - **Remedy**: 100% offline pen-drive wheel repository (`OFFLINE_PENDRIVE_TOOLKIT`). Never rely on campus Wi-Fi.
2. **Restricted Sudo / Root Access**:
   - Lab PC user accounts (`student` or `guest`) usually lack root (`sudo`) privileges.
   - **Remedy**: All Python virtual environments must be created in `$HOME/hpc_env` or local user directories without system-wide package modification.
3. **Projector HDMI & Audio Glitches**:
   - Arrive 45 minutes early on Day 1. Verify projector resolution (1920x1080), HDMI handshake, audio cable, and whiteboard marker availability before students enter.
""")

# ==============================================================================
# 02 EDULATERAL FOUNDATION INTELLIGENCE
# ==============================================================================

write_f("02_Edulateral_Foundation_Intelligence/edulateral_corporate_and_business_model.md", """# 🏢 Edulateral Foundation: Corporate Structure, OEM MoUs & Delivery Protocol
**Corporate Entity**: Edulateral Private Limited / Edulateral Foundation  
**CIN**: `U85499KA2023PTC182423` (RoC Bangalore, Karnataka | Incorporated: Dec 20, 2023)  
**Registered Office**: #950, 16th Main, 13th Cross, B Block, Sahakaranagar, Bangalore North – 560092  
**Executive Hub**: The Pavilion, 62/63 Church Street, Off MG Road, Bangalore – 560001  

---

## 1. Corporate Ecosystem & Key Decision Makers

```
┌────────────────────────────────────────────────────────┐
│                   EDULATERAL FOUNDATION                │
├──────────────────────────┬─────────────────────────────┤
│  Y. B. DILIP KUMAR       │  PEDINA SREEJA              │
│  (Director / Management) │  (Program Operations Exec)  │
│  • dilip@edulateral.com  │  • sreeja@edulateral.com    │
│  • OEM & University MoUs │  • Mob: +91 9861773390      │
│  • High-level contracts  │  • Trainer Ops & Billing    │
└──────────────────────────┴─────────────────────────────┘
```

### 1.1 Yoganathan Bangalore Dilip Kumar (Dilip Kumar)
* **Profile**: Seasoned education entrepreneur and institutional bridge. Has spent 15+ years establishing technical collaborations between tier-1 MNCs (Intel, NEC, Microsoft) and private universities across India.
* **Operational Goal**: Ensuring university management (GLA Chancellor/Dean) is wowed by training quality, ensuring renewed multi-year contracts and expansion of Intel/NEC Centers of Excellence.

### 1.2 Pedina Sreeja (Program Operations Executive)
* **Profile**: The direct operational handler for trainers. Rigorous on institutional discipline, compliance, timely attendance reporting, and curriculum alignment.
* **Key Requirements Enforced by Sreeja**:
  1. Professional formal attire.
  2. Advance submission of all PowerPoint presentations (`.pptx`).
  3. Strict adherence to agreed syllabus flow without deviating into unapproved topics.
  4. Preparation of 25 objective MCQs per day for student assessment.
  5. 100% adherence to Edulateral branding banner/logo.
  6. Strict zero-tolerance policy on personal social media posting.

---

## 2. Business Model: How Edulateral Operates

1. **The University MoU**: Edulateral signs a comprehensive agreement with the university (e.g. GLA University). The university pays Edulateral a multi-lakh contract fee to set up specialized infrastructure (Intel Unnati Lab, NEC CoE) and deliver expert-led Block Teaching.
2. **The Trainer Model**: Edulateral contracts industry practitioners or specialized trainers (like Shivam Gupta) on a fixed honorarium (₹18,000 INR for 5 days) to deliver the training under the Edulateral banner.
3. **The IP Lock**: To prevent trainers from poaching clients or conducting private workshops directly with the university, Edulateral enforces strict intellectual property clauses, non-circumvention rules, and social media embargoes.

---

## 3. Financial, Billing & TDS Protocol (Section 194J)

* **Total Remuneration**: ₹18,000 INR gross.
* **Milestone 1**: 50% advance on Day 1 (₹9,000 gross). Net after 10% TDS = **₹8,100 INR**.
* **Milestone 2**: 50% final balance within 15 working days post-completion (₹9,000 gross). Net after 10% TDS = **₹8,100 INR**.
* **Total Net Realized**: **₹16,200 INR**.
* **Tax Compliance**:
  - Deducted at 10% under Section 194J of the Income Tax Act against your PAN.
  - Form 16A TDS certificate will be credited to your 26AS/AIS in Q3 FY 2026-27.
  - **Crucial Action**: Ensure your PAN card and bank details matching your PAN name are submitted to Sreeja prior to Day 1 to avoid statutory 20% TDS under Section 206AA.
""")

# ==============================================================================
# 03 MANASAI TECHNOLOGY DEEP DOSSIER
# ==============================================================================

write_f("03_ManasAI_Technology_Deep_Dossier/manasai_corporate_profile_and_vrindavan_base.md", """# 🧠 ManasAI Technology Private Limited: Research-Driven Frontier AI
**Corporate Name**: ManasAI Technology Private Limited  
**CIN**: `U62011UW2026PTC0257450` (RoC-Uttar Pradesh II | Incorporated: August 18, 2026)  
**Registered Office**: Govinda 2D 101, Omaxe Eternity, Chhatikara Road, Sunrakh Bangar, Vrindaban, Mathura, UP – 281121  
**Website**: `https://manasai.tech` | **Email**: `admin@manasai.tech`  
**Tagline**: *"Intelligence for inner wellbeing. Grounded in signals. Guided by research."*  

---

## 1. Geographic & Strategic Significance (Vrindavan, Mathura)

Notice the physical location of ManasAI: **Omaxe Eternity, Chhatikara Road, Vrindaban, Mathura**!
- This is located within a 15-minute drive from **GLA University, Mathura** (Chaumuhan).
- Vrindavan serves as the research and contemplative base for exploring consciousness, meditation states, and inner wellbeing through physiological instrumentation.

---

## 2. Core Leadership Team

```
┌────────────────────────────────────────────────────────────────────────┐
│                   MANASAI TECHNOLOGY LEADERSHIP                        │
├──────────────────────────┬─────────────────────────┬───────────────────┤
│  DR. JYOTIRANJAN BEURIA  │  RAJAT GARG             │  AKASH SHARMA     │
│  (Chief Scientist)       │  (Chief Technology Off) │  (Marketing Head) │
│  • jb@manasai.tech       │  • rajat@manasai.tech   │  • akash@manasai  │
│  • IIT Roorkee, HRI,     │  • IIT Roorkee, Univ.   │  • Founder, Habit │
│    IIT Mandi (Physics)   │    Minnesota | ex-Google│    Mantra         │
└──────────────────────────┴─────────────────────────┴───────────────────┘
```

### 2.1 Dr. Jyotiranjan Beuria (Chief Scientist & Director)
- Alumnus of **IIT Roorkee**, **Harish-Chandra Research Institute (HRI) Prayagraj**, and **IIT Mandi**.
- Theoretical physicist. Leads scientific direction across **physics-informed neural networks (PINNs)**, physical AI, reservoir computing, quantum consciousness, and integrating classical Indic knowledge systems with cognitive science.

### 2.2 Rajat Garg (Chief Technology Officer)
- B.Tech in Electronics & Communication Engineering from **IIT Roorkee**; M.S. in Computer Science from the **University of Minnesota**.
- Elite corporate engineering background: **Google**, **Amazon**, and **VMware**.
- Translates deep mathematical and consciousness research into deployable embedded firmware, signal processing pipelines, and AI systems.
- Coordinates the GLA University Block Teaching with Edulateral Foundation and engaged Shivam Gupta.

### 2.3 Akash Sharma (Marketing & Collaboration Head / Director)
- Entrepreneur and collaboration strategist. Previously founded **HabitMantra** in the health and wellness technology space.
- Manages institutional partnerships, clinical research collaborations, and research kit distribution.

---

## 3. Flagship Product: SakshiSense™ Wearable Sensing

* **Core Concept**: Research-grade wearable instrumentation providing **unfiltered raw biometric signal access** for academic and clinical research laboratories.
* **Form Factors**:
  1. **SakshiSense Ring**: Titanium-styled continuous physiological monitoring ring.
  2. **SakshiSense Wristband**: Graphite research-grade multi-sensor band.
* **Biometric Signal Streams**:
  - **PPG (Photoplethysmography)**: Raw optical pulse waveforms (heart rate, HRV, vascular stiffness).
  - **IMU (Inertial Measurement Unit)**: 6/9-axis movement, tremor, physical restlessness.
  - **EDA (Electrodermal Activity)**: Galvanic skin response, sympathetic nervous system arousal.
  - **Acoustic Context (Sound)**: Environmental audio context and speech prosody.
* **Target Applications**: Stress & anxiety modeling, attention & cognitive distraction analysis.
* **Research Partner**: **CPCSci at ISS Delhi** (Center for Positivism and Consciousness Science at the Institute for Science and Spirituality, Delhi).
""")

# ==============================================================================
# 04 KRISHNAYAN AI DEEP DOSSIER
# ==============================================================================

write_f("04_Krishnayan_AI_Deep_Dossier/krishnayan_ai_organizational_profile_pune.md", """# 🕉️ Krishnayan AI: Where Consciousness Meets Intelligence
**Brand Entity**: Krishnayan AI  
**Website**: `https://krishnayanai.com` | **Email**: `info@krishnayanai.com` | **Phone**: `+91 98183 36841`  
**Registered Operating Address**: Flat #202, C-Wing, Barsana Society, near ISKCON NVCC, Tilkernagar, Kondhwa Budhruk, Pune – 411048  
**Tagline**: *"Consciousness meets Intelligence"*, *"Empathy + Purpose = Eternal Success"*  

---

## 1. Founding Vision & The Conscious Leadership Ethos

Krishnayan AI is a purpose-driven AI solutions, campus training, and corporate leadership organization that bridges cutting-edge modern computer science with the timeless principles of conscious leadership and purpose-driven action.

* **The Name**: *Krishnayan* draws inspiration from Lord Krishna — symbolizing supreme wisdom, tactical mastery, and selfless, dedicated action (*Karmayoga*).
* **Location Symbolism**: Operating out of **Barsana Society**, directly adjacent to **ISKCON New Vedic Cultural Centre (NVCC) in Pune**.
* **Philanthropic Core**: Pledges a substantial portion of profits toward charitable and community initiatives, including cow protection (Gau Seva) and rural education.

---

## 2. Leadership Team

1. **Rajat Garg** (Co-Founder):
   - M.S. CS (Univ. of Minnesota) | B.Tech ECE (IIT Roorkee) | ex-Google, Amazon, VMware.
   - Drives technical architecture, scalable AI systems, and high-performance engineering curriculum design.
2. **Vineet Bhardwaj** (Co-Founder & Head of Academia):
   - Alumnus of **E&ICT Academy, IIT Kanpur** (3 years of core academic deployment).
   - 5+ years in enterprise corporate training; 3 years as a DevOps Engineer.
   - Specializes in transforming engineering college students into career-ready software professionals.
3. **Devamira Das (Farzad Motishaw)** (Leadership Coach & Workplace Dynamics Specialist):
   - India's First Certified **"Fight-Clean" Coach**.
   - Certified 3 Vital Questions® & TED* Practitioner (USA); mentored by Prof. Maria Cristina Casanova (UN Advisor, New York).
   - 25+ years corporate career as a Chartered Accountant in audit and systems compliance; 14+ years in relationship coaching, workplace dynamics, and conscious leadership.
4. **Ravi Srivastava** (Executive Head – Trainings):
   - 30+ years of corporate capability development, process excellence (NIIT Ltd), and enterprise training aligned with tech giants like Infosys and Wipro.

---

## 3. Core Offerings & Strategic Partnerships

1. **Campus Training Programs**: Intensive technical bootcamps across premier institutions (**VIT, LPU, PSIT Kanpur, GNIOT Greater Noida**) covering AI/ML, Full-Stack Python, DevOps, and Placement Prep.
2. **Corporate Training**: Executive coaching, emotional intelligence, and transforming workplace drama into high-performance synergy.
3. **AI Solutions & Consulting**: Custom machine learning models, voice automation (**CallMatic** partnership), and CRM pipelines (**Snap.pe**, **ManageMyLeads**).
4. **Indian Knowledge Systems (IKS)**: Strategic partnership with the **Institute for Science and Spirituality (ISS)**.

---

## 4. Connection to Shivam Gupta

In Shivam's workspace, the resume file `krishnayan-python-ai-developer.pdf` was tailored specifically for his role as a **Python Full-Stack & AI Systems Engineer** at/with Krishnayan AI. Shivam's proven leadership as President of ITM Developers Club and builder of high-concurrency platforms (SAY-IDC) aligns seamlessly with Krishnayan AI's mission.
""")

# ==============================================================================
# 05 KEY PERSONNEL PROFILES
# ==============================================================================

write_f("05_Key_Personnel_Profiles/rajat_garg_deep_dossier.md", """# 👤 Rajat Garg: The Central Architect & Linchpin
**Email**: `rajat@manasai.tech` / `rajatgarg.iitr@gmail.com`  
**Alma Mater**: B.Tech ECE — IIT Roorkee | M.S. Computer Science — University of Minnesota  
**Former Employers**: Google · Amazon · VMware  
**Current Roles**:
- Chief Technology Officer @ **ManasAI Technology Private Limited** (Vrindavan, Mathura)
- Co-Founder @ **Krishnayan AI** (Pune)
- Academic & Operations Coordinator for GLA University Block Teaching @ **Edulateral Foundation**

---

## 1. Professional Background & Technical Archetype

Rajat Garg represents the highest caliber of Indian systems engineering:
- Graduated from **IIT Roorkee** in Electronics & Communication Engineering.
- Completed Master's in Computer Science at the **University of Minnesota** (renowned for high-performance computing, distributed systems, and data mining).
- Cut his teeth at the apex of global Big Tech: **Google**, **Amazon**, and **VMware**. At VMware and Amazon, he worked on large-scale virtualization, distributed systems, hypervisors, and cloud infrastructure.
- Athletic Discipline: Represented IIT Roorkee in the Inter-IIT Athletics Team.

---

## 2. Rajat's Psychological Expectations from Shivam

When Rajat forwarded Sreeja's email to Shivam with the subject *"GLA University -Block Teaching process, payment terms, T&C, presentation and Marketing From 16th Nov to 20th Nov 2026 :High Performance Computing"*, he was placing immense trust in Shivam:

1. **Why Rajat Picked Shivam**:
   - Rajat knows Shivam is a hungry, high-horsepower engineer who built high-concurrency systems (SAY-IDC in Go/React), ran developer clubs (IDC), and understands real software.
   - Rajat does NOT want a theoretical academic who reads slides. He wants someone who commands the terminal, demonstrates real engineering, and inspires students.
2. **What Would Disappoint Rajat**:
   - Getting flustered by student cross-questions.
   - Reading directly off slides without drawing architecture on the whiteboard.
   - Blaming campus internet for a halted lab session.
   - Violating Edulateral's IP or social media embargoes.
3. **What Will Thrill Rajat**:
   - Shivam walking into GLA University, completely prepared with 100% offline code, stunning the students with deep silicon knowledge, handling every AI cross-question effortlessly, and receiving a glowing 5-star review from GLA Dean Prof. Ashish Sharma and Edulateral's Dilip Kumar!
""")

print("[SUCCESS] Phase 1: Institutional, Corporate and Personnel Intelligence Dossiers Built!")
