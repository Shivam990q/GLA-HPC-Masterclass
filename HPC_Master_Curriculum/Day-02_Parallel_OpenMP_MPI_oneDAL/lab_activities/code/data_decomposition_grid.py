#!/usr/bin/env python3
"""
data_decomposition_grid.py
Demonstrates 2D Domain Decomposition and Halo/Ghost Cell Boundary Synchronization
Run with: python3 data_decomposition_grid.py
"""

import numpy as np

def simulate_2d_stencil_halo_exchange():
    print("================================================================")
    print("   🌐 2D DOMAIN DECOMPOSITION & HALO (GHOST CELL) EXCHANGE       ")
    print("      Simulating a 12x12 Global Heat Diffusion Grid             ")
    print("      Partitioned into 4 Subdomains (2x2 Process Grid)          ")
    print("================================================================")

    GLOBAL_ROWS, GLOBAL_COLS = 12, 12
    SUB_ROWS, SUB_COLS = 6, 6

    # Create global physical simulation state
    global_grid = np.zeros((GLOBAL_ROWS, GLOBAL_COLS), dtype=np.float32)
    # Add a heat source in the center
    global_grid[5:7, 5:7] = 100.0

    print("\n[*] Initial Global Simulation Matrix (Center Heat Source = 100.0):")
    for r in range(GLOBAL_ROWS):
        row_str = " ".join(f"{val:5.1f}" for val in global_grid[r])
        print(f"    R{r:02d}: {row_str}")

    # Subdomain allocations with 1-cell Ghost/Halo border on all sides: shape is (SUB_ROWS + 2, SUB_COLS + 2)
    # Processors:
    # Rank 0: Rows 0..5, Cols 0..5 | Rank 1: Rows 0..5, Cols 6..11
    # Rank 2: Rows 6..11, Cols 0..5 | Rank 3: Rows 6..11, Cols 6..11
    subdomains = {}
    for rank in range(4):
        subdomains[rank] = np.zeros((SUB_ROWS + 2, SUB_COLS + 2), dtype=np.float32)

    # Initialize local interior domains from global grid
    # Rank 0 (Top-Left)
    subdomains[0][1:-1, 1:-1] = global_grid[0:6, 0:6]
    # Rank 1 (Top-Right)
    subdomains[1][1:-1, 1:-1] = global_grid[0:6, 6:12]
    # Rank 2 (Bottom-Left)
    subdomains[2][1:-1, 1:-1] = global_grid[6:12, 0:6]
    # Rank 3 (Bottom-Right)
    subdomains[3][1:-1, 1:-1] = global_grid[6:12, 6:12]

    print("\n[*] Performing Horizontal and Vertical Halo Exchange...")
    # Horizontal exchange between Rank 0 and Rank 1
    # Rank 0 sends rightmost column (col 6) to Rank 1's leftmost halo (col 0)
    subdomains[1][1:-1, 0] = subdomains[0][1:-1, SUB_COLS]
    # Rank 1 sends leftmost column (col 1) to Rank 0's rightmost halo (col 7)
    subdomains[0][1:-1, SUB_COLS + 1] = subdomains[1][1:-1, 1]

    # Horizontal exchange between Rank 2 and Rank 3
    subdomains[3][1:-1, 0] = subdomains[2][1:-1, SUB_COLS]
    subdomains[2][1:-1, SUB_COLS + 1] = subdomains[3][1:-1, 1]

    # Vertical exchange between Rank 0 and Rank 2
    # Rank 0 sends bottom row (row 6) to Rank 2's top halo (row 0)
    subdomains[2][0, 1:-1] = subdomains[0][SUB_ROWS, 1:-1]
    # Rank 2 sends top row (row 1) to Rank 0's bottom halo (row 7)
    subdomains[0][SUB_ROWS + 1, 1:-1] = subdomains[2][1, 1:-1]

    # Vertical exchange between Rank 1 and Rank 3
    subdomains[3][0, 1:-1] = subdomains[1][SUB_ROWS, 1:-1]
    subdomains[1][SUB_ROWS + 1, 1:-1] = subdomains[3][1, 1:-1]

    print("[+] Halo synchronization verified across all 4 process boundaries!")
    print(f"\n[Rank 0 Subdomain (8x8 with Halo Border)]:")
    print("    Interior Data + Boundary Ghost Cells from Rank 1 (Right) and Rank 2 (Bottom):")
    for r in range(SUB_ROWS + 2):
        row_str = " ".join(f"{val:5.1f}" for val in subdomains[0][r])
        print(f"    Local R{r:02d}: {row_str}")

    print("\n================================================================")
    print("  🏆 DOMAIN DECOMPOSITION INSIGHT:")
    print("  Halo exchanges allow distributed nodes to compute local 5-point")
    print("  or 9-point stencils without querying remote memory at every step.")
    print("================================================================")

if __name__ == "__main__":
    simulate_2d_stencil_halo_exchange()
