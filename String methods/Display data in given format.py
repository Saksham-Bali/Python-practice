item = input("Enter the name of the item:")
price = input("Enter the price of the item:")
n = 25 - len(price)
item = item.ljust(n, '.')
display_data = item + price
print(display_data)

'''or'''

total_len = len(item) + len(price)
dots = '.' * (25 - total_len)
dis_data = item + dots + price
print(dis_data)
