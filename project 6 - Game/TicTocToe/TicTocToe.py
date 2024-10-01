import multiplayer     
import time
import single_player

user_choice = int(input("pc=> 1 , two player=> 2 : "))
if user_choice == 1:
  while True:  
    start_time =  time.time()  
    single_player.show_board()
    single_player.user_move()
    result = single_player.check_game()
    if result:
        single_player.show_board()
        break
        
    single_player.computer_move()
    result = single_player.check_game()
    if result:
         single_player.show_board()
         break
    end_time = time.time()
    execution_time = end_time - start_time
    print(f": {execution_time:.6f} ")
if user_choice == 2:
    start_time =  time.time()
    multiplayer.show_board()
    multiplayer.main()
 
 
    
    end_time = time.time()
    execution_time = end_time - start_time
    print(f": {execution_time:.6f} ")
    
    


