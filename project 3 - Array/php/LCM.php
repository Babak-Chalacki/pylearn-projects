<?php
if (isset($_GET['num1']) && isset($_GET['num2'])) {
    $num1 = intval($_GET['num1']);
    $num2 = intval($_GET['num2']);

    if ($num1 < $num2) {
        $smaller = $num1;
    } else {
        $smaller = $num2;
    }

    $gcd = 1;
    for ($i = 1; $i <= $smaller; $i++) {
        if ($num1 % $i == 0 && $num2 % $i == 0) {
            $gcd = $i;
        }
    }

    $lcm = ($num1 * $num2) / $gcd;

    echo "The Least Common Multiple (LCM) of $num1 and $num2 is: $lcm";
} else {
    echo "Please provide both num1 and num2 in the URL.";
}
?>