n = int(input("Enter the number whose table is needed: "))
print("The multiplication table of", n, 'is:')
for i in range(1, 11):
    prod = n * i
    print(n, 'X', i, '=', prod)
