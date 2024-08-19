<?php
function rollDie() {
    return rand(1, 6); 
}


while (true) {
    $computer = rollDie();
    echo "Computer number = $computer\n"; 

    if ($computer == 6) {
        echo "You win!\n"; 
    } else {
        echo "You lose!\n"; 
        break; 
    }
}
?>