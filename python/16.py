import random
best=7
number=random.randint(1, 100)
print("Guess number between 1 and 100")
for i in range(7):
    guess = int(input("Enter guess:"))
    if guess==number:
        print("Correct! Attempts used:", i+1)
        if i+1<best:
            best=i+1
            print("New best score")
        break
    if guess>number:
        print("Too high")
    else:
        print("Too low")
    if abs(guess-number)<=5:
        print("Close guess")
    print("Attempts left:",6-i)
if guess!=number:
    print("You lost.Number was",number)
print("Best score:", best)
