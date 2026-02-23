#User Input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Addition
addition=num1 + num2
print(f"Addition:{num1}+{num2}={addition}")

#Subtraction
subtraction=num1 - num2
print(f"Subtraction:{num1}-{num2}={subtraction}")

#Multiplication
multiplication=num1 * num2
print(f"Multiplication:{num1}*{num2}={multiplication}")

#Division
if num2!= 0:
    division = num1 / num2
    print(f"Division:{num1}/{num2}={division:.2f}")
else:
    print("Division:Cannot divide by zero")

#Modulus
if num2!= 0:
    modulus=num1%num2
    print(f"Modulus:{num1}%{num2}={modulus}")
else:
    print("Modulus:(Cannot divide by zero")

#Exponentiation
exponent=num1**num2
print(f"Exponentiation:{num1}^{num2}={exponent}")

