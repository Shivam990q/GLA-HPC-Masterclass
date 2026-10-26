"""
build_unified_header_all_decks.py
================================================================================
Universal Master Branding & Zero-Collision Layout Engine
GLA University Block Teaching | High Performance Computing Masterclass
Edulateral Foundation Official Branding

Design Architecture:
- Canvas: 1376 x 768 (16:9 Widescreen)
- Top Header Bar: 86px height
  - Background: Pearl Cream #F8FBFA (RGB: 248, 251, 250)
  - Blueprint Division Line: 2px Slate #B8BEB0 (RGB: 184, 190, 176) at y: 84..86
  - Left Typography:
    * Row 1 (y: 20): GLA UNIVERSITY  •  DEPARTMENT OF COMPUTER ENGINEERING (17pt Bold Navy)
    * Row 2 (y: 48): HIGH PERFORMANCE COMPUTING & DISTRIBUTED AI MASTERCLASS  |  INDUSTRY BLOCK TEACHING (12pt Slate)
  - Right Logo:
    * Edulateral Foundation Official Logo (tight-cropped, no transparent margin)
    * Fixed location: x = 1181, y = 14 across 100% of slides (never moves, never jumps)
    * Size: 159 x 58 px (large, crisp, authoritative, masterclass-grade)
- Slide Content Area:
  - Height: 682 px (y: 86..768)
  - Proportional Scaling Factor: 682 / 768 = 0.88802 (zero horizontal/vertical distortion)
  - Scaled Width: 1222 px, centered horizontally (off_x = 77 px)
  - Side gutters: seamless background color matched to slide canvas
- Bottom-Right NotebookLM Watermark:
  - Cleaned completely using Telea inpainting [y: 740..766, x: 1250..1374]
- Multi-Folder Synchronization:
  - Central Repository: NotebookLM_Master_Decks_Organized/
  - LMS Upload Decks: LMS_Upload_Decks/
  - Day Specific Folders: Day-01 through Day-05/
  - Offline Pendrive Toolkit: OFFLINE_PENDRIVE_TOOLKIT/04_PRESENTATIONS_PPTX/
================================================================================
"""

import os
import shutil
import zipfile
import cv2
import numpy as np
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.normpath(r"c:\Users\Rose\Videos\GLA Trainings")
SRC_DIR = r"C:\Users\Rose\Downloads\Documents"
HPC_DIR = os.path.join(BASE_DIR, "HPC_Master_Curriculum")

CENTRAL_DIR = os.path.join(HPC_DIR, "NotebookLM_Master_Decks_Organized")
LMS_DIR = os.path.join(HPC_DIR, "LMS_Upload_Decks")
PENDRIVE_DIR = os.path.join(HPC_DIR, "OFFLINE_PENDRIVE_TOOLKIT", "04_PRESENTATIONS_PPTX")
RENDER_DIR = os.path.join(BASE_DIR, "_build_scripts", "_all_70_unified_slides")
os.makedirs(RENDER_DIR, exist_ok=True)

TEMP_WORK = os.path.join(BASE_DIR, "_temp_unified_header_build")
if os.path.exists(TEMP_WORK):
    shutil.rmtree(TEMP_WORK)
os.makedirs(TEMP_WORK, exist_ok=True)

# 1. Prepare Tight Logo
raw_logo_path = os.path.join(BASE_DIR, "edulateral_official_logo.png")
raw_logo = Image.open(raw_logo_path)
alpha_box = raw_logo.getchannel("A").getbbox()
tight_logo = raw_logo.crop(alpha_box).convert("RGBA")
tight_logo_path = os.path.join(BASE_DIR, "_build_scripts", "edulateral_tight_logo.png")
tight_logo.save(tight_logo_path)

# Canvas and Header Layout Specifications
CANVAS_W, CANVAS_H = 1376, 768
HEADER_H = 86
CONTENT_H = CANVAS_H - HEADER_H  # 682 px

# Logo Sizing & Fixed Position
LOGO_H = 58
LOGO_W = int(LOGO_H * tight_logo.width / tight_logo.height)  # 159 px
LOGO_SCALED = tight_logo.resize((LOGO_W, LOGO_H), Image.Resampling.LANCZOS)
FIXED_LOGO_X = CANVAS_W - LOGO_W - 36  # 1181 px
FIXED_LOGO_Y = (HEADER_H - LOGO_H) // 2  # 14 px

FONT_BOLD = ImageFont.truetype(r"C:\Windows\Fonts\arialbd.ttf", 17)
FONT_SUB = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf", 12)

DECKS = [
    {
        "day": "Day-01",
        "src_pptx": "High_Performance_AI_Foundations.pptx",
        "folder": "Day-01_HPC_Linux_Shell_oneAPI",
        "day_pptx": "Day_01_HPC_Foundations_Linux_oneAPI.pptx",
        "central_name": "Day_01_High_Performance_AI_Foundations.pptx",
        "lms_name": "Day_01_HPC_Foundations_Linux_oneAPI_LMS.pptx",
        "pendrive_name": "Day-01_Fundamentals_of_HPC_Linux_and_oneAPI.pptx",
        "slide_count": 15
    },
    {
        "day": "Day-02",
        "src_pptx": "High_Performance_AI_Acceleration.pptx",
        "folder": "Day-02_Parallel_OpenMP_MPI_oneDAL",
        "day_pptx": "Day_02_Traditional_ML_Parallel_Computing.pptx",
        "central_name": "Day_02_High_Performance_AI_Acceleration.pptx",
        "lms_name": "Day_02_Traditional_ML_Parallel_Computing_LMS.pptx",
        "pendrive_name": "Day-02_Traditional_ML_and_Parallel_Computing.pptx",
        "slide_count": 12
    },
    {
        "day": "Day-03",
        "src_pptx": "Distributed_Deep_Learning_on_HPC.pptx",
        "folder": "Day-03_DeepLearning_TF_Slurm_Horovod",
        "day_pptx": "Day_03_Deep_Learning_HPC_Slurm.pptx",
        "central_name": "Day_03_Distributed_Deep_Learning_on_HPC.pptx",
        "lms_name": "Day_03_Deep_Learning_HPC_Slurm_LMS.pptx",
        "pendrive_name": "Day-03_Deep_Learning_on_HPC_and_Slurm.pptx",
        "slide_count": 15
    },
    {
        "day": "Day-04",
        "src_pptx": "Distributed_AI_Cluster_Optimization.pptx",
        "folder": "Day-04_Distributed_Slurm_VTune_Profiling",
        "day_pptx": "Day_04_Distributed_AI_VTune_Profiling.pptx",
        "central_name": "Day_04_Distributed_AI_Cluster_Optimization.pptx",
        "lms_name": "Day_04_Distributed_AI_VTune_Profiling_LMS.pptx",
        "pendrive_name": "Day-04_Distributed_AI_and_VTune_Profiling.pptx",
        "slide_count": 13
    },
    {
        "day": "Day-05",
        "src_pptx": "Generative_AI_on_Intel_HPC.pptx",
        "folder": "Day-05_GenAI_LLMs_Gaudi_OpenVINO",
        "day_pptx": "Day_05_GenAI_LLMs_Gaudi_OpenVINO.pptx",
        "central_name": "Day_05_Generative_AI_on_Intel_HPC.pptx",
        "lms_name": "Day_05_GenAI_LLMs_Gaudi_OpenVINO_LMS.pptx",
        "pendrive_name": "Day-05_Generative_AI_and_LLMs_on_Intel_HPC.pptx",
        "slide_count": 15
    }
]

def build_unified_deck(deck_info):
    day_tag = deck_info["day"]
    src_path = os.path.join(SRC_DIR, deck_info["src_pptx"])
    print(f"\n========================================================")
    print(f"[*] Processing {day_tag}: {deck_info['src_pptx']} ({deck_info['slide_count']} slides)")
    print(f"========================================================")
    
    # Unpack PPTX
    unzip_dir = os.path.join(TEMP_WORK, day_tag)
    if os.path.exists(unzip_dir):
        shutil.rmtree(unzip_dir)
    shutil.unpack_archive(src_path, unzip_dir, "zip")
    
    rels_dir = os.path.join(unzip_dir, "ppt", "slides", "_rels")
    
    for s_idx in range(1, deck_info["slide_count"] + 1):
        rel_file = os.path.join(rels_dir, f"slide{s_idx}.xml.rels")
        root = ET.fromstring(open(rel_file, "rb").read())
        img_target = [r.attrib["Target"] for r in root if "image" in r.attrib["Type"]][0].replace("../", "")
        img_path = os.path.join(unzip_dir, "ppt", img_target)
        
        # Load raw slide image
        img = cv2.imread(img_path)
        
        # 1. Clean bottom-right NotebookLM watermark via Telea Inpainting
        mask = np.zeros((768, 1376), dtype=np.uint8)
        mask[740:766, 1250:1374] = 255
        clean_img = cv2.inpaint(img, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
        
        # 2. Proportional Scaling into Content Area
        scale_factor = CONTENT_H / 768.0  # 682 / 768 = 0.88802
        scaled_w = int(1376 * scale_factor)  # 1222 px
        scaled_img = cv2.resize(clean_img, (scaled_w, CONTENT_H), interpolation=cv2.INTER_LANCZOS4)
        
        # 3. Canvas Construction
        bg_color = clean_img[10, 10].tolist()  # Sample authentic slide background
        canvas = np.full((CANVAS_H, CANVAS_W, 3), bg_color, dtype=np.uint8)
        
        # Center slide content horizontally below the header bar
        off_x = (CANVAS_W - scaled_w) // 2  # 77 px
        canvas[HEADER_H:CANVAS_H, off_x:off_x+scaled_w] = scaled_img
        
        # 4. Header Bar Construction
        # Pearl-cream header background #F8FBFA
        canvas[0:HEADER_H, :] = [248, 251, 250]
        # Blueprint technical line at bottom of header
        canvas[HEADER_H-2:HEADER_H, :] = [184, 190, 176]
        
        # Convert to PIL for anti-aliased typography and alpha compositing
        pil_img = Image.fromarray(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_img)
        
        # Executive Header Typography
        draw.text((36, 20), "GLA UNIVERSITY  •  DEPARTMENT OF COMPUTER ENGINEERING", fill=(15, 23, 42), font=FONT_BOLD)
        draw.text((36, 48), "HIGH PERFORMANCE COMPUTING & DISTRIBUTED AI MASTERCLASS  |  INDUSTRY BLOCK TEACHING", fill=(71, 85, 105), font=FONT_SUB)
        
        # Fixed-Location Official Logo
        pil_img.paste(LOGO_SCALED, (FIXED_LOGO_X, FIXED_LOGO_Y), LOGO_SCALED)
        
        # Save back to PPTX media folder (overwrites original slide image)
        pil_img.save(img_path, "PNG")
        
        # Save render copy for visual verification
        clean_day = day_tag.replace("-", "")
        slide_out_png = os.path.join(RENDER_DIR, f"{clean_day}_Slide{s_idx:02d}.png")
        pil_img.save(slide_out_png, "PNG")
        
        print(f"  [+] {day_tag} Slide {s_idx:02d}: Unified Header & Fixed Logo stamped -> {slide_out_png}")
        
    # Repack to PPTX
    repack_base = os.path.join(TEMP_WORK, f"{day_tag}_unified")
    shutil.make_archive(repack_base, "zip", unzip_dir)
    unified_pptx = repack_base + ".pptx"
    if os.path.exists(unified_pptx):
        os.remove(unified_pptx)
    shutil.move(repack_base + ".zip", unified_pptx)
    print(f"[+] Successfully repacked: {unified_pptx} ({os.path.getsize(unified_pptx)} bytes)")
    
    # Multi-directory sync
    targets = [
        ("Central Organized", os.path.join(CENTRAL_DIR, deck_info["central_name"])),
        ("LMS Decks", os.path.join(LMS_DIR, deck_info["lms_name"])),
        ("Day Folder", os.path.join(HPC_DIR, deck_info["folder"], deck_info["day_pptx"])),
        ("Pendrive Toolkit", os.path.join(PENDRIVE_DIR, deck_info["pendrive_name"]))
    ]
    
    for label, target_path in targets:
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        try:
            shutil.copy2(unified_pptx, target_path)
            print(f"  [SYNC] {label}: {target_path}")
        except Exception as e:
            print(f"  [!] Sync error on {label} ({target_path}): {e}")

if __name__ == "__main__":
    print("=" * 80)
    print("STARTING COMPLETE MASTER UNIFIED BRANDING ENGINE FOR ALL 70 SLIDES")
    print("=" * 80)
    
    total_slides = 0
    for deck in DECKS:
        build_unified_deck(deck)
        total_slides += deck["slide_count"]
        
    print("\n" + "=" * 80)
    print(f"COMPLETED ALL {total_slides} SLIDES ACROSS ALL 5 MASTER DECKS!")
    print(f"All renders saved to: {RENDER_DIR}")
    print("=" * 80)
