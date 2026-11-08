import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import os

from CoordGeo.line.funcs import line_gen_num

# Question 37
# Pole height = 6 m
# Angle of elevation to the top of pole = 60 degrees
# Angle of depression from top of tower to P = 45 degrees
# Use sqrt(3) = 1.73

pole_height = 6
tan60 = 1.73
tan45 = 1

# Let tower height = h and horizontal distance = x
# tan(45) = h/x => x = h
# tan(60) = (h + 6)/x
# Therefore, sqrt(3) = (h + 6)/h

tower_height = pole_height / (tan60 - tan45)
distance = tower_height
total_height = tower_height + pole_height

# Print the solution
print("=" * 55)
print("       QUESTION 37 - TOWER AND POLE")
print("=" * 55)

print("\nGiven:")
print("Height of pole = 6 m")
print("Angle of elevation to top of pole = 60 degrees")
print("Angle of depression from top of tower = 45 degrees")
print("Use sqrt(3) = 1.73")

print("\nLet:")
print("Height of tower = h metres")
print("Distance from P to foot of tower = x metres")

print("\nStep 1: Use the angle of depression")
print("tan(45 degrees) = h/x")
print("1 = h/x")
print("Therefore, x = h")

print("\nStep 2: Use the angle of elevation to the top of the pole")
print("tan(60 degrees) = (h + 6)/x")
print("1.73 = (h + 6)/x")

print("\nSince x = h:")
print("1.73 = (h + 6)/h")
print("1.73h = h + 6")
print("0.73h = 6")
print(f"h = 6/0.73 = {tower_height:.2f} m")

print("\nStep 3: Find the horizontal distance")
print("x = h")
print(f"x = {distance:.2f} m")

print("\n" + "=" * 55)
print("                 FINAL ANSWERS")
print(f"Height of tower = {tower_height:.2f} m")
print(f"Distance from P to tower = {distance:.2f} m")
print(f"Total height of tower and pole = {total_height:.2f} m")
print("=" * 55)


# Generate a line using CoordGeo
def draw_line(ax, P, Q, **kwargs):
    P_vec = np.array([[P[0]], [P[1]]])
    Q_vec = np.array([[Q[0]], [Q[1]]])

    line = line_gen_num(P_vec, Q_vec, 100)

    ax.plot(
        line[0, :],
        line[1, :],
        **kwargs
    )


# --------------------------------------------------
# Draw the diagram
# --------------------------------------------------

# Coordinates
P = (0, 0)
B = (distance, 0)              # Foot of tower
T = (distance, tower_height)   # Top of tower
U = (distance, total_height)   # Top of pole

fig, ax = plt.subplots(figsize=(10, 7))

# Ground
draw_line(
    ax, (-1, 0), (distance + 2, 0),
    color="black",
    linewidth=2
)

# Tower
draw_line(
    ax, B, T,
    color="black",
    linewidth=4,
    label="Tower"
)

# Pole on top of tower
draw_line(
    ax, T, U,
    color="red",
    linewidth=4,
    label="Pole (6 m)"
)

# Line of sight from P to top of pole
draw_line(
    ax, P, U,
    linestyle="--",
    color="blue",
    linewidth=2,
    label="Line of sight"
)

# Horizontal line from P to top of tower (for angle of depression)
draw_line(
    ax, P, T,
    linestyle=":",
    color="gray",
    linewidth=1.5
)

# Mark points
for label, point in [
    ("P", P),
    ("B", B),
    ("T", T),
    ("U", U)
]:
    ax.scatter(point[0], point[1], color="black", zorder=4)
    ax.annotate(label, point, xytext=(6, 5),
                textcoords="offset points", fontsize=12)

# Dimension labels
ax.annotate(
    f"Tower height = {tower_height:.2f} m",
    (distance, tower_height / 2),
    xytext=(15, 0),
    textcoords="offset points"
)

ax.annotate(
    "Pole = 6 m",
    (distance, tower_height + pole_height / 2),
    xytext=(15, 0),
    textcoords="offset points",
    color="red"
)

ax.annotate(
    f"Distance = {distance:.2f} m",
    (distance / 2, 0),
    xytext=(0, 10),
    textcoords="offset points",
    ha="center"
)

# Angle of elevation at P
angle = np.degrees(np.arctan2(total_height, distance))
angle_arc = Arc(P, 2, 2, angle=0, theta1=0, theta2=angle,
                color="green", linewidth=2)
ax.add_patch(angle_arc)
ax.text(1.1, 0.5, "60 degrees", color="green")

# Angle of depression at T
ax.text(
    distance - 2.5,
    tower_height + 0.4,
    "45 degrees",
    color="purple"
)

# Formatting
ax.set_title("Question 37: Tower and Pole")
ax.set_xlabel("Horizontal distance (m)")
ax.set_ylabel("Height (m)")
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend(loc="upper left")

ax.set_xlim(-1, distance + 4)
ax.set_ylim(-1, total_height + 3)

plt.tight_layout()

# Save the image
plt.savefig("s37.png", dpi=300, bbox_inches="tight")
print("\nDiagram saved as s37.png")
#os.system("termux-open s37.png")

# Display the image
plt.show()
