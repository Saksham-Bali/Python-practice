a = int(input("Enter the first term of the series: "))
d = int(input("Enter the common difference for the series: "))
n = int(input("Enter the number of terms in the series: "))
a_n = a + n * d
print("The AP series is as follows: ")
for i in range(a, a_n, d):
    print(i)
