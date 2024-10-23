
# age = int(input('Enter your age: '))
# sv = 18
# nguoi_lon = 21

# if age < sv:
#     print("You are not eligible to apply for a driver's license.")
# else:
#     print("You are eligible to apply for a driver's license.")
#     if age >= nguoi_lon:
#         print("Congratulations on receiving one more benefits: ")
#         print("You are also eligible to rent a car.")
#     else: 
#         print("You need to be at least 21 years old to rent a car.")

# # Fixed_ex1:
# if age < 0 or age > 120:
#     print("Invalid age")
# elif age < sv:
#     print("You are not eligible to apply for a driver's license.")
# else:
#     print("You are eligible to apply for a driver's license.")
#     if age >= nguoi_lon:
#         print("You are also eligible to rent a car.")
#     else:
#         print("You need to be at least 21 years old to rent a car.")


# ex2:
# income = int(input("Can you enter your income please: ")) 
# credit_score = int(input("And your credit score: "))
# if income >= 50000 and credit_score >= 700:
#     print("You are eligible for a loan with low interest rates.")
#     if income >= 100000: 
#         print("You are eligible for a loan with the lowest interest rates.")
# else: 
#     if income >= 30000 and credit_score >= 500: 
#         print("You are eligible for a loan with moderate interest rates.")
#     else: 
#         print("Sorry, you are not eligible for a loan at this time.")


#ex3: 
product = input("Plz enter the product: ")
price = float(input("And its price: "))
quantity = int(input("Also its quantity: "))

sp = max(len("Product"), len(product)) + 2
gia = max(len("Price"), len(f"{price:.2f}")) + 2
sl = max(len("Quantity"), len(str(quantity))) + 2
bang = "+" + "-"*(sp) + "+" + "-"*(gia) + "+" + "-"*(sl) + "+"
print(bang)
print(f"|{"Product":^{sp}}|{"Price":>{gia}}|{"Quantity":^{sl}}|")
print(bang)
print(f"|{product:^{sp}}|{price:^{gia}}|{quantity:^{sl}}|")
print(bang)
