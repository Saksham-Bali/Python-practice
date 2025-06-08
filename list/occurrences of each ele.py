l1 = input("Enter the elements of the list (separated by spaces):").split()
result = []
for x in l1:
    if x not in result:
        num = l1.count(x)
        result.extend([x, num])
print("The occurrences of each element in the list are: ", result)
