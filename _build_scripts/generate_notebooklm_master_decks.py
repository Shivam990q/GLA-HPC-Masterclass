"""
generate_notebooklm_master_decks.py
Constructs the ultra-high-end NotebookLM-style PowerPoint presentation decks
for Day 1 and Day 5 of the GLA University HPC Master Class.
Features:
- NotebookLM design system (Deep Obsidian background, frosted slate cards, electric cyan/indigo accents)
- Multi-card architectural layouts, terminal code blocks, mathematical formulas, and telemetry metrics
- Explicit Trainer Division (Shivam Gupta vs Rajat Garg) addressing Rajat's LMS upload request
- Full detailed presenter notes on every single slide
"""

import os
import shutil
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# Paths
BASE_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings")
DAY1_DIR = BASE_DIR / "HPC_Master_Curriculum" / "Day-01_HPC_Linux_Shell_oneAPI"
DAY5_DIR = BASE_DIR / "HPC_Master_Curriculum" / "Day-05_GenAI_LLMs_Gaudi_OpenVINO"
EDULATERAL_DIR = BASE_DIR / "HPC_Master_Curriculum" / "Edulateral_Official_Presentations"

for p in [DAY1_DIR, DAY5_DIR, EDULATERAL_DIR]:
    p.mkdir(parents=True, exist_ok=True)

# NotebookLM Color Palette
C_BG            = RGBColor(11, 17, 32)     # #0B1120 Deep Obsidian
C_SURFACE       = RGBColor(22, 32, 50)     # #162032 Slate Container Card
C_SURFACE_ALT   = RGBColor(30, 41, 59)     # #1E293B Inner Slate Box
C_BORDER_SUBTLE = RGBColor(30, 58, 95)     # #1E3A5F Subtle Card Border
C_BORDER_ACTIVE = RGBColor(56, 189, 248)   # #38BDF8 Electric Cyan Border
C_CYAN          = RGBColor(56, 189, 248)   # #38BDF8 Cyan Accent
C_INDIGO        = RGBColor(129, 140, 248)  # #818CF8 Electric Indigo
C_EMERALD       = RGBColor(52, 211, 153)   # #34D399 Emerald Accent
C_AMBER         = RGBColor(251, 191, 36)   # #FBBF24 Amber Accent
C_TEXT_WHITE    = RGBColor(248, 250, 252)  # #F8FAFC White Text
C_TEXT_MUTED    = RGBColor(148, 163, 184)  # #94A3B8 Muted Gray
C_TERMINAL_BG   = RGBColor(15, 23, 42)     # #0F172A Terminal Dark
C_TERMINAL_TEXT = RGBColor(74, 222, 128)   # #4ADE80 Terminal Green

def add_notebooklm_header(slide, title, breadcrumb, trainer_tag="LEAD TRAINER: SHIVAM GUPTA"):
    # Category Pill
    pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.4), Inches(4.5), Inches(0.32))
    pill.fill.solid()
    pill.fill.fore_color.rgb = C_SURFACE
    pill.line.color.rgb = C_BORDER_SUBTLE
    tf_p = pill.text_frame
    tf_p.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_p = tf_p.paragraphs[0]
    p_p.text = f"  GLA UNIVERSITY // LMS COURSEWARE  "
    p_p.font.size = Pt(10)
    p_p.font.bold = True
    p_p.font.color.rgb = C_CYAN

    # Trainer Tag Pill
    t_pill = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.5), Inches(0.4), Inches(4.0), Inches(0.32))
    t_pill.fill.solid()
    t_pill.fill.fore_color.rgb = C_SURFACE
    t_pill.line.color.rgb = C_INDIGO
    tf_tp = t_pill.text_frame
    tf_tp.vertical_anchor = MSO_ANCHOR.MIDDLE
    p_tp = tf_tp.paragraphs[0]
    p_tp.text = f"  {trainer_tag}  "
    p_tp.font.size = Pt(10)
    p_tp.font.bold = True
    p_tp.font.color.rgb = C_INDIGO
    p_tp.alignment = PP_ALIGN.RIGHT

    # Main Title
    tb = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.75))
    tf = tb.text_frame
    tf.word_wrap = True
    p_t = tf.paragraphs[0]
    p_t.text = title
    p_t.font.size = Pt(22)
    p_t.font.bold = True
    p_t.font.color.rgb = C_TEXT_WHITE

    p_b = tf.add_paragraph()
    p_b.text = breadcrumb
    p_b.font.size = Pt(12)
    p_b.font.color.rgb = C_CYAN

def build_dual_card_slide(slide, left_data, right_data):
    # Left Card
    card_l = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(5.7), Inches(5.3))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = C_SURFACE
    card_l.line.color.rgb = left_data.get("border_color", C_BORDER_ACTIVE)
    card_l.line.width = Pt(1.2)

    tf_l = card_l.text_frame
    tf_l.word_wrap = True
    p_lh = tf_l.paragraphs[0]
    p_lh.text = left_data["title"]
    p_lh.font.size = Pt(16)
    p_lh.font.bold = True
    p_lh.font.color.rgb = left_data.get("title_color", C_CYAN)
    p_lh.space_after = Pt(12)

    for b in left_data["bullets"]:
        pb = tf_l.add_paragraph()
        pb.text = f"• {b}"
        pb.font.size = Pt(13)
        pb.font.color.rgb = C_TEXT_WHITE
        pb.space_after = Pt(8)

    # Right Card
    card_r = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), Inches(5.7), Inches(5.3))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = C_SURFACE
    card_r.line.color.rgb = right_data.get("border_color", C_INDIGO)
    card_r.line.width = Pt(1.2)

    tf_r = card_r.text_frame
    tf_r.word_wrap = True
    p_rh = tf_r.paragraphs[0]
    p_rh.text = right_data["title"]
    p_rh.font.size = Pt(16)
    p_rh.font.bold = True
    p_rh.font.color.rgb = right_data.get("title_color", C_INDIGO)
    p_rh.space_after = Pt(12)

    for b in right_data["bullets"]:
        pb = tf_r.add_paragraph()
        pb.text = f"• {b}"
        pb.font.size = Pt(13)
        pb.font.color.rgb = C_TEXT_WHITE
        pb.space_after = Pt(8)

def build_triple_card_slide(slide, cards_data):
    x_positions = [Inches(0.8), Inches(4.75), Inches(8.7)]
    width = Inches(3.8)
    height = Inches(5.3)

    for idx, c in enumerate(cards_data):
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x_positions[idx], Inches(1.6), width, height)
        card.fill.solid()
        card.fill.fore_color.rgb = C_SURFACE
        card.line.color.rgb = c.get("border_color", C_BORDER_SUBTLE)
        card.line.width = Pt(1.2)

        tf = card.text_frame
        tf.word_wrap = True
        ph = tf.paragraphs[0]
        ph.text = c["title"]
        ph.font.size = Pt(15)
        ph.font.bold = True
        ph.font.color.rgb = c.get("title_color", C_CYAN)
        ph.space_after = Pt(12)

        for b in c["bullets"]:
            pb = tf.add_paragraph()
            pb.text = f"• {b}"
            pb.font.size = Pt(12)
            pb.font.color.rgb = C_TEXT_WHITE
            pb.space_after = Pt(8)

def build_terminal_code_slide(slide, concept_data, code_data):
    # Top Concept Card
    top_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(11.7), Inches(1.8))
    top_card.fill.solid()
    top_card.fill.fore_color.rgb = C_SURFACE
    top_card.line.color.rgb = C_CYAN
    tf_top = top_card.text_frame
    tf_top.word_wrap = True
    p_th = tf_top.paragraphs[0]
    p_th.text = concept_data["title"]
    p_th.font.size = Pt(15)
    p_th.font.bold = True
    p_th.font.color.rgb = C_CYAN
    p_th.space_after = Pt(6)

    for b in concept_data["bullets"]:
        pb = tf_top.add_paragraph()
        pb.text = f"• {b}"
        pb.font.size = Pt(12)
        pb.font.color.rgb = C_TEXT_WHITE
        pb.space_after = Pt(4)

    # Bottom Terminal Container
    term_card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(3.6), Inches(11.7), Inches(3.3))
    term_card.fill.solid()
    term_card.fill.fore_color.rgb = C_TERMINAL_BG
    term_card.line.color.rgb = C_BORDER_SUBTLE
    term_card.line.width = Pt(1.0)

    tf_term = term_card.text_frame
    tf_term.word_wrap = True
    pt_h = tf_term.paragraphs[0]
    pt_h.text = f"🖥️  TERMINAL EXECUTION // {code_data.get('lang', 'BASH / DPC++')}"
    pt_h.font.size = Pt(11)
    pt_h.font.bold = True
    pt_h.font.color.rgb = C_CYAN
    pt_h.space_after = Pt(8)

    for line in code_data["code_lines"]:
        pl = tf_term.add_paragraph()
        pl.text = line
        pl.font.size = Pt(11)
        pl.font.name = "Consolas"
        pl.font.color.rgb = C_TERMINAL_TEXT if not line.startswith("//") and not line.startswith("#") else C_TEXT_MUTED
        pl.space_after = Pt(3)

def build_cover_slide(prs, day_num, title, subtitle):
    blank_layout = prs.slide_layouts[6]
    slide = prs.slides.add_slide(blank_layout)

    # Background
    bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid()
    bg.fill.fore_color.rgb = C_BG
    bg.line.fill.background()

    # Center Hero Card
    hero = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.9), Inches(11.333), Inches(5.7))
    hero.fill.solid()
    hero.fill.fore_color.rgb = C_SURFACE
    hero.line.color.rgb = C_BORDER_ACTIVE
    hero.line.width = Pt(1.5)

    tf = hero.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE

    p0 = tf.paragraphs[0]
    p0.text = "GLA UNIVERSITY // DEPARTMENT OF COMPUTER ENGINEERING & APPLICATIONS"
    p0.font.size = Pt(13)
    p0.font.bold = True
    p0.font.color.rgb = C_CYAN
    p0.alignment = PP_ALIGN.CENTER
    p0.space_after = Pt(6)

    p1 = tf.add_paragraph()
    p1.text = "HIGH PERFORMANCE COMPUTING MASTER CLASS"
    p1.font.size = Pt(22)
    p1.font.bold = True
    p1.font.color.rgb = C_TEXT_WHITE
    p1.alignment = PP_ALIGN.CENTER

    p2 = tf.add_paragraph()
    p2.text = f"DAY {day_num}: {title.upper()}"
    p2.font.size = Pt(32)
    p2.font.bold = True
    p2.font.color.rgb = C_CYAN
    p2.alignment = PP_ALIGN.CENTER
    p2.space_after = Pt(8)

    p3 = tf.add_paragraph()
    p3.text = subtitle
    p3.font.size = Pt(16)
    p3.font.color.rgb = C_TEXT_MUTED
    p3.alignment = PP_ALIGN.CENTER
    p3.space_after = Pt(24)

    # Instructional Allocation Box inside cover
    p4 = tf.add_paragraph()
    p4.text = "═══════════════════════════════════════════════════════════════════════"
    p4.font.size = Pt(11)
    p4.font.color.rgb = C_BORDER_SUBTLE
    p4.alignment = PP_ALIGN.CENTER

    p5 = tf.add_paragraph()
    p5.text = "LEAD INSTRUCTOR: Shivam Gupta (~SEED~) | SYSTEMS & SILICON ARCHITECTURE"
    p5.font.size = Pt(13)
    p5.font.bold = True
    p5.font.color.rgb = C_EMERALD
    p5.alignment = PP_ALIGN.CENTER

    p6 = tf.add_paragraph()
    p6.text = "CO-TRAINER / CHANNEL LEAD: Rajat Garg (Ramāpriya Das) | ACADEMIC & ENTERPRISE ALIGNMENT"
    p6.font.size = Pt(13)
    p6.font.bold = True
    p6.font.color.rgb = C_INDIGO
    p6.alignment = PP_ALIGN.CENTER

    p7 = tf.add_paragraph()
    p7.text = "Contracting Partner: Edulateral Foundation | Technical Alliance: Intel Unnati & NEC Supercomputing"
    p7.font.size = Pt(12)
    p7.font.color.rgb = C_TEXT_MUTED
    p7.alignment = PP_ALIGN.CENTER

    notes = slide.notes_slide.notes_text_frame
    notes.text = f"Official LMS Cover Slide for Day {day_num}. Welcome GLA University B.Tech 7th Semester students. Set high-authority systems engineering expectations."
    return slide

def generate_day1_deck():
    print("[*] Generating NotebookLM Master Presentation for Day 1...")
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # Slide 1: Cover
    build_cover_slide(prs, 1, "HPC Fundamentals, Linux Systems & Intel oneAPI", "Silicon Microarchitecture, Vectorization, OS Kernel Mechanics & Heterogeneous DPC++/SYCL")

    # Slide 2: Course Charter & LMS Syllabus Mapping
    s2 = prs.slides.add_slide(blank)
    bg = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s2, "Course Charter & LMS Syllabus Mapping", "MODULE 01.01 // ACADEMIC GOVERNANCE", "JOINT INSTRUCTIONAL MAPPING")
    build_dual_card_slide(s2, {
        "title": "GLA University Academic Charter",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Program: B.Tech Computer Science & Engineering (7th Semester).",
            "Target Cohort: Advanced Elective in High Performance & Distributed Systems.",
            "LMS Course Code: GLA-HPC-BCSG701 // Block Teaching Format.",
            "Pedagogy: Problem-Based Learning, Whiteboard Systems Breakdown, Hands-On Live Lab Execution.",
            "Grading Scheme: 20% Lab Submissions, 30% Daily Evaluative MCQs, 50% Capstone Implementation."
        ]
    }, {
        "title": "Intel Unnati & Edulateral Compliance",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Authorized Technical Alignment: Intel oneAPI Center of Excellence & NEC Supercomputing.",
            "Industrial Outcome: Equipping students with native silicon optimization skills demanded by global hardware & AI firms.",
            "Zero Hallucination Mandate: Strictly empirical hardware validation; no unverified claims or slide-reading.",
            "Offline Self-Containment: All lab benchmarks executed on local cluster nodes independent of cloud internet.",
            "Repository Artifacts: All source code, datasets, and scripts verified with zero compilation errors."
        ]
    })
    s2.notes_slide.notes_text_frame.text = "Present this slide to align students and faculty observers with the official course charter. Emphasize that the course is professionally graded and monitored for LMS completion."

    # Slide 3: Trainer Division Matrix (Addressing Rajat's prompt)
    s3 = prs.slides.add_slide(blank)
    bg = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s3, "Instructional Division & Trainer Matrix", "MODULE 01.02 // PODIUM RESPONSIBILITIES", "OFFICIAL TOPIC SPLIT")
    build_dual_card_slide(s3, {
        "title": "Shivam Gupta (~SEED~) — Lead Systems Trainer",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Silicon Microarchitecture: Von Neumann limits, Cache hierarchy, and the Memory Wall physics.",
            "AVX-512 Vectorization: SIMD math, FMA registers, assembly emission, and instruction pipelining.",
            "Linux Kernel Architecture: `task_struct`, core pinning (`numactl`, `taskset`), context switch analysis.",
            "Intel oneAPI & SYCL: DPC++ runtime, Unified Shared Memory (USM) engines, Level Zero execution.",
            "Live Benchmark Defense: Terminal execution, compiler optimization reports, student trap question counter-demos."
        ]
    }, {
        "title": "Rajat Garg (Ramāpriya Das) — Academic & Channel Lead",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Academic Alignment: Curriculum mapping to GLA University departmental guidelines.",
            "Supercomputing Context: Enterprise HPC case studies, US DoE Aurora and Frontier architectures.",
            "Laboratory Operations: Lab network configuration, workstation access tokens, and environment setup.",
            "LMS Governance: Managing MCQ evaluation logs, attendance records, and student assessment uploads.",
            "Placement Mentorship: Guiding final-year students on systems engineering interview rubrics."
        ]
    })
    s3.notes_slide.notes_text_frame.text = "This slide directly resolves the LMS question posed by Rajat Garg. Clearly defines who leads what on the podium, establishing absolute instructional cohesion."

    # Slide 4: The HPC Imperative & Supercomputing Milestones
    s4 = prs.slides.add_slide(blank)
    bg = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s4, "The High Performance Computing Imperative", "MODULE 01.03 // THE PHYSICAL LIMITS", "LEAD: SHIVAM GUPTA")
    build_triple_card_slide(s4, [
        {
            "title": "1. The Death of Dennard Scaling",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "Prior to 2006, clock speeds doubled every 18 months at constant power density.",
                "Thermal Dissipation Limit (100W/cm²): CPUs hit a thermal wall at ~5 GHz.",
                "Voltage cannot scale below ~0.7V without quantum tunneling leakage.",
                "Performance growth shifted entirely from raw frequency to parallelism."
            ]
        },
        {
            "title": "2. The Exascale Threshold",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "1 ExaFLOP = 10¹⁸ floating-point operations every second.",
                "Aurora Supercomputer: 10,000+ nodes powered by Intel Xeon CPUs & Intel Data Center Max GPUs.",
                "Delivers over 1 Exaflop using SYCL and oneAPI cross-architecture code.",
                "Frontier Supercomputer: Oak Ridge National Lab exascale leader."
            ]
        },
        {
            "title": "3. The Software Dilemma",
            "title_color": C_AMBER,
            "border_color": C_AMBER,
            "bullets": [
                "Hardware is massively parallel; standard code is overwhelmingly serial.",
                "A naive Python or unoptimized C++ script runs on exactly 1 core.",
                "98% of silicon execution units sit completely idle in typical software.",
                "HPC bridges the chasm between physical silicon and application code."
            ]
        }
    ])
    s4.notes_slide.notes_text_frame.text = "Explain why we cannot simply wait for faster single-core CPUs anymore. Modern computing requires mastering parallelism and memory management."

    # Slide 5: Von Neumann vs Heterogeneous NUMA Architecture
    s5 = prs.slides.add_slide(blank)
    bg = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s5, "Von Neumann Architecture vs Heterogeneous NUMA", "MODULE 01.04 // HARDWARE TOPOLOGY", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s5, {
        "title": "Classical Von Neumann Bottleneck (1945)",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Unified shared bus connects CPU arithmetic logic to memory.",
            "Instructions and data compete for the exact same physical bus channels.",
            "CPU processing speed outpaced bus transmission latency by 100x.",
            "Result: The CPU spends the majority of its clock cycles stalled waiting for data."
        ]
    }, {
        "title": "Modern Heterogeneous NUMA Architecture",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Multi-socket servers integrate independent memory controllers per socket.",
            "Local Memory Access: Core accesses local DDR5 channel in ~70 ns.",
            "Remote Memory Access: Core accesses remote socket memory over UPI bus in ~140 ns (2x latency penalty).",
            "Accelerators (GPUs, HPUs, FPGAs) connect via high-speed PCIe Gen5 / CXL interconnects.",
            "HPC systems software MUST orchestrate data placement to preserve memory locality."
        ]
    })
    s5.notes_slide.notes_text_frame.text = "Draw the NUMA socket diagram on the board. Point out that unmanaged memory allocations degrade performance by 40% simply due to inter-socket bus hops."

    # Slide 6: The Memory Wall — Latency Hierarchy
    s6 = prs.slides.add_slide(blank)
    bg = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s6, "The Memory Wall: Silicon Latency Hierarchy", "MODULE 01.05 // PHYSICAL TIMINGS", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s6, {
        "title": "Exact Silicon Latency Spectrum (Intel Xeon)",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "CPU Registers (1 KB): 0.3 ns latency | 1 clock cycle | Instantaneous.",
            "L1 Data Cache (32-48 KB): 1.0 ns latency | 4-5 clock cycles.",
            "L2 Unified Cache (1-2 MB): 3.5 ns latency | 14 clock cycles.",
            "L3 Shared Cache (LLC, 30-50 MB): 14.0 ns latency | 45-50 clock cycles.",
            "Main Memory (DDR5 DRAM): 75-90 ns latency | 240+ clock cycles (STALL!).",
            "NVMe SSD Storage: 10,000 to 50,000 ns latency | 30,000+ clock cycles."
        ]
    }, {
        "title": "The Human Scale Analogy",
        "title_color": C_AMBER,
        "border_color": C_AMBER,
        "bullets": [
            "If 1 CPU clock cycle (0.3 ns) is equivalent to 1 SECOND in human time:",
            "L1 Cache access is like reaching for an apple on your desk (4 seconds).",
            "L2 Cache access is like walking to the refrigerator in the kitchen (14 seconds).",
            "L3 Cache access is like walking down the driveway to the mailbox (50 seconds).",
            "DRAM Memory access is like driving to the grocery store across town (4.5 minutes!).",
            "NVMe Disk access is like traveling to Antarctica on a cargo boat (1.5 years!).",
            "HPC Takeaway: High performance computing is the art of never leaving your desk!"
        ]
    })
    s6.notes_slide.notes_text_frame.text = "This is Shivam's signature whiteboard hook. When students hear the human analogy, the concept of memory latency clicks permanently."

    # Slide 7: Operational Intensity & Roofline Principle
    s7 = prs.slides.add_slide(blank)
    bg = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s7, "Operational Intensity & The Roofline Principle", "MODULE 01.06 // MATHEMATICAL LIMITS", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s7, {
        "title": "Operational Intensity Formulation",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Formula: I = Work (FLOPs) / Traffic (Bytes transferred from DRAM).",
            "Low Operational Intensity: Vector Add y[i] = a[i] + b[i] (1 FLOP for 3 reads/writes = 0.083 FLOPs/Byte).",
            "High Operational Intensity: Matrix Multiplication C = A x B (2N³ FLOPs for 3N² bytes = O(N) FLOPs/Byte).",
            "Memory-Bound Region: Performance is strictly throttled by DDR5 bus bandwidth (GB/s). Adding faster CPU cores yields ZERO speedup.",
            "Compute-Bound Region: Performance is throttled by ALU floating-point units. Vectorization yields massive speedups."
        ]
    }, {
        "title": "The Inflection Point on Intel Xeon",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Peak Floating-Point Compute: ~3,000 GFLOPS (3 TFLOPS per socket).",
            "Peak Memory Bandwidth: ~250 GB/s (8-channel DDR5).",
            "Inflection Point: I* = Peak Compute / Peak Bandwidth = 3000 / 250 = 12 FLOPs/Byte.",
            "The Golden Rule: If your code computes fewer than 12 operations per byte moved from RAM, your hardware is waiting for the memory bus 90% of the time.",
            "Solution: Loop tiling, cache blocking, and register reuse to keep bytes inside L1/L2 caches."
        ]
    })
    s7.notes_slide.notes_text_frame.text = "Write the Roofline formula on the board. Explain that amateur programmers blame the CPU when the memory bus is actually the bottleneck."

    # Slide 8: CPU Microarchitecture & Pipeline Execution
    s8 = prs.slides.add_slide(blank)
    bg = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s8, "CPU Microarchitecture & Pipeline Execution", "MODULE 01.07 // PIPELINE ANATOMY", "LEAD: SHIVAM GUPTA")
    build_triple_card_slide(s8, [
        {
            "title": "1. Instruction Fetch & Decode",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "x86 CISC instructions decoded into simple, fixed-length micro-operations (uOps).",
                "Branch Target Buffer (BTB) predicts code branch paths speculatively.",
                "Branch misprediction penalty: 15-20 cycles wasted flushing the pipeline.",
                "Instruction cache misses trigger Frontend Bound stalls."
            ]
        },
        {
            "title": "2. Out-of-Order Execution Engine",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "Reservation Station reorders instructions based on data availability, not source code line order.",
                "Register Renaming eliminates false write-after-read hazards.",
                "Multiple parallel execution ports (Port 0 to Port 7).",
                "Dedicated ports for integer math, vector math, memory loads, and stores."
            ]
        },
        {
            "title": "3. Reorder Buffer & Commit",
            "title_color": C_EMERALD,
            "border_color": C_EMERALD,
            "bullets": [
                "Instructions commit results to architectural registers in original program order.",
                "Retiring: uOps that executed and committed successfully (The ideal state).",
                "Backend Bound stalls: uOps waiting for memory loads or execution ports.",
                "HPC goal: Keep Retiring percentage above 70%."
            ]
        }
    ])
    s8.notes_slide.notes_text_frame.text = "Walk through the life of an instruction from fetch to retire. Point out how branch mispredictions and memory stalls drain throughput."

    # Slide 9: SIMD Vector Architecture (AVX-512)
    s9 = prs.slides.add_slide(blank)
    bg = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s9, "SIMD Vector Computing Architecture (AVX-512)", "MODULE 01.08 // VECTOR SILICON", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s9, {
        "title": "Evolution of x86 Vector Registers",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Scalar x86: RAX, RBX (64 bits) | 1 operation per cycle.",
            "SSE / SSE4.2: XMM0 - XMM15 (128 bits) | 4 x 32-bit floats per cycle.",
            "AVX / AVX2: YMM0 - YMM15 (256 bits) | 8 x 32-bit floats per cycle.",
            "AVX-512: ZMM0 - ZMM31 (512 bits) | 16 x 32-bit floats per cycle!",
            "Register File Expansion: AVX-512 doubles register count from 16 to 32, eliminating register spilling to RAM."
        ]
    }, {
        "title": "16-Lane Parallel Execution in 1 Clock Cycle",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "ZMM0: [ a0 | a1 | a2 | a3 | a4 | a5 | ... | a15 ] (512 bits)",
            "+",
            "ZMM1: [ b0 | b1 | b2 | b3 | b4 | b5 | ... | b15 ] (512 bits)",
            "=",
            "ZMM2: [ c0 | c1 | c2 | c3 | c4 | c5 | ... | c15 ] (1 Cycle!)",
            "Scalar execution takes 16 separate instructions over 16 clock cycles.",
            "AVX-512 executes all 16 additions in a SINGLE instruction in 1 clock cycle.",
            "Throughput speedup: Exactly 16x for single-precision floating-point operations."
        ]
    })
    s9.notes_slide.notes_text_frame.text = "Emphasize that AVX-512 is not software multi-threading; it is hardware vector parallelism inside a single CPU core."

    # Slide 10: Fused Multiply-Add (FMA) Mathematics
    s10 = prs.slides.add_slide(blank)
    bg = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s10, "Fused Multiply-Add (FMA) & Peak Compute Math", "MODULE 01.09 // SILICON THROUGHPUT", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s10, {
        "title": "The FMA Workhorse: r = (a * b) + c",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Computes multiplication and addition in a single hardware cycle with a single rounding step.",
            "Eliminates intermediate floating-point rounding errors (higher numerical precision).",
            "Each FMA counts as 2 FLOPs (1 multiply + 1 addition).",
            "Intel Xeon Scalable cores feature TWO 512-bit FMA execution ports (Port 0 and Port 5).",
            "Each 512-bit FMA unit computes 16 single-precision FMAs per cycle = 32 FLOPs per unit."
        ]
    }, {
        "title": "Theoretical Peak Flops Calculation",
        "title_color": C_AMBER,
        "border_color": C_AMBER,
        "bullets": [
            "FLOPs/cycle/core = 2 (FMA units) x 16 (elements) x 2 (FLOPs/FMA) = 64 FLOPs/cycle.",
            "For a 32-core Intel Xeon Scalable processor running at 3.0 GHz base clock:",
            "Peak = 32 cores x 3.0 x 10⁹ cycles/sec x 64 FLOPs/cycle = 6.144 TFLOPS!",
            "Compare this to scalar code (1 FLOP/cycle):",
            "Scalar Peak = 32 x 3.0 x 10⁹ x 1 = 0.096 TFLOPS.",
            "Conclusion: Writing unvectorized code wastes 98.4% of the silicon you paid for!"
        ]
    })
    s10.notes_slide.notes_text_frame.text = "Write the 6.144 TFLOPS calculation on the board. Show the students that compiler vectorization unlocks massive computational capability."

    # Slide 11: Linux OS Kernel Architecture for HPC
    s11 = prs.slides.add_slide(blank)
    bg = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s11, "Linux Operating System Architecture for HPC", "MODULE 01.10 // KERNEL INTERNALS", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s11, {
        "title": "Kernel Space vs User Space Boundaries",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Ring 0 (Kernel Space): Full hardware access, driver execution, page table management.",
            "Ring 3 (User Space): Sandboxed application execution; communicates via system calls (syscalls).",
            "System Call Overhead: Switching from Ring 3 to Ring 0 costs ~100-300 ns due to CPU mode switch.",
            "HPC Optimization: Minimizing syscalls in tight compute loops; using huge pages (2MB / 1GB) to reduce TLB misses."
        ]
    }, {
        "title": "Virtual Memory & Page Cache Behavior",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Linux Virtual Memory Manager translates virtual addresses to physical DRAM via Page Tables.",
            "Translation Lookaside Buffer (TLB): On-die hardware cache of address translations.",
            "The Page Cache: Linux treats free RAM as wasted RAM. File I/O is automatically cached in memory.",
            "Dirty Pages & Flush: Asynchronous background writeback (`pdflush`/`kswapd`) to NVMe storage.",
            "In HPC, reading warm datasets from the Page Cache operates at DDR5 memory speed (~50 GB/s)."
        ]
    })
    s11.notes_slide.notes_text_frame.text = "Explain why Linux rules supercomputing: transparency, deterministic memory management, and hardware event access."

    # Slide 12: Processes vs Threads at the Kernel Level
    s12 = prs.slides.add_slide(blank)
    bg = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s12, "Processes vs Threads: Kernel Data Structures", "MODULE 01.11 // PROCESS MANAGEMENT", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s12, {
        "title": "The Unified `struct task_struct`",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "At the Linux kernel level, processes and threads are both represented by `task_struct`.",
            "Both are spawned using the `clone()` system call with flags:",
            "Process (`fork()`): Creates independent virtual memory space (`mm_struct`), file tables, and signals.",
            "Thread (`pthread_create()`): Shares virtual memory (`CLONE_VM`), open file descriptors (`CLONE_FILES`), and signal handlers (`CLONE_SIGHAND`)."
        ]
    }, {
        "title": "Context Switching Cost Analysis",
        "title_color": C_AMBER,
        "border_color": C_AMBER,
        "bullets": [
            "Process Context Switch: Cost ~1,000 to 3,000 ns.",
            "Requires reloading CR3 register, invalidating the TLB cache, and evicting L1 cache lines.",
            "Thread Context Switch: Cost ~100 to 300 ns. Retains identical TLB address mappings.",
            "HPC Strategy: Match thread count to physical hardware cores to eliminate OS context switching entirely."
        ]
    })
    s12.notes_slide.notes_text_frame.text = "Explain that threads share memory pointers directly, while processes are isolated. This sets the stage for OpenMP (threads) vs MPI (processes)."

    # Slide 13: CPU Affinity & Core Pinning
    s13 = prs.slides.add_slide(blank)
    bg = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s13, "CPU Affinity & Hardware Core Pinning", "MODULE 01.12 // THREAD PINNING", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s13, {
        "title": "The Problem: OS Thread Migration",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Linux CFS (Completely Fair Scheduler) migrates threads between CPU cores for load balancing.",
            "Cache Cold Miss Penalty: When Thread A moves from Core 0 to Core 16, all its L1/L2 caches are cold!",
            "Memory Bus Thrashing: Cross-socket migrations trigger remote NUMA memory traffic.",
            "Performance Jitter: Thread migration causes latency spikes in scientific simulations."
        ]
    }, {
        "title": "The HPC Solution: Explicit Pinning",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "`taskset -c 0-7 ./my_program`: Pins the process strictly to physical cores 0 through 7.",
            "`numactl --cpunodebind=0 --membind=0`: Binds compute and memory allocation to NUMA node 0.",
            "`export OMP_PROC_BIND=close`: Pins OpenMP threads to adjacent cores to share L3 cache.",
            "`export OMP_PLACES=cores`: Restricts threads from bouncing across hyperthreads.",
            "Result: 100% cache warm execution with zero scheduler migration overhead."
        ]
    })
    s13.notes_slide.notes_text_frame.text = "Demonstrate taskset live. Show how unpinned threads wander across CPU cores in htop, while pinned threads lock solidly onto assigned cores."

    # Slide 14: Linux Telemetry & Diagnostic Commands
    s14 = prs.slides.add_slide(blank)
    bg = s14.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s14, "Linux Systems Telemetry & Diagnostics", "MODULE 01.13 // CLI TOOLKIT", "LEAD: SHIVAM GUPTA")
    build_terminal_code_slide(s14, {
        "title": "Essential Diagnostic CLI Toolkit for HPC Systems Engineers",
        "bullets": [
            "Every systems engineer must query hardware capabilities directly from `/proc` and kernel interfaces.",
            "Verify core count, vector flags (`avx512f`, `avx2`), cache topology, and NUMA node distances before running workloads."
        ]
    }, {
        "lang": "BASH SHELL DIAGNOSTICS",
        "code_lines": [
            "# 1. Query full hardware architecture and cache topology",
            "lscpu | grep -E 'Model name|CPU\\(s\\)|Thread|L1d|L2|L3|NUMA'",
            "",
            "# 2. Inspect active vector SIMD flags on current silicon",
            "grep -m1 -o -E 'avx512[a-z0-9_]*|avx2|fma|sse4_2' /proc/cpuinfo",
            "",
            "# 3. Measure hardware performance counters in real time",
            "perf stat -e cycles,instructions,cache-references,cache-misses ./my_binary",
            "",
            "# 4. Query NUMA nodes and memory distribution",
            "numactl --hardware && numastat -c"
        ]
    })
    s14.notes_slide.notes_text_frame.text = "Have all students run these 4 commands on their lab workstations right now to inspect their local silicon specs."

    # Slide 15: Bash Shell Automation for HPC
    s15 = prs.slides.add_slide(blank)
    bg = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s15, "Bash Shell Automation for HPC Clusters", "MODULE 01.14 // SHELL PIPELINES", "LEAD: SHIVAM GUPTA")
    build_terminal_code_slide(s15, {
        "title": "Writing Production-Grade HPC Cluster Batch Automation Scripts",
        "bullets": [
            "Automated benchmark sweeps, environment configuration, and strict error handling.",
            "`set -e`: Exit immediately if any command returns a non-zero status. `set -o pipefail`: Detect pipeline failures."
        ]
    }, {
        "lang": "BASH HPC AUTOMATION SCRIPT",
        "code_lines": [
            "#!/bin/bash",
            "set -euo pipefail # Strict error handling for cluster scripts",
            "",
            "# Load oneAPI compiler suite",
            "source /opt/intel/oneapi/setvars.sh > /dev/null 2>&1",
            "",
            "# Parameterized Benchmark Sweep across thread counts",
            "for THREADS in 1 2 4 8 16 32; do",
            "    export OMP_NUM_THREADS=$THREADS",
            "    export OMP_PROC_BIND=close",
            "    echo -n \"[Benchmark] Running with $THREADS threads... \"",
            "    ./benchmark_bin | grep 'GFLOPS'",
            "done"
        ]
    })
    s15.notes_slide.notes_text_frame.text = "Walk through the shell script syntax. Show how bash scripts automate parameter sweeps and data logging across compute nodes."

    # Slide 16: Compiler Optimization Pipeline (`gcc` vs `icx`)
    s16 = prs.slides.add_slide(blank)
    bg = s16.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s16, "Compiler Optimization: `gcc` vs Intel `icx`", "MODULE 01.15 // CODE GENERATION", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s16, {
        "title": "Compiler Optimization Flag Levels",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "`-O0`: No optimization. Pure scalar code, exact mapping to source lines for debugging.",
            "`-O1`: Basic block optimization, dead code elimination, register variable assignment.",
            "`-O2`: Extensive optimization, function inlining, instruction scheduling, loop invariant motion.",
            "`-O3`: Aggressive optimization: loop unrolling, auto-vectorization, FMA instruction fusion.",
            "`-xHost`: Generates instructions for the highest instruction set supported by the host CPU (AVX-512/AVX2)."
        ]
    }, {
        "title": "Why Intel `icx` Beats Standard `gcc` on x86",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Intel oneAPI compiler (`icx` / `icpx`) is built on LLVM with Intel-proprietary microarchitectural code generators.",
            "Accurate Cost Heuristics: Tuned for exact Intel L1/L2 cache sizes and execution port latencies.",
            "Interprocedural Optimization (`-ipo`): Analyzes across compilation units to inline functions globally.",
            "Optimization Reports (`-qopt-report=3`): Generates human-readable reports explaining exactly which loops vectorized and why others failed.",
            "Benchmark Reality: `icx` routinely delivers 15% to 35% higher throughput than `gcc -O3` on Intel silicon."
        ]
    })
    s16.notes_slide.notes_text_frame.text = "Emphasize the compiler report flag. It teaches students how to write code that the compiler's auto-vectorizer can actually understand."

    # Slide 17: The Intel oneAPI Heterogeneous Paradigm
    s17 = prs.slides.add_slide(blank)
    bg = s17.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s17, "The Intel oneAPI Heterogeneous Paradigm", "MODULE 01.16 // OPEN STANDARDS", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s17, {
        "title": "The Proprietary Trap: NVIDIA CUDA",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "CUDA is proprietary vendor lock-in. Compiles exclusively to NVIDIA PTX assembly.",
            "Code written in CUDA cannot run on Intel CPUs, Intel Data Center GPUs, or AMD Instinct accelerators.",
            "Enterprises are held hostage to hardware backlogs and $30,000 chip pricing.",
            "Rewriting a 500,000-line CUDA codebase for a new supercomputer costs millions of dollars."
        ]
    }, {
        "title": "The Open Future: Intel oneAPI & SYCL",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Based on the Khronos Group open standard **SYCL**.",
            "Single C++ source codebase targeting heterogeneous processors.",
            "Runs natively on Intel Xeon CPUs, Intel Arc / Max GPUs, and FPGAs.",
            "Compiles to NVIDIA GPUs (via Codeplay oneAPI plugins) and AMD GPUs (via AdaptiveCpp/hipSYCL).",
            "Adopted by the US Department of Energy's Aurora Supercomputer (>1 Exaflop)."
        ]
    })
    s17.notes_slide.notes_text_frame.text = "Frame oneAPI as career empowerment: mastering open heterogeneous programming makes students 10x more valuable than single-vendor developers."

    # Slide 18: oneAPI Software Stack & Level Zero
    s18 = prs.slides.add_slide(blank)
    bg = s18.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s18, "Intel oneAPI Software Stack & Level Zero", "MODULE 01.17 // RUNTIME ARCHITECTURE", "LEAD: SHIVAM GUPTA")
    build_triple_card_slide(s18, [
        {
            "title": "1. oneAPI Toolkits & Libraries",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "Base Toolkit: oneAPI DPC++/C++ Compiler, VTune Profiler, Advisor.",
                "oneMKL: Math Kernel Library (BLAS, LAPACK, FFTs, RNGs).",
                "oneDAL: Data Analytics Library (accelerated machine learning).",
                "oneDNN: Deep Neural Network library powering PyTorch and TensorFlow."
            ]
        },
        {
            "title": "2. SYCL / DPC++ Front-End",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "Modern standard ISO C++17/20 syntax.",
                "Splits host control code from device execution kernels.",
                "Compiles device code into SPIR-V (Standard Portable Intermediate Representation).",
                "Asynchronous execution graph managed by SYCL runtime."
            ]
        },
        {
            "title": "3. Intel Level Zero Runtime",
            "title_color": C_EMERALD,
            "border_color": C_EMERALD,
            "bullets": [
                "Bare-metal low-level hardware abstraction interface.",
                "Direct low-overhead access to Intel GPU execution units.",
                "Sub-microsecond command queue submission latency.",
                "Direct peer-to-peer memory transactions across PCIe and fabric links."
            ]
        }
    ])
    s18.notes_slide.notes_text_frame.text = "Walk through the oneAPI architecture stack from high-level libraries down to Level Zero bare-metal drivers."

    # Slide 19: SYCL / DPC++ Execution Model
    s19 = prs.slides.add_slide(blank)
    bg = s19.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s19, "SYCL / DPC++ Execution Model", "MODULE 01.18 // KERNEL DISPATCH", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s19, {
        "title": "The Queue & Device Selectors",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "`sycl::queue q;`: The primary channel connecting host CPU code to compute devices.",
            "Device Selectors query hardware at runtime:",
            "`sycl::default_selector_v`: Automatically selects highest-performance GPU; falls back to CPU.",
            "`sycl::cpu_selector_v`: Strictly targets host multicore CPU.",
            "`sycl::gpu_selector_v`: Strictly targets discrete or integrated GPU accelerator.",
            "Queues are asynchronous by default. Commands return immediately to the host."
        ]
    }, {
        "title": "Work-Item Hierarchy",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Work-Item: The smallest execution unit. An individual thread executing a kernel on 1 element.",
            "Work-Group: A collection of work-items that execute concurrently on the same compute unit.",
            "Work-groups share high-speed local scratchpad memory (`local_accessor`) and can synchronize with barriers.",
            "ND-Range: The N-dimensional problem space (1D, 2D, or 3D grid) spanning all work-items.",
            "`parallel_for(range<1>(N), [=](id<1> i) {...})`: Launches N work-items across the device."
        ]
    })
    s19.notes_slide.notes_text_frame.text = "Explain the hierarchy on the board: Work-Item -> Work-Group -> ND-Range. It maps directly to GPU threads, thread blocks, and grid."

    # Slide 20: Unified Shared Memory (USM) Architecture
    s20 = prs.slides.add_slide(blank)
    bg = s20.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s20, "Unified Shared Memory (USM) Architecture", "MODULE 01.19 // MEMORY ALLOCATION", "LEAD: SHIVAM GUPTA")
    build_triple_card_slide(s20, [
        {
            "title": "1. `malloc_shared`",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "Accessible by BOTH host CPU and device kernels directly.",
                "Hardware/driver page migration engine moves 4KB pages across PCIe on-demand.",
                "Easiest programming model with standard C++ pointers.",
                "Trade-off: Initial page fault latency on first migration."
            ]
        },
        {
            "title": "2. `malloc_device`",
            "title_color": C_EMERALD,
            "border_color": C_EMERALD,
            "bullets": [
                "Allocates memory strictly in Device High-Bandwidth Memory (HBM/GDDR).",
                "Host CPU CANNOT dereference this pointer directly (triggers segfault).",
                "Zero page-fault latency during kernel execution.",
                "Explicit async copies via `q.memcpy()` for maximum PCIe burst bandwidth."
            ]
        },
        {
            "title": "3. `malloc_host`",
            "title_color": C_AMBER,
            "border_color": C_AMBER,
            "bullets": [
                "Allocates pinned host DRAM memory.",
                "Accessible by host CPU and directly readable by device over PCIe.",
                "No page swapping by OS kernel.",
                "Ideal for staging buffers and streaming real-time sensor data."
            ]
        }
    ])
    s20.notes_slide.notes_text_frame.text = "Emphasize that production HPC uses malloc_device with explicit copies for deterministic latency, while beginner labs start with malloc_shared."

    # Slide 21: Production DPC++ Vector Add Code Walkthrough
    s21 = prs.slides.add_slide(blank)
    bg = s21.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s21, "Production DPC++ Vector Add Walkthrough", "MODULE 01.20 // KERNEL SOURCE", "LEAD: SHIVAM GUPTA")
    build_terminal_code_slide(s21, {
        "title": "Line-by-Line Anatomy of a Complete SYCL / DPC++ Heterogeneous Application",
        "bullets": [
            "Compilation command: `icpx -fsycl -O3 -xHost dpcpp_vector_add.cpp -o dpcpp_vector_add`",
            "Notice the synchronization point: `q.wait()` must be called before reading output on the host."
        ]
    }, {
        "lang": "C++ / SYCL DPC++",
        "code_lines": [
            "#include <sycl/sycl.hpp>",
            "#include <iostream>",
            "",
            "constexpr size_t N = 10000000; // 10 Million elements",
            "",
            "int main() {",
            "    sycl::queue q(sycl::default_selector_v);",
            "    std::cout << \"[*] Device: \" << q.get_device().get_info<sycl::info::device::name>() << \"\\n\";",
            "",
            "    float* a = sycl::malloc_shared<float>(N, q);",
            "    float* b = sycl::malloc_shared<float>(N, q);",
            "    float* c = sycl::malloc_shared<float>(N, q);",
            "",
            "    for (size_t i = 0; i < N; ++i) { a[i] = 1.0f; b[i] = 2.0f; }",
            "",
            "    q.parallel_for(sycl::range<1>(N), [=](sycl::id<1> i) {",
            "        c[i] = a[i] + b[i];",
            "    }).wait(); // Wait for kernel execution to finish!",
            "",
            "    std::cout << \"[+] Result at index 0: \" << c[0] << \" (Expected: 3.0)\\n\";",
            "    sycl::free(a, q); sycl::free(b, q); sycl::free(c, q);",
            "    return 0;",
            "}"
        ]
    })
    s21.notes_slide.notes_text_frame.text = "Walk through the code line-by-line on screen. Point out why the lambda captures by value [=] (pointers are copied into the kernel context)."

    # Slide 22: Hands-On Laboratory Roadmap
    s22 = prs.slides.add_slide(blank)
    bg = s22.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s22, "Hands-On Laboratory Roadmap: Day 1 Labs", "MODULE 01.21 // HANDS-ON WORKSHOP", "JOINT LAB WORKSHOP")
    build_dual_card_slide(s22, {
        "title": "Lab 1: Linux Core Pinning & Performance Counters",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Objective: Verify cache misses and execution jitter under OS scheduling vs core pinning.",
            "Step 1: Write an unpinned multithreaded matrix calculation loop.",
            "Step 2: Profile hardware events using `perf stat -e cache-misses,cycles ./binary`.",
            "Step 3: Pin the workload using `taskset -c 0-3` and observe cache miss reductions.",
            "Deliverable: Record execution time delta and submit terminal log to GLA LMS."
        ]
    }, {
        "title": "Lab 2: SYCL USM Vector Add & Benchmarking",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Objective: Compile and benchmark a heterogeneous DPC++ kernel on 50 Million floats.",
            "Step 1: Initialize SYCL queue with `default_selector_v` and print device properties.",
            "Step 2: Implement USM vector add kernel and benchmark against scalar C++.",
            "Step 3: Modify kernel to compute Vector Triad: C[i] = A[i] + scalar * B[i].",
            "Deliverable: Measure speedup factor (e.g. 23.3x) and upload timing chart."
        ]
    })
    s22.notes_slide.notes_text_frame.text = "Announce that both labs must be completed and terminal screenshots uploaded to the GLA LMS portal for Day 1 lab grading."

    # Slide 23: Classroom Defense & Gotchas Matrix
    s23 = prs.slides.add_slide(blank)
    bg = s23.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s23, "Common Laboratory Errors & 5-Second Fixes", "MODULE 01.22 // TROUBLESHOOTING", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s23, {
        "title": "Top Common Student Errors in Lab",
        "title_color": C_AMBER,
        "border_color": C_AMBER,
        "bullets": [
            "Error 1: `icpx: command not found` or `dpcpp: command not found`.",
            "Error 2: `error: no device available of type default`.",
            "Error 3: Segmentation fault (core dumped) immediately after kernel launch.",
            "Error 4: `fatal error: sycl/sycl.hpp: No such file or directory`."
        ]
    }, {
        "title": "Instant 5-Second Field Solutions",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Fix 1: Source environment variables: `source /opt/intel/oneapi/setvars.sh`.",
            "Fix 2: Set fallback device: `export ONEAPI_DEVICE_SELECTOR=opencl:cpu`.",
            "Fix 3: Student accessed output array before calling `q.wait()`. Ensure synchronization!",
            "Fix 4: Student compiled with standard `g++` instead of `icpx -fsycl`. Use proper oneAPI compiler driver."
        ]
    })
    s23.notes_slide.notes_text_frame.text = "Keep this slide displayed during the hands-on lab block. 95% of student troubleshooting requests are solved by these 4 fixes."

    # Slide 24: LMS Upload Summary & Bibliography
    s24 = prs.slides.add_slide(blank)
    bg = s24.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s24, "LMS Upload Summary & Reference Bibliography", "MODULE 01.23 // COURSE SUMMARY", "JOINT INSTRUCTIONAL MAPPING")
    build_triple_card_slide(s24, [
        {
            "title": "1. Daily LMS Submissions",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "Upload Lab 1 and Lab 2 terminal execution logs before 5:00 PM.",
                "Complete the Day 1 Evaluative Assessment (25 MCQs) on the GLA LMS portal.",
                "Minimum passing score: 70% for daily certification eligibility."
            ]
        },
        {
            "title": "2. Official Reference Reading",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "Intel oneAPI Programming Guide: software.intel.com/oneapi.",
                "Data Parallel C++ (DPC++): Master book by James Reinders et al. (Apress Open Access).",
                "Computer Architecture: A Quantitative Approach (Hennessy & Patterson, 6th Ed.).",
                "Linux Kernel Development (Robert Love, 3rd Ed.)."
            ]
        },
        {
            "title": "3. Tomorrow's Preview (Day 2)",
            "title_color": C_EMERALD,
            "border_color": C_EMERALD,
            "bullets": [
                "Parallel Computing Paradigms: OpenMP shared-memory multi-threading.",
                "The False Sharing Trap on 64-byte cache lines & MESI protocol.",
                "Distributed Memory Programming with MPI (Point-to-Point & Collectives).",
                "Intel oneDAL: 30x Scikit-Learn acceleration with two lines of code!"
            ]
        }
    ])
    s24.notes_slide.notes_text_frame.text = "Concluding remarks for Day 1. Congratulate students on mastering single-node vector hardware and heterogeneous SYCL computing. Prep them for Day 2 parallel scaling."

    # Save Day 1 deck
    out_d1_local = DAY1_DIR / "Day-01_HPC_Linux_Shell_oneAPI_Master_Deck.pptx"
    out_d1_edu = EDULATERAL_DIR / "Day-01_HPC_Foundations_Linux_oneAPI_NotebookLM.pptx"
    out_d1_root = BASE_DIR / "Day-01_HPC_Linux_oneAPI_NotebookLM_LMS.pptx"

    prs.save(out_d1_local)
    shutil.copy(out_d1_local, out_d1_edu)
    shutil.copy(out_d1_local, out_d1_root)
    print(f"[OK] Saved Day 1 Master Deck: {out_d1_local.name}")

def generate_day5_deck():
    print("[*] Generating NotebookLM Master Presentation for Day 5...")
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank = prs.slide_layouts[6]

    # Slide 1: Cover
    build_cover_slide(prs, 5, "Generative AI, LLMs on Intel HPC, Gaudi & OpenVINO", "Transformer Attention Physics, Memory Bandwidth Limits, KV-Cache Math, Gaudi Networking & INT8 Quantization")

    # Slide 2: Day 5 Charter & LMS Syllabus Mapping
    s2 = prs.slides.add_slide(blank)
    bg = s2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s2, "Day 5 Charter & LMS Syllabus Mapping", "MODULE 05.01 // ACADEMIC GOVERNANCE", "JOINT INSTRUCTIONAL MAPPING")
    build_dual_card_slide(s2, {
        "title": "GLA University Day 5 Capstone Charter",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Program: B.Tech Computer Science & Engineering (7th Semester).",
            "Focus: Generative AI, Large Language Models (LLMs), and Edge/Data Center Deployment.",
            "LMS Module: GLA-HPC-DAY05 // Grand Finale & Enterprise Capstone.",
            "Core Competencies: Transformer silicon physics, KV-cache memory math, Intel Gaudi HPUs, and OpenVINO quantization.",
            "Final Evaluation: 25 Master MCQs + Production FastAPI Customer Support Bot Deployment."
        ]
    }, {
        "title": "Intel AI & Edulateral Compliance",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Authorized Technical Alignment: Intel AI Acceleration Architecture & Habana Gaudi.",
            "Industry Relevance: Moving beyond naive API wrappers to high-performance inference engine engineering.",
            "Zero Placeholder Mandate: Complete end-to-end runnable code for OpenVINO and FastAPI microservices.",
            "Offline Self-Containment: Synthetic test datasets, quantized models, and standalone evaluation app.",
            "Course Completion: Eligibility for Edulateral-Intel HPC Course Completion Certificate."
        ]
    })
    s2.notes_slide.notes_text_frame.text = "Introduce Day 5 as the grand culmination of the 5-day training. Connect everything learned about memory, vectorization, and clusters to the generative AI revolution."

    # Slide 3: Trainer Division Matrix (Addressing Rajat's prompt)
    s3 = prs.slides.add_slide(blank)
    bg = s3.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s3, "Instructional Division & Trainer Matrix", "MODULE 05.02 // PODIUM RESPONSIBILITIES", "OFFICIAL TOPIC SPLIT")
    build_dual_card_slide(s3, {
        "title": "Shivam Gupta (~SEED~) — Lead Systems & AI Trainer",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Attention Silicon Physics: Scaled Dot-Product math, Prefill vs Decode execution regimes.",
            "The Memory Wall in GenAI: Memory bandwidth limits, KV-Cache memory formula derivations.",
            "Intel Gaudi Architecture: MME matrix engines, TPC vector cores, on-die 24x 100GbE networking.",
            "Intel OpenVINO Optimization: Model Optimizer, NNCF PTQ vs QAT, INT8/INT4 weight compression.",
            "Production Serving: High-throughput async FastAPI microservice architecture with token streaming."
        ]
    }, {
        "title": "Rajat Garg (Ramāpriya Das) — Academic & Channel Lead",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Market & Economic Landscape: Enterprise Total Cost of Ownership (TCO) — Intel Gaudi vs NVIDIA H100.",
            "Industry Applications: Real-world enterprise deployment architectures in finance, healthcare, and education.",
            "Capstone Project Evaluation: Reviewing student FastAPI chatbot endpoints and scoring rubrics.",
            "LMS Final Certification: Verifying student cumulative 5-day assessment logs and course wrap-up.",
            "Post-Workshop Roadmap: Guiding students on Intel Certified Developer & AI Systems careers."
        ]
    })
    s3.notes_slide.notes_text_frame.text = "Explicitly states the podium division for Day 5. Shivam drives the deep mathematical and code systems engineering, while Rajat anchors the economic and certification elements."

    # Slide 4: Generative AI Revolution & HPC Demands
    s4 = prs.slides.add_slide(blank)
    bg = s4.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s4, "The Generative AI Revolution & HPC Demands", "MODULE 05.03 // THE COMPUTE EXPONENT", "LEAD: SHIVAM GUPTA")
    build_triple_card_slide(s4, [
        {
            "title": "1. Exponential Compute Scaling",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "LLM compute demand grew 10x per year since 2018 (far outstripping Moore's Law).",
                "GPT-4 required an estimated 2.1 x 10²⁵ FLOPs over 25,000 GPUs.",
                "Llama-3 70B required ~15 million GPU hours of training compute.",
                "AI is no longer computer science theory; AI is massive-scale industrial HPC engineering."
            ]
        },
        {
            "title": "2. Training vs Inference Clusters",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "Training: Long-running batch compute. Massive backward pass gradients synchronized via Ring-AllReduce.",
                "Inference: Real-time latency-critical serving. User requests arrive dynamically with strict SLAs (<50 ms time-to-first-token).",
                "Over 85% of global data center AI budgets are spent on INFERENCE at runtime!"
            ]
        },
        {
            "title": "3. The Data Center Power Crisis",
            "title_color": C_AMBER,
            "border_color": C_AMBER,
            "bullets": [
                "An 8-GPU NVIDIA H100 server consumes over 10.2 Kilowatts of continuous power.",
                "AI data centers are constrained by grid electrical capacity, not rack space.",
                "Efficiency Mandate: Model compression and CPU inference optimization (OpenVINO) are essential to survive."
            ]
        }
    ])
    s4.notes_slide.notes_text_frame.text = "Set the stage for why optimization matters. Companies cannot afford to deploy unoptimized models; electrical power and hardware costs force architectural efficiency."

    # Slide 5: Transformer Decoder-Only Architecture
    s5 = prs.slides.add_slide(blank)
    bg = s5.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s5, "The Transformer Decoder-Only Architecture", "MODULE 05.04 // MODEL ANATOMY", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s5, {
        "title": "Structural Block Breakdown",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Input Tokenizer: Maps raw text strings into discrete integer tokens from vocabulary V (~32k to 128k).",
            "Token & Positional Embedding: Maps tokens into dense dimension d_model (e.g. 4096) with Rotary Position Embeddings (RoPE).",
            "Stacked Transformer Layers (e.g. 32 layers in 7B, 80 layers in 70B):",
            "1. RMSNorm (Root Mean Square Normalization).",
            "2. Multi-Head / Grouped-Query Attention (MHA/GQA).",
            "3. Residual Skip Connection (x + Attention(x)).",
            "4. Feed-Forward Network: SwiGLU gated activation layer (maps d_model to 3.5x d_model).",
            "Output Linear Head: Unembeds hidden states back to vocabulary logits for softmax sampling."
        ]
    }, {
        "title": "Computational Characterization",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Over 98% of the mathematical operations in a transformer are General Matrix Multiplications (GEMM).",
            "Attention QKᵀ: Matrix multiplication of Query by Key.",
            "Attention Softmax(.)V: Matrix multiplication of Attention weights by Value.",
            "Linear Projection Layers (W_q, W_k, W_v, W_o): Dense matrix multiplications.",
            "Feed-Forward Gated Projections (W_gate, W_up, W_down): Giant matrix multiplications.",
            "Silicon Takeaway: Accelerating transformers is 100% about maximizing GEMM throughput and memory bandwidth!"
        ]
    })
    s5.notes_slide.notes_text_frame.text = "Walk through the transformer block. Emphasize that transformers are conceptually simple: alternating matrix multiplications and normalization layers."

    # Slide 6: Scaled Dot-Product Attention Mechanics
    s6 = prs.slides.add_slide(blank)
    bg = s6.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s6, "Scaled Dot-Product Attention Mechanics", "MODULE 05.05 // ATTENTION MATH", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s6, {
        "title": "Mathematical Formulation",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Formula: Attention(Q, K, V) = softmax( (Q Kᵀ) / √d_k ) V",
            "Query (Q): What the current token is looking for.",
            "Key (K): What previous tokens contain.",
            "Value (V): The actual informational payload.",
            "Scale Factor 1/√d_k: Prevents the dot products from growing excessively large, which pushes softmax into regions with vanishing gradients."
        ]
    }, {
        "title": "Complexity & Memory Bottleneck",
        "title_color": C_AMBER,
        "border_color": C_AMBER,
        "bullets": [
            "Computational Complexity: O(L² · d) where L is sequence length.",
            "As context length expands (e.g. from 2,048 to 128,000 tokens), attention compute explodes quadratically!",
            "At 128k context, Q Kᵀ generates a 128,000 x 128,000 matrix per head per layer.",
            "FlashAttention Innovation: Tiles the Q Kᵀ matrix in SRAM cache to avoid writing intermediate attention matrices to DRAM.",
            "Without SRAM tiling, attention crashes GPU memory instantly at long contexts."
        ]
    })
    s6.notes_slide.notes_text_frame.text = "Write the attention equation on the board. Explain why quadratic complexity O(L^2) makes long-context LLMs a massive HPC challenge."

    # Slide 7: MHA vs MQA vs GQA (Attention Evolution)
    s7 = prs.slides.add_slide(blank)
    bg = s7.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s7, "Attention Evolution: MHA vs MQA vs GQA", "MODULE 05.06 // HEAD OPTIMIZATION", "LEAD: SHIVAM GUPTA")
    build_triple_card_slide(s7, [
        {
            "title": "1. Multi-Head Attention (MHA)",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "Original Transformer & Llama-1.",
                "Equal number of Query, Key, and Value heads (e.g. 32 Q, 32 K, 32 V).",
                "Full expressive representation.",
                "Severe Bottleneck: Massive KV-Cache memory consumption during inference."
            ]
        },
        {
            "title": "2. Multi-Query Attention (MQA)",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "Extreme memory compression (e.g. Falcon).",
                "32 Query heads share ONE single Key head and ONE single Value head.",
                "Reduces KV-cache memory traffic by 32x!",
                "Trade-off: Noticeable degradation in reasoning and accuracy on complex tasks."
            ]
        },
        {
            "title": "3. Grouped-Query Attention (GQA)",
            "title_color": C_EMERALD,
            "border_color": C_EMERALD,
            "bullets": [
                "The Modern Industry Standard (Llama-2 70B, Llama-3, Mistral 7B).",
                "Groups Query heads to share Key/Value heads (e.g. 32 Q heads split into 8 groups of 4).",
                "Only 8 Key and 8 Value heads in memory!",
                "Achieves 4x KV-cache memory reduction with ZERO loss in model quality."
            ]
        }
    ])
    s7.notes_slide.notes_text_frame.text = "Highlight that Grouped-Query Attention was created specifically by HPC systems engineers to solve the inference memory bottleneck."

    # Slide 8: The Two Faces of LLM Inference: Prefill vs Decode
    s8 = prs.slides.add_slide(blank)
    bg = s8.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s8, "The Two Faces of Inference: Prefill vs Decode", "MODULE 05.07 // INFERENCE PHASES", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s8, {
        "title": "Phase 1: Prefill (Prompt Processing)",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Input: User sends a prompt with 500 tokens.",
            "Execution: All 500 tokens are processed simultaneously in parallel.",
            "Matrix Operation: Dense GEMM (General Matrix-Matrix Multiply).",
            "Arithmetic Character: Strictly COMPUTE-BOUND.",
            "Hardware State: Compute units (AMX / Tensor Cores) saturated at 95%+ utilization.",
            "Metric: Time-To-First-Token (TTFT)."
        ]
    }, {
        "title": "Phase 2: Decode (Autoregressive Generation)",
        "title_color": C_AMBER,
        "border_color": C_AMBER,
        "bullets": [
            "Input: Generates ONE token at a time sequentially (x_t+1 = Model(x_t)).",
            "Execution: For each single token, EVERY weight of the model must be loaded from RAM into registers!",
            "Matrix Operation: GEMV (General Matrix-Vector Multiply).",
            "Arithmetic Character: Strictly MEMORY-BANDWIDTH BOUND.",
            "Hardware State: Compute units sit 90% idle waiting for DDR5/HBM memory bus transfers.",
            "Metric: Inter-Token Latency (ITL / Tokens per second)."
        ]
    })
    s8.notes_slide.notes_text_frame.text = "Contrast Prefill vs Decode clearly. Explain why reading 14 GB of weights across the bus to generate a single word makes the decode phase memory-bound."

    # Slide 9: The Memory Wall of Generative AI
    s9 = prs.slides.add_slide(blank)
    bg = s9.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s9, "The Memory Wall of Generative AI", "MODULE 05.08 // BANDWIDTH LIMITS", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s9, {
        "title": "The Physics of Single-Token Generation",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Consider a 7-Billion parameter LLM in FP16 precision (14 Gigabytes of weights).",
            "To generate ONE token, the hardware MUST stream all 14 GB from memory into execution registers.",
            "Theoretical Peak Generation Speed = Memory Bandwidth / Model Size in Bytes.",
            "Standard Laptop (DDR5 @ 50 GB/s): Max speed = 50 / 14 = 3.5 tokens/sec.",
            "Enterprise Server (8-Channel DDR5 @ 250 GB/s): Max speed = 250 / 14 = 17.8 tokens/sec.",
            "High-End GPU (HBM3 @ 2,000 GB/s): Max speed = 2000 / 14 = 142 tokens/sec."
        ]
    }, {
        "title": "Why Quantization Breaks the Bottleneck",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Notice: Generation speed is directly bounded by the denominator (Model Size in Bytes)!",
            "If we quantize the 7B model from FP16 (14 GB) to INT4 (3.5 GB):",
            "The memory bus only transfers 3.5 GB per token instead of 14 GB!",
            "Speed on Enterprise Server jumps from 17.8 tokens/sec to 250 / 3.5 = 71.4 tokens/sec!",
            "A pure 4x speedup achieved with ZERO hardware changes purely through silicon memory reduction."
        ]
    })
    s9.notes_slide.notes_text_frame.text = "Demonstrate the mathematical formula for generation speed. Show students that quantization is not just about saving disk space; it directly multiplies generation speed."

    # Slide 10: The KV-Cache Mathematical Formulation
    s10 = prs.slides.add_slide(blank)
    bg = s10.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s10, "The KV-Cache Mathematical Formulation", "MODULE 05.09 // MEMORY SIZING", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s10, {
        "title": "Exact Mathematical Derivation",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Formula: Bytes = 2 x 2 x n_layers x n_heads x d_head x L_seq x Batch x Bytes_per_element",
            "Factor 2: One for Keys (K), one for Values (V).",
            "Factor 2: 16-bit precision (2 bytes for FP16/BF16).",
            "For Llama-3 8B (32 layers, 32 heads, d_head = 128, FP16):",
            "Bytes/token = 2 x 2 x 32 x 32 x 128 x 2 = 524,288 bytes = 0.524 MB per token!",
            "At sequence length L = 4,096 tokens: 4096 x 0.524 MB = 2.15 GB per user request!"
        ]
    }, {
        "title": "Concurrent Production Serving Sizing",
        "title_color": C_AMBER,
        "border_color": C_AMBER,
        "bullets": [
            "Single User (Batch = 1): KV-Cache = 2.15 GB.",
            "16 Concurrent Users (Batch = 16): KV-Cache = 34.4 GB!",
            "64 Concurrent Users (Batch = 64): KV-Cache = 137.6 GB!",
            "The Shocking Reality: At high concurrency, the KV-Cache memory consumption DWARFS the 14 GB model weights!",
            "Without efficient KV-cache memory management, serving servers crash with Out-Of-Memory (OOM) errors."
        ]
    })
    s10.notes_slide.notes_text_frame.text = "Write the KV-cache sizing numbers on the whiteboard. Highlight why 64 concurrent users require 137 GB of memory just for the cache."

    # Slide 11: PagedAttention & vLLM Architecture
    s11 = prs.slides.add_slide(blank)
    bg = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s11, "Virtual Memory for LLMs: PagedAttention", "MODULE 05.10 // MEMORY PAGING", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s11, {
        "title": "Traditional Contiguous Memory Allocation",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Pre-allocates contiguous memory blocks for maximum potential context length (e.g. 4,096 tokens).",
            "Internal Fragmentation: A request only uses 200 tokens, but 4,096 tokens were reserved. 95% of memory wasted!",
            "External Fragmentation: Dynamically allocated buffers leave unusable memory holes across RAM.",
            "Serving systems routinely waste 60% to 80% of their memory capacity."
        ]
    }, {
        "title": "The PagedAttention Innovation (vLLM)",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Inspired by classic Operating System Virtual Memory Paging.",
            "Divides the KV-cache into fixed-size physical blocks / pages (e.g. 16 tokens per block).",
            "Physical memory blocks are allocated dynamically on-demand as tokens generate.",
            "Virtual-to-Physical Block Table maps logical token sequences to non-contiguous physical RAM.",
            "Memory waste drops below 4%! Allows serving systems to handle 2x to 4x higher concurrency on identical hardware."
        ]
    })
    s11.notes_slide.notes_text_frame.text = "Explain that PagedAttention is not new math; it is classic OS virtual memory paging applied brilliantly to transformer KV states."

    # Slide 12: Specialized AI Silicon: Intel Gaudi 2 & 3
    s12 = prs.slides.add_slide(blank)
    bg = s12.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s12, "Specialized AI Silicon: Intel Gaudi Architecture", "MODULE 05.11 // HPU HARDWARE", "LEAD: SHIVAM GUPTA")
    build_triple_card_slide(s12, [
        {
            "title": "1. Matrix Math Engine (MME)",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "Purpose-built hardware systolic arrays.",
                "Executes dense GEMM and convolution tensor operations.",
                "Native hardware support for FP8, BF16, and FP16 formats.",
                "Zero legacy graphics circuitry (no ray tracing, no display ports)."
            ]
        },
        {
            "title": "2. Tensor Processing Cores (TPC)",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "Custom VLIW (Very Long Instruction Word) SIMD vector cores.",
                "Fully programmable by software engineers using C++ kernels.",
                "Executes activation functions (GELU, Swish), normalization (RMSNorm), and custom loss functions.",
                "High-bandwidth internal SRAM scratchpad."
            ]
        },
        {
            "title": "3. Integrated High-Speed Memory",
            "title_color": C_EMERALD,
            "border_color": C_EMERALD,
            "bullets": [
                "Gaudi 2: 96 GB HBM2e memory delivering 2.45 TB/sec bandwidth.",
                "Gaudi 3: 128 GB HBM3 memory delivering 3.7 TB/sec bandwidth.",
                "Massive capacity allows hosting 70B parameter models on a single chip without pipeline splitting."
            ]
        }
    ])
    s12.notes_slide.notes_text_frame.text = "Introduce the Heterogeneous Processing Unit (HPU) architecture. Contrast general-purpose GPUs with dedicated deep learning accelerators."

    # Slide 13: Intel Gaudi Integrated On-Die Networking
    s13 = prs.slides.add_slide(blank)
    bg = s13.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s13, "Intel Gaudi Integrated On-Die Networking", "MODULE 05.12 // ROBUST CLUSTER FABRIC", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s13, {
        "title": "The Industry Standard: NVIDIA GPU Networking",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "NVIDIA H100 GPU requires separate Mellanox ConnectX-7 NIC PCIe cards.",
            "Communication traverses GPU -> PCIe Gen5 bus -> Host CPU PCIe Root Complex -> NIC -> Switch.",
            "Requires expensive proprietary NVLink switches ($$$) for intra-chassis communication.",
            "High packaging complexity, power consumption, and massive hardware component costs."
        ]
    }, {
        "title": "The Intel Gaudi Innovation: 24x 100GbE On-Die",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Intel Gaudi integrates 24 ports of 100GbE (Gigabit Ethernet) DIRECTLY ON THE SILICON DIE!",
            "Native RoCE v2 (RDMA over Converged Ethernet) with sub-microsecond latency.",
            "Gaudi chips plug directly into each other across standard enterprise optical cables.",
            "Zero host PCIe bottlenecks. No proprietary switch hardware required.",
            "Enables effortless scaling from 8-chip servers to 1,024-chip supercomputing clusters at 50% lower networking cost."
        ]
    })
    s13.notes_slide.notes_text_frame.text = "This is Intel Gaudi's crown jewel. On-die 24x 100GbE RoCE v2 eliminates proprietary switch hardware and cuts cluster costs in half."

    # Slide 14: Intel Gaudi vs NVIDIA H100 Comparison
    s14 = prs.slides.add_slide(blank)
    bg = s14.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s14, "Intel Gaudi vs NVIDIA H100 Comparison", "MODULE 05.13 // ARCHITECTURAL BENCHMARKS", "CO-LEAD: RAJAT GARG")
    build_dual_card_slide(s14, {
        "title": "Architectural Specification Comparison",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Hardware Parameter | NVIDIA H100 SXM5 | Intel Gaudi 3",
            "Process Node | TSMC 4N (5nm) | TSMC 5nm",
            "Memory Capacity | 80 GB HBM3 | 128 GB HBM3 (+60% larger)",
            "Memory Bandwidth | 3.35 TB/s | 3.70 TB/s",
            "Networking | 8x 400G PCIe ConnectX-7 | 24x 200GbE Integrated On-Die",
            "Software Stack | Proprietary CUDA | Open PyTorch / Habanalabs SynapseAI"
        ]
    }, {
        "title": "Total Cost of Ownership (TCO) & Economics",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "NVIDIA H100 Server Cost: ~$250,000 to $300,000 with 6-month delivery backlogs.",
            "Intel Gaudi 2/3 Server Cost: Estimated 1/3rd to 1/2 the acquisition cost of H100.",
            "Llama-2 / Llama-3 Benchmarks: Gaudi delivers near-parity throughput on training and superior price-to-performance on inference.",
            "Enterprise Decision: Gaudi allows enterprises to build twice as large AI clusters within identical IT capital expenditure budgets."
        ]
    })
    s14.notes_slide.notes_text_frame.text = "Rajat Garg takes lead on this slide to discuss corporate TCO, procurement economics, and why major cloud providers (AWS, Intel Developer Cloud) deploy Gaudi."

    # Slide 15: Model Compression & Quantization Paradigms
    s15 = prs.slides.add_slide(blank)
    bg = s15.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s15, "Model Compression & Quantization Paradigms", "MODULE 05.14 // NUMERICAL PRECISION", "LEAD: SHIVAM GUPTA")
    build_triple_card_slide(s15, [
        {
            "title": "1. FP32 & BF16 Precision",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "FP32: 32 bits (4 bytes) | 7B model = 28 GB.",
                "BF16: 16 bits (2 bytes) | 7B model = 14 GB.",
                "Standard training precision.",
                "Massive memory bus footprint during edge deployment."
            ]
        },
        {
            "title": "2. INT8 Quantization",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "INT8: 8 bits (1 byte) | 7B model = 7 GB.",
                "50% memory traffic reduction.",
                "Leverages hardware INT8 VNNI / AMX vector instructions.",
                "Zero perceptual loss in response quality (<0.5% perplexity delta)."
            ]
        },
        {
            "title": "3. INT4 Weight Compression",
            "title_color": C_EMERALD,
            "border_color": C_EMERALD,
            "bullets": [
                "INT4: 4 bits (0.5 bytes) | 7B model = 3.5 GB!",
                "Extreme 4x compression.",
                "Fits full 7B parameter LLMs into edge laptops and small CPU servers.",
                "25+ tokens/second on standard Intel Core/Xeon CPUs."
            ]
        }
    ])
    s15.notes_slide.notes_text_frame.text = "Show the visual reduction in memory size from 28 GB down to 3.5 GB. Explain how integer representation maps to hardware registers."

    # Slide 16: Quantization Mathematics: Affine Scaling
    s16 = prs.slides.add_slide(blank)
    bg = s16.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s16, "Quantization Mathematics: Scale & Zero-Point", "MODULE 05.15 // MATHEMATICAL FOUNDATIONS", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s16, {
        "title": "Affine (Asymmetric) Quantization Equations",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Quantization Formula: q = clamp( round(x / S) + Z, q_min, q_max )",
            "Scale Factor (S): S = (x_max - x_min) / (q_max - q_min)",
            "Zero-Point (Z): Z = round(-x_min / S) + q_min",
            "Dequantization Formula: x_approx = S * (q - Z)",
            "Symmetric Quantization (Z = 0): Range is symmetric [-M, M]. Faster on hardware because Z subtraction is eliminated."
        ]
    }, {
        "title": "Hardware Dot-Product Acceleration",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "When multiplying two INT8 matrices, the CPU uses `VPDPBUSD` (AVX-512 VNNI).",
            "Computes thirty-two 8-bit integer multiplications and accumulates into 32-bit integer in ONE cycle!",
            "Intel AMX systolic tile engine: Computes 2,048 INT8 operations per cycle per core!",
            "Result: 4x faster matrix multiplication throughput compared to FP32, using 75% less memory bus bandwidth."
        ]
    })
    s16.notes_slide.notes_text_frame.text = "Break down the Scale (S) and Zero-Point (Z) formulas on the whiteboard. Explain why asymmetric quantization preserves accuracy on skewed ReLU/GELU activations."

    # Slide 17: Post-Training Quantization (PTQ) vs QAT
    s17 = prs.slides.add_slide(blank)
    bg = s17.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s17, "PTQ vs Quantization-Aware Training (QAT)", "MODULE 05.16 // CALIBRATION ALGORITHMS", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s17, {
        "title": "Post-Training Quantization (PTQ)",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Workflow: Takes an already trained FP32 model and a small calibration dataset (~100-300 samples).",
            "Calibration: Passes data through the model to record activation distributions and outliers.",
            "Optimization: Calculates optimal S and Z using KL-Divergence or Mean Squared Error (MSE) minimization.",
            "Pros: Extremely fast (takes 5-15 minutes), requires zero model retraining or GPUs.",
            "Cons: Potential 1-2% accuracy drop on highly sensitive attention layers."
        ]
    }, {
        "title": "Quantization-Aware Training (QAT)",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Workflow: Inserts 'FakeQuantize' nodes into the PyTorch compute graph during fine-tuning.",
            "Forward Pass: Clamps weights and activations to 8-bit precision.",
            "Backward Pass: Computes gradients in full FP32 using the Straight-Through Estimator (STE).",
            "Optimization: Weights learn to adjust and compensate for quantization noise dynamically.",
            "Pros: Near 100% recovery of original baseline accuracy.",
            "Cons: Requires compute time, training pipelines, and labeled datasets."
        ]
    })
    s17.notes_slide.notes_text_frame.text = "Explain that PTQ via OpenVINO NNCF is standard for enterprise deployment because it takes minutes rather than weeks of retraining."

    # Slide 18: Intel OpenVINO Toolkit Architecture
    s18 = prs.slides.add_slide(blank)
    bg = s18.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s18, "The Intel OpenVINO Toolkit Architecture", "MODULE 05.17 // OPTIMIZATION ENGINE", "LEAD: SHIVAM GUPTA")
    build_triple_card_slide(s18, [
        {
            "title": "1. Model Optimizer & Graph Conversion",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "Imports PyTorch, ONNX, and TensorFlow models.",
                "Fuses adjacent operations (Linear + Bias + ReLU).",
                "Prunes redundant identity nodes and dead graph branches.",
                "Exports to OpenVINO Intermediate Representation (IR): `.xml` (topology) and `.bin` (weights)."
            ]
        },
        {
            "title": "2. NNCF Compression Framework",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "Neural Network Compression Framework (NNCF).",
                "Automates 8-bit and 4-bit weight compression.",
                "Advanced data-free and calibration-based quantization.",
                "SmoothQuant and AWQ (Activation-Aware Weight Quantization) support."
            ]
        },
        {
            "title": "3. OpenVINO High-Speed Runtime",
            "title_color": C_EMERALD,
            "border_color": C_EMERALD,
            "bullets": [
                "Lightweight C++ inference engine with zero heavy framework overhead.",
                "Dynamic multi-threading via Intel TBB (Threading Building Blocks).",
                "Automatic hardware dispatch to Intel CPUs, Arc GPUs, and NPUs.",
                "Asynchronous multi-stream execution queues."
            ]
        }
    ])
    s18.notes_slide.notes_text_frame.text = "Explain the three-stage OpenVINO pipeline: Convert -> Compress (NNCF) -> Execute (Runtime)."

    # Slide 19: Intel Xeon AMX & VNNI Acceleration
    s19 = prs.slides.add_slide(blank)
    bg = s19.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s19, "Intel Xeon AMX & VNNI Hardware Acceleration", "MODULE 05.18 // SILICON MATRIX TILES", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s19, {
        "title": "Intel AMX (Advanced Matrix Extensions)",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "Introduced in 4th & 5th Gen Intel Xeon Scalable (Sapphire Rapids / Emerald Rapids).",
            "Dedicated 2D hardware matrix coprocessor built directly into each CPU core.",
            "8 Two-Dimensional Tile Registers (TMM0 - TMM7), each holding 1 KB of matrix data.",
            "Tile Matrix Multiply Unit (TMUL): Computes 16x64 multiplied by 64x16 matrix blocks.",
            "Throughput: Computes 2,048 INT8 operations or 1,024 BF16 operations per cycle per core!"
        ]
    }, {
        "title": "AVX-512 VNNI (Vector Neural Network Instructions)",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Supported across modern Intel Xeon and Core client processors.",
            "Fused INT8 Dot-Product instruction: VPDPBUSD.",
            "Replaces 3 separate instructions (load, multiply, accumulate) with 1 single instruction.",
            "Delivers 3x to 5x higher inference throughput compared to standard FP32 math.",
            "Enables enterprises to run production LLM inference on existing CPU server infrastructure."
        ]
    })
    s19.notes_slide.notes_text_frame.text = "Show how Intel AMX brings GPU-style tensor systolic arrays directly into the CPU die, delivering 2,048 operations per clock cycle."

    # Slide 20: Production LLM Serving Architecture
    s20 = prs.slides.add_slide(blank)
    bg = s20.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s20, "Production LLM Serving: FastAPI Microservices", "MODULE 05.19 // ASYNC SERVING", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s20, {
        "title": "Asynchronous Event-Driven Serving Pipeline",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "FastAPI + Uvicorn ASGI Server: Non-blocking asynchronous event loop handling 1,000+ concurrent requests.",
            "OpenVINO Async Infer Request: Offloads token generation to background threads, freeing the Python GIL.",
            "Continuous Batching: Groups incoming requests dynamically into the current forward pass.",
            "Token Streaming: Server-Sent Events (SSE) or WebSockets stream generated tokens in real time."
        ]
    }, {
        "title": "Production Deployment Telemetry",
        "title_color": C_INDIGO,
        "border_color": C_INDIGO,
        "bullets": [
            "Health Check Endpoint (`GET /healthz`): Reports memory footprint and inference queue depth.",
            "Metrics Endpoint (`GET /metrics`): Prometheus counters for latency, throughput, and error rates.",
            "Worker Management: Multi-process Uvicorn workers pinned to distinct NUMA sockets via `taskset`.",
            "Zero Cloud Lock-in: Runs on bare-metal enterprise servers or Docker containers."
        ]
    })
    s20.notes_slide.notes_text_frame.text = "Explain the difference between toy Jupyter notebook inference and production microservice architecture."

    # Slide 21: Code Walkthrough: OpenVINO INT8 Pipeline
    s21 = prs.slides.add_slide(blank)
    bg = s21.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s21, "Code Walkthrough: Production OpenVINO Pipeline", "MODULE 05.20 // EXECUTABLE CODE", "LEAD: SHIVAM GUPTA")
    build_terminal_code_slide(s21, {
        "title": "Compiling, Quantizing, and Executing an OpenVINO Model in Python",
        "bullets": [
            "Notice line 8: Compiling with `PERFORMANCE_HINT: THROUGHPUT` automatically instantiates optimal thread pools.",
            "Benchmark result: 5.2x latency speedup and 75% memory footprint reduction on CPU."
        ]
    }, {
        "lang": "PYTHON // OPENVINO & FASTAPI",
        "code_lines": [
            "import openvino as ov",
            "from openvino.runtime import Core",
            "",
            "core = Core() # Initialize OpenVINO runtime",
            "model = core.read_model(model=\"model.xml\") # Read Intermediate Representation",
            "",
            "# Compile model for CPU with throughput optimization hint",
            "compiled_model = core.compile_model(model, \"CPU\", {\"PERFORMANCE_HINT\": \"THROUGHPUT\"})",
            "infer_request = compiled_model.create_infer_request()",
            "",
            "# Run asynchronous inference",
            "infer_request.start_async(inputs={\"input_ids\": input_tensor})",
            "infer_request.wait() # Await hardware completion",
            "output_tensor = infer_request.get_output_tensor()",
            "print(\"[+] Generated token logits shape:\", output_tensor.data.shape)"
        ]
    })
    s21.notes_slide.notes_text_frame.text = "Walk through the code on screen. Show how OpenVINO compile_model automatically configures multi-threading across CPU cores."

    # Slide 22: Hands-On Capstone Project: Support Chatbot
    s22 = prs.slides.add_slide(blank)
    bg = s22.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s22, "Capstone: AI Customer Support Bot Deployment", "MODULE 05.21 // CAPSTONE WORKSHOP", "JOINT LAB WORKSHOP")
    build_dual_card_slide(s22, {
        "title": "Capstone Project Specifications",
        "title_color": C_CYAN,
        "border_color": C_BORDER_ACTIVE,
        "bullets": [
            "File: `HPC_Master_Curriculum/Day-05_GenAI_LLMs_Gaudi_OpenVINO/live_demo/llm_fastapi_server.py`",
            "Objective: Deploy an enterprise customer support bot service answering GLA University inquiries.",
            "Features: NLP intent recognition, TF-IDF vectorization, confidence thresholding, and fallback routing.",
            "Concurrency Test: Run 50 simultaneous client requests using `locust` or multi-threaded `curl` script.",
            "Evaluation Criteria: Zero 500 errors, sub-20ms response latency, clean JSON responses."
        ]
    }, {
        "title": "Student Execution Steps",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Step 1: Launch FastAPI server: `python llm_fastapi_server.py` on port 8000.",
            "Step 2: Send test query via Swagger UI (`http://127.0.0.1:8000/docs`).",
            "Step 3: Test fallback trigger: Submit an out-of-domain prompt and verify graceful fallback.",
            "Step 4: Measure inference throughput in requests per second.",
            "Step 5: Export terminal benchmark log and upload to GLA LMS for final capstone grading."
        ]
    })
    s22.notes_slide.notes_text_frame.text = "Instruct all students to launch their FastAPI servers. Walk around the room verifying that every student has an active local endpoint."

    # Slide 23: Classroom Defense & Troubleshooting Matrix
    s23 = prs.slides.add_slide(blank)
    bg = s23.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s23, "Common Laboratory Errors & 5-Second Fixes", "MODULE 05.22 // TROUBLESHOOTING", "LEAD: SHIVAM GUPTA")
    build_dual_card_slide(s23, {
        "title": "Top Common Student Errors in GenAI Lab",
        "title_color": C_AMBER,
        "border_color": C_AMBER,
        "bullets": [
            "Error 1: `ImportError: No module named 'openvino'`.",
            "Error 2: `RuntimeError: Dynamic shapes are not supported for this hardware target`.",
            "Error 3: Out-Of-Memory (OOM) during batch inference on workstation.",
            "Error 4: FastAPI server hangs when multiple client requests arrive."
        ]
    }, {
        "title": "Instant 5-Second Field Solutions",
        "title_color": C_EMERALD,
        "border_color": C_EMERALD,
        "bullets": [
            "Fix 1: Activate environment: `pip install openvino nncf optimum`.",
            "Fix 2: Reshape model with static bounds: `model.reshape({'input_ids': [1, 128]})`.",
            "Fix 3: Reduce batch size or enable INT8 quantization via OpenVINO NNCF.",
            "Fix 4: Student used synchronous blocking function inside `async def`. Use threadpool executor or asynchronous infer requests."
        ]
    })
    s23.notes_slide.notes_text_frame.text = "Display this slide during the afternoon capstone session. Solves all common student gotchas immediately."

    # Slide 24: Course Conclusion & Certification
    s24 = prs.slides.add_slide(blank)
    bg = s24.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg.fill.solid(); bg.fill.fore_color.rgb = C_BG; bg.line.fill.background()
    add_notebooklm_header(s24, "Course Conclusion & Official Certification", "MODULE 05.23 // VALEDICTORY", "JOINT INSTRUCTIONAL MAPPING")
    build_triple_card_slide(s24, [
        {
            "title": "1. Final LMS Submissions",
            "title_color": C_CYAN,
            "border_color": C_BORDER_ACTIVE,
            "bullets": [
                "Submit Capstone FastAPI execution logs to GLA LMS.",
                "Complete the Day 5 Evaluative Assessment (25 MCQs).",
                "Faculty confirmation of lab assignment completion."
            ]
        },
        {
            "title": "2. Certification Criteria",
            "title_color": C_INDIGO,
            "border_color": C_INDIGO,
            "bullets": [
                "Official Certificate: Issued by Edulateral Foundation & Intel Unnati.",
                "Criteria: 80%+ cumulative attendance across all 5 days.",
                "Minimum 70% average score across daily MCQ assessments.",
                "Successful submission of all laboratory benchmarks."
            ]
        },
        {
            "title": "3. The Systems Engineer Mindset",
            "title_color": C_EMERALD,
            "border_color": C_EMERALD,
            "bullets": [
                "You now understand computing from silicon registers to distributed clusters.",
                "You do not write code and hope it runs fast; you engineer performance.",
                "Welcome to the elite community of High Performance Systems Architects.",
                "Congratulations on graduating the GLA HPC Master Class!"
            ]
        }
    ])
    s24.notes_slide.notes_text_frame.text = "Deliver the valedictory address. Praise students for completing an intensive, rigorous 5-day curriculum. Close with an inspiring message about engineering excellence."

    # Save Day 5 deck
    out_d5_local = DAY5_DIR / "Day-05_GenAI_LLMs_Gaudi_OpenVINO_Master_Deck.pptx"
    out_d5_edu = EDULATERAL_DIR / "Day-05_GenAI_LLMs_OpenVINO_Gaudi_NotebookLM.pptx"
    out_d5_root = BASE_DIR / "Day-05_GenAI_LLMs_Gaudi_OpenVINO_NotebookLM_LMS.pptx"

    prs.save(out_d5_local)
    shutil.copy(out_d5_local, out_d5_edu)
    shutil.copy(out_d5_local, out_d5_root)
    print(f"[OK] Saved Day 5 Master Deck: {out_d5_local.name}")

if __name__ == "__main__":
    generate_day1_deck()
    generate_day5_deck()
    print("[SUCCESS] NotebookLM-Quality Master PPTX Presentations Generated Successfully!")
