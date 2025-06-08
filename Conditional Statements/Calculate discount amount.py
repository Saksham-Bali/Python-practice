amount = float(input("Enter the bill amount: "))
if amount <= 1000:
    percent_discount = 10
elif 1000 < amount <= 5000:
    percent_discount = 20
elif 5000 < amount <= 10000:
    percent_discount = 30
else:
    percent_discount = 50
discount = (percent_discount / 100) * amount
discounted_amt = amount - discount
print("The discounted amount is: ", discounted_amt)
