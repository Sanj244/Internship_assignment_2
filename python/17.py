#Input 
user_input = input("Enter word/number: ")

#Original and cleaning
original = str(user_input)
text = original.lower()

#reverse
reversed_text=text[::-1]
print(f"Original:{original}")
print(f"Reversed:{original[::-1]}")

if text==reversed_text:
    print("PALINDROME")
else:
    print("NOT A PALINDROME")