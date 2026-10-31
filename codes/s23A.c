#include <stdio.h>
#include <math.h>

int main()
{
    double cos45 = 1.0 / sqrt(2.0);
    double sin30 = 1.0 / 2.0;
    double cos30 = sqrt(3.0) / 2.0;

    double term1 = 2.0 * sqrt(2.0) * cos45 * sin30;
    double term2 = 2.0 * sqrt(3.0) * cos30;
    double answer = term1 + term2;

    printf("========== QUESTION 23 (A) ==========\n\n");

    printf("Expression:\n");
    printf("2*sqrt(2)*cos(45)*sin(30) + 2*sqrt(3)*cos(30)\n\n");

    printf("Step 1: Use standard trigonometric values.\n");
    printf("cos(45) = 1/sqrt(2)\n");
    printf("sin(30) = 1/2\n");
    printf("cos(30) = sqrt(3)/2\n\n");

    printf("Step 2: Substitute the values.\n");
    printf("Term 1 = 2*sqrt(2)*(1/sqrt(2))*(1/2)\n");
    printf("       = 1\n\n");

    printf("Term 2 = 2*sqrt(3)*(sqrt(3)/2)\n");
    printf("       = 3\n\n");

    printf("Step 3: Add both terms.\n");
    printf("Answer = 1 + 3 = 4\n\n");

    printf("Final Answer = %.0f\n", answer);
    printf("=====================================\n");

    return 0;
}
