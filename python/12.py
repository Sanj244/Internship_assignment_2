# --- Standard Table ---
num = int(input("Enter number: "))
end_range = int(input("Enter range (end): "))

print(f"\nMultiplication Table of {num}")
# We use end_range + 1 because the range function stops before the last number
for i in range(1, end_range + 1):
    print(f"{num} x {i} = {num * i}")