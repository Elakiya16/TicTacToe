
# board
# display Board
# play game
# check win
# check rows
# check columns
# check diagonals
# check Tie
# flip player

# -----global variables------
Board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

# if game is still going
game_still_going = True
# who won? or tie?
winner = None
# whose turn is it
current_player = "x"
def display_board():
    print(Board[0]+"|"+Board[1]+"|"+Board[2])
    print(Board[3]+"|"+Board[4]+"|"+Board[5])
    print(Board[6]+"|"+Board[7]+"|"+Board[8])
def play_game():

    #  display initial board
    display_board()
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)
        check_if_game_over()
        flip_player()
# the game is ended
    if winner == "x" or winner == "o":
        print(winner + " Won...")
    elif winner == None:
        print("Tie...")


def handle_turn(player):

    print(player + "'s turn..")
    position = input("Enter position from 1 to 9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Enter position from 1 to 9: ")
        position = int(position) - 1
        if Board[position] == "-":
            valid = True
        else:
            print("You can't go there.")

    Board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    # set up global variables
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return
def check_rows():
    global game_still_going
    # check if any rows have all the same value
    row_1 = Board[0] == Board[1] == Board[2] != "-"
    row_2 = Board[3] == Board[4] == Board[5] != "-"
    row_3 = Board[6] == Board[7] == Board[8] != "-"
    # if any row have match
    if row_1 | row_2 | row_3:
        game_still_going = False
    # return the winner (x or o)
    if row_1:
        return Board[0]
    if row_2:
        return Board[3]
    if row_3:
        return Board[6]
    return

def check_columns():
    global game_still_going
    # check if any rows have all the same value
    column_1 = Board[0] == Board[3] == Board[6] != "-"
    column_2 = Board[1] == Board[4] == Board[7] != "-"
    column_3 = Board[2] == Board[5] == Board[8] != "-"
    # if any column have match
    if column_1 | column_2 | column_3:
        game_still_going = False
    # return the winner (x or o)
    if column_1:
        return Board[0]
    if column_2:
        return Board[1]
    if column_3:
        return Board[2]
    return

def check_diagonals():
    global game_still_going
    # check if any rows have all the same value
    diagonal_1 = Board[0] == Board[4] == Board[8] != "-"
    diagonal_2 = Board[6] == Board[4] == Board[2] != "-"

    # if any row have match
    if diagonal_1 | diagonal_2:
        game_still_going = False
    # return the winner (x or o)
    if diagonal_1:
        return Board[0]
    elif diagonal_2:
        return Board[6]
    return

def check_if_tie():
    global game_still_going
    if "-" not in Board:
        game_still_going = False
    return

def flip_player():
    global current_player
    # if a current player was x, then then changes it to o
    if current_player == "x":
        current_player = "o"
    # if a current player was o, then then changes it to x
    elif current_player == "o":
        current_player = "x"
    return



play_game()
