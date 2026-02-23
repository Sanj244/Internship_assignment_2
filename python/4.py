#Setup
current=2026
#Input
birth=int(input("Enter your birth year: "))

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

# --- Step 1: Get Current Date (Static Reference) ---
print("--- Set Current Date ---")
curr_day = int(input("Enter current day (1-31): "))
curr_month = int(input("Enter current month (1-12): "))
curr_year = int(input("Enter current year (YYYY): "))

# --- Step 2: Get Birth Date ---
print("\n--- Set Birth Date ---")
b_day = int(input("Enter birth day (1-31): "))
b_month = int(input("Enter birth month (1-12): "))
b_year = int(input("Enter birth year (YYYY): "))

# --- Step 3: Accurate Age Logic ---
# Base age subtraction
age = curr_year - b_year

# Adjust if birthday hasn't happened yet this year
if (curr_month < b_month) or (curr_month == b_month and curr_day < b_day):
    age -= 1

# --- Step 4: Calculations ---
months = age * 12
days = int(age * 365.25) # .25 accounts for leap years
hours = days * 24
minutes = hours * 60
years_to_100 = 100 - age

# --- Step 5: Display Results ---
print("\n" + "═"*35)
print(f"      PRECISION AGE REPORT")
print("═"*35)
print(f"Current Age      : {age} years")
print(f"Age in Months    : {months:,}")
print(f"Age in Days      : {days:,}")
print(f"Age in Hours     : {hours:,}")
print(f"Age in Minutes   : {minutes:,}")
print(f"Years until 100  : {years_to_100 if years_to_100 > 0 else 0}")
print("═"*35)