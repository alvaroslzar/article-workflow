#!/usr/bin/env python
"""Setup script: Generate images and build PDF."""

import subprocess
import sys
import time
from pathlib import Path
import os

def run_cmd(cmd, desc, quiet=False):
    """Run shell command and report status."""
    print(f"Running: {desc}")
    try:
        subprocess.run(cmd, check=True,
                      stdout=subprocess.DEVNULL if quiet else None,
                      stderr=subprocess.DEVNULL if quiet else None)
        print(f"✓ {desc} completed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"✗ {desc} failed: {e}")
        return False

def main():
    start = time.time()
    base = Path(__file__).parent
    
    # Generate images
    gen_script = base / "src" / "generate_images.py"
    if not gen_script.exists():
        print(f"Error: {gen_script} not found"); sys.exit(1)
    if not run_cmd([sys.executable, str(gen_script)], "Image generation"):
        sys.exit(1)
    
    # Build PDF
    latex_dir = base / "latex"
    main_tex = latex_dir / "main.tex"
    if not main_tex.exists():
        print(f"Error: {main_tex} not found"); sys.exit(1)
    
    os.chdir(latex_dir)
    if not run_cmd(["pdflatex", "-interaction=nonstopmode", "main.tex"],
                   "Build PDF", quiet=True):
        sys.exit(1)
    
    # Cleanup auxiliary files
    for ext in ['.aux', '.log', '.out', '.toc', '.lot', '.lof', '.fls']:
        (latex_dir / f"main{ext}").unlink(missing_ok=True)
    
    elapsed = time.time() - start
    print(f"\n✓ Setup completed successfully! ({elapsed:.2f}s)")

if __name__ == "__main__":
    main()
