work_hours = [ int(x) for x in input("Enter the work hours per day in a week (separated by spaces): ").split()]
hourly_wage = int(input("Enter the hourly wage of the person:"))
salary = 0
for x in work_hours:
    salary = salary + (x * hourly_wage)
print("The salary of the person is: ", salary)
