#include <stdio.h>
#include <math.h>

int main()
{
    double sin60 = sqrt(3.0) / 2.0;
    double cos30 = sqrt(3.0) / 2.0;
    double cos60 = 1.0 / 2.0;
    double sin30 = 1.0 / 2.0;

    double lhs = sin(90.0 * 3.141592653589793 / 180.0);
    double rhs = sin60 * cos30 + cos60 * sin30;

    printf("========== QUESTION 23 (B) ==========\n\n");

    printf("Given: A = 60 degrees, B = 30 degrees\n\n");

    printf("To verify:\n");
    printf("sin(A+B) = sin(A)*cos(B) + cos(A)*sin(B)\n\n");

    printf("Step 1: Calculate the LHS.\n");
    printf("LHS = sin(60 + 30)\n");
    printf("    = sin(90)\n");
    printf("    = 1\n\n");

    printf("Step 2: Calculate the RHS.\n");
    printf("RHS = sin(60)*cos(30) + cos(60)*sin(30)\n");
    printf("    = (sqrt(3)/2)*(sqrt(3)/2) + (1/2)*(1/2)\n");
    printf("    = 3/4 + 1/4\n");
    printf("    = 1\n\n");

    printf("LHS = %.2f\n", lhs);
    printf("RHS = %.2f\n\n", rhs);

    if (fabs(lhs - rhs) < 1e-9)
        printf("Hence proved: LHS = RHS.\n");
    else
        printf("The identity could not be verified.\n");

    printf("=====================================\n");

    return 0;
}
