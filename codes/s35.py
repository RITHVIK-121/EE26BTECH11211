import numpy as np
import matplotlib.pyplot as plt

from CoordGeo.line.funcs import line_gen_num

# Coordinates of triangle ABC
A = (1, 1)
B = (8, 1)
C = (3, 7)

# Points D and E divide AB and AC proportionally
D = (4, 1)

# Choose E on AC so that DE is parallel to BC
t = (D[0] - A[0]) / (B[0] - A[0])
E = (A[0] + t * (C[0] - A[0]),
     A[1] + t * (C[1] - A[1]))


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


# Create the figure
fig, ax = plt.subplots(figsize=(8, 7))

# Draw triangle ABC using CoordGeo
triangle = generate_path([A, B, C, A])

ax.plot(
    triangle[0, :],
    triangle[1, :],
    linewidth=2,
    color="black",
    label="Triangle ABC"
)

# Draw DE parallel to BC using CoordGeo
DE = generate_path([D, E])

ax.plot(
    DE[0, :],
    DE[1, :],
    linewidth=2.5,
    color="red",
    label="DE || BC"
)

# Mark points
points = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E
}

for name, point in points.items():
    ax.scatter(point[0], point[1], color="black", zorder=3)
    ax.annotate(
        name,
        point,
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=12
    )

# Add theorem text
ax.text(
    4.0, 6.0,
    "DE || BC",
    fontsize=11,
    ha="center"
)

ax.set_title("Question 35: Basic Proportionality Theorem")
ax.set_xlabel("X-coordinate")
ax.set_ylabel("Y-coordinate")

ax.set_aspect("equal", adjustable="box")
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()

# Save the image
plt.savefig("s35.png", dpi=300, bbox_inches="tight")
print("Diagram saved as s35.png")

# Display the diagram
plt.show()
