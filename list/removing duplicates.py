l1 = [3, 5, 7, 9, 3, 6, 5, 2, 3 , 7, 10]
i = 0
while i < len(l1):
    if l1.count(l1[i]) > 1:
        l1.remove(l1[i])
    else:
        i += 1
l1.sort()
print(l1)
