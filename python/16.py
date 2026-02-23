import random
number=random.randint(1, 100)
print("Guess a number between 1 and 100")
for i in range(7):
    guess=int(input("Enter guess:"))
    if guess==number:
        print("Correct!")
        break
    elif guess>number:
        print("Too high")
    else:
        print("Too low")
    print("Attempts left:",6-i)
if guess!=number:
    print("Game over.Number was",number)
