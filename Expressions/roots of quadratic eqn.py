import math
a = float(input("Enter the value of the coefficient of x square: "))
b = float(input("Enter the value of the coefficient of x: "))
c = float(input("Enter the value of the constant: "))
r1 = (- b + math.sqrt(b ** 2 - 4 * a * c)) /(2 * a)
r2 = (- b - math.sqrt(b ** 2 - 4 * a * c)) /(2 * a)
print("The roots of the quadratic equation are: ", r1, r2)
