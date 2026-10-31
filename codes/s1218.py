
import numpy as np
import matplotlib.pyplot as plt
import os

from CoordGeo.line.funcs import line_gen_num

from mpl_toolkits.mplot3d import Axes3D

# Origin
O = np.array([0, 0, 0]).reshape(3, 1)

# Direction cosines
alpha = np.radians(30)
beta = np.radians(120)

l = np.cos(alpha)
m = np.cos(beta)
n = 0

# Direction vector
B = np.array([l, m, n]).reshape(3, 1)

# Generate vector using CoordGeo
V = line_gen_num(O, B, 100)

# Create 3D figure
fig = plt.figure(figsize=(9, 8))
ax = fig.add_subplot(111, projection='3d')

# Coordinate axes
ax.quiver(0, 0, 0, 1.3, 0, 0,
          color='black', arrow_length_ratio=0.08)

ax.quiver(0, 0, 0, 0, 1.3, 0,
          color='black', arrow_length_ratio=0.08)

ax.quiver(0, 0, 0, 0, 0, 1.3,
          color='black', arrow_length_ratio=0.08)

# Axis labels
ax.text(1.4, 0, 0, 'X')
ax.text(0, 1.4, 0, 'Y')
ax.text(0, 0, 1.4, 'Z')

# Plot direction vector
ax.plot(V[0], V[1], V[2],
        color='red', linewidth=2.5,
        label='Direction vector')

# Mark endpoint
ax.scatter(B[0], B[1], B[2],
           color='red', s=40)

ax.text(l, m, n, ' A', fontsize=12)

# 30 degree angle arc in XY plane
t = np.linspace(-alpha, 0, 100)
r = 0.35

ax.plot(r*np.cos(t), r*np.sin(t),
        np.zeros(100), color='blue', linewidth=2)

ax.text(0.4, -0.12, 0, '30°', color='blue')

# 120 degree angle arc in XY plane
t = np.linspace(-alpha, np.pi/2, 100)

ax.plot(0.55*np.cos(t),
        0.55*np.sin(t),
        np.zeros(100),
        color='green', linewidth=2)

ax.text(0.15, 0.48, 0, '120°', color='green')

# 90 degree angle arc between vector and Z-axis
t = np.linspace(0, np.pi/2, 100)

v = np.array([l, m, 0])

arc = np.array([
    0.4*np.cos(t)*v[0],
    0.4*np.cos(t)*v[1],
    0.4*np.sin(t)
])

ax.plot(arc[0], arc[1], arc[2],
        color='purple', linewidth=2)

ax.text(0.1, -0.2, 0.4, '90°',
        color='purple')

# Origin
ax.scatter(0, 0, 0, color='black', s=30)
ax.text(0, 0, 0, ' O')

# Graph settings
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

ax.set_xlim(-0.3, 1.5)
ax.set_ylim(-1, 1.5)
ax.set_zlim(-0.3, 1.5)

ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=25, azim=-55)

plt.title('Direction Angles in 3D')
plt.savefig('s1218.png',
            dpi=300, bbox_inches='tight')
#os.system("termux-open s1218.png")
plt.show()

