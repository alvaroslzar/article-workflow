import os
import numpy as np
from matplotlib import pyplot as plt


script_dir = os.path.dirname(os.path.abspath(__file__))
FIGURES_FOLDER = os.path.abspath(os.path.join(script_dir, "..", "latex", "figures"))


x = np.linspace(-np.pi, np.pi, 100)
y = np.sin(x)

plt.plot(x,y)
plt.savefig(os.path.abspath(os.path.join(FIGURES_FOLDER, "my_image.pdf")))

# New figure
x = np.linspace(-np.pi, np.pi, 100)
y = np.cos(x)

plt.plot(x,y)
plt.savefig(os.path.abspath(os.path.join(FIGURES_FOLDER, "my_new_image.pdf")))