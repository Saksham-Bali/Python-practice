n = int(input("Enter a number: "))
bin_n = ''
while n > 0:
    r = n % 2
    n = n // 2
    bin_n = str(r) + bin_n

print("The number in its binary form is: ", bin_n)
