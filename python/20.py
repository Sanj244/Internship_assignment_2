def factorial(n):
    if n<0:
        return "Not defined"
    f=1
    for i in range(1, n+1):
        f=f*i
    return f
def prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def fibonacci(n):
    a=0
    b=1
    for i in range(n-1):
        c=a + b
        a=b
        b=c
    return a
def sum_digits(n):
    s=0
    for d in str(abs(n)):
        s+=int(d)
    return s
def reverse_num(n):
    r=str(abs(n))[::-1]
    if n < 0:
        return-int(r)
    return int(r)
def armstrong(n):
    temp=abs(n)
    power=len(str(temp))
    s=0
    for d in str(temp):
        s+=int(d) ** power
    return s==n
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return abs(a*b) // gcd(a,b)
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    return s==n

print("1 Factorial")
print("2 Prime")
print("3 Fibonacci")
print("4 Sum digits")
print("5 Reverse number")
print("6 Armstrong")
print("7 GCD")
print("8 LCM")
print("9 Perfect number")
ch=input("Enter choice:")
n1=int(input("Enter number:"))
if ch=="1":
    print("Result:",factorial(n1))
elif ch=="2":
    if prime(n1):
        print("Prime number")
    else:
        print("Not prime")
elif ch=="3":
    print("Fibonacci:",fibonacci(n1))
elif ch=="4":
    print("Sum:",sum_digits(n1))
elif ch=="5":
    print("Reverse:",reverse_num(n1))
elif ch=="6":
    print("Armstrong:",armstrong(n1))
elif ch=="7":
    n2=int(input("Second number: "))
    print("GCD:",gcd(n1, n2))
elif ch=="8":
    n2=int(input("Second number: "))
    print("LCM:",lcm(n1, n2))
elif ch=="9":
    print("Perfect number:",perfect(n1))
else:
    print("Invalid choice")