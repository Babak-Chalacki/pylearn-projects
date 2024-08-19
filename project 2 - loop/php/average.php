<?php

$total_course = 0;
$number_course = 0;


if (isset($_GET['course'])) {
  
    $courses = explode(',', $_GET['course']);

    foreach ($courses as $course) {
        $course = trim($course); 

        
        if (strtolower($course) === "exit") {
            break;
        }

        if (is_numeric($course)) {
            $course = floatval($course);
            $number_course += 1;
            $total_course += $course;
        } else {
            echo "Please enter a valid number or type 'exit'.\n";
            continue;
        }
    }
}

if ($number_course > 0) {
    echo "Your average: " . ($total_course / $number_course) . "\n";
} else {
    echo "Invalid input\n";
}
?>