print("Hello! Welcome to Calculator!")
print("You can calculate only two numbers.")

def main():
    def final():
        print("Thank you for using the calculator.")
        print()
        exit()


    while True:
        num_1 = float(input("Enter a number: "))
        num_2 = float(input("Enter a number: "))

        print("Enter the operation:")
        print("1. Addition: ")
        print("2. Subtraction: ")
        print("3. Multiplication: ")
        print("4. Division: ")
        result = 0
        while True:
            choice = input("Enter the choice: ")

            if choice == "1":
                result = num_1 + num_2
                break

            elif choice == "2":
                result = num_1 - num_2
                break

            elif choice == "3":
                result = num_1 * num_2
                break

            elif choice == "4":
                result = num_1 / num_2
                break

            else:
                print("Invalid choice")
                continue

        print("Your numbers were: " + str(num_1) + " and: " + str(num_2))
        print("The result of your choice: " + choice + " is: " + str(result))
        while True:
            selection = (input("Do you want to continue the program (yes/no): ")).lower()

            if selection == "no":
                final()
            elif selection == "yes":
                main()
            else:
                print("Invalid input")
                continue

main()

