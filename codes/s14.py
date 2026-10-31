import matplotlib.pyplot as plt
import numpy as np
import os
# Question 15: Largest cone inscribed in a cube

# 1. Define dimensions
edge = 2
r = edge / 2
h = edge

# 2. Calculate the volume of the cone
volume = (1 / 3) * np.pi * r**2 * h

# 3. Print the complete solution in the terminal
print("=" * 45)
print("          QUESTION 14 - SOLUTION")
print("=" * 45)

print("\nGiven:")
print(f"Edge of the cube = {edge} cm")
print(f"Radius of the cone = {r} cm")
print(f"Height of the cone = {h} cm")

print("\nStep 1: Formula for the volume of a cone")
print("Volume = (1/3) * pi * r^2 * h")

print("\nStep 2: Substitute the values")
print(f"Volume = (1/3) * pi * ({r})^2 * {h}")

print("\nStep 3: Simplify")
print(f"Volume = (1/3) * pi * {r**2} * {h}")
print(f"Volume = {volume:.4f} cm^3")

print("\nFinal Answer:")
print(f"Volume of the cone = (2*pi/3) cm^3")
print(f"Approximate volume = {volume:.4f} cm^3")

print("=" * 45)

# 4. Initialize a 3D figure
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection="3d")

# 5. Draw the wireframe outline of the cube
for x in [0, edge]:
    for y in [0, edge]:
        ax.plot([x, x], [y, y], [0, edge],
                color="gray", linestyle="--", alpha=0.5)
        ax.plot([x, x], [0, edge], [y, y],
                color="gray", linestyle="--", alpha=0.5)
        ax.plot([0, edge], [x, x], [y, y],
                color="gray", linestyle="--", alpha=0.5)

# 6. Generate coordinates for the cone
z = np.linspace(0, h, 100)
theta = np.linspace(0, 2 * np.pi, 100)
theta_grid, z_grid = np.meshgrid(theta, z)

# Radius decreases linearly toward the vertex
r_z = r * (1 - z_grid / h)

x_cone = r + r_z * np.cos(theta_grid)
y_cone = r + r_z * np.sin(theta_grid)

# 7. Draw the cone surface
ax.plot_surface(
    x_cone, y_cone, z_grid,
    color="cyan", alpha=0.4, edgecolor="none"
)

# 8. Highlight the circular base
x_base = r + r * np.cos(theta)
y_base = r + r * np.sin(theta)

ax.plot(
    x_base, y_base, np.zeros_like(x_base),
    color="blue", linewidth=2.5,
    label="Cone base (r = 1 cm)"
)

# 9. Add labels and title
ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")
ax.set_zlabel("Z (cm)")
ax.set_title("Largest Cone Inscribed in a 2 cm Cube")

ax.set_xlim(0, edge)
ax.set_ylim(0, edge)
ax.set_zlim(0, edge)
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=22, azim=45)

ax.legend()

# 10. Save and display the diagram
plt.savefig("s14.png", dpi=300, bbox_inches="tight")
print("\nDiagram saved as s14.png")
#os.system("termux-open s14.png")
plt.show()
