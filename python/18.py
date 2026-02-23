# --- Math Functions ---

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Cannot divide by zero."
    return a % b

def power(a, b):
    return a ** b

# --- Main Calculator Function ---

def calculator():
    while True:
        print("\n--- FUNCTIONAL CALCULATOR ---")
        print("1. Add      2. Subtract   3. Multiply")
        print("4. Divide   5. Modulus    6. Power")
        print("7. Exit")
        
        choice = input("\nSelect an option (1-7): ")

        if choice == '7':
            print("Exiting... Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Result: {modulus(num1, num2)}")
            elif choice == '6':
                print(f"Result: {power(num1, num2)}")
        else:
            print("Invalid choice, please try again.")

# Run the program
calculator()