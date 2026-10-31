#include <stdio.h>

int main()
{
    float winning, losing;

    winning = 0.79;
    losing = 1.0 - winning;

    printf("QUESTION 2: PROBABILITY\n\n");

    printf("Probability of winning = %.2f\n", winning);

    printf("Probability of losing = 1 - Probability of winning\n");
    printf("                     = 1 - %.2f\n", winning);
    printf("                     = %.2f\n", losing);

    printf("\nFinal Answer = %.2f\n", losing);
    printf("Correct Option: (D)\n");

    return 0;
}
