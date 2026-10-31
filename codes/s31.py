    
    


    
  
import numpy as np
import matplotlib.pyplot as plt
import os
# Question 31: Hollow right circular cylinder

# Given values
height = 14
difference = 1
volume = 176
pi = 22 / 7

# Step 1: Calculate the sum of the radii
# Volume = pi * h * (R^2 - r^2)
# R^2 - r^2 = (R-r)(R+r)
# R-r = 1

sum_radii = volume / (pi * height * difference)

# Step 2: Calculate outer and inner radii
outer_radius = (sum_radii + difference) / 2
inner_radius = (sum_radii - difference) / 2

# Print solution
print("=" * 55)
print("       QUESTION 31 - HOLLOW CYLINDER")
print("=" * 55)

print("\nGiven:")
print("Height of cylinder = 14 cm")
print("Difference between outer and inner radii = 1 cm")
print("Volume of metal = 176 cm^3")

print("\nStep 1: Use the formula for the volume of metal")
print("V = pi * h * (R^2 - r^2)")

print("\nStep 2: Factorise")
print("V = pi * h * (R-r)(R+r)")

print("\nSubstitute the given values:")
print("176 = (22/7) * 14 * 1 * (R+r)")
print("176 = 44 * (R+r)")
print("R+r = 176/44")
print(f"R+r = {sum_radii:.0f}")

print("\nStep 3: Solve the two equations")
print("R+r = 4")
print("R-r = 1")
print("\nAdding both equations:")
print("2R = 5")
print(f"R = {outer_radius:.1f} cm")

print("\nSubtracting the equations:")
print("2r = 3")
print(f"r = {inner_radius:.1f} cm")

print("\nStep 4: Verify the volume")
calculated_volume = pi * height * (
    outer_radius**2 - inner_radius**2
)
print(f"V = (22/7) * 14 * ({outer_radius:.1f}^2 - {inner_radius:.1f}^2)")
print(f"V = {calculated_volume:.0f} cm^3")

print("\n" + "=" * 55)
print("                 FINAL ANSWER")
print(f"Outer radius = {outer_radius:.1f} cm")
print(f"Inner radius = {inner_radius:.1f} cm")
print("=" * 55)

# --------------------------------------------------
# Draw a 3D hollow cylinder
# --------------------------------------------------

fig = plt.figure(figsize=(11, 9))
ax = fig.add_subplot(111, projection="3d")

theta = np.linspace(0, 2 * np.pi, 160)
z = np.linspace(0, height, 100)
Theta, Z = np.meshgrid(theta, z)

# Outer curved surface: light and transparent
X_outer = outer_radius * np.cos(Theta)
Y_outer = outer_radius * np.sin(Theta)

ax.plot_surface(
    X_outer, Y_outer, Z,
    color="skyblue",
    alpha=0.20,
    edgecolor="none",
    shade=False
)

# Inner curved surface: contrasting and more opaque
X_inner = inner_radius * np.cos(Theta)
Y_inner = inner_radius * np.sin(Theta)

ax.plot_surface(
    X_inner, Y_inner, Z,
    color="orange",
    alpha=0.85,
    edgecolor="none",
    shade=True
)

# Top and bottom annular surfaces
radial = np.linspace(inner_radius, outer_radius, 40)
Theta_ring, Radial = np.meshgrid(theta, radial)

for z_level in [0, height]:
    X_ring = Radial * np.cos(Theta_ring)
    Y_ring = Radial * np.sin(Theta_ring)
    Z_ring = np.full_like(X_ring, z_level)

    ax.plot_surface(
        X_ring, Y_ring, Z_ring,
        color="lightgreen",
        alpha=0.75,
        edgecolor="none",
        shade=False
    )

# Draw clear boundary circles for both radii
for radius, color, width in [
    (outer_radius, "blue", 2.5),
    (inner_radius, "darkred", 2.5)
]:
    circle_x = radius * np.cos(theta)
    circle_y = radius * np.sin(theta)

    ax.plot(circle_x, circle_y, np.zeros_like(theta),
            color=color, linewidth=width)
    ax.plot(circle_x, circle_y, np.full_like(theta, height),
            color=color, linewidth=width)

# Draw radius indicators in different directions
# Outer radius along positive X direction
ax.plot(
    [0, outer_radius], [0, 0], [height, height],
    color="blue", linewidth=3
)

# Inner radius along positive Y direction
ax.plot(
    [0, 0], [0, inner_radius], [height, height],
    color="darkred", linewidth=3
)

# Radius labels placed away from one another
ax.text(
    outer_radius / 2, -0.45, height + 0.8,
    "Outer radius = 2.5 cm",
    color="blue",
    fontsize=10,
    ha="center"
)

ax.text(
    -0.2, inner_radius / 2, height + 0.8,
    "Inner radius = 1.5 cm",
    color="darkred",
    fontsize=10,
    ha="center"
)

# Dimension line for height
ax.plot(
    [outer_radius + 0.7, outer_radius + 0.7],
    [0, 0],
    [0, height],
    color="black",
    linestyle="--",
    linewidth=2
)

ax.text(
    outer_radius + 0.9, 0, height / 2,
    "Height = 14 cm",
    color="black"
)

# Title and formatting
ax.set_title(
    "Question 31: Hollow Right Circular Cylinder",
    pad=25,
    fontsize=13
)

ax.set_xlabel("X (cm)")
ax.set_ylabel("Y (cm)")
ax.set_zlabel("Height (cm)")

ax.set_xlim(-3.8, 4.8)
ax.set_ylim(-3.8, 3.8)
ax.set_zlim(0, 16)

ax.set_box_aspect((1, 1, 2))
ax.view_init(elev=25, azim=35)

plt.tight_layout()

# Save image
plt.savefig("s31.png", dpi=300, bbox_inches="tight")
print("\n3D diagram saved as s31.png")
#os.system("termux-open s31.png")
# Display image
plt.show()


