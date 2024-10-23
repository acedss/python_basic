product = input('Enter the product name: ')
price = float(input('Enter the price: '))
quantity = int(input('Enter the quantity: '))

# Calculate the maximum length needed for each column
product_len = max(len('Product'), len(product))
price_len = max(len('Price'), len(f'${price:.2f}'))
quantity_len = max(len('Quantity'), len(str(quantity)))

# Create a format string based on the calculated lengths
format_str = f"+{'-'*(product_len+2)}+{'-'*(price_len+2)}+{'-'*(quantity_len+2)}+"
header_str = f"|{'Product':^{product_len+2}}|{'Price':^{price_len+2}}|{'Quantity':^{quantity_len+2}}|"
data_str = f"|{product:^{product_len+2}}|{'$' + f'{price:.2f}':^{price_len+2}}|{quantity:^{quantity_len+2}}|"

# Print the table
print(format_str)
print(header_str)
print(format_str)
print(data_str)
print(format_str)
