s1 = input("Enter the first string:")
s2 = input("Enter the second string:")
if len(s1) == len(s2):
    s3 = sorted(s1)
    s3 = ''.join(s3)
    s4 = sorted(s2)
    s4 = ''.join(s4)
    if s3 == s4:
        print("The given strings are anagram.")
    else:
        print("The given strings are not anagram.")
else:
    print("The given strings are not anagram.")

# #or
# if len(s1) == len(s2):
#     for x in s1:
#         if x not in s2:
#             print('The given strings are not anagram.')
#             break;
#     else:
#         print('The given strings are anagram.')
