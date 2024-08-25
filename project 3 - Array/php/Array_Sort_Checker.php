<?php
if (isset($_GET['array'])) {
    $array = explode(',', $_GET['array']);
    $array = array_map('intval', $array);
    
    $isSorted = true;
    for ($i = 0; $i < count($array) - 1; $i++) {
        if ($array[$i] > $array[$i + 1]) {
            $isSorted = false;
            break;
        }
    }

    if ($isSorted) {
        echo "آرایه مرتب است.";
    } else {
        echo "آرایه مرتب نیست.";
    }
}
?>