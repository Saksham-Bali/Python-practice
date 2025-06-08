n = int(input("Enter a number: "))
fact = n
for i in range(n - 1, 0, -1):
    fact = fact * i
print("The factorial of the given number is: ", fact)
