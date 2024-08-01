<?php
if (
    isset($_GET["weight"])
    &&
    isset($_GET["height"])
) {
    $height = $_GET["height"];
    $weight = $_GET["weight"];

    $bmi = $weight / ($height ** 2);

    if ($bmi < 18.5) {
        echo "Underweight";
    } elseif ($bmi >= 18.5 && $bmi < 25) {
        echo "Normal weight";
    } elseif ($bmi >= 25 && $bmi < 30) {
        echo "Overweight";
    } elseif ($bmi >= 30 && $bmi < 35) {
        echo "Obese";
    } elseif ($bmi >= 35 && $bmi < 40) {
        echo "Extra obese";
    } else {
        echo "Severely obese";
    }
} else {
    echo "Please enter your weight and height";
}