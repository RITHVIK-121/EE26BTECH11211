import numpy as np
import matplotlib.pyplot as plt
import os

from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

# Parabola y^2 = 4x in the first quadrant
x = np.linspace(0, 4, 300)
y = 2 * np.sqrt(x)

# Generate parabola using line_gen_num
curve = np.zeros((2, 0))

for i in range(len(x) - 1):
    A = np.array([[x[i]], [y[i]]])
    B = np.array([[x[i+1]], [y[i+1]]])

    segment = line_gen_num(A, B, 2)
    curve = np.hstack((curve, segment[:, :1]))

curve = np.hstack((curve, np.array([[4], [4]])))

# Plot
plt.figure(figsize=(9, 7))

plt.plot(curve[0], curve[1], label=r'$y^2=4x$')

# Shade A2: from x=0 to x=4
plt.fill_between(x, 0, y, alpha=0.2, label=r'$A_2$')

# Shade A1: from x=0 to x=1
x1 = np.linspace(0, 1, 100)
y1 = 2 * np.sqrt(x1)
plt.fill_between(x1, 0, y1, alpha=0.6, label=r'$A_1$')

# Vertical boundaries
plt.axvline(1, linestyle='--', label='x = 1')
plt.axvline(4, linestyle='--', label='x = 4')

# Mark important points
G = np.array([[0, 1, 4],
              [0, 2, 4]])

plt.scatter(G[0], G[1], color='red')
label_pts(G, ['O', '(1,2)', '(4,4)'])

# Coordinate axes
plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.xlabel('x')
plt.ylabel('y')
plt.title(r'Regions under the parabola $y^2=4x$')

plt.xlim(-0.5, 4.5)
plt.ylim(-0.5, 5)
plt.grid(True)
plt.legend()

plt.savefig('s1242.png', dpi=300, bbox_inches='tight')
#s.system("termux-open s1242.png")
plt.show()
