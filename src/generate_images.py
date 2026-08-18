import os
import numpy as np
from matplotlib import pyplot as plt


script_dir = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.abspath(os.path.join(script_dir, "..", "latex", "figures"))

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

plt.plot(x,y)
plt.savefig(os.path.abspath(os.path.join(OUTPUT_DIR, "my_image.pdf")))