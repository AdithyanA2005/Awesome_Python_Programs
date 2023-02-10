import random
import string
import os
import words

# This function will return a lowercased word from the list defined inside the words module
def get_random_word():
    no_of_words_available = len(words.word_list)
    word_index = random.randrange(no_of_words_available)
    word = words.word_list[word_index].lower()
    return word


# Function to print the list of available words
def print_avail_alphabets(avail_alphabets):
    print("Available Letters:", end=" ")
    for alphabet in avail_alphabets:
        print(alphabet, end="  ")
    print()


# This function will print the hangman diagram
def print_figure(head, body, hand_one, hand_two, leg_one, leg_two):
    """
    COMPLETE FIGURE
    ╭─────────────╮
    │             |
    │             O
    │            /|\
    │            / \
    │
    ╰─────────────────
    """

    # Top holder bar
    print("╭─────────────╮")
    print("│             │")

    # If mans head is present
    if head: print("│             O")
    else: print("│")

    # If mans body is presend
    if body:
        if hand_one and hand_two:  # For both hands
            print("│            /|\\")
        elif hand_one or hand_two:  # For only one hand
            print("│            /|")
        else:  # For only body
            print("│             |")
    else:
        print("│")

    # If mans legs are present
    if leg_one and leg_two:  # If both legs are present
        print("│            / \\")
    elif leg_one or leg_two:  # If only one leg is present
        print("│            /")
    else:
        print("│")

    # Holder base bar
    print("│")
    print("╰─────────────────")


# This function will print the guessed word char list in a single line
def print_guessed_word(guessed_word):
    guessed_word_str = " ".join(guessed_char_list)
    print(guessed_word_str)


if __name__ == "__main__":
    # List defining which parts of the body are visible
    man = [
        False, # Head
        False, # Body
        False, # Hand_One
        False, # Hand_Two
        False, # Leg_One
        False, # Leg_Two
    ]       

    word_char_list = list(get_random_word())  # Predefined word as a list of characters
    word_length = len(word_char_list)  # Predefined word char list length
    avail_alphabets = list(string.ascii_lowercase)  # Letters available for the word
    guessed_char_list = ["_"] * word_length  # Guessed chars list where empty-spaces are shown as "_"

    while True:
        print_avail_alphabets(avail_alphabets)  # To print list of available alphabets
        print_figure(man[0], man[1], man[2], man[3], man[4], man[5])  # Print the hangman diagram

        # Terminate app if hangman is completely hanged
        if all(man):
            print("GAMEOVER")
            print("--------")
            break

        # Print the guessed words
        print_guessed_word(guessed_char_list)  

        # Take input and clear the screen
        char = input("\nEnter character: ").lower()
        os.system("clear")

        # If input length is not 1 or if it is not a alphabet
        if len(char) != 1 or not char.isalpha() :
            continue

        # If player guessed a wrong character as input
        if char not in word_char_list:
            for i in range(len(man)):
                if man[i] == False:
                    man[i] = True
                    break

        try:  # If character is present inside the list
            while True:
                index = word_char_list.index(char)  # Get index of the alphabet in the word list
                guessed_char_list[index] = word_char_list[index]  # Set the letter in the guessed word
                word_char_list[index] = 0  # Change the char in original word to 0
        except ValueError:  # If the alphabet is no more in the word_char_list remove it from the alphabets list
            if char not in word_char_list and char in avail_alphabets:
                avail_alphabets.remove(char)  # Remove alphabet if alphabet is no more in the word
