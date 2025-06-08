#include <stdio.h>

int isPrime(int num) {
    // Check if the number is prime
    if (num <= 1) {
        return 0;
    }
    for (int i = 2; i * i <= num; ++i) {
        if (num % i == 0) {
            return 0;
        }
    }
    return 1;
}

int main() {
    int num1, num2;
    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    printf("Prime numbers between %d and %d are: ", num1, num2);
    for (int i = num1; i <= num2; ++i) {
        if (isPrime(i)) {
            printf("%d ", i);
        }
    }
    return 0;
}