"""
##############################################################################
SNAKE WATER GUN:-                                                            #
#################                                                            #
                                                                             #
                #######################################################      #
                 In this game the Player will play with the computer         #
                 'Computer' and the user 'Player'                            #
                #######################################################      #
                                                                             #
##############################################################################
"""

# Importing Modules needed for the game
import random


# FUNCTION'S
# Function's needed for the program
from numpy import poly1d


def playRule(computer, player):
    # 1) If the computer and the player choose same nothing will happen
    if computer == player:
        return None

    # 2) If the computer chooses 'Snake'
    elif computer == 's':
        # and player choose 'Water', Computer got point
        if player == 'w':
            return False
        # or Player choose 'Gun', Player got point
        elif player == 'g':
            return True

    # 3) If computer chooses 'Water'
    elif computer == 'w':
        # and player choose 'Gun', Computer got point
        if player == 'g':
            return False
        # or player choose 'Snake', Player got point
        elif player == 's':
            return True

    # 4) If compute chooses 'Gun'
    elif computer == 'g':
        # and player choose 'Snake', Computer got point
        if player == 's':
            return False
        # or player choose 'Water', Player got point
        elif player == 'w':
            return True


# PROGRAM START HERE:

# There are only 10 rounds
NoOfRounds = 10

# We are creating a variable points to calculate the scores
points = 0

# We will also show the rules to the user
print("There are only 10 rounds\n"
      "If you scored more than 6 time\n"
      "You will 'win' otherwise You 'loose'\n")
# To run the code infinitely many times
while NoOfRounds > 0:
    # First the turn is for the computer and we will print
    print("\n__________________________________________\n"
          f"No of tries left: {NoOfRounds}\n"
          f"__________________________________________\n"
          "Computer Turn: Snake(s) Water(w) or Gun(g)")

    # We use the 'Random' module to make the computer choose "'s' or 'w' or 'g'"  randomly the 'randint' provide number
    # from first number to the last number
    RandomNumber = random.randint(1, 3)

    # Now we will assign the numbers to snake or water or gun
    if RandomNumber == 1:  # If random number is 1 the computer choose for 'Snake'
        Computer = 's'

    elif RandomNumber == 2:  # If random number is 2 the computer choose for 'Water'
        Computer = 'w'

    elif RandomNumber == 3:  # If random number is 3 the computer choose for 'Gun'
        Computer = 'g'

    # After the computer have choose we will tell the user that the comuter had choosed
    print(f"Computer Choose")

    # After the computer it is the players turn to put the input
    Player = input("\nYour Turn: Snake(s) Water(w) or Gun(g)")

    # We are calling the function we created earlier in 'result'
    result = playRule(Computer, Player)

    # We will also show the selection of the Computer and the Player to the user
    print(f"\nComputer Choose: {Computer}")
    print(f"You Choose: {Player}\n")

    # Now we are creating other if case to declare who had scored the point

    if result is None:  # if The user and the computer are in tie('None')
        points = points
        print("This turn was a tie round")

    elif result:  # If the player scored
        points = points + 1
        print("You Scored the Point")

    else:  # If the computer scored
        points = points - 1
        print('Computer Scored the Point ')

    # after each rounds the number of round is reduced
    NoOfRounds = NoOfRounds - 1
    print(points)

# Now Finally we need to print who is the winner
if points > 5:  # If the user scored more than computer
    print(f"YOU HAVE 'WINED' : {points}")

elif points < 5:  # if The user scored less than computer
    print(f"YOU 'LOOSE' : {points}")

elif points == 5:  # If the match was a tie
    print(f"THE MATCH IS A TIE : {points}")
