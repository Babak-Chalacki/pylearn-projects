<?php
if (isset($_GET['length'])) {
    $n = intval($_GET['length']);
    $snake = '';

    for ($i = 0; $i < $n; $i++) {
        if ($i % 2 == 0) {
            $snake .= '*';
        } else {
            $snake .= '#';
        }
    }

    echo $snake;
}
?>