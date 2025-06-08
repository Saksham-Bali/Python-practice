#include <stdio.h>

int gcd(int num1, int num2) {
    // Find the GCD using Euclid's algorithm
    while (num2 != 0) {
        int temp = num2;
        num2 = num1 % num2;
        num1 = temp;
    }
    return num1;
}

int main() {
    int num1, num2;
    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    // Check if the GCD of the two numbers is 1
    if (gcd(num1, num2) == 1) {
        printf("%d and %d are coprime", num1, num2);
    } else {
        printf("%d and %d are not coprime", num1, num2);
    }
    return 0;
}