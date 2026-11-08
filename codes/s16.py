import numpy as np
import matplotlib.pyplot as plt
import os

from CoordGeo.line.funcs import line_gen_num


# Question 17: Find the other end of a diameter

# Given coordinates
center = (2, 0)
A = (6, 0)

# Calculate the other endpoint using the midpoint formula
h, k = center
x1, y1 = A

x2 = 2 * h - x1
y2 = 2 * k - y1

B = (x2, y2)

# Calculate the radius
radius = np.sqrt((x1 - h)**2 + (y1 - k)**2)


# Print the solution in the terminal
print("=" * 45)
print("          QUESTION 16 - SOLUTION")
print("=" * 45)

print("\nGiven:")
print(f"Centre of the circle = {center}")
print(f"One end of the diameter A = {A}")

print("\nStep 1: Use the midpoint formula")
print("Centre = ((x1 + x2)/2, (y1 + y2)/2)")

print("\nStep 2: Substitute the coordinates")
print(f"2 = (6 + x2)/2")
print(f"4 = 6 + x2")
print(f"x2 = 4 - 6 = {x2}")

print("\nFor the y-coordinate:")
print(f"0 = (0 + y2)/2")
print(f"y2 = {y2}")

print("\nStep 3: Write the other endpoint")
print(f"B = ({x2}, {y2})")

print("\nFinal Answer: (-2, 0)")
print("Correct Option: (c)")
print("=" * 45)


# Generate circle coordinates
theta = np.linspace(0, 2 * np.pi, 500)

circle_x = h + radius * np.cos(theta)
circle_y = k + radius * np.sin(theta)


# Convert coordinates into column vectors
# Generate the circle using CoordGeo
circle = np.zeros((2, 0))

for i in range(len(theta) - 1):

    P = np.array([
        [circle_x[i]],
        [circle_y[i]]
    ])

    Q = np.array([
        [circle_x[i + 1]],
        [circle_y[i + 1]]
    ])

    segment = line_gen_num(P, Q, 2)

    circle = np.hstack((circle, segment[:, :1]))

# Add the final point to complete the circle
circle = np.hstack((
    circle,
    np.array([[circle_x[-1]], [circle_y[-1]]])
))


# Generate diameter AB using CoordGeo
A1 = np.array([[x1], [y1]])
B1 = np.array([[x2], [y2]])

diameter = line_gen_num(B1, A1, 2)


# Create figure
fig, ax = plt.subplots(figsize=(8, 8))


# Plot circle
ax.plot(
    circle[0, :],
    circle[1, :],
    label="Circle"
)


# Plot diameter
ax.plot(
    diameter[0, :],
    diameter[1, :],
    linestyle="--",
    label="Diameter AB"
)


# Mark the centre and diameter endpoints
ax.scatter(
    [h, x1, x2],
    [k, y1, y2],
    zorder=3
)


# Label the points
ax.annotate(
    "Centre O (2, 0)",
    (h, k),
    xytext=(8, 10),
    textcoords="offset points"
)

ax.annotate(
    "A (6, 0)",
    (x1, y1),
    xytext=(5, 10),
    textcoords="offset points"
)

ax.annotate(
    "B (-2, 0)",
    (x2, y2),
    xytext=(-55, 10),
    textcoords="offset points"
)


# Set axes and grid
ax.axhline(0, linewidth=1)
ax.axvline(0, linewidth=1)

ax.set_xlabel("X-coordinate")
ax.set_ylabel("Y-coordinate")

ax.set_title("Question 17: Circle and Its Diameter")

ax.set_aspect("equal", adjustable="box")
ax.grid(True)
ax.legend()

ax.set_xlim(-3, 7)
ax.set_ylim(-5, 5)


# Save the image
plt.savefig("s16.png", dpi=300, bbox_inches="tight")

print("\nCircle diagram saved as s16.png")

plt.show()
