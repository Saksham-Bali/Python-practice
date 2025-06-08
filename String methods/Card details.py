card_num = input("Enter the card number:")
display = card_num[12:len(card_num):1]
display = display.rjust(16, '*')
print(display)
