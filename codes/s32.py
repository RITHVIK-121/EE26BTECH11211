import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon
import os

from CoordGeo.line.funcs import line_gen_num

# Question 32
# Radius = 21 cm, central angle = 60 degrees

r = 21
theta_deg = 60
theta = np.radians(theta_deg)
pi = 22 / 7

# (i) Length of the arc
arc_length = (theta_deg / 360) * 2 * pi * r

# (ii) Area of the minor segment
sector_area = (theta_deg / 360) * pi * r**2
triangle_area = 0.5 * r**2 * np.sin(theta)
segment_area = sector_area - triangle_area

# Print solution
print("=" * 55)
print("       QUESTION 32 - SOLUTION")
print("=" * 55)

print("\nGiven:")
print(f"Radius r = {r} cm")
print(f"Central angle = {theta_deg} degrees")

print("\nPART (i): LENGTH OF THE ARC")
print("Formula: Arc length = (theta/360) * 2*pi*r")
print(f"= (60/360) * 2 * (22/7) * {r}")
print(f"= {arc_length:.2f} cm")

print("\nPART (ii): AREA OF THE MINOR SEGMENT")

print("\nStep 1: Find the area of the sector")
print("Sector area = (theta/360) * pi*r^2")
print(f"= (60/360) * (22/7) * {r}^2")
print(f"= {sector_area:.2f} cm^2")

print("\nStep 2: Find the area of the triangle")
print("Triangle area = (1/2)*r^2*sin(60 degrees)")
print(f"= (1/2)*{r}^2*sin(60 degrees)")
print(f"= {triangle_area:.2f} cm^2")

print("\nStep 3: Find the area of the minor segment")
print("Minor segment area = Sector area - Triangle area")
print(f"= {sector_area:.2f} - {triangle_area:.2f}")
print(f"= {segment_area:.2f} cm^2")

print("\n" + "=" * 55)
print("                 FINAL ANSWERS")
print(f"(i) Arc length = {arc_length:.2f} cm")
print(f"(ii) Minor segment area = {segment_area:.2f} cm^2")
print("=" * 55)


# Generate a line segment using CoordGeo
def draw_line(ax, P, Q, **kwargs):
    P_vec = np.array([[P[0]], [P[1]]])
    Q_vec = np.array([[Q[0]], [Q[1]]])

    line = line_gen_num(P_vec, Q_vec, 2)

    ax.plot(
        line[0, :],
        line[1, :],
        **kwargs
    )


# Generate a connected curved path using CoordGeo
def draw_path(ax, points, **kwargs):
    segments = []

    for i in range(len(points) - 1):
        P_vec = np.array([[points[i][0]], [points[i][1]]])
        Q_vec = np.array([[points[i + 1][0]], [points[i + 1][1]]])

        segment = line_gen_num(P_vec, Q_vec, 2)

        if i == 0:
            segments.append(segment)
        else:
            segments.append(segment[:, 1:])

    path = np.hstack(segments)

    ax.plot(
        path[0, :],
        path[1, :],
        **kwargs
    )


# --------------------------------------------------
# Draw the circle and shade the minor segment
# --------------------------------------------------

fig, ax = plt.subplots(figsize=(9, 9))

# Circle with centre O
circle = Circle((0, 0), r, fill=False, linewidth=2)
ax.add_patch(circle)

# Points on the circle
A = (r, 0)
B = (r * np.cos(theta), r * np.sin(theta))

# Shade the minor segment bounded by the chord and arc
arc_angles = np.linspace(0, theta, 200)
arc_x = r * np.cos(arc_angles)
arc_y = r * np.sin(arc_angles)

segment_points = [(0, 0)] + list(zip(arc_x, arc_y))
sector = Polygon(
    segment_points,
    closed=True,
    alpha=0.15
)
ax.add_patch(sector)

# Shade the minor segment with the chord boundary
segment_polygon_points = [(A[0], A[1]), (B[0], B[1])] + list(
    zip(arc_x[::-1], arc_y[::-1])
)

segment_polygon = Polygon(
    segment_polygon_points,
    closed=True,
    alpha=0.45,
    label="Minor segment"
)
ax.add_patch(segment_polygon)

# Draw radii and chord using CoordGeo
draw_line(ax, (0, 0), A, linewidth=2, label="Radius")
draw_line(ax, (0, 0), B, linewidth=2)
draw_line(ax, A, B, linewidth=2, label="Chord")

# Draw the highlighted minor arc using CoordGeo
arc_points = list(zip(arc_x, arc_y))
draw_path(
    ax,
    arc_points,
    linewidth=3,
    label="Minor arc"
)

# Mark the centre and endpoints
ax.scatter([0, A[0], B[0]], [0, A[1], B[1]], zorder=4)

ax.annotate("O (Centre)", (0, 0),
            xytext=(-25, -18), textcoords="offset points")
ax.annotate("A", A, xytext=(7, -15), textcoords="offset points")
ax.annotate("B", B, xytext=(-15, 8), textcoords="offset points")

# Draw a small arc to indicate the 60-degree angle
angle_radius = 4
angle_x = angle_radius * np.cos(arc_angles)
angle_y = angle_radius * np.sin(arc_angles)
ax.plot(angle_x, angle_y, linestyle="--", linewidth=1.5)

ax.text(
    5.2 * np.cos(theta / 2),
    5.2 * np.sin(theta / 2),
    "60 degrees",
    ha="center"
)

# Add radius and arc labels
ax.text(11, -2.5, "r = 21 cm")
ax.text(11, 8, f"Arc length = {arc_length:.2f} cm")
ax.text(5, 3, "Minor segment")

ax.set_title(
    "Question 32: Arc Length and Area of Minor Segment",
    pad=18
)
ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")
ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-25, 27)
ax.set_ylim(-25, 27)
ax.grid(True)
ax.legend(loc="lower left")

# Save and display the diagram
plt.savefig("s32.png", dpi=300, bbox_inches="tight")
print("\nDiagram saved as s32.png")
#os.system("termux-open s32.png")

plt.show()
