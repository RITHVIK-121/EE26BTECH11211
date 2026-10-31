#include <stdio.h>
#include<math.h>
int main()
{
    printf("========== QUESTION 11 ==========\n\n");

    printf("Given points: (3, -5) and (x, -5)\n");
    printf("Distance between the points = 15 units\n\n");

    printf("Step 1: Use the distance formula.\n");
    printf("d = sqrt((x2 - x1)^2 + (y2 - y1)^2)\n\n");

    printf("Step 2: Substitute the values.\n");
    printf("15 = sqrt((x - 3)^2 + (-5 + 5)^2)\n");
    printf("15 = sqrt((x - 3)^2)\n");
    printf("15 = |x - 3|\n\n");

    printf("Step 3: Consider both possibilities.\n");
    printf("x - 3 = 15  =>  x = 18\n");
    printf("x - 3 = -15 =>  x = -12\n\n");

    printf("Final Answer: x = 18 or x = -12\n");
    printf("Correct Option: (c)\n");

    printf("=================================\n");

    return 0;
}
