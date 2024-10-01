import random


game_board =[['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]


def show_board():
    for row in game_board:
       for cell in row:
           print(cell,end="")
       print()   


def user_move():
    while True:
        try:  
            row = int(input("enter row (0-2)=> "))
            col = int(input("enter col (0-2)=> "))
            if game_board[row][col] == "-":
                game_board[row][col] = "X"
                break
            else:
                print("cell is full")
        except (ValueError , IndexError):
            print("please enter numbers between 0 and 2.")    
                

def computer_move():
    empty_cell = [(i,j) for i in range(3) for j in range(3) if game_board[i][j] == '-']
    if empty_cell:
        row , col = random.choice(empty_cell)
        game_board[row][col] = "O"

def check_game():
    for i in range(3):
        if game_board[i][0] == "X" and game_board[i][1] == "X" and game_board[i][2] == "X":
            print("X wins")
            return True
        if game_board[i][0] == "O" and game_board[i][1] == "O" and game_board[i][2] == "O":
            print("O wins")
            return True
    for i in range(3):
        if game_board[0][i] == "O" and game_board[1][i] == "O" and game_board[2][i] == "O":
            print("O wins")
            return True    
        if game_board[0][i] == "X" and game_board[1][i] == "X" and game_board[2][i] == "X":
            print("X wins")
            return True    
    if (game_board[0][0] == 'X' and game_board[1][1] == 'X' and game_board[2][2] == 'X') or \
       (game_board[0][2] == 'X' and game_board[1][1] == 'X' and game_board[2][0] == 'X'):
        print("X wins")
        return True
    elif (game_board[0][0] == 'O' and game_board[1][1] == 'O' and game_board[2][2] == 'O') or \
         (game_board[0][2] == 'O' and game_board[1][1] == 'O' and game_board[2][0] == 'O'):  
        print("O wins")
        return True
    if all(cell in ['X', 'O'] for row in game_board for cell in row):
        print("It's a draw!")
        return True
    return False
        