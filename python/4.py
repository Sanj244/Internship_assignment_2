#Setup
current=2026
#Input
birth=int(input("Enter your birth year:"))

#Calculations 
age=current-birth
months=age*12
days=age*365
hours=days*24
minutes=hours*60
years_to_100=100-age

#Output
print(f"1.Current Age:{age}")
print(f"2.Age in Month:{months}")
print(f"3.Age in Days{days}")
print(f"4.Age in Hours:{hours}")
print(f"5.Age in Minutes:{minutes}")
print(f"6.Years until 100:{years_to_100}")

