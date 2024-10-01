

game_board =[['-','-','-'],
             ['-','-','-'],
             ['-','-','-']]


def show_board():
    for row in game_board:
       for cell in row:
           print(cell,end='')
       print()
       
def player_symbol(symbol):
    while True:
        try: 
            user_row = int(input(f'enter the row player {symbol} '))      
            user_col = int(input(f'enter the col player {symbol} ')) 
            if check_game():
                break
            if choice_validator(user_row,user_col,symbol):
                break
        except ValueError:
          print("Please enter integers only.")  
     

def choice_validator(row,col,user_symbol):
    if 0 <= row <= 2 and 0 <= col <= 2:
        if game_board[row][col] == 'X' or game_board[row][col] == 'O':
            print("cell is full")
            return False
        else:
            game_board[row][col] = user_symbol  
            show_board() 
            return True
    else:
        print('out of range') 
        return False  


        
def check_game():
    for i in range(3):
        if game_board[i][0] == 'X' and game_board[i][1] == 'X' and game_board[i][2] == 'X':
            print("X wins")
            return True
        elif game_board[i][0] == 'O' and game_board[i][1] == 'O' and game_board[i][2] == 'O':
            print("O wins")
            return True
            
    for i in range(3):
        if game_board[0][i] == 'X' and game_board[1][i] == 'X' and game_board[2][i] == 'X':
            print("X wins")
            return True
        elif game_board[0][i] == 'O' and game_board[1][i] == 'O' and game_board[2][i] == 'O':
            print("O wins")
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

def main(): 
    while True:  
        player_symbol('X') 
        if check_game():
            break  
            
        player_symbol('O')
        if check_game():
            break
                          
        
         
user_choice = int(input("pc=> 1 , two player=> 2 : "))
if user_choice == 1:
    print("ok")
    
if user_choice == 2:
    show_board()
    main()
 
 
    
       
    
 
