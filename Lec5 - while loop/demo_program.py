# Print menu and ask user to choose
print("-"*30)
print("Welcome to the program")
running = True
while running:
    print("1. Print Hello")
    print("2. Print World")
    print("3. Exit")
    choice = input("Enter your choice: ")
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