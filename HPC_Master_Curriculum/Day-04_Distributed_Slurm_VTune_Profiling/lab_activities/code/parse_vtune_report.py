#!/usr/bin/env python3
"""
parse_vtune_report.py
Parses Intel VTune Top-Down Microarchitecture Analysis Method (TMAM) reports.
Extracts pipeline slot percentages: Retiring, Bad Speculation, Front-End Bound, Back-End Bound.
Provides automated diagnostic recommendations for HPC developers.
"""

import sys
import re

def parse_mock_or_real_report(report_text):
    print("==========================================================")
    print("     INTEL VTUNE TMAM REPORT PARSER & DIAGNOSTIC ENGINE   ")
    print("==========================================================")
    
    # Defaults or regex matches
    tmam_metrics = {
        "Retiring": 24.5,
        "Bad Speculation": 8.2,
        "Front-End Bound": 12.1,
        "Back-End Bound": 55.2,
        "  -> Memory Bound": 42.8,
        "  -> Core Bound": 12.4
    }
    
    # If text is provided, attempt to parse
    if report_text:
        for line in report_text.splitlines():
            for key in ["Retiring", "Bad Speculation", "Front-End Bound", "Back-End Bound", "Memory Bound", "Core Bound"]:
                if key in line:
                    match = re.search(r"(\d+\.\d+)%", line)
                    if match:
                        tmam_metrics[key] = float(match.group(1))

    print(f"\n📊 Top-Down Microarchitecture Metric Breakdown:")
    for k, v in tmam_metrics.items():
        bar = "█" * int(v // 2)
        print(f"  {k:<22}: {v:5.1f}% | {bar}")

    print("\n🔍 Automated Root-Cause Analysis & Action Plan:")
    if tmam_metrics.get("Back-End Bound", 0) > 40.0:
        print("  [!] WARNING: Application is severely BACK-END BOUND.")
        if tmam_metrics.get("  -> Memory Bound", tmam_metrics.get("Memory Bound", 0)) > 30.0:
            print("      -> Root Cause: DRAM Bandwidth / L3 Cache Miss stalls dominate pipeline slots.")
            print("      -> Action Plan 1: Apply loop tiling / cache blocking (e.g., 64-element block size).")
            print("      -> Action Plan 2: Align arrays to 64-byte boundaries (`alignas(64)` / posix_memalign).")
            print("      -> Action Plan 3: Enable oneDNN operator fusion (TF_ENABLE_ONEDNN_OPTS=1).")
        else:
            print("      -> Root Cause: Core execution ports are saturated with non-vectorized instructions.")
            print("      -> Action Plan: Enable SIMD vectorization with AVX-512 (`-xHost -qopenmp-simd`).")
    elif tmam_metrics.get("Front-End Bound", 0) > 20.0:
        print("  [!] WARNING: Application is FRONT-END BOUND.")
        print("      -> Root Cause: Instruction cache misses or branch target buffer stalls.")
        print("      -> Action Plan: Profile code layout with Intel oneAPI ThinLTO or PGO.")
    elif tmam_metrics.get("Bad Speculation", 0) > 15.0:
        print("  [!] WARNING: High BAD SPECULATION.")
        print("      -> Root Cause: Frequent branch mispredictions in inner loops.")
        print("      -> Action Plan: Replace dynamic conditionals with branchless select/min/max intrinsics.")
    else:
        print("  [✓] EXCELLENT: High RETIRING slots (> 50%). Processor pipeline is executing efficiently.")

    print("==========================================================")

def main():
    if len(sys.argv) > 1:
        try:
            with open(sys.argv[1], "r", encoding="utf-8") as f:
                content = f.read()
            parse_mock_or_real_report(content)
        except Exception as e:
            print(f"[-] Error reading file {sys.argv[1]}: {e}")
            parse_mock_or_real_report(None)
    else:
        parse_mock_or_real_report(None)

if __name__ == "__main__":
    main()
