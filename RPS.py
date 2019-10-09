import random

exit = False

print("Hello, and welcome to Rock Paper Scissors")

print("""
Press 1 for rock
Press 2 for paper
Press 3 for scissors
Press 4 to exit
""")
while exit != True: 
    # Get user input
    userChoice = input("Choice:")
    while not userChoice: # In case user submits empty string
        userChoice = input("Choice:")
    
    # Cast input to int
    userChoice = int(userChoice)

    # User Chooses to exit
    if userChoice == 4:
        exit = True
    # Verify valid number was selected, no othe valid options to choose from
    elif userChoice != 1 and userChoice != 2 and userChoice != 3:
        print("Invalid Input, Try Again")

    # Get random computer choice
    computerChoice = random.randint(1,3)

    # Find game result and print it
    if userChoice == 1 and computerChoice == 1:
        print("ROCK VS. ROCK, Tie Game!")
    elif userChoice == 1 and computerChoice == 2:
        print("ROCK VS. PAPER, You Lose :(")
    elif userChoice == 1 and computerChoice == 3:
        print("ROCK VS. SCISSORS, You Win!")
    elif userChoice == 2 and computerChoice == 1:
        print("PAPER VS. ROCK, You Win!")
    elif userChoice == 2 and computerChoice == 2:
        print("PAPER VS. PAPER, Tie Game!")
    elif userChoice == 2 and computerChoice == 3:
        print("PAPER VS. SCISSORS, You Lose :(")
    elif userChoice == 3 and computerChoice == 1:
        print("SCISSORS VS. ROCK, You Lose :(")
    elif userChoice == 3 and computerChoice == 2:
        print("SCISSORS VS. PAPER, You Win!")
    elif userChoice == 3 and computerChoice == 3:
        print("SCISSORS VS. SCISSORS, Tie Game!")


print("Exiting Game")