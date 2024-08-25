import random
while True:
    choices = ["rock","paper","scissors"]
    cumpoterChoice = random.choice(choices)
    userChoice = input("enter your choice").lower()
    
    if userChoice not in choices:
        print(f"invalid {userChoice}")
    else:
        print(f"cumpoterChoice = {cumpoterChoice}")
        print(f"your Choice = {userChoice}")
    
        if cumpoterChoice == userChoice:
            print("equal")
        elif (cumpoterChoice == "rock" and userChoice == "scissors") or\
        (cumpoterChoice == "scissors" and userChoice == "papaer") or\
        (cumpoterChoice == "paper" and userChoice == "rock") :
            print("cumpoter win")
        else:
            print("you win")    
                
