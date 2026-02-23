#part 1
num=int(input("Enter a number: "))
if num<=1:
    print(num,"is NOT a PRIME number")
elif num==2:
    print("2 is a PRIME number")
else:
    prime=True  
    for i in range(2,num):
        if num%i==0:
            prime=False
            break
    if prime:
        print(num,"is a PRIME number")
    else:
        print(num,"is NOT a PRIME number")
#part 2
start=int(input("Enter start range:"))
end=int(input("Enter end range:"))
print("Prime numbers in this range:")
for num in range(start,end+1):
    if num>1:
        prime=True
        for i in range(2,num):
            if num%i==0:
                prime=False
                break    
        if prime:
            print(num)