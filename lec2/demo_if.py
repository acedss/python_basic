operator = input("Enter operator: [+, -, *, /]: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


if operator not in ['+', '-', '*', '/']: 
    result = "Invalid operator"
elif operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
else:
    result = num1 / num2






    

