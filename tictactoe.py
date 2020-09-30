# tic-tac-toe by JAUHAR

'''
    First move is of 'X'
    Coordinates as following:
    (1, 3) (2, 3) (3, 3)
    (1, 2) (2, 2) (3, 2)
    (1, 1) (2, 1) (3, 1)
    Game ends when any one of the player wins or there is a draw

    ---- example gameplay ----
    ---------
    |       |
    |       |
    |       |
    ---------
    Enter the coordinates: > 2 2
    ---------
    |       |
    |   X   |
    |       |
    ---------
    Enter the coordinates: > 1 3
    ---------
    | O     |
    |   X   |
    |       |
    ---------
    Enter the coordinates: > 3 1
    ---------
    | O     |
    |   X   |
    |     X |
    ---------
    Enter the coordinates: > 1 2
    ---------
    | O     |
    | O X   |
    |     X |
    ---------
    Enter the coordinates: > 1 1
    ---------
    | O     |
    | O X   |
    | X   X |
    ---------
    Enter the coordinates: > 3 2
    ---------
    | O     |
    | O X O |
    | X   X |
    ---------
    Enter the coordinates: > 2 1
    ---------
    | O     |
    | O X O |
    | X X X |
    ---------
    X wins

'''

# board is the virtual game board, initially empty
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

def print_board(board):
    print('-' * 9)
    print('|', board[0][2], board[1][2], board[2][2], '|')
    print('|', board[0][1], board[1][1], board[2][1], '|')
    print('|', board[0][0], board[1][0], board[2][0], '|')
    print('-' * 9)

# function has_a_row() takes a char parameter, either 'X' or 'O',
# checks whether or not the move results in a win
def has_a_row(char):
    text = [char, char, char]
    cells = [element for row in board for element in row]
    if cells[0:3] == text or cells[3:6] == text or cells[6:9] == text:
        return True
    if (cells[0:7:3] == text or cells[1:8:3] == text or cells[2:9:3] == text):
        return True
    if cells[0:9:4] == text or cells[2:8:2] == text:
        return True
    return False

# game starts from here
# ------------------------------------------------------------------------------------
print_board(board)

# The number of chance is 9, since there are at most 9 places to fill on the board
chance = 0
while(True):
    # only integer values of x and y between 1 and 3 are valid
    x, y = input('Enter the coordinates: > ').split()
    if x not in '1234567890' or y not in '1234567890':
        print('You should enter numbers!')
    elif x not in '123' or y not in '123':
        print('Coordinates should be from 1 to 3')
    elif board[int(x) - 1][int(y) - 1] in 'XO':
        print('This cell is occupied! Choose another one!')
    else:
        # add X to the coordinate on even turn
        if chance % 2 == 0:
            board[int(x) - 1][int(y) - 1] = 'X'
            print_board(board)
            if has_a_row('X'):
                print('X wins')
                break
        else:
        # add O to the coordinate on odd turn
            board[int(x) - 1][int(y) - 1] = 'O'
            print_board(board)
            if has_a_row('O'):
                print('O wins')
                break
        chance += 1

    # board is filled and nobody wins => Draw
    if chance >= 9 and not has_a_row('X') and not has_a_row('O'):
        print('Draw')
        break


# ---------- END -----------------

