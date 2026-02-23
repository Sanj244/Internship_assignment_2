#Temperature 
print("1.Celsius to Fahrenheit")
print("2.Fahrenheit to Celsius")
print("3.Celsius to Kelvin")
print("4.Kelvin to Celsius")
print("5.Fahrenheit to Kelvin")
print("6.Kelvin to Fahrenheit")
choice=input("Select an option (1-6):")

#Input  
temp=float(input("Enter temperature value"))

#Calculation 
if choice=='1':
    # Celsius to Fahrenheit
    result=(temp*9/5)+32
    print(f"{temp} C is {result:.2f} F")

elif choice=='2':
    # Fahrenheit to Celsius
    result=(temp-32)*5/9
    print(f"{temp} F is {result:.2f} C")

elif choice=='3':
    # Celsius to Kelvin
    result=temp+273.15
    print(f"{temp} C is {result:.2f} K")

elif choice=='4':
    # Kelvin to Celsius
    result=temp-273.15
    print(f"{temp} K is {result:.2f} C")

elif choice=='5':
    # Fahrenheit to Kelvin
    result = (temp-32)*5/9+273.15
    print(f"{temp} F is {result:.2f} K")

elif choice=='6':
    # Kelvin to Fahrenheit
    result=(temp-273.15)*9/5+32
    print(f"{temp} K is {result:.2f} F")

else:
    print("Invalid input")