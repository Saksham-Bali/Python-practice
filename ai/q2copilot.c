#include <stdio.h>

int power(int x, unsigned int y, int m) {
    if (y == 0)
        return 1;
    int p = power(x, y / 2, m) % m;
    p = (p * p) % m;

    return (y % 2 == 0) ? p : (x * p) % m;
}

int main() {
    int x, y, m;
    printf("Enter x, y and m: ");
    scanf("%d %d %d", &x, &y, &m);
    printf("Result: %d", power(x, y, m));
    return 0;
} 