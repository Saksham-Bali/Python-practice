password = input("Enter the password:")
confirm_pass = input("Re-enter password to confirm:")
if password == confirm_pass:
    print("The new password has been created.")
elif password.casefold() == confirm_pass.casefold():
    print("Please make sure that the cases entered in the passwords are same.")
else:
    print("Please re-enter the confirm password.")
