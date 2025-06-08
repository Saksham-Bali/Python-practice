#include <stdio.h>
int main()
{
    int a;
    int b;
    printf("Enter the value of a: ");
    scanf("%d", &a);
    printf("Enter the value of b: ");
    scanf("%d", &b);
    while( a != b)
    {
        if( a > b)
        {
            a = a - b;
        }
        else
        {
            b = b - a;
        }
    }
    printf("GCD of the given numbers = %d", a);
    return 0;
}
