import random

Random_Number = random.randint(10, 15)
attempts = 0

while True:
    user_number = int(input("Enter your guess (between 10 and 15): "))
    attempts += 1
    
    if user_number == Random_Number:
        print("💋 Congratulations! You've guessed the correct number!")
        print(f"You took {attempts} attempts.")
        break  
    elif user_number > 15 or user_number < 10:
        print("❌ Please guess a number between 10 and 15.")
    elif user_number > Random_Number:
        print("🔽 Lower! Try a smaller number.")
    elif user_number < Random_Number:
        print("🔼 Higher! Try a larger number.")
    if user_number > 12:
        print("Hint: Your guess is greater than 12.")
    elif user_number < 12:
        print("Hint: Your guess is less than 12.")
