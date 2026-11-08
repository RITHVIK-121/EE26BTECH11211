import numpy as np
import matplotlib.pyplot as plt
import os

from CoordGeo.line.funcs import line_gen_num

# Coordinates of the points
A = (1, 2)
B = (2, 3)
P = (8/5, 13/5)

# Plot the line segment AB using CoordGeo
A_vec = np.array([[A[0]], [A[1]]])
B_vec = np.array([[B[0]], [B[1]]])

AB = line_gen_num(A_vec, B_vec, 100)

plt.plot(
    AB[0, :],
    AB[1, :],
    'b-',
    label='Line segment AB'
)

# Plot the points
plt.scatter(A[0], A[1], color='red', s=70)
plt.scatter(B[0], B[1], color='red', s=70)
plt.scatter(P[0], P[1], color='green', s=70)

# Label the points
plt.annotate('A (1, 2)', A, xytext=(-35, -15),
             textcoords='offset points')

plt.annotate('B (2, 3)', B, xytext=(8, 5),
             textcoords='offset points')

plt.annotate('P (8/5, 13/5)', P, xytext=(8, -20),
             textcoords='offset points')

# Draw coordinate axes
plt.axhline(y=0, color='black', linewidth=0.8)
plt.axvline(x=0, color='black', linewidth=0.8)

# Add grid
plt.grid(True, linestyle='--', alpha=0.6)

# Set axis limits
plt.xlim(0, 3)
plt.ylim(0, 4)

# Add labels and title
plt.xlabel('x-coordinate')
plt.ylabel('y-coordinate')
plt.title('Question 24: Section Formula')

# Add legend
plt.legend()

# Keep equal scaling on both axes
plt.gca().set_aspect('equal', adjustable='box')

# Save the image before displaying it
plt.savefig('s24.png', dpi=300, bbox_inches='tight')
#os.system("termux-open s24.png")

# Display the graph
plt.show()
