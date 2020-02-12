# ------------------- Global Variables -----------------------
# Game board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# if game still going
game_still_going = True

# who win? or tie?
winner = None

# Whose turn si it
current_player = "X"

def startScreen():
    print("Welcome to the game of Tic Tac Toe!")
    userResponse = input("Do you want to play the game? (Y/N) ")

    if userResponse == 'y':
        print("Okay, let's go.\n")
    elif userResponse == 'Y':
        print("Okay, let's go.\n")        
    else:
        print("Not okay. Bye.")
        exit

def displayBoard():
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")

# Play the game of Tic Tac Toe
def playGame():
    global current_player

    # Show the start screen
    startScreen()

    #Display initial board
    displayBoard()

    while game_still_going:
        
        # Handle a single turn of an arbitary player
        handleTurn()

        # Check if game has ended
        check_if_game_over()

        # Flip to the other player
        current_player = flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print("\n" + winner + " won.")
    elif winner == None:
        print("\n" + "Tie.")

def handleTurn():

    print("\n" + current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    print()

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print ("It's been occupied. Select again.")


    board[position] = current_player
    displayBoard()

def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    # set up global variables
    global winner

    # Check rows
    row_winner = check_rows()
    # Check columns
    column_winner = check_columns()
    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # there was no win
        winner = None
    
def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False

def check_rows():
    global game_still_going
    # check if any of the rows have the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row matches, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():
    global game_still_going
    # check if any of the rows have the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any row matches, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

def check_diagonals():
    global game_still_going
    # check if any of the rows have the same value
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    # if any row matches, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    # return winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

def flip_player():
    global current_player

    return "O" if current_player == "X" else "X"

#Main Function
playGame()
    


    

