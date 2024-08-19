<?php
if ($_SERVER["REQUEST_METHOD"] == "GET") {
   
    $choose = isset($_GET['choose']) ? $_GET['choose'] : '';

    if ($choose == "1") {
       
        $hour = isset($_GET['hour']) ? intval($_GET['hour']) : 0;
        $minute = isset($_GET['minute']) ? intval($_GET['minute']) : 0;
        $second = isset($_GET['second']) ? intval($_GET['second']) : 0;

        $total_seconds = ($hour * 3600) + ($minute * 60) + $second;
        echo "Your time in seconds: " . $total_seconds;
    } elseif ($choose == "2") {
       
        $user_time = isset($_GET['user_time']) ? intval($_GET['user_time']) : 0;

        $hours = floor($user_time / 3600);
        $minutes = floor(($user_time % 3600) / 60);
        $seconds = $user_time % 60;

        echo "Your time is: " . $hours . " hours, " . $minutes . " minutes, and " . $seconds . " seconds.";
    } else {
        echo "Invalid choice. Please enter 1 or 2.";
    }
} else {
    echo "Please use the GET method to provide input.";
}
?>