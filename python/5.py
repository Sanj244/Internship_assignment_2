#Input
bill_amount = float(input("Enter total bill:"))
num_people = int(input("Number of people:"))
tax_percent = float(input("Tax percentage:"))
tip_percent = float(input("Tip percentage:"))

#Calculation
tax_amount = bill_amount*(tax_percent/100)
after_tax = bill_amount+tax_amount
tip_amount = after_tax*(tip_percent/100)

#Totals
total_bill=after_tax+tip_amount
per_person=total_bill/num_people

#Output 
print(f"Subtotal:{bill_amount:>10.2f}")
print(f"Tax ({tax_percent}%):{tax_amount:>10.2f}")
print(f"After tax:{after_tax:>10.2f}")
print(f"Tip {tip_percent}:{tip_amount:>10.2f}")
print(f"Total:{total_bill:>10.2f}")
print(f"Per person :{per_person:>10.2f}")