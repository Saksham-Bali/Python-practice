john = float(input("Enter the age of john: "))
smith = float(input("Enter the age of smith: "))
ajay = float(input("Enter the age of ajay: "))
if john > smith and john > ajay:
    print("John is the eldest.")
elif smith > ajay:
    print("Smith is the eldest.")
else:
    print("Ajay is the eldest.")
    