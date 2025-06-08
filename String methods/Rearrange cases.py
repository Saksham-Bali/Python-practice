s = input("Enter a string:")
lower = ''
upper = ''
for x in s:
    if x.islower():
        lower = lower + x
    else:
        upper = upper + x
print("The rearranged string is:", lower + upper)
