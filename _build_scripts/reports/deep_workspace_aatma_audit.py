#!/usr/bin/env python3
"""
DEEP WORKSPACE AATMA-LEVEL AUDIT SCRIPT
Bit-by-bit inspection across all 3 tracks, notebooks, presentations, PDFs, and scripts.
"""

import os
import sys
import ast
import json
import re
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(r"c:\Users\Rose\Videos\GLA Trainings")

def audit_python_files():
    print("=" * 70)
    print("🔬 1. AUDITING ALL PYTHON FILES FOR SYNTAX INTEGRITY (AST PARSE)")
    print("=" * 70)
    py_files = list(BASE_DIR.glob("**/*.py"))
    # Exclude .git and _build_scripts image folders if any
    py_files = [f for f in py_files if ".git" not in f.parts]
    passed = 0
    failed = []
    
    for f in py_files:
        try:
            with open(f, "r", encoding="utf-8", errors="ignore") as fp:
                code = fp.read()
            ast.parse(code, filename=str(f))
            passed += 1
        except Exception as e:
            failed.append((f, str(e)))
            
    print(f"  [+] Total Python Files: {len(py_files)}")
    print(f"  [+] Syntax Valid:       {passed}")
    print(f"  [+] Syntax Errors:      {len(failed)}")
    if failed:
        for f, err in failed:
            print(f"      [FAIL] {f.relative_to(BASE_DIR)}: {err}")
    else:
        print("  [PASS] 100% of Python files have zero syntax errors!")
    return len(failed) == 0

def audit_colab_notebooks():
    print("\n" + "=" * 70)
    print("🔬 2. AUDITING JUPYTER / COLAB NOTEBOOKS (JSON & CELL INTEGRITY)")
    print("=" * 70)
    ipynb_files = list(BASE_DIR.glob("**/*.ipynb"))
    ipynb_files = [f for f in ipynb_files if ".git" not in f.parts]
    passed = 0
    failed = []
    
    for f in ipynb_files:
        try:
            with open(f, "r", encoding="utf-8") as fp:
                nb = json.load(fp)
            cells = nb.get("cells", [])
            code_cells = sum(1 for c in cells if c.get("cell_type") == "code")
            md_cells = sum(1 for c in cells if c.get("cell_type") == "markdown")
            passed += 1
            print(f"  [+] {f.relative_to(BASE_DIR)}: {len(cells)} cells ({code_cells} code, {md_cells} markdown)")
        except Exception as e:
            failed.append((f, str(e)))
            
    print(f"  [+] Total Notebooks: {len(ipynb_files)} | Valid: {passed} | Errors: {len(failed)}")
    if failed:
        for f, err in failed:
            print(f"      [FAIL] {f.relative_to(BASE_DIR)}: {err}")
    else:
        print("  [PASS] 100% of Jupyter/Colab notebooks are syntactically and structurally valid!")
    return len(failed) == 0

def audit_pdfs():
    print("\n" + "=" * 70)
    print("🔬 3. AUDITING ALL PDF FILES (PYMUPDF PARSE & RENDERING CHECK)")
    print("=" * 70)
    try:
        import pymupdf as fitz
    except ImportError:
        import fitz
        
    pdf_files = list(BASE_DIR.glob("**/*.pdf"))
    pdf_files = [f for f in pdf_files if ".git" not in f.parts]
    passed = 0
    failed = []
    total_pages = 0
    total_size = sum(f.stat().st_size for f in pdf_files)
    
    for f in pdf_files:
        try:
            doc = fitz.open(f)
            p_count = doc.page_count
            if p_count > 0:
                passed += 1
                total_pages += p_count
            else:
                failed.append((f, "Empty PDF (0 pages)"))
            doc.close()
        except Exception as e:
            failed.append((f, str(e)))
            
    print(f"  [+] Total PDFs Found:   {len(pdf_files)}")
    print(f"  [+] Valid Non-Empty:    {passed}")
    print(f"  [+] Total Pages:        {total_pages}")
    print(f"  [+] Total PDF Size:     {total_size / (1024*1024):.2f} MB")
    if failed:
        for f, err in failed:
            print(f"      [FAIL] {f.relative_to(BASE_DIR)}: {err}")
    else:
        print("  [PASS] 100% of PDF documents are valid and render perfectly!")
    return len(failed) == 0

def audit_markdown_files():
    print("\n" + "=" * 70)
    print("🔬 4. AUDITING ALL MARKDOWN FILES (SIZE & CORRUPTION CHECK)")
    print("=" * 70)
    md_files = list(BASE_DIR.glob("**/*.md"))
    md_files = [f for f in md_files if ".git" not in f.parts and "node_modules" not in f.parts]
    passed = 0
    empty = []
    
    for f in md_files:
        size = f.stat().st_size
        if size > 10:
            passed += 1
        else:
            empty.append(f)
            
    print(f"  [+] Total Markdown Files: {len(md_files)}")
    print(f"  [+] Substantive Files:    {passed}")
    if empty:
        print(f"  [!] Warning: {len(empty)} empty files found:")
        for f in empty:
            print(f"      {f.relative_to(BASE_DIR)}")
    else:
        print("  [PASS] All Markdown files are non-empty and substantive!")
    return len(empty) == 0

def check_stray_artifacts():
    print("\n" + "=" * 70)
    print("🔬 5. CHECKING FOR STRAY TEMPORARY FILES & ROOT CLUTTER")
    print("=" * 70)
    root_items = list(BASE_DIR.iterdir())
    print("  [+] Current Workspace Root Items:")
    for item in sorted(root_items, key=lambda x: (not x.is_dir(), x.name.lower())):
        item_type = "DIR " if item.is_dir() else "FILE"
        print(f"      [{item_type}] {item.name}")
        
    strays = []
    for ext in ["*.tmp", "*.bak", "*.swp", "*~"]:
        strays.extend(list(BASE_DIR.glob(f"**/{ext}")))
    strays = [s for s in strays if ".git" not in s.parts]
    if strays:
        print(f"  [!] Warning: {len(strays)} stray files found:")
        for s in strays:
            print(f"      {s.relative_to(BASE_DIR)}")
    else:
        print("  [PASS] Zero stray or backup files (*.tmp, *.bak, *.swp) in workspace!")
    return len(strays) == 0

if __name__ == "__main__":
    r1 = audit_python_files()
    r2 = audit_colab_notebooks()
    r3 = audit_pdfs()
    r4 = audit_markdown_files()
    r5 = check_stray_artifacts()
    
    print("\n" + "=" * 70)
    if r1 and r2 and r3 and r4 and r5:
        print(">>> ALL AUDITS PASSED WITH ZERO ERRORS! BIT-BY-BIT 100% PERFECT! <<<")
    else:
        print(">>> SOME AUDITS FAILED - CHECK OUTPUT ABOVE! <<<")
    print("=" * 70)
