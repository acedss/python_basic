# Print menu and ask user to choose
print("-"*30)
print("Welcome to the program")
running = True
def print_menu():
    print("1. Print Hello")
    print("2. Print World")
    print("3. Exit")
    print("asdfasdfadsf")
    choice = input("Enter your choice: ")
    return choice
while running:
    choice = print_menu()
    if choice == "1":
        print("Hello")
    elif choice == "2":
        print("World")
    elif choice == "3":
        running = False
        print("Thank you for using the program")
    else:
        print("Invalid choice. Please try again!")

# function hoac exception