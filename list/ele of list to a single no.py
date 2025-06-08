l1 = [int(x) for x in input("Enter the elements of the list (separated by spaces): ").split()]
num = ''
for x in l1:
    num = num + str(x)
num = int(num)
print("The number formed by concatenating elements of the list is: ", num)
