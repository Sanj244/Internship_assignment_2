year = int(input("Enter a year: "))

if year % 4 == 0:
    print(f"{year} is a Leap Year.")
    print("Reason: It is divisible by 4.")

else:
    print(f"{year} is NOT a Leap Year.")
    print("Reason: It is not divisible by 4.")