#include <stdio.h>

int main()
{
    int a, d, S40;

    printf("========================================\n");
    printf("       QUESTION 33(B) - SOLUTION\n");
    printf("========================================\n");

    printf("\nGiven:\n");
    printf("Number of terms = 40\n");
    printf("Sum of first 9 terms = 153\n");
    printf("Sum of last 6 terms = 687\n");

    printf("\nStep 1: Use the sum of the first 9 terms\n");
    printf("S9 = 9/2 * [2a + 8d] = 153\n");
    printf("2a + 8d = 34\n");
    printf("a + 4d = 17      ...(1)\n");

    printf("\nStep 2: Use the sum of the last 6 terms\n");
    printf("Last 6 terms are a+34d through a+39d.\n");
    printf("Their sum = 3 * [(a+34d) + (a+39d)]\n");
    printf("= 6a + 219d = 687\n");
    printf("2a + 73d = 229   ...(2)\n");

    printf("\nStep 3: Solve the equations\n");
    printf("From (1): a = 17 - 4d\n");
    printf("Substitute into (2):\n");
    printf("2(17 - 4d) + 73d = 229\n");
    printf("34 - 8d + 73d = 229\n");
    printf("65d = 195\n");

    d = 195 / 65;
    a = 17 - 4 * d;

    printf("d = %d\n", d);
    printf("a = 17 - 4(%d) = %d\n", d, a);

    printf("\nStep 4: Find the sum of all 40 terms\n");
    printf("S40 = 40/2 * [2a + 39d]\n");
    S40 = (40 * (2 * a + 39 * d)) / 2;

    printf("S40 = 20 * [2(%d) + 39(%d)]\n", a, d);
    printf("S40 = %d\n", S40);

    printf("\n========================================\n");
    printf("             FINAL ANSWERS\n");
    printf("First term = %d\n", a);
    printf("Common difference = %d\n", d);
    printf("Sum of all 40 terms = %d\n", S40);
    printf("========================================\n");

    return 0;
}
