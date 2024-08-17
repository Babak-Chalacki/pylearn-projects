import random


Random_Number = random.randint(10, 15)
attempts = 0
while True:
    user_number = int(input("Enter your guess: "))
    attempts += 1
    if user_number == Random_Number:
        print("💋 Congratulations! You've guessed the correct number!")
        print(f"You took {attempts} attempts.")
        break  
    else:
        print("🤢 Try again!")
