import matplotlib.pyplot as plt
import os
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

# Plot the rectangle ABCD
fig, ax = plt.subplots(figsize=(9, 9))

# Rectangle ABCD
rectangle_x = [A[0], B[0], C[0], D[0], A[0]]
rectangle_y = [A[1], B[1], C[1], D[1], A[1]]

ax.plot(rectangle_x, rectangle_y, marker="o",
        label="Rectangle ABCD")

# Quadrilateral PQRS
pqrs_x = [P[0], Q[0], R[0], S[0], P[0]]
pqrs_y = [P[1], Q[1], R[1], S[1], P[1]]

ax.plot(pqrs_x, pqrs_y, marker="o",
        label="Quadrilateral PQRS")

# Diagonals of PQRS
ax.plot([P[0], R[0]], [P[1], R[1]],
        linestyle="--", label="Diagonal PR")

ax.plot([Q[0], S[0]], [Q[1], S[1]],
        linestyle="--", label="Diagonal QS")

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
