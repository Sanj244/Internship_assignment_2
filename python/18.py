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

def square_root(a):
    if a < 0:
        return "Not possible"
    return a**0.5

def percentage(total, part):
    if total==0:
        return "Invalid"
    return (part/total)*100
def calculator():
    print("1 Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Modulus")
    print("6 Power")
    print("7 Square Root")
    print("8 Percentage")
    choice = input("Select option: ")
    if choice in ['1','2','3','4','5','6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice=='1':
            print("Result:",add(num1,num2))
        elif choice=='2':
            print("Result:",subtract(num1,num2))
        elif choice=='3':
            print("Result:",multiply(num1,num2))
        elif choice=='4':
            print("Result:",divide(num1,num2))
        elif choice=='5':
            print("Result:",modulus(num1,num2))
        elif choice=='6':
            print("Result:",power(num1,num2))
    elif choice=='7':
        num = float(input("Enter number: "))
        print("Result:",square_root(num))
    elif choice=='8':
        total = float(input("Enter total value: "))
        part = float(input("Enter obtained value: "))
        print("Percentage:",percentage(total,part))
    else:
        print("Invalid choice")
calculator()
