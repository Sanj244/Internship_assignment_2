#Input
age = int(input("Enter age: "))
day = input("Enter day of the week (Monday-Sunday): ").title()
tickets = int(input("Enter number of tickets: "))

#Base Price based on Age
if age < 3:
    base_price = 0
    category = "Free (Infant)"
elif age <= 12:
    base_price = 150
    category = "Child"
elif age <= 59:
    base_price = 300
    category = "Adult"
else:
    base_price = 200
    category = "Senior"

#Discount Logic
weekend = ["Friday", "Saturday", "Sunday"]
discount = 0

if day in weekend:
    discount=base_price*0.20

#Totals
price_after_discount=base_price-discount
total_amount=price_after_discount*tickets

#Output
print(f"\nCategory: {category}")
print(f"Base Price: ₹{base_price}")
print(f"Discount: ₹{discount}")
print(f"Price after discount: ₹{price_after_discount}")
print(f"Total Amount for {tickets} ticket(s): ₹{total_amount}")