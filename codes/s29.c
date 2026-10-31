#include <stdio.h>

int main()
{
    int R, N;

    printf("========================================\n");
    printf("       QUESTION 29 - SOLUTION\n");
    printf("========================================\n");

    printf("\nLet Rashmi's present age = R years\n");
    printf("Let Nazma's present age = N years\n");

    printf("\nStep 1: Form the first equation\n");
    printf("Three years ago:\n");
    printf("R - 3 = 3(N - 3)\n");
    printf("R - 3 = 3N - 9\n");
    printf("R = 3N - 6\n");
    printf("R - 3N = -6     ...(1)\n");

    printf("\nStep 2: Form the second equation\n");
    printf("Ten years later:\n");
    printf("R + 10 = 2(N + 10)\n");
    printf("R + 10 = 2N + 20\n");
    printf("R - 2N = 10     ...(2)\n");

    printf("\nStep 3: Subtract equation (1) from equation (2)\n");
    printf("(R - 2N) - (R - 3N) = 10 - (-6)\n");
    printf("N = 16\n");

    N = 16;

    printf("\nStep 4: Calculate Rashmi's age using equation (2)\n");
    printf("R - 2N = 10\n");
    printf("R - 2(16) = 10\n");
    printf("R - 32 = 10\n");

    R = 10 + 2 * N;

    printf("R = %d\n", R);

    printf("\nStep 5: Verify the answer\n");
    printf("Three years ago:\n");
    printf("Rashmi = %d years\n", R - 3);
    printf("Nazma = %d years\n", N - 3);
    printf("3 * Nazma's age = %d\n", 3 * (N - 3));

    printf("\nTen years later:\n");
    printf("Rashmi = %d years\n", R + 10);
    printf("Nazma = %d years\n", N + 10);
    printf("2 * Nazma's age = %d\n", 2 * (N + 10));

    printf("\n========================================\n");
    printf("           FINAL ANSWER\n");
    printf("Rashmi's present age = %d years\n", R);
    printf("Nazma's present age = %d years\n", N);
    printf("========================================\n");

    return 0;
}
