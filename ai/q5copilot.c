#include <stdio.h>

int gcd(int a, int b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

int areCoprime(int a, int b) {
    return (gcd(a, b) == 1);
}

int main() {
    int lower, upper;
    printf("Enter lower and upper limit: ");
    scanf("%d %d", &lower, &upper);

    printf("Coprime pairs between %d and %d are:\n", lower, upper);
    for (int i = lower; i <= upper; ++i) {
        for (int j = i + 1; j <= upper; ++j) {
            if (areCoprime(i, j)) {
                printf("(%d, %d)\n", i, j);
            }
        }
    }
    return 0;
}