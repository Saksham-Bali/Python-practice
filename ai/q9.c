#include <stdio.h>
int calcgcd(int a, int b)
{
    while( a != b)
    {
        if(a > b)
        {
            a = a - b;
        }
        else
        {
            b = b - a;
        }
    }
   return a;
}
int main()
{
    int a;
    int b;
    printf("Enter the value of a: ");
    scanf("%d", &a);
    printf("Enter the value of b: ");
    scanf("%d", &b);
    int gcd = calcgcd(a, b);
    printf("The GCD of %d and %d is %d\n", a, b, gcd);
    int lcm = (a * b) / gcd;
    printf("The LCM of %d and %d is %d", a, b, lcm);
    return 0;
}