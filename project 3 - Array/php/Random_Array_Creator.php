<?php
$myArrays = [];

if (isset($_GET['user_char'])) {
    $user_char = $_GET['user_char'];
    
    if (in_array($user_char, $myArrays)) {
        echo "$user_char is already exist.<br>";
        echo "Enter other words.<br>";
    } else {
        $myArrays[] = $user_char;
        echo "$user_char has been added.<br>";
    }
}

if (!empty($myArrays)) {
    echo "Current words: " . implode(", ", $myArrays) . "<br>";
}
?>

<form method="get">
    <input type="text" name="user_char" required>
    <input type="submit" value="Submit">
</form>