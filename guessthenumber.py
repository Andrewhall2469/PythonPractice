import random
number = random.randint(1,100)
print (number)
numGuess = int(input("How many guesses you can take: "))

a = 0
winCon = "N"

while a < numGuess:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > number:
        print("Lower")
    elif guess < number:
        print("Higher")
    elif guess == number:
        winCon = "Y"
        break
    a=a+1

print (winCon)

if winCon == "Y":
    print("Congratulations, you did it in",a,"guesses")
else:
    print("Game over, the correct answer was:",number)