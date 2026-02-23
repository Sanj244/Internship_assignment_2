def count_words(text):
    return len(text.split())

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def count_consonants(text):
    vowels = "aeiouAEIOU"
    # Counts only letters that aren't vowels
    return sum(1 for char in text if char.isalpha() and char not in vowels)

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    clean_text = "".join(text.split()).lower()
    return clean_text == clean_text[::-1]

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    return "".join(char for char in text if char not in vowels)

def word_frequency(text):
    words = text.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def longest_word(text):
    words = text.split()
    if not words: return ""
    return max(words, key=len)

def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")
    print(f"Words          : {count_words(text)}")
    print(f"Vowels         : {count_vowels(text)}")
    print(f"Consonants     : {count_consonants(text)}")
    print(f"Reversed       : {reverse_text(text)}")
    print(f"Palindrome     : {'Yes' if is_palindrome(text) else 'No'}")
    print(f"Without vowels : {remove_vowels(text)}")
    
    lw = longest_word(text)
    print(f"Longest word   : {lw} ({len(lw)} letters)")
    
    freq = word_frequency(text)
    freq_str = ", ".join([f"{k}: {v}" for k, v in freq.items()])
    print(f"Word Frequency : {freq_str}")

# --- Run the program ---
user_text = input("Enter text: ")
analyze_text(user_text)