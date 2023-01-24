'''
 X | O | X
---+---+---
 O | O | X
---+---+---
   | X |
'''

import random


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3)
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
    print("\n")


def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board


def printx(square_num):
    global board
    board[((square_num - 1) // 3)][(square_num - 1 - ((square_num - 1) // 3)*3)] = "X"
    print_board_and_legend(board)

def put_in_board(board, mark, square_num):
    board[(square_num - 1) // 3][
    square_num - 1 - ((square_num - 1) // 3)*3] = mark

def get_free_squares(board):
    L = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                L.append([i, j])
    return L

def make_random_move(board, mark):
    count = 0
    while count < 1:
        rand = (int(10 * random.random()))
        if board[(rand - 1) // 3][
        rand - 1 - ((rand - 1) // 3)*3] == " ":
            put_in_board(board, mark, rand)
            count += 1


def is_row_all_marks(board, row_i, mark):
    return board[row_i][0] == board[row_i][1] == board[row_i][2] == mark


def is_col_all_marks(board, col_i, mark):
    return board[0][col_i] == board[1][col_i] == board[2][col_i] == mark


def check_diag(board, mark):
    if board[0][0] == board[1][1] == board[2][2] == mark or board[0][2] == board[1][1] == board[2][0] == mark:
        return True
    return False

def is_win(board, mark):
    t_f = False
    if check_diag(board, mark) == True:
        t_f = True
    for i in range(3):
        if is_col_all_marks(board, i, mark) == True or is_row_all_marks(board, i, mark) == True:
            t_f = True
    return t_f

def computer_move(board, mark):
    for i in get_free_squares(board):
        board[i[0]][i[1]] = mark
        if is_win(board, mark):
            return
        else:
            board[i[0]][i[1]] = " "
    make_random_move(board, mark)

if __name__ == '__main__':
    #board = make_empty_board()
    #print_board_and_legend(board)
    #val = input("sup")
    #print(val)

    print("\n\n")

    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    #print(is_win(board,"X"))
    #t_f = is_row_all_marks(board, 0, "X")
    #print(t_f)
    print(board)
    print(get_free_squares(board))
    #make_random_move(board,"X")
    #print_board_and_legend(board)
    #printx(1)
    #put_in_board(board, "X", 9 )
    #asking two users to enter values
    '''
    for i in range(9):
        input_num = int(input("Please enter a number between 1 and 9"))
        if (i%2 == 0):
            mark = "X"
        else:
            mark = "O"
        put_in_board(board, mark, input_num)

        '''

    #AI vs user

'''
    for i in range(10):
        computer_move(board,"X")
        print_board_and_legend(board)
        if is_win(board, "X") == True:
            print("The computer won")
            break
        input_num = int(input("Please enter a number between 1 and 9"))
        put_in_board(board, "O", input_num)
        print_board_and_legend(board)
        if is_win(board, "O") == True:
            print("You won")
            break
            '''

























