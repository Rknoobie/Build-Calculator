def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y

def calculator():
    print("Welcome to the Python Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            choice = input("Enter the number of the operation you'd like to perform (1/2/3/4): ")
            
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                
                if choice == '1':
                    print(f"The result is: {add(num1, num2)}")
                elif choice == '2':
                    print(f"The result is: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"The result is: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"The result is: {divide(num1, num2)}")
            else:
                print("Invalid input. Please select a valid operation.")
            
            # Ask the user if they want to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
            if next_calculation != 'yes':
                print("Thank you for using the calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numerical values only.")

if __name__ == "__main__":
    calculator()
