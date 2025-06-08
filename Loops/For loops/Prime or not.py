import math
n = int(input("Enter a number: "))
a = math.ceil(math.sqrt(n))
for i in range(2, a + 1):
    if n % i == 0 and i != n:
        print("It is a composite number.")
        break
else:
        print("It is a prime number.")
