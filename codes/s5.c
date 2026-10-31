#include <stdio.h>

int main()
{
    int p = 18;
    int q = 20;

    printf("QUESTION 5: LCM OF ALGEBRAIC EXPRESSIONS\n\n");

    printf("Given:\n");
    printf("p = 18*a^2*b^4\n");
    printf("q = 20*a^3*b^2\n\n");

    printf("Step 1: Find the LCM of 18 and 20.\n");
    printf("18 = 2 * 3^2\n");
    printf("20 = 2^2 * 5\n");
    printf("LCM(18, 20) = 2^2 * 3^2 * 5 = 180\n\n");

    printf("Step 2: Select the highest power of each variable.\n");
    printf("For a: max(a^2, a^3) = a^3\n");
    printf("For b: max(b^4, b^2) = b^4\n\n");

    printf("Step 3: Combine the results.\n");
    printf("LCM(p, q) = 180*a^3*b^4\n\n");

    printf("Final Answer: 180*a^3*b^4\n");
    printf("Correct Option: (D)\n");

    return 0;
}
