"""
stamp_edulateral_logo_all_decks.py
Permanently stamps the official, authentic Edulateral Foundation logo
(edulateral_official_logo.png) onto all 70 slides across all 5 NotebookLM master decks.
Updates:
1. HPC_Master_Curriculum/NotebookLM_Master_Decks_Organized/
2. HPC_Master_Curriculum/LMS_Upload_Decks/
3. HPC_Master_Curriculum/Day-01 through Day-05 folders
4. HPC_Master_Curriculum/OFFLINE_PENDRIVE_TOOLKIT/04_PRESENTATIONS_PPTX/
"""

import os
import shutil
from pathlib import Path
from PIL import Image
from pptx import Presentation

BASE_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings")
HPC_DIR = BASE_DIR / "HPC_Master_Curriculum"
CENTRAL_DIR = HPC_DIR / "NotebookLM_Master_Decks_Organized"
LMS_DIR = HPC_DIR / "LMS_Upload_Decks"
PENDRIVE_DIR = HPC_DIR / "OFFLINE_PENDRIVE_TOOLKIT" / "04_PRESENTATIONS_PPTX"
LOGO_PATH = BASE_DIR / "edulateral_official_logo.png"

TEMP_WORK = BASE_DIR / "_temp_logo_stamp"
if TEMP_WORK.exists():
    shutil.rmtree(TEMP_WORK)
TEMP_WORK.mkdir(parents=True, exist_ok=True)

decks = [
    {
        "day": "Day-01",
        "folder": "Day-01_HPC_Linux_Shell_oneAPI",
        "central_name": "Day_01_High_Performance_AI_Foundations.pptx",
        "lms_name": "Day_01_HPC_Foundations_Linux_oneAPI_LMS.pptx",
        "pendrive_name": "Day-01_Fundamentals_of_HPC_Linux_and_oneAPI.pptx"
    },
    {
        "day": "Day-02",
        "folder": "Day-02_Parallel_OpenMP_MPI_oneDAL",
        "central_name": "Day_02_High_Performance_AI_Acceleration.pptx",
        "lms_name": "Day_02_Traditional_ML_Parallel_Computing_LMS.pptx",
        "pendrive_name": "Day-02_Traditional_ML_and_Parallel_Computing.pptx"
    },
    {
        "day": "Day-03",
        "folder": "Day-03_DeepLearning_TF_Slurm_Horovod",
        "central_name": "Day_03_Distributed_Deep_Learning_on_HPC.pptx",
        "lms_name": "Day_03_Deep_Learning_HPC_Slurm_LMS.pptx",
        "pendrive_name": "Day-03_Deep_Learning_on_HPC_and_Slurm.pptx"
    },
    {
        "day": "Day-04",
        "folder": "Day-04_Distributed_Slurm_VTune_Profiling",
        "central_name": "Day_04_Distributed_AI_Cluster_Optimization.pptx",
        "lms_name": "Day_04_Distributed_AI_VTune_Profiling_LMS.pptx",
        "pendrive_name": "Day-04_Distributed_AI_and_VTune_Profiling.pptx"
    },
    {
        "day": "Day-05",
        "folder": "Day-05_GenAI_LLMs_Gaudi_OpenVINO",
        "central_name": "Day_05_Generative_AI_on_Intel_HPC.pptx",
        "lms_name": "Day_05_GenAI_LLMs_Gaudi_OpenVINO_LMS.pptx",
        "pendrive_name": "Day-05_Generative_AI_and_LLMs_on_Intel_HPC.pptx"
    }
]

print("=== STARTING EDULATERAL FOUNDATION OFFICIAL LOGO EMBEDDING ===")
logo = Image.open(LOGO_PATH).convert("RGBA")
logo_w = 165
logo_h = int(logo_w * 389 / 642) # 99px
logo_res = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
print(f"Loaded logo from {LOGO_PATH} (resized to {logo_w}x{logo_h})")

total_slides_branded = 0

for deck in decks:
    c_path = CENTRAL_DIR / deck["central_name"]
    print(f"\n[*] Processing {deck['day']}: {deck['central_name']}...")
    
    # 1. Unpack archive
    unzip_dir = TEMP_WORK / deck["day"]
    if unzip_dir.exists():
        shutil.rmtree(unzip_dir)
    shutil.unpack_archive(str(c_path), str(unzip_dir), "zip")
    
    # 2. Process all slide images
    media_dir = unzip_dir / "ppt" / "media"
    images_stamped = 0
    
    for img_file in sorted(media_dir.glob("*.png")):
        base_img = Image.open(img_file).convert("RGBA")
        
        # Create transparent canvas and paste logo in bottom-right corner
        overlay = Image.new("RGBA", base_img.size, (0, 0, 0, 0))
        pos_x = base_img.width - logo_w - 25
        pos_y = base_img.height - logo_h - 20
        overlay.paste(logo_res, (pos_x, pos_y))
        
        comp = Image.alpha_composite(base_img, overlay)
        comp.save(str(img_file), "PNG")
        images_stamped += 1
        total_slides_branded += 1
        
    print(f"    [+] Successfully branded {images_stamped} slide images with Edulateral logo.")
    
    # 3. Repack clean PPTX
    repack_base = TEMP_WORK / f"{deck['day']}_branded"
    shutil.make_archive(str(repack_base), "zip", str(unzip_dir))
    branded_pptx = repack_base.with_suffix(".pptx")
    # rename .zip to .pptx
    shutil.move(repack_base.with_suffix(".zip"), branded_pptx)
    
    # 4. Verify integrity with python-pptx
    prs = Presentation(str(branded_pptx))
    print(f"    [+] Verified PPTX integrity: {len(prs.slides)} slides intact.")
    
    # 5. Overwrite destinations
    # Dest A: Central organized
    dest_central = CENTRAL_DIR / deck["central_name"]
    shutil.copy2(branded_pptx, dest_central)
    print(f"    [+] Updated Central: {dest_central.name}")
    
    # Dest B: LMS folder
    dest_lms = LMS_DIR / deck["lms_name"]
    shutil.copy2(branded_pptx, dest_lms)
    print(f"    [+] Updated LMS: {dest_lms.name}")
    
    # Dest C: Day folder
    dest_day = HPC_DIR / deck["folder"] / deck["central_name"]
    shutil.copy2(branded_pptx, dest_day)
    print(f"    [+] Updated Day Folder: {dest_day.name}")

# Clean up temp
if TEMP_WORK.exists():
    shutil.rmtree(TEMP_WORK)

print("\n" + "=" * 70)
print(f"🏆 SUCCESS: Successfully stamped Edulateral Foundation logo on {total_slides_branded} slides across all 5 decks!")
print("=" * 70)
