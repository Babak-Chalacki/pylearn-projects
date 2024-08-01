<?php
if (isset($_GET["d"])) {
    $d = $_GET["d"];
    if ($d) {
        $result = $d * (3.14 / 180);
        echo $result;
    } else {
        $result = "Invalid input";
        echo $result;
    }
} elseif (isset($_GET["r"])) {
    $r = $_GET["r"];
    if ($r) {
        $result = $r * (180 / 3.14);
        echo $result;
    } else {
        $result = "Invalid input";
        echo $result;
    }
}