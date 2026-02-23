#input
text = input("Enter text:")
words = text.split()

print("Words:",len(words))
vowels = "aeiouAEIOU"
v = 0
c = 0
for ch in text:
    if ch in vowels:
        v+=1
    elif ch.isalpha():
        c+=1
print("Vowels:",v)
print("Consonants:",c)
print("Reverse:",text[::-1])
clean=text.replace(" ", "").lower()
if clean==clean[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
new_text=""
for ch in text:
    if ch not in vowels:
        new_text+=ch
print("Without vowels:",new_text)
longest=""
for w in words:
    if len(w)>len(longest):
        longest=w
print("Longest word:", longest)
freq={}
for w in words:
    w=w.lower()
    if w in freq:
        freq[w]+=1
    else:
        freq[w]=1
print("Word frequency:", freq)