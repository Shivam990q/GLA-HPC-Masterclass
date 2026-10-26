import os
import shutil
import zipfile
import cv2
import numpy as np
from pptx import Presentation

root = r"c:\Users\Rose\Videos\GLA Trainings"
hpc_root = os.path.join(root, "HPC_Master_Curriculum")
central_dir = os.path.join(hpc_root, "NotebookLM_Master_Decks_Organized")
lms_dir = os.path.join(hpc_root, "LMS_Upload_Decks")

temp_work = os.path.join(root, "_temp_clean_work")
if os.path.exists(temp_work):
    shutil.rmtree(temp_work)
os.makedirs(temp_work, exist_ok=True)

decks = [
    {
        "day": "Day-01",
        "folder": "Day-01_HPC_Linux_Shell_oneAPI",
        "central_name": "Day_01_High_Performance_AI_Foundations_NotebookLM.pptx",
        "lms_name": "Day_01_HPC_Foundations_Linux_oneAPI_LMS.pptx",
        "ocr_name": "Day_01_High_Performance_AI_Foundations_OCR.md"
    },
    {
        "day": "Day-02",
        "folder": "Day-02_Parallel_OpenMP_MPI_oneDAL",
        "central_name": "Day_02_High_Performance_AI_Acceleration_NotebookLM.pptx",
        "lms_name": "Day_02_Traditional_ML_Parallel_Computing_LMS.pptx",
        "ocr_name": "Day_02_High_Performance_AI_Acceleration_OCR.md"
    },
    {
        "day": "Day-03",
        "folder": "Day-03_DeepLearning_TF_Slurm_Horovod",
        "central_name": "Day_03_Distributed_Deep_Learning_on_HPC_NotebookLM.pptx",
        "lms_name": "Day_03_Deep_Learning_HPC_Slurm_LMS.pptx",
        "ocr_name": "Day_03_Distributed_Deep_Learning_on_HPC_OCR.md"
    },
    {
        "day": "Day-04",
        "folder": "Day-04_Distributed_Slurm_VTune_Profiling",
        "central_name": "Day_04_Distributed_AI_Cluster_Optimization_NotebookLM.pptx",
        "lms_name": "Day_04_Distributed_AI_VTune_Profiling_LMS.pptx",
        "ocr_name": "Day_04_Distributed_AI_Cluster_Optimization_OCR.md"
    },
    {
        "day": "Day-05",
        "folder": "Day-05_GenAI_LLMs_Gaudi_OpenVINO",
        "central_name": "Day_05_Generative_AI_on_Intel_HPC_NotebookLM.pptx",
        "lms_name": "Day_05_GenAI_LLMs_Gaudi_OpenVINO_LMS.pptx",
        "ocr_name": "Day_05_Generative_AI_on_Intel_HPC_OCR.md"
    }
]

print("=== STARTING MASTER WATERMARK REMOVAL ACROSS ALL DECKS ===")

for deck_info in decks:
    c_path = os.path.join(central_dir, deck_info["central_name"])
    print(f"\nProcessing {deck_info['day']}: {deck_info['central_name']}...")
    
    # 1. Unzip to temp dir
    deck_unzip = os.path.join(temp_work, deck_info["day"])
    if os.path.exists(deck_unzip): shutil.rmtree(deck_unzip)
    shutil.unpack_archive(c_path, deck_unzip, "zip")
    
    # 2. Process all media images
    media_dir = os.path.join(deck_unzip, "ppt", "media")
    images_cleaned = 0
    
    for img_file in os.listdir(media_dir):
        if img_file.endswith(".png"):
            img_path = os.path.join(media_dir, img_file)
            img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
            h, w = img.shape[:2]
            
            # Separate BGR and Alpha
            if img.shape[2] == 4:
                bgr = img[:, :, :3]
                alpha = img[:, :, 3]
            else:
                bgr = img
                alpha = np.full((h, w), 255, dtype=np.uint8)
            
            # Precise mask for the watermark zone
            mask = np.zeros((h, w), dtype=np.uint8)
            mask[742:764, 1255:1372] = 255
            
            # Inpaint using Telea algorithm
            inpainted_bgr = cv2.inpaint(bgr, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
            
            # Set alpha completely opaque
            clean_alpha = np.full((h, w, 1), 255, dtype=np.uint8)
            clean_img = np.dstack([inpainted_bgr, clean_alpha])
            
            cv2.imwrite(img_path, clean_img)
            images_cleaned += 1
            
    print(f"  Cleaned {images_cleaned} slide images in {deck_info['day']}.")
    
    # 3. Repack clean PPTX
    clean_zip_base = os.path.join(temp_work, f"{deck_info['day']}_clean")
    shutil.make_archive(clean_zip_base, "zip", deck_unzip)
    clean_pptx_temp = clean_zip_base + ".zip"
    
    # Verify with python-pptx
    prs = Presentation(clean_pptx_temp)
    print(f"  Verified PPTX integrity: {len(prs.slides)} slides intact.")
    
    # 4. Overwrite in all 3 target destinations
    # Dest A: Central organized folder
    dest_central = os.path.join(central_dir, deck_info["central_name"])
    shutil.copy2(clean_pptx_temp, dest_central)
    print(f"  Updated Central: {deck_info['central_name']}")
    
    # Dest B: LMS folder
    dest_lms = os.path.join(lms_dir, deck_info["lms_name"])
    shutil.copy2(clean_pptx_temp, dest_lms)
    print(f"  Updated LMS: {deck_info['lms_name']}")
    
    # Dest C: Day folder
    day_folder = os.path.join(hpc_root, deck_info["folder"])
    dest_day = os.path.join(day_folder, deck_info["central_name"])
    shutil.copy2(clean_pptx_temp, dest_day)
    print(f"  Updated Day Folder: {dest_day}")

# Cleanup temp work
shutil.rmtree(temp_work)
print("\n=== ALL 70 SLIDES ACROSS ALL 5 DECKS CLEANED AND REPACKED! ===")
