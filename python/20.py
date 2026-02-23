# --- 1. Factorial ---
def factorial(n):
    if n < 0: return "Not defined for negative numbers"
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

# --- 2. Prime Check ---
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# --- 3. Fibonacci (nth number) ---
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a if n > 0 else 0

# --- 4. Sum of Digits ---
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# --- 5. Reverse Number ---
def reverse_number(n):
    sign = -1 if n < 0 else 1
    rev = int(str(abs(n))[::-1])
    return rev * sign

# --- 6. Armstrong Number ---
def is_armstrong(n):
    digits = [int(d) for d in str(abs(n))]
    power = len(digits)
    return sum(d**power for d in digits) == n

# --- 7. GCD (Greatest Common Divisor) ---
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# --- 8. LCM (Least Common Multiple) ---
def lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // gcd(a, b)

# --- 9. Perfect Number ---
def is_perfect_number(n):
    if n < 1: return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# --- 10. Main Menu ---
def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM MENU ===")
        print("1. Factorial    2. Prime Check    3. Fibonacci")
        print("4. Sum Digits   5. Reverse Num    6. Armstrong")
        print("7. GCD          8. LCM            9. Perfect Num")
        print("10. Exit")
        
        choice = input("\nPick an option: ")
        if choice == "10": break

        num1 = int(input("Enter number: "))
        
        if choice == "1": print(f"Result: {factorial(num1)}")
        elif choice == "2": print(f"Prime: {is_prime(num1)}")
        elif choice == "3": print(f"Fibonacci value: {fibonacci(num1)}")
        elif choice == "4": print(f"Sum of digits: {sum_of_digits(num1)}")
        elif choice == "5": print(f"Reversed: {reverse_number(num1)}")
        elif choice == "6": print(f"Armstrong: {is_armstrong(num1)}")
        elif choice == "7" or choice == "8":
            num2 = int(input("Enter second number: "))
            if choice == "7": print(f"GCD: {gcd(num1, num2)}")
            else: print(f"LCM: {lcm(num1, num2)}")
        elif choice == "9": print(f"Perfect Number: {is_perfect_number(num1)}")
        else: print("Invalid Choice!")

math_menu()