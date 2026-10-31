import numpy as np
import matplotlib.pyplot as plt
import os

from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

def f(x):
    return np.exp(x) - np.exp(-x) + x - np.arctan(x)

# Generate points
x = np.linspace(-3, 3, 500)
y = f(x)

# Plot the curve using line_gen_num
for i in range(len(x) - 1):
    A = np.array([[x[i]], [y[i]]])
    B = np.array([[x[i+1]], [y[i+1]]])

    line = line_gen_num(A, B, 2)
    plt.plot(line[0, :], line[1, :], 'b')

# Mark the origin
G = np.array([[0], [0]])
label_pts(G, ['O'])

plt.scatter(0, 0, color='red', zorder=5)

# Coordinate axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(r'$f(x)=e^x-e^{-x}+x-\tan^{-1}x$')

plt.grid(True)
plt.xlim(-3, 3)
plt.ylim(-25, 25)

plt.savefig('s1227.png', dpi=300, bbox_inches='tight')
#os.system("termux-open s1227.png")
plt.show()
