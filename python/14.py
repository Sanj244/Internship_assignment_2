#Input
num=int(input("Enter a number:"))

#factorial logic
if num<0:
    print("Please enter a non-negative integer")
elif num==0:
    print("1")
else:
    factorial=1
    for i in range(1,num+1):
        factorial = factorial*i
    print(f"The factorial of {num} is {factorial}")