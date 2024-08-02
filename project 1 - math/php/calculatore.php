<?php

if (isset($_GET["num1"]) && isset($_GET["op"]) && isset($_GET["num2"])) {
    $num1 = $_GET["num1"];
    $op = $_GET["op"];
    $num2 = $_GET["num2"];

    if (is_numeric($num1) && is_numeric($num2)) {
        switch ($op) {
            case "+":
                $result = $num1 + $num2;
                break;
            case "-":
                $result = $num1 - $num2;
                break;
            case "*":
                $result = $num1 * $num2;
                break;
            case "/":
                if ($num2 != 0) {
                    $result = $num1 / $num2;
                } else {
                    $result = "error";
                }
                break;
            default:
                $result = "error";
        }
        echo $result;
    } else {
        echo " Invalid input";
    }
} else {
    echo "Missing input";
}
