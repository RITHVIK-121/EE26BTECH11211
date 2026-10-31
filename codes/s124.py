
import numpy as np
import matplotlib.pyplot as plt
import os

from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

# First branch: y = |x| + 3, x <= -3
A1 = np.array([-8, 11]).reshape(-1, 1)
B1 = np.array([-3, 6]).reshape(-1, 1)

# Second branch: y = -2x, -3 < x < 3
A2 = np.array([-3, 6]).reshape(-1, 1)
B2 = np.array([3, -6]).reshape(-1, 1)

# Third branch: y = 6x + 2, x >= 3
A3 = np.array([3, 20]).reshape(-1, 1)
B3 = np.array([7, 26]).reshape(-1, 1)

# Generate line points using CoordGeo
x1 = line_gen_num(A1, B1, 100)
x2 = line_gen_num(A2, B2, 100)
x3 = line_gen_num(A3, B3, 100)

# Plot the three branches
plt.plot(x1[0, :], x1[1, :], label=r'$y=|x|+3,\ x\leq -3$')
plt.plot(x2[0, :], x2[1, :], label=r'$y=-2x,\ -3<x<3$')
plt.plot(x3[0, :], x3[1, :], label=r'$y=6x+2,\ x\geq 3$')

# Closed endpoint at (-3, 6)
P = np.array([[-3], [6]])
plt.scatter(P[0], P[1], color='black', zorder=5)

# Open endpoint at (3, -6)
plt.scatter(3, -6, facecolors='white',
            edgecolors='black', s=70, zorder=5)

# Closed endpoint at (3, 20)
plt.scatter(3, 20, color='black', s=50, zorder=5)

# Label important points using CoordGeo
G = np.array([[-3, 3, 3],
              [6, -6, 20]])

label_pts(G, ['$(-3,6)$', '$(3,-6)$', '$(3,20)$'])

# Coordinate axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.xlabel('$x$')
plt.ylabel('$f(x)$')

plt.xlim(-9, 8)
plt.ylim(-9, 25)

plt.xticks(np.arange(-9, 9, 1))
plt.yticks(np.arange(-8, 26, 2))

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.title('Graph of the Piecewise Function')

plt.gca().set_aspect('equal', adjustable='box')

plt.savefig('s124.png', dpi=300, bbox_inches='tight')
#os.system("termux-open s124.png")
plt.show()

