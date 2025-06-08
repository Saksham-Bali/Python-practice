N = int(input("Enter the number of numbers: "))
max_of_N = 0
i = 1
while i <= N:
    n = int(input("Enter the number: "))
    if n > max_of_N:
        max_of_N = n
    i += 1
print("The maximum from the given numbers is: ", max_of_N)
