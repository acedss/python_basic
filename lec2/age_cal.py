dob_input = input('Enter your date of birth: ')
# try: 
#     dob = int(dob_input)

#     current_year = 2024

#     if dob > current_year:
#         print('Invalid year') 

#     else:
#         age = current_year - dob
#         print(f'Your age is {age}')
#         if age >= 18:
#             print('You are an adult')
#         else:
#             print('You are a minor')
# except ValueError:
#     print('Invalid input')


dob = int(dob_input)

current_year = 2024

if dob > current_year:
    print('Invalid year') 

else:
    age = current_year - dob
    print(f'Your age is {age}')
    if age >= 18:
        print('You are an adult')
    else:
        print('You are a minor')