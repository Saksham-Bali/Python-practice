N = int(input("Enter the number of numbers whose sum is to be found: "))
i = 1
sum_of_num = 0
while i <= N:
    num = int(input("Enter the number "))
    sum_of_num = sum_of_num + num
    i = i + 1
print("The sum of given numbers is: ", sum_of_num)
