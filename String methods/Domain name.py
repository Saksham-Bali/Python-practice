email_address = input("Enter your email address:")
s = email_address.split('@')
username = s[0]
domain = s[1]
print("The username is:", username)
print("The domain is:", domain)