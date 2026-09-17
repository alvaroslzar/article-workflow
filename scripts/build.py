#!/usr/bin/env python
"""Build script: Generate images and build PDF."""

import subprocess
import sys
import time
from pathlib import Path
import os

def run_cmd(cmd, desc, quiet=False, announce=True):
    """Run shell command and report status."""
    if announce:
        print(f"Running: {desc}")
    try:
        subprocess.run(cmd, check=True,
                      stdout=subprocess.DEVNULL if quiet else None,
                      stderr=subprocess.DEVNULL if quiet else None)
        if announce:
            print(f"✓ {desc} completed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"✗ {desc} failed: {e}")
        return False

def install_deps(requirements_path):
    """Install dependencies from requirements.txt if not already installed."""
    print("Installing dependencies from requirements.txt...")
    subprocess.run([sys.executable, "-m", "pip", "install", "-r",
                    str(requirements_path)], check=True)
    print("✓ Dependencies installed")

def run_generate_images(gen_script):
    if not gen_script.exists():
        print(f"Error: {gen_script} not found"); sys.exit(1)
    if not run_cmd([sys.executable, str(gen_script)], "Image generation"):
        sys.exit(1)

def make_wls_executable(script_path):
    if not script_path.exists():
        print(f"Error: {script_path} not found"); sys.exit(1)
    if not run_cmd(["bash", str(script_path)], "Make .wls executable"):
        sys.exit(1)

def build_pdf(manuscript_dir):
    main_tex = manuscript_dir / "main.tex"
    if not main_tex.exists():
        print(f"Error: {main_tex} not found"); sys.exit(1)

    os.chdir(manuscript_dir)
    print("Running: Build PDF")
    latex_cmd = ["pdflatex", "-interaction=nonstopmode", "-synctex=1", "main.tex"]
    if not run_cmd(latex_cmd, "Build PDF", quiet=True, announce=False):
        sys.exit(1)

    aux_path = manuscript_dir / "main.aux"
    aux_text = aux_path.read_text(encoding="utf-8", errors="replace") if aux_path.exists() else ""
    commands = []

    # Select the bibliography tool only when the first LaTeX pass requests it.
    if (manuscript_dir / "main.bcf").exists():
        commands.append(["biber", "main"])
    elif r"\bibdata{" in aux_text:
        commands.append(["bibtex", "main"])

    commands.extend([latex_cmd, latex_cmd])
    for cmd in commands:
        if not run_cmd(cmd, "Build PDF", quiet=True, announce=False):
            sys.exit(1)
    print("✓ Build PDF completed")

    for ext in [
        '.aux', '.log', '.out', '.toc', '.lot', '.lof', '.nav', '.snm',
        '.fls', '.blg', '.fdb_latexmk', '.bbl', '.synctex.gz', '.bcf', '.run.xml'
    ]:
        (manuscript_dir / f"main{ext}").unlink(missing_ok=True)

def main():
    start = time.time()
    base = Path(__file__).parent

    install_deps(base / ".." / "requirements.txt")

    gen_script = base / ".." / "src" / "generate_images.py"
    run_generate_images(gen_script)

    wls_script = base / "make-wls-executable.sh"
    make_wls_executable(wls_script)

    manuscript_dir = base / ".." / "src" / "manuscript"
    build_pdf(manuscript_dir)

    elapsed = time.time() - start
    print(f"\nBuilt project successfully in {elapsed:.2f} s.")

if __name__ == "__main__":
    main()
