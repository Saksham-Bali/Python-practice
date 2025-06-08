import math
print("The prime numbers from 1 to 100 are:")
for i in range(2, 101):
    a = math.ceil(math.sqrt(i))
    for j in range(2, a + 1):
        if i % j == 0 and j != i:
            break
    else:
        print(i)