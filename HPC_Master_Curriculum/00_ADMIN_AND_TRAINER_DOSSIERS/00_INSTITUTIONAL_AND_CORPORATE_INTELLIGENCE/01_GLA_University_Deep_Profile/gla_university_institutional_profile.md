# 🏛️ GLA University Mathura: Complete Institutional & Academic Dossier
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
