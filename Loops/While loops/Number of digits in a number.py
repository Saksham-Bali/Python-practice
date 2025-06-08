n = int(input("Enter the number: "))
i = 0
while n > 0:
    n = n // 10
    i = i + 1
print("The number of digits in the number are: ",i)
