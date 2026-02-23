print("1.Pattern 1")
print("2.Pattern 2")
print("3.Pattern 3")
print("4.Pattern 4")
print("5.Pattern 5")

choice=int(input("Enter pattern choice:"))
n=int(input("Enter height:"))

#ascending number tower
if choice==1:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
#same number tower
elif choice==2:
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=" ")
        print()

#descending tower
elif choice==3:
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end=" ")
        print()
#mirror tower
elif choice==4:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for j in range(i-1,0,-1):
            print(j,end="")
        print()
#stars tower
elif choice==5:
    for i in range(1,n+1):
    print("*" * i)

else:
    print("Invalid choice")
