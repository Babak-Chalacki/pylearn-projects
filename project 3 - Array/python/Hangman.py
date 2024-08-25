import random

words = ["python", "hangman", "programming", "developer", "challenge", "computer", "science"]
chosen_word = random.choice(words)
guessed_letters = []
max_attempts = 6
attempts = 0

print("Welcome to Hangman!")
print("_ " * len(chosen_word))  

while attempts < max_attempts:
    guess = input("Guess a letter: ").lower()  
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        print("Good guess!")
    else:
        print("Oops! That letter is not in the word.")
        attempts += 1  

    current_state = ''.join(letter if letter in guessed_letters else '_' for letter in chosen_word)
    print("Current word: ", ' '.join(current_state))

    if '_' not in current_state:
        print("🎉 Congratulations! You've guessed the word:", chosen_word)
        break

if attempts == max_attempts:
    print("😢 You've run out of attempts! The word was:", chosen_word)