<?php
if (isset($_GET['number'])) {
    $number = (int) $_GET['number'];

    if ($number < 1) {
        echo "output: no";
    } else {
        $factorial = 1;
        $i = 1;

        while ($factorial < $number) {
            $i++;
            $factorial *= $i;
        }

        if ($factorial == $number) {
            echo "output: yes";
        } else {
            echo "output: no";
        }
    }
} else {
    echo "Please provide a number as a query parameter.";
}
?>