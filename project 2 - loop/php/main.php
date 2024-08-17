<?php
$randomNumber = rand(10, 15);
$attempts = 0;

echo "Welcome to the Number Guessing Game!\n";

while (true) {
    $userInput = readline("Enter your guess: ");
    
    $userNumber = (int)$userInput;
    $attempts++;

    if ($userNumber === $randomNumber) {
        echo "💋 Congratulations! You've guessed the correct number!\n";
        echo "You took $attempts attempts.\n";
        break;  
    } else {
        echo "🤢 Try again!\n";
    }
}
?>