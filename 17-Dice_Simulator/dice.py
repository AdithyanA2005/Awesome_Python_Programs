import random


class Dice:
    @staticmethod
    def normal_roll():
        """
        This will return a random number of the dice
        """
        score_number = random.randint(1, 6)
        return score_number

    @staticmethod
    def win_roll():
        """
        This will return a number from dice with more winning chances
        """
        score_number = random.randint(1, 6)
        rand_number = random.randint(0, 3)
        if score_number < 4:
            score_number = score_number + rand_number
            return score_number
        else:
            return score_number

    @staticmethod
    def loose_roll():
        """
        This will return a number from the dice with more loosing chances
        """
        score_number = random.randint(1, 6)
        rand_number = random.randint(0, 3)
        if score_number >= 4:
            score_number = score_number - rand_number
            return score_number
        else:
            return score_number
