#include <stdio.h>

int main()
{
    int a, t8, d, S20;

    printf("========================================\n");
    printf("       QUESTION 33(A) - SOLUTION\n");
    printf("========================================\n");

    printf("\nGiven:\n");
    printf("First term + Eighth term = 32\n");
    printf("First term * Eighth term = 60\n");

    printf("\nStep 1: Form the equations\n");
    printf("a + (a + 7d) = 32\n");
    printf("2a + 7d = 32\n");
    printf("a(a + 7d) = 60\n\n");

    printf("Step 2: Find the first and eighth terms\n");
    printf("The two numbers are 2 and 30 because:\n");
    printf("2 + 30 = 32\n");
    printf("2 * 30 = 60\n");

    printf("\nThere are two possible orders.\n");

    printf("\nCase 1: First term = 2, Eighth term = 30\n");
    a = 2;
    t8 = 30;
    d = (t8 - a) / 7;

    printf("d = (30 - 2)/7 = %d\n", d);
    S20 = (20 * (2 * a + 19 * d)) / 2;

    printf("Sum of first 20 terms:\n");
    printf("S20 = 20/2 * [2a + 19d]\n");
    printf("S20 = %d\n", S20);

    printf("\nCase 2: First term = 30, Eighth term = 2\n");
    a = 30;
    t8 = 2;
    d = (t8 - a) / 7;

    printf("d = (2 - 30)/7 = %d\n", d);
    S20 = (20 * (2 * a + 19 * d)) / 2;

    printf("Sum of first 20 terms:\n");
    printf("S20 = 20/2 * [2a + 19d]\n");
    printf("S20 = %d\n", S20);

    printf("\n========================================\n");
    printf("For an increasing A.P.:\n");
    printf("First term = 2\n");
    printf("Common difference = 4\n");
    printf("Sum of first 20 terms = 800\n");
    printf("========================================\n");

    return 0;
}
