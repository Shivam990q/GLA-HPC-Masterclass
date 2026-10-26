import cv2
import numpy as np
from pptx import Presentation
from pathlib import Path
import io
from PIL import Image

decks_dir = Path(r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\NotebookLM_Master_Decks_Organized")
pptx_files = [p for p in sorted(decks_dir.glob("*.pptx")) if not p.name.startswith("~$")]

all_slides = []

for p in pptx_files:
    prs = Presentation(p)
    for i, slide in enumerate(prs.slides):
        img = Image.open(io.BytesIO(slide.shapes[0].image.blob)).convert("RGB")
        arr = np.array(img)
        h, w, _ = arr.shape
        gray = cv2.cvtColor(arr, cv2.COLOR_RGB2GRAY)
        
        # In these slides, background is cream/off-white (values 230-255)
        # Content is text, diagrams, boxes (values < 210)
        content_mask = (gray < 210).astype(np.uint8)
        
        # Exclude our stamped logo zone (x: 1175..1360, y: 640..760)
        content_mask[640:768, 1175:1376] = 0
        
        all_slides.append({
            "deck": p.stem,
            "slide": i + 1,
            "mask": content_mask,
            "img": img
        })

print(f"Loaded and masked {len(all_slides)} slides.")

# Now let's test potential logo candidate locations:
# Logo aspect ratio is 642 x 389.
# Let's consider logo sizes:
# Size A: 140 x 85
# Size B: 120 x 73
# Size C: 100 x 61
# Size D: 160 x 97

candidate_positions = {
    # 1. Top Right corner (above or to the side of title)
    "TR_corner_small": (1230, 10, 120, 73),
    "TR_corner_mini": (1240, 12, 105, 64),
    "TR_above_frame": (1230, 2, 115, 70),
    
    # 2. Top Left corner
    "TL_corner_small": (25, 10, 120, 73),
    "TL_above_title": (45, 8, 110, 67),
    
    # 3. Bottom Left corner
    "BL_margin": (25, 690, 120, 73),
    "BL_corner": (40, 680, 110, 67),
    
    # 4. Bottom Center / Footer
    "Bottom_Center": (600, 700, 120, 73),
    "Top_Center": (600, 8, 120, 73),
    
    # 5. Let's see what is inside the drafting frame margins
}

for name, (px, py, pw, ph) in candidate_positions.items():
    collision_count = 0
    colliding_slides = []
    for s in all_slides:
        patch = s["mask"][py : py + ph, px : px + pw]
        dark_pixels = patch.sum()
        if dark_pixels > 25: # small tolerance for minor noise/grid line
            collision_count += 1
            colliding_slides.append((s["deck"], s["slide"], dark_pixels))
    print(f"Candidate '{name}': {collision_count}/70 collisions")
    if collision_count <= 10:
        for d, sl, dp in colliding_slides:
            print(f"   -> {d} S{sl}: {dp} dark px")
