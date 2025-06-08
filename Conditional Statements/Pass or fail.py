marks_m = float(input("Enter the marks scored in maths: "))
marks_p = float(input("Enter the marks scored in physics: "))
marks_c = float(input("Enter the marks scored in chemistry: "))
if 0 <= marks_p <= 100 and 0 <= marks_c <= 100 and 0 <= marks_m <= 100:
    print("The marks entered are valid.")
    if marks_p >= 45 and marks_c >= 45 and marks_m >= 45:
        print("The student passed.")
    else:
        print("The student failed.")
else:
    print("The marks are entered are invalid.")
