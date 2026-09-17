<!--
Template designed for scientific articles workflow written in LaTeX with simulations and figure generation in Python.

Template author: Álvaro Salazar Cuadros
https://github.com/alvaroslzar
-->


# Draft title

This repository contains the TEX source and Python scripts for the `<project-name>`

Authors: `author_name_1`, `author_name_2`, etc.


## Setup

### First time (one-time only)

Create a virtual environment and install the dependencies (macOS/Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

#### Notebook dependencies (optional)

If you want to run the notebooks, then install the optional notebook dependencies and also run the `setup-nb-filter.sh` script.

```bash
pip3 install -r nb-requirements.txt
bash scripts/setup-nb-filter.sh
```

### Every time after

Build the project by running the following script in the root directory:

```bash
python3 scripts/build.py
```


## Citation

The use of this work in scientific publications must be properly acknowledged.
Please cite the following:

**BibTeX**
```
<BibTeX_citation>
```

## License

This work is licensed under a Creative Commons Attribution 4.0 International License ([CC BY 4.0](/LICENSE)).