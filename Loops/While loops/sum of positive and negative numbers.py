N = int(input("Enter the number of numbers to be entered: "))
p_sum = 0
n_sum = 0
i = 1
while i <= N:
    num = int(input("Enter the number: "))
    if num >= 0 :
        p_sum = p_sum + num
    else:
        n_sum = n_sum + num
    i += 1
print("The sum of positive numbers is: ", p_sum, "and the sum of negative numbers is: ", n_sum)
