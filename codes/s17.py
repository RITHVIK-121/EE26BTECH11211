import numpy as np
import matplotlib.pyplot as plt
import os
# Question 21: Solve using the matrix method

# Given equations:
# 7x - 2y = 5
# 8x + 7y = 15

# Matrix equation AX = B
A = np.array([
    [7, -2],
    [8,  7]
], dtype=float)

B = np.array([5, 15], dtype=float)


print("\nStep 1: Write the equations")
print("7x - 2y = 5")
print("8x + 7y = 15")

print("\nStep 2: Write AX = B")
print("\nA =")
print(A)

print("\nX = [x, y]^T")
print("\nB =")
print(B)

print("\nStep 3: Matrix equation")
print("AX = B")

print("\nStep 4: Find the determinant of A")
det_A = np.linalg.det(A)
print("det(A) = (7 * 7) - (-2 * 8)")
print(f"det(A) = {7*7 - (-2)*8}")
print(f"det(A) = {det_A:.0f}")

if abs(det_A) < 1e-10:
    print("\nThe matrix has no inverse.")
    print("The equations cannot be solved uniquely.")
else:
    print("\nStep 5: Find the inverse of A")
    A_inv = np.linalg.inv(A)
    print("A^(-1) =")
    print(np.round(A_inv, 4))

    print("\nStep 6: Calculate X = A^(-1)B")
    X = np.linalg.solve(A, B)

    x, y = X

    print("\nX =")
    print(np.round(X, 4))

    print("\nStep 7: Final answer")
    print(f"x = {x:.0f}")
    print(f"y = {y:.0f}")

    print("\nVerification:")
    print(f"7x - 2y = {7*x - 2*y:.0f}")
    print(f"8x + 7y = {8*x + 7*y:.0f}")

    print("\nFinal Answer: x = 1, y = -1")
    print("=" * 45)

    # Plot both linear equations
    x_values = np.linspace(-3, 5, 400)

    y1 = (7*x_values - 5) / 2
    y2 = (15 - 8*x_values) / 7

    plt.figure(figsize=(8, 6))
    plt.plot(x_values, y1, label="7x - 2y = 5")
    plt.plot(x_values, y2, label="8x + 7y = 15")

    plt.scatter(x, y, zorder=3, label=f"Intersection ({x:.0f}, {y:.0f})")
    plt.annotate(
        f"({x:.0f}, {y:.0f})",
        (x, y),
        xytext=(8, 8),
        textcoords="offset points"
    )

    plt.axhline(0, linewidth=1)
    plt.axvline(0, linewidth=1)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()

    plt.savefig("s17.png", dpi=300, bbox_inches="tight")
    print("\nGraph saved as s17.png")
#os.system("termux-open s17.png")
    plt.show()
