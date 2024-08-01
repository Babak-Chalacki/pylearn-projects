<?php

if (
    isset($_GET["name"]) && isset($_GET["family"]) &&
    isset($_GET["num1"]) && is_numeric($_GET["num1"]) &&
    isset($_GET["num2"]) && is_numeric($_GET["num2"]) &&
    isset($_GET["num3"]) && is_numeric($_GET["num3"])
) {

    $name = $_GET["name"];
    $family = $_GET["family"];
    $num1 = $_GET["num1"];
    $num2 = $_GET["num2"];
    $num3 = $_GET["num3"];

    $result = ($num1 + $num2 + $num3) / 3;

    if ($result >= 17) {
        echo "$name" . "$family" . "A";
    } elseif ($result >= 12 && $result < 17) {
        echo "$name" . "$family" . "B";
    } else {
        echo "$name" . "$family" . "C";
    }
} else {
    echo "Invalid input";
}