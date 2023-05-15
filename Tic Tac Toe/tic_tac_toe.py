def display_board(board):
    blankBoard = """
    ___________________
    |     |     |     |
    |  7  |  8  |  9  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  4  |  5  |  6  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  1  |  2  |  3  |
    |     |     |     |
    |-----------------|
    """

    for i in range(1, 10):
        if board[i] == 'O' or board[i] == 'X':
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)


def player_input():
    player1 = input("Pick a marker 'X' or 'O' ")
    while True:
        if player1.upper() == 'X':
            player2 = 'O'
            print(f"You've chosen {player1}, player 2 will be {player2}")
            return player1.upper(), player2
        elif player1.upper() == 'O':
            player2 = 'X'
            print(f"You've chosen {player1}, player 2 will be {player2}")
            return player1.upper(), player2
        else:
            player1 = input("Please pick a marker 'X' or 'O'")

player_input()
