import matplotlib.pyplot as plt
import numpy as np
import Read
import re
import os
import sys

# Read in arguments
ftop=sys.argv[1]

# Parameters
sum_axis = (0,1)

#Reading
density,sizes=Read.topology(ftop)
density_2d=density.sum(axis=sum_axis)

# Make plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X = np.arange(0,sizes[2])
Y = np.arange(0,sizes[3])
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y,density_2d, rstride=1, cstride=1,
                cmap="viridis", edgecolor='none')
ax.set_title('Topological charge');

plt.savefig(ftop.replace(".dat",".png"))
