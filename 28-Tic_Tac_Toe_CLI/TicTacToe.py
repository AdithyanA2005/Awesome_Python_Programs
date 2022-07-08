class TicTacToe:
    # Init Functions
    def __init__(self, X_State, O_State):
        self.xState = X_State
        self.oState = O_State

    # Get the value to be placed in a box
    def getBoardValue(self, place):
        value = "X" if self.xState[place] else ("O" if self.oState[place] else place)
        return value

    # Print the board with appropriate values or symbols
    def printBoard(self):
        print("\n")
        print(f" {self.getBoardValue(0)} │ {self.getBoardValue(1)} │ {self.getBoardValue(2)}")
        print("───│───│───")
        print(f" {self.getBoardValue(3)} │ {self.getBoardValue(4)} │ {self.getBoardValue(5)}")
        print("───│───│───")
        print(f" {self.getBoardValue(6)} │ {self.getBoardValue(7)} │ {self.getBoardValue(8)}")
        print("\n")

    # Checks for player win
    def checkWin(self):
        # Win Chances
        winChances = [
            # Row wins
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],

            # Column wins
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],

            # Diagonal wins
            [0, 4, 8],
            [2, 4, 6]
        ]

        for chance in winChances:
            if (sum([self.xState[chance[0]], self.xState[chance[1]], self.xState[chance[2]]]) == 3): return 1  # If X wins
            if (sum([self.oState[chance[0]], self.oState[chance[1]], self.oState[chance[2]]]) == 3): return 0  # If O wins
        return -1  # If no player wins
