<?php
$choices = array("rock", "paper", "scissors");

$userChoice = isset($_GET['choice']) ? strtolower($_GET['choice']) : '';

$computerChoice = $choices[array_rand($choices)];

if (!in_array($userChoice, $choices)) {
    echo "Invalid choice: $userChoice";
} else {
    echo "Computer's choice: $computerChoice\n";
    echo "Your choice: $userChoice\n";

    if ($userChoice == $computerChoice) {
        echo "It's a tie!";
    } elseif (
        ($computerChoice == "rock" && $userChoice == "scissors") ||
        ($computerChoice == "scissors" && $userChoice == "paper") ||
        ($computerChoice == "paper" && $userChoice == "rock")
    ) {
        echo "Computer wins!";
    } else {
        echo "You win!";
    }
}
?>