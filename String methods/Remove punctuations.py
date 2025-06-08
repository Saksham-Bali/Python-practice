s1 = input("Enter a string:")
s2 = ''
for x in s1:
    if x.isalnum():
        s2 = s2 + x
print("The string with all the punctuations removed is:", s2)
