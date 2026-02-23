# --- Step 1: Input ---
user_input = input("Enter word/number: ")

# --- Step 2: Cleaning the data ---
# We convert to string (in case it's a number) and lowercase (for words)
original = str(user_input)
clean_text = original.lower()

# --- Step 3: Reversing ---
# [::-1] is the simplest way to flip a string in Python
reversed_text = clean_text[::-1]

# --- Step 4: Display Results ---
print(f"Original: {original}")

# For the reversed display, we flip the original case-sensitive version
print(f"Reversed: {original[::-1]}")

if clean_text == reversed_text:
    print("Result: PALINDROME")
else:
    print("Result: NOT A PALINDROME")