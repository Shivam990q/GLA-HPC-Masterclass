import cv2
import numpy as np
from PIL import Image
from pptx import Presentation
from pathlib import Path
import io

decks_dir = Path(r"c:\Users\Rose\Videos\GLA Trainings\HPC_Master_Curriculum\NotebookLM_Master_Decks_Organized")
deck1_path = decks_dir / "Day_01_High_Performance_AI_Foundations.pptx"
prs = Presentation(deck1_path)

# Let's inspect slide 14 (Image 2 from user)
slide14 = prs.slides[13]
img14 = Image.open(io.BytesIO(slide14.shapes[0].image.blob)).convert("RGB")
arr14 = np.array(img14)
h, w, _ = arr14.shape
gray = cv2.cvtColor(arr14, cv2.COLOR_RGB2GRAY)

print(f"Slide 14 dimensions: {w}x{h}")

# Let's find horizontal lines and vertical lines using morphological ops
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold=100, minLineLength=200, maxLineGap=10)

horiz_lines = []
vert_lines = []

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if abs(y1 - y2) <= 2: # horizontal
            horiz_lines.append((min(y1, y2), min(x1, x2), max(x1, x2)))
        elif abs(x1 - x2) <= 2: # vertical
            vert_lines.append((min(x1, x2), min(y1, y2), max(y1, y2)))

print(f"Found {len(horiz_lines)} horizontal lines, {len(vert_lines)} vertical lines.")
# Sort by y and x
horiz_lines.sort(key=lambda item: item[0])
vert_lines.sort(key=lambda item: item[0])

print("Top 5 horizontal lines (y, x_min, x_max):")
for hl in horiz_lines[:5]:
    print(" ", hl)
print("Bottom 5 horizontal lines (y, x_min, x_max):")
for hl in horiz_lines[-5:]:
    print(" ", hl)

print("Left 5 vertical lines (x, y_min, y_max):")
for vl in vert_lines[:5]:
    print(" ", vl)
print("Right 5 vertical lines (x, y_min, y_max):")
for vl in vert_lines[-5:]:
    print(" ", vl)
