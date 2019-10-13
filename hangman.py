import random

def checkForWin(guessedArray):
    for i in range(len(guessedArray)):
        if guessedArray[i] == False:
            return False
    
    return True

def printWord(choice, guessedArray):
    phraseLength = len(choice)
    for i in range(phraseLength):
        # Show all spaces in name
        if choice[i] == ' ':
            guessedArray[i] = True

        # User has guessed this letter, display it
        if guessedArray[i] == True:
            print(choice[i], end = " ")
        # User has not guessed this letter, hide it
        else:
            print("_", end = " ")

print("WELCOME TO HANG MAN")

# List of movies that can be used for the game
moviesArr = ["UP", "IT", "Iron Man", "Titanic", "The Lion King", 
             "Tropic Thunder", "The Matrix", "Frozen"]

# Randomly select phrase for game
choice = random.choice(moviesArr)
phraseLength = len(choice)

# Keep track if string[i] has been guessed
guessedArray = [False] * phraseLength

guessesLeft = 5

runGame = True
while runGame == True:
    # Print # of guesses left
    if guessesLeft > 0:
        print(str(guessesLeft) + " guesses remaining")
    else:
        print("Out of guesses, you lose :(")
        exit()
    
    # Print word being guessed - "_" for not yet guessed letters
    printWord(choice, guessedArray)
    
    if checkForWin(guessedArray) == True:
        print("\nYou Win!")
        exit()

    print()# print newline
        
    userChoice = input("Enter a letter: ")

    # Invalid input (no input / input too long)
    if len(userChoice) == 0 or len(userChoice) > 1:
        print("Invalid input, try again")
        continue

    # Keep track of if a valid letter was found this round
    found = False

    # Check if user guesses a correct letter
    for i in range(phraseLength):
        if userChoice.lower() == choice[i].lower():
            guessedArray[i] = True
            found = True
    
    if not found:
        guessesLeft -= 1

