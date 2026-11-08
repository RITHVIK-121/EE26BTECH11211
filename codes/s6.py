import matplotlib.pyplot as plt
import numpy as np
import math
import os

from CoordGeo.line.funcs import line_gen_num

# Coordinates of the triangle
A = (5, -6)
B = (6, 4)
C = (0, 0)

# D is the midpoint of BC because AD is a median
D = ((B[0] + C[0]) / 2, (B[1] + C[1]) / 2)

# Calculate the length of median AD
AD = math.sqrt((A[0] - D[0])**2 + (A[1] - D[1])**2)

# Print the solution in the terminal
print("========== QUESTION 6 ==========")
print("Given: A(5, -6), B(6, 4), C(0, 0)")
print("AD is a median of triangle ABC.")
print()

print("Step 1: Find the midpoint D of BC.")
print("D = ((6 + 0)/2, (4 + 0)/2)")
print(f"D = ({D[0]:.0f}, {D[1]:.0f})")
print()

print("Step 2: Apply the distance formula.")
print("AD = sqrt((5 - 3)^2 + (-6 - 2)^2)")
print("   = sqrt(2^2 + (-8)^2)")
print("   = sqrt(4 + 64)")
print("   = sqrt(68) = 2sqrt(17)")
print(f"AD = {AD:.2f} units")
print()

print("Final Answer: sqrt(68) units")
print("Correct Option: (a)")
print("================================")


# Convert coordinates into column vectors for CoordGeo
A1 = np.array([[A[0]], [A[1]]])
B1 = np.array([[B[0]], [B[1]]])
C1 = np.array([[C[0]], [C[1]]])
D1 = np.array([[D[0]], [D[1]]])


# Generate triangle ABC using CoordGeo
AB = line_gen_num(A1, B1, 2)
BC = line_gen_num(B1, C1, 2)
CA = line_gen_num(C1, A1, 2)

# Join the three sides without duplicating common points
triangle = np.hstack((AB, BC[:, 1:], CA[:, 1:]))


# Generate median AD using CoordGeo
median = line_gen_num(A1, D1, 2)


# Draw triangle ABC and median AD
fig, ax = plt.subplots(figsize=(8, 7))

ax.plot(
    triangle[0, :],
    triangle[1, :],
    marker="o",
    label="Triangle ABC"
)

ax.plot(
    median[0, :],
    median[1, :],
    linestyle="--",
    marker="o",
    label="Median AD"
)


# Label the vertices and midpoint
for point, name in [(A, "A"), (B, "B"), (C, "C"), (D, "D")]:
    ax.annotate(
        f"{name}{point}",
        point,
        xytext=(5, 5),
        textcoords="offset points"
    )


ax.set_title("Question 6: Median AD")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)
ax.axhline(0)
ax.axvline(0)
ax.legend()
ax.set_aspect("equal", adjustable="datalim")


# Save the diagram as s6.png
plt.savefig("s6.png", dpi=200, bbox_inches="tight")

plt.show()

print("Diagram saved as s6.png")
