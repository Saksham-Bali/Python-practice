#include <stdio.h>

int extendedGCD(int a, int b, int* x, int* y) {
    if (a == 0) {
        *x = 0;
        *y = 1;
        return b;
    }

    int x1, y1;
    int gcd = extendedGCD(b % a, a, &x1, &y1);

    *x = y1 - (b / a) * x1;
    *y = x1;

    return gcd;
}

int modInverse(int a, int m) {
    int x, y;
    int g = extendedGCD(a, m, &x, &y);
    if (g != 1) {
        printf("Inverse doesn't exist");
        return -1;
    } else {
        int res = (x % m + m) % m;
        return res;
    }
}

int main() {
    int a, m;
    printf("Enter a and m: ");
    scanf("%d %d", &a, &m);
    printf("Modulo multiplicative inverse is %d", modInverse(a, m));
    return 0;
}