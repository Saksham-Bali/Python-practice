#include <stdio.h>
#include <math.h>

int main() {
    int lower, upper;
    printf("Enter two numbers: ");
    scanf("%d %d", &lower, &upper);

    printf("Pythagorean quadruples between %d and %d are:\n", lower, upper);
    for (int a = lower; a <= upper; ++a) {
        for (int b = a; b <= upper; ++b) {
            for (int c = b; c <= upper; ++c) {
                for (int d = c; d <= upper; ++d) {
                    if (a * a + b * b + c * c == d * d) {
                        printf("(%d, %d, %d, %d)\n", a, b, c, d);
                    }
                }
            }
        }
    }
    return 0;
}