<?php
session_start();

if (!isset($_SESSION['chosen_word'])) {
    $words = ["python", "hangman", "programming", "developer", "challenge", "computer", "science"];
    $_SESSION['chosen_word'] = $words[array_rand($words)];
    $_SESSION['guessed_letters'] = [];
    $_SESSION['attempts'] = 0;
    $_SESSION['max_attempts'] = 6;
}

$chosen_word = $_SESSION['chosen_word'];
$guessed_letters = $_SESSION['guessed_letters'];
$attempts = $_SESSION['attempts'];
$max_attempts = $_SESSION['max_attempts'];

if (isset($_GET['guess'])) {
    $guess = strtolower($_GET['guess']);
    
    if (strlen($guess) != 1 || !ctype_alpha($guess)) {
        echo "Please enter a single letter.<br>";
    } elseif (in_array($guess, $guessed_letters)) {
        echo "You've already guessed that letter. Try again.<br>";
    } else {
        $guessed_letters[] = $guess;
        $_SESSION['guessed_letters'] = $guessed_letters;

        if (strpos($chosen_word, $guess) === false) {
            echo "Oops! That letter is not in the word.<br>";
            $attempts++;
            $_SESSION['attempts'] = $attempts;
        } else {
            echo "Good guess!<br>";
        }

        $current_state = '';
        foreach (str_split($chosen_word) as $letter) {
            $current_state .= in_array($letter, $guessed_letters) ? $letter : '_';
        }

        echo "Current word: " . implode(' ', str_split($current_state)) . "<br>";

        if (strpos($current_state, '_') === false) {
            echo "🎉 Congratulations! You've guessed the word: $chosen_word<br>";
            session_destroy();
            exit;
        }
    }
}

if ($attempts >= $max_attempts) {
    echo "😢 You've run out of attempts! The word was: $chosen_word<br>";
    session_destroy();
    exit;
}

echo "<form method='get'>";
echo "<input type='text' name='guess' maxlength='1' required>";
echo "<input type='submit' value='Guess'>";
echo "</form>";
?>