<?php

if (isset($_GET["side1"]) && isset($_GET["side2"]) && isset($_GET["side3"])) {
    $side1 = $_GET["side1"];
    $side2 = $_GET["side2"];
    $side3 = $_GET["side3"];
    $result = $side1 + $side2 > $side3 || $side1 + $side3 > $side2 || $side3 + $side2 > $side1;
    if ($result) {
        echo "it is triangle";
    } else {
        echo "its not a triangle";
    }
} else {
    echo "laugh";
}
