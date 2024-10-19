product = input('Enter the product name: ')
price = float(input('Enter the price: '))
quantity = int(input('Enter the quantity: '))

n_len = len(str(product))
print(n_len)

print("+" + "-"*20 + "+" + "-"*20 + "+" + "-"*20 + "+")
print(f"|{'Product':^20}|{"Price":^20}|{'Quantity':^20}|")
print("+" + "-"*20 + "+" + "-"*20 + "+" + "-"*20 + "+")
print(f"|{product:^20}|{'$' + f'{price:.2f}':^20}|{quantity:^20}|")
print("+" + "-"*20 + "+" + "-"*20 + "+" + "-"*20 + "+")
