# GUESS_NUMBER_GAME_SIMPLE

# Protocols:-

# Number of guesses = 10
# Print number of guesses left each time
# Game Over When Guesses are all wrong
# No of guesses taken to win

# Coding start's here

# We are importing the random module to choose a random number for the guess
import random


# Let the number('RandomNumber') be the number to be guessed
Random_Number = random.randint(1, 99)

# Let the number('RandomNumber') be the number to be guessed
Random_Number = 15

# Let the number of rounds ('no_of_guesses') default be set at 0
No_of_guesses = 10

# We are creating a 'WHILE LOOP' marked at True to run it infinitely many times
while No_of_guesses > 0:

    # To show the number of try's left
    print(f"Try's left: {No_of_guesses}")

    # Input from the user is stored in variable ("Random_Guess")
    Random_Guess= int(input("Enter your guess"))

    #
    # CORRECT ANSWER
    # If the users input is correct
    if Random_Guess == Random_Number:
        print(f"____________________________\n"
              f"          SUCCESS             \n"
              f"You win and the answer is {Random_Number}"
              f"\n____________________________\n"
              f"You took {11 - No_of_guesses} try's to win")
        break

    #
    # LOWER INPUT:-
    # If the user input is lower than 'Random_Number'
    elif Random_Guess < Random_Number:

        # If the user input is between 10 digit lower than 'Random_Number'
        if Random_Guess > (Random_Number - 10):
            print("Your guess is Smaller \n")

        # If the user input is lower than 10 digit less the 'Random_Number'
        elif Random_Guess <= (Random_Number - 10):
            print("Your guess is very Smaller \n")

    #
    # GREATER INPUT:-
    # If the user input is greater than 'Random_Number'
    elif Random_Guess > Random_Number:

        # If the user input is between Random_Number and Random_Number increased by 10
        if Random_Guess <= Random_Number + 10:
            print("Your guess is Large \n")

        # If the user input is greater than Random_Number increased by 10
        elif Random_Guess > Random_Number + 10:
            print("Your guess is Very Large \n")

    # User can type '1230321' to exit the game
    elif Random_Guess == 1230321:
        break

    # For any input based error it will show
    else:
        print("Unknown Error")
        break

    # This is used because, each time when a input is given, one try should be reduced
    No_of_guesses = No_of_guesses - 1
    continue

# This case will be runned if the user doesn't enter the right number within the given try's
if Random_Guess != Random_Number:
    print(f":    GAME OVER!!!\n"
          f"Better luck next time")
