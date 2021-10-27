import random

print("You have 3 chances to guess right!! \n")

intervalNumber = int(input("Enter the size of interval: \n"))

intervalNumberValue = random.randint(0, intervalNumber)

print(intervalNumberValue)

chanceCounter = 3
 
while ( chanceCounter != 0):

    guessedNumber = int(input("Guess a number: \n"))
    chanceCounter-= 1
    if intervalNumberValue > guessedNumber:
        print("Heat \n")
        print("Your number: ", guessedNumber)
        print("Your chances: ", chanceCounter)
    elif intervalNumberValue < guessedNumber:
        print("Freeze \n")
        print(guessedNumber)
        print("Your chances: ", chanceCounter)
    elif intervalNumberValue == guessedNumber:
        print("YOU WIN!")
        chanceCounter = 3
    
    