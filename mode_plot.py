import matplotlib.pyplot as plt
import numpy as np
import Read
import sys

# Read in arguments
Mode = str(sys.argv[1])
sizes=[int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])]

# Parameters
Sum_over= (0,1)
Chirality= 1
colors = 3
spin_length = 4
#sizes=[4,4,20,20]

#Read mode
zeromode, density, sizes=Read.bin_mode(Mode,sizes,colors,spin_length)
density_2d=Chirality*density.sum(axis=Sum_over)

# Make plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
X = np.arange(0,sizes[2])
Y = np.arange(0,sizes[3])
X, Y = np.meshgrid(X, Y)

surf = ax.plot_surface(X, Y,density_2d, rstride=1, cstride=1,
                cmap="viridis", edgecolor='none')
ax.set_title('Topological charge');

plt.savefig(Mode+".png")
