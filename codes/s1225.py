import numpy as np
import matplotlib.pyplot as plt
import os

from CoordGeo.line.funcs import line_gen_num
from CoordGeo.plotting.funcs import label_pts

# Define the function
def f(x):
    return x + 1/x

# Function to generate curve using CoordGeo
def generate_curve(x_values):

    X = np.zeros((2, 0))

    for i in range(len(x_values)-1):

        A = np.array([
            [x_values[i]],
            [f(x_values[i])]
        ])

        B = np.array([
            [x_values[i+1]],
            [f(x_values[i+1])]
        ])

        pts = line_gen_num(A, B, 2)

        if i == 0:
            X = pts
        else:
            X = np.hstack((X, pts[:, 1:]))

    return X


# Generate points on both branches
x1 = np.linspace(-4, -0.08, 500)
x2 = np.linspace(0.08, 4, 500)

X1 = generate_curve(x1)
X2 = generate_curve(x2)

# Plot the function
plt.plot(X1[0], X1[1],
         label=r'$f(x)=x+\frac{1}{x}$')

plt.plot(X2[0], X2[1],
         color='C0')

# Local maximum and minimum points
G = np.array([
    [-1, 1],
    [-2, 2]
])

# Mark maximum and minimum
plt.scatter(G[0], G[1],
            color='red', s=65, zorder=5)

# Label points using CoordGeo
label_pts(G, [
    'Local Maximum (-1,-2)',
    'Local Minimum (1,2)'
])

# Vertical asymptote
plt.axvline(0, color='black',
            linestyle='--',
            label='x = 0 (Asymptote)')

# Coordinate axes
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)

# Graph settings
plt.xlabel('$x$')
plt.ylabel('$f(x)$')

plt.xlim(-4, 4)
plt.ylim(-6, 6)

plt.xticks(np.arange(-4, 5, 1))
plt.yticks(np.arange(-6, 7, 1))

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.title(r'Graph of $f(x)=x+\frac{1}{x}$')

plt.savefig('s1225.png',
            dpi=300, bbox_inches='tight')

#os.system("termux-open s1225.png")
plt.show()
