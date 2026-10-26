import os
import shutil

base = r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum"
dest_central = os.path.join(base, "NotebookLM_Master_Decks_Organized")
os.makedirs(dest_central, exist_ok=True)

mappings = [
    {
        "day": "Day-01",
        "folder": "Day-01_HPC_Linux_Shell_oneAPI",
        "src_pptx": "High_Performance_AI_Foundations.pptx",
        "clean_name": "Day_01_High_Performance_AI_Foundations_NotebookLM.pptx",
        "ocr_src": "Day_01_High_Performance_AI_Foundations_OCR.md"
    },
    {
        "day": "Day-02",
        "folder": "Day-02_Parallel_OpenMP_MPI_oneDAL",
        "src_pptx": "High_Performance_AI_Acceleration.pptx",
        "clean_name": "Day_02_High_Performance_AI_Acceleration_NotebookLM.pptx",
        "ocr_src": "Day_02_High_Performance_AI_Acceleration_OCR.md"
    },
    {
        "day": "Day-03",
        "folder": "Day-03_DeepLearning_TF_Slurm_Horovod",
        "src_pptx": "Distributed_Deep_Learning_on_HPC.pptx",
        "clean_name": "Day_03_Distributed_Deep_Learning_on_HPC_NotebookLM.pptx",
        "ocr_src": "Day_03_Distributed_Deep_Learning_on_HPC_OCR.md"
    },
    {
        "day": "Day-04",
        "folder": "Day-04_Distributed_Slurm_VTune_Profiling",
        "src_pptx": "Distributed_AI_Cluster_Optimization.pptx",
        "clean_name": "Day_04_Distributed_AI_Cluster_Optimization_NotebookLM.pptx",
        "ocr_src": "Day_04_Distributed_AI_Cluster_Optimization_OCR.md"
    },
    {
        "day": "Day-05",
        "folder": "Day-05_GenAI_LLMs_Gaudi_OpenVINO",
        "src_pptx": "Generative_AI_on_Intel_HPC.pptx",
        "clean_name": "Day_05_Generative_AI_on_Intel_HPC_NotebookLM.pptx",
        "ocr_src": "Day_05_Generative_AI_on_Intel_HPC_OCR.md"
    }
]

for m in mappings:
    src_p = os.path.join(base, m["src_pptx"])
    central_p = os.path.join(dest_central, m["clean_name"])
    shutil.copy2(src_p, central_p)
    print("Copied to central:", m["clean_name"])
    
    ocr_p = os.path.join(base, m["ocr_src"])
    if os.path.exists(ocr_p):
        shutil.copy2(ocr_p, os.path.join(dest_central, m["ocr_src"]))
    
    # Copy to Day folder
    day_folder_path = os.path.join(base, m["folder"])
    day_deck_dest = os.path.join(day_folder_path, m["clean_name"])
    shutil.copy2(src_p, day_deck_dest)
    if os.path.exists(ocr_p):
        shutil.copy2(ocr_p, os.path.join(day_folder_path, m["ocr_src"]))
    print("Copied to folder:", m["folder"], "->", m["clean_name"])

print("ALL 5 DECKS ORGANIZED CLEANLY ACROSS FOLDERS!")
