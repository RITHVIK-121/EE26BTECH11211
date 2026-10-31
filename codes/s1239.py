import numpy as np
import matplotlib.pyplot as plt
import os

from CoordGeo.line.funcs import line_gen_num

# Points A and B
A = np.array([[2], [3], [4]])
B = np.array([[4], [5], [8]])

# Midpoint
M = (A + B) / 2

# Direction vectors of given lines
d1 = np.array([[3], [-16], [7]])
d2 = np.array([[3], [8], [-5]])

# Direction vector perpendicular to both
d = np.cross(d1.flatten(), d2.flatten()).reshape(3, 1)

# Generate line segment AB
AB = line_gen_num(A, B, 100)

# Generate required line through M
P = M - 3*d
Q = M + 3*d
L = line_gen_num(P, Q, 100)

# Generate first given line
P1 = np.array([[8], [-19], [10]])
Q1 = P1 + 0.4*d1
L1 = line_gen_num(P1 - 3*d1, Q1 + 3*d1, 100)

# Generate second given line
P2 = np.array([[15], [29], [5]])
Q2 = P2 + 0.4*d2
L2 = line_gen_num(P2 - 3*d2, Q2 + 3*d2, 100)

# 3D Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(AB[0], AB[1], AB[2], label='Line segment AB')
ax.plot(L[0], L[1], L[2], label='Required perpendicular line')
ax.plot(L1[0], L1[1], L1[2], label='First given line')
ax.plot(L2[0], L2[1], L2[2], label='Second given line')

# Mark points
ax.scatter(A[0], A[1], A[2], color='red')
ax.scatter(B[0], B[1], B[2], color='red')
ax.scatter(M[0], M[1], M[2], color='black')

# Labels
ax.text(2, 3, 4, 'A')
ax.text(4, 5, 8, 'B')
ax.text(3, 4, 6, 'M')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_title('Question 39 - Three Dimensional Plot')
ax.legend()
ax.grid(True)

plt.savefig('s1239.png', dpi=300, bbox_inches='tight')
#os.system("termux-open s1239.png")
plt.show()
