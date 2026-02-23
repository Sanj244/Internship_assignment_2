#input 
n=int(input("Enter number of inputs: "))
sum=0
for i in range(n):
    num=int(input("Enter number: "))
    sum=sum+num
    if i==0:
        max=num
        min=num
    else:
        if num>max:
            max=num
        if num<min:
            min=num
avg=sum/n
print("Sum =",sum)
print("Average =",avg)
print("Maximum =",max)
print("Minimum =",min)