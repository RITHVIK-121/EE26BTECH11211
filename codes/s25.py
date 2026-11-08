import numpy as np
import matplotlib.pyplot as plt
import os

from CoordGeo.line.funcs import line_gen_num

# Question 26(B): Diagonals of PQRS bisect each other

# Coordinates of rectangle ABCD
A = (-1, -1)
B = (-1, 6)
C = (3, 6)
D = (3, -1)

# Function to calculate the midpoint
def midpoint(P, Q):
    return ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)

# Calculate midpoints
P = midpoint(A, B)
Q = midpoint(B, C)
R = midpoint(C, D)
S = midpoint(D, A)

# Function to find the midpoint of a diagonal
mid_PR = midpoint(P, R)
mid_QS = midpoint(Q, S)

# Print calculations in the terminal
print("=" * 50)
print("       QUESTION 25 - SOLUTION")
print("=" * 50)

print("\nGiven:")
print("A = (-1, -1)")
print("B = (-1, 6)")
print("C = (3, 6)")
print("D = (3, -1)")

print("\nStep 1: Find the midpoints")

print("\nP is the midpoint of AB:")
print(f"P = {P}")

print("\nQ is the midpoint of BC:")
print(f"Q = {Q}")

print("\nR is the midpoint of CD:")
print(f"R = {R}")

print("\nS is the midpoint of DA:")
print(f"S = {S}")

print("\nStep 2: Find the midpoint of diagonal PR")
print(f"Midpoint of PR = {mid_PR}")

print("\nStep 3: Find the midpoint of diagonal QS")
print(f"Midpoint of QS = {mid_QS}")

print("\nStep 4: Compare the midpoints")

if mid_PR == mid_QS:
    print("Midpoint of PR = Midpoint of QS")
    print("Therefore, the diagonals bisect each other.")
else:
    print("The diagonals do not bisect each other.")

print("\nHence proved.")
print("=" * 50)


# Generate a connected path using CoordGeo
def generate_path(points, num=100):
    segments = []

    for i in range(len(points) - 1):
        P_vec = np.array([[points[i][0]], [points[i][1]]])
        Q_vec = np.array([[points[i + 1][0]], [points[i + 1][1]]])

        segment = line_gen_num(P_vec, Q_vec, num)

        if i == 0:
            segments.append(segment)
        else:
            segments.append(segment[:, 1:])

    return np.hstack(segments)


# Plot the rectangle ABCD
fig, ax = plt.subplots(figsize=(9, 9))

# Rectangle ABCD
rectangle_points = [A, B, C, D, A]
rectangle = generate_path(rectangle_points)

ax.plot(
    rectangle[0, :],
    rectangle[1, :],
    marker="o",
    label="Rectangle ABCD"
)

# Quadrilateral PQRS
pqrs_points = [P, Q, R, S, P]
pqrs = generate_path(pqrs_points)

ax.plot(
    pqrs[0, :],
    pqrs[1, :],
    marker="o",
    label="Quadrilateral PQRS"
)

# Diagonals of PQRS
PR = generate_path([P, R])
QS = generate_path([Q, S])

ax.plot(
    PR[0, :],
    PR[1, :],
    linestyle="--",
    label="Diagonal PR"
)

ax.plot(
    QS[0, :],
    QS[1, :],
    linestyle="--",
    label="Diagonal QS"
)

# Mark all vertices
points = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "P": P,
    "Q": Q,
    "R": R,
    "S": S
}

for label, point in points.items():
    ax.annotate(
        f"{label} {point}",
        point,
        xytext=(7, 7),
        textcoords="offset points"
    )

# Mark the intersection of the diagonals
ax.scatter(
    mid_PR[0], mid_PR[1],
    marker="x", s=100,
    label="Intersection of diagonals"
)

ax.annotate(
    f"O {mid_PR}",
    mid_PR,
    xytext=(8, -15),
    textcoords="offset points"
)

# Formatting
ax.set_title("Question 25: Diagonals of PQRS")
ax.set_xlabel("X-coordinate")
ax.set_ylabel("Y-coordinate")

ax.axhline(0, linewidth=0.8)
ax.axvline(0, linewidth=0.8)

ax.set_xlim(-2, 4)
ax.set_ylim(-2, 7)
ax.set_aspect("equal", adjustable="box")

ax.grid(True)
ax.legend()

# Save the image
plt.savefig("s25.png", dpi=300, bbox_inches="tight")

print("\nImage saved as s25.png")
#os.system("termux-open s25.png")

# Display the diagram
plt.show()
