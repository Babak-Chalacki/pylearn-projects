<?php

if (isset($_GET["side1"]) && isset($_GET["side2"]) && isset($_GET["side3"])) {
    $side1 = $_GET["side1"];
    $side2 = $_GET["side2"];
    $side3 = $_GET["side3"];
    $result = $side1 + $side2 + $side3;
    if ($result == 180) {
        echo "it is triangle";
    } else {
        echo "its not a triangle";
    }
} else {
    echo "laugh";
}