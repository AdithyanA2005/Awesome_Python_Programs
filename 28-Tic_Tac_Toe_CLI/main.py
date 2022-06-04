from TicTacToe import TicTacToe

if __name__ == "__main__":
    X_State = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    O_State = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    game = TicTacToe(X_State, O_State)
    turn = 1  # 1 for X && 0 for O

    while True:
        # Printing the board
        game.printBoard()

        # Chance for player X
        if turn == 1:
            print("Chance for X")
            value = int(input("Please enter a place: "))
            game.xState[value] = 1

        # Chance for player O
        else:
            print("Chance for O")
            value = int(input("Please enter a place: "))
            game.oState[value] = 1

        # Changing players
        turn = 1 - turn

        # Checks for Player win
        wins = game.checkWin()

        # If X winned            
        if wins == 0: 
            print("Player O won the match")
            break

        # If O winned            
        if wins == 1: 
            print("Player X won the match")
            break
