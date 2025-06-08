n = int(input("Enter a number: "))
og_n = n
rev_n = 0
while n > 0:
    r = n % 10
    n = n // 10
    rev_n = rev_n * 10 + r
if rev_n == og_n:
    print("The given number", og_n, "and its reverse are palindrome.")
else:
    print("The given number", og_n, "and its reverse are not palindrome.")
