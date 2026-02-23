def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Cannot divide by zero"
    return a/b

def modulus(a,b):
    if b==0:
        return "Cannot divide by zero"
    return a%b

def power(a,b):
    return a**b

#Calculator  
def calculator():
    print("CALCULATOR")
    print("1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Moduluo\n6.Power")
    choice = input("\nSelect an option (1-6): ")
    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice=='1':
            print(f"Result: {add(num1,num2)}")
        elif choice=='2':
            print(f"Result: {subtract(num1,num2)}")
        elif choice=='3':
            print(f"Result: {multiply(num1,num2)}")
        elif choice=='4':
            print(f"Result: {divide(num1,num2)}")
        elif choice=='5':
            print(f"Result: {modulus(num1,num2)}")
        elif choice=='6':
            print(f"Result: {power(num1,num2)}")
    else:
        print("Invalid choice")
calculator()