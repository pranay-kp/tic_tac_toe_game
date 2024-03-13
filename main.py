print('''
  _______ _____ _____   _______       _____   _______ ____  ______
 |__   __|_   _/ ____| |__   __|/\   / ____| |__   __/ __ \|  ____|
    | |    | || |         | |  /  \ | |         | | | |  | | |__
    | |    | || |         | | / /\ \| |         | | | |  | |  __|
    | |   _| || |____     | |/ ____ | |____     | | | |__| | |____
    |_|  |_____\_____|    |_/_/    \_\_____|    |_|  \____/|______|

''')


def check_winner(board, player):
    #rows and columns
    for i in range(3):
        if all( board[i][j] == player for j in range(3)):
            return True
        if all( board[j][i] == player for j in range(3)):
            return True

    #diagonals
    if all (board[i][i] == player for i in range(3)):
        return True
    if all (board[i][2-i] == player for i in range(3)):
        return True

    return False


board = [[' ',' ',' '],
         [' ',' ',' '],
         [' ',' ',' ']]

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("_" * 9)

print_board(board)
while True:


    while True:
        user1_row = int(input("User 1 Select row 0,1,2 "))
        user1_col = int(input(" User 1 Select col 0,1,2 "))

        if board[user1_row][user1_col] == " ":
            board[user1_row][user1_col] = "X"
            print_board(board)
            break
        else:
            print("position already occupied")

    if check_winner(board, "X"):
        print("User1 wins!")
        break

    #checking draw
    if all(cell != " " for row in board for cell in row):
        print("It's a draw!")
        break


    while True:
        user2_row = int(input("User 2, select row (0, 1, 2): "))
        user2_col = int(input("User 2, select column (0, 1, 2): "))

        if board[user2_row][user2_col] == " ":
            board[user2_row][user2_col] = "O"
            print_board(board)
            break
        else:
            print("That position is already taken. Try again.")

    if check_winner(board, "O"):
        print("User2 wins!")
        break

    # checking draw
    if all(cell != " " for row in board for cell in row):
        print("It's a draw!")
        break








