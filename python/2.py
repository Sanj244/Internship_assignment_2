#Input
n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

#Addition
addition=n1+n2
print(f"Addition:{n1}+{n2}={addition}")

#Subtraction
subtraction=n1-n2
print(f"Subtraction:{n1}-{n2}={subtraction}")
    
#Multiplication
multiplication=n1 * n2
print(f"Multiplication:{n1}*{n2}={multiplication}")

#Division
if n2!= 0:
    division = n1 / n2
    print(f"Division:{n1}/{n2}={division:.2f}")
else:
    print("Division:Cannot divide by zero")

#Modulus
if n2!= 0:
    modulus=n1%n2
    print(f"Modulus:{n1}%{n2}={modulus}")
else:
    print("Cannot divide by zero")

#Exponentiation
exponent=n1**n2         
print(f"Exponentiation:{n1}^{n2}={exponent}")

