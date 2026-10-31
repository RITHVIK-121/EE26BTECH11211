#include <stdio.h>

int main()
{
    int a = 7;
    int an = 84;
    int n;

    double Sn = 2093.0 / 2.0;

    printf("QUESTION 4: ARITHMETIC PROGRESSION\n\n");

    printf("First term a = %d\n", a);
    printf("Nth term an = %d\n", an);
    printf("Sum Sn = %.1f\n\n", Sn);

    printf("Formula: Sn = n/2 * (a + an)\n\n");

    printf("Substituting values:\n");
    printf("%.1f = n/2 * (%d + %d)\n", Sn, a, an);

    n = (int)((2 * Sn) / (a + an));

    printf("n = (2 * %.1f) / (%d + %d)\n", Sn, a, an);
    printf("n = %.1f / %d\n", 2 * Sn, a + an);
    printf("n = %d\n", n);

    printf("\nFinal Answer: n = %d\n", n);
    printf("Correct Option: (C)\n");

    return 0;
}
