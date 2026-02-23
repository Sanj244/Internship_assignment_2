#Get User Input
sentence = input("Enter a sentence: ").strip()
if not sentence:
    print("Please enter a valid sentence")
else:
    words = sentence.split()
    total_character= len(sentence)
    no_spaces = total_character - sentence.count(" ")
#Results 
    print(f"1.Original sentence:{sentence}")
    print(f"2.Total(with spaces):{total_character}")
    print(f"3.Total:{no_spaces}")
    print(f"4.Word count:{len(words)}")
    print(f"5.In UPPERCASE:{sentence.upper()}")
    print(f"6.In lowercase:{sentence.lower()}")
    print(f"7.In Title Case:{sentence.title()}")
    print(f"8.The first word is:{words[0]}")
    print(f"9.The last word is:{words[-1]}")
    print(f"10.Backward:{sentence[::-1]}")