from dice import Dice
import sys


class Player:
    def __init__(self):
        print("CHOOSE YOUR DICE \n----------------")
        print("Press '1' for Player-1 \nPress '2' for Player-2 \nPress '3' for Player-3 \nPress 'Q' for Quiting")

    def play(self):
        result = self.roll_dice()
        print(result)

    def roll_dice(self):
        dice_version = self.choose_dice_version()
        dice_type = self.choose_dice_type(dice_version)
        if dice_type == "normal_roll":
            dice_roll = dice.normal_roll()
        elif dice_type == "win_roll":
            dice_roll = dice.win_roll()
        elif dice_type == "loose_roll":
            dice_roll = dice.loose_roll()
        else:
            dice_roll = "Error"
        return dice_roll

    @staticmethod
    def choose_dice_version():
        selection = input("Select The Dice Number")
        return selection

    @staticmethod
    def choose_dice_type(selection):
        if selection == "1":
            return "normal_roll"
        elif selection == "2":
            return "win_roll"
        elif selection == "3":
            return "loose_roll"
        elif selection == "Q":
            sys.exit("See you again, Bye")
        elif selection == "q":
            sys.exit("See you again, Bye")
        else:
            return "error"


dice = Dice()
