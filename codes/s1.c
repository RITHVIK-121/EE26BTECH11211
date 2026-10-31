#include <stdio.h>
#include <math.h>

int main()
{
    printf("========================================\n");
    printf("  CBSE CLASS 10 MATHEMATICS - Q1\n");
    printf("========================================\n\n");

    printf("Given polynomial:\n");
    printf("p(x) = 2x^2 - k*sqrt(2)*x + 1\n\n");

    printf("Sum of zeroes = sqrt(2)\n\n");

    printf("Step 1: Use the formula for the sum of zeroes.\n");
    printf("Sum of zeroes = -Coefficient of x / Coefficient of x^2\n\n");

    printf("Step 2: Substitute the coefficients.\n");
    printf("Sum of zeroes = -(-k*sqrt(2)) / 2\n");
    printf("              = k*sqrt(2) / 2\n\n");

    printf("Step 3: Given that the sum of zeroes is sqrt(2).\n");
    printf("k*sqrt(2) / 2 = sqrt(2)\n\n");

    printf("Step 4: Multiply both sides by 2.\n");
    printf("k*sqrt(2) = 2*sqrt(2)\n\n");

    printf("Step 5: Divide both sides by sqrt(2).\n");
    printf("k = 2\n\n");

    printf("========================================\n");
    printf("Final Answer: k = 2\n");
    printf("Correct Option: (b)\n");
    printf("========================================\n");

    return 0;
}
