#Input
num = int(input("Enter a number: "))

#Simple Logic
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    factorial = 1
    # Loop from 1 up to the number
    for i in range(1, num + 1):
        factorial = factorial * i
    
    print(f"The factorial of {num} is {factorial}")