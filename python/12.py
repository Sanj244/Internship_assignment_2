#input
num=int(input("Enter number: "))
range=int(input("Enter range:"))
#print table
print(f"Multiplication Table of {num}")
for i in range(1,range+1):
    print(f"{num}x{i}={num*i}")