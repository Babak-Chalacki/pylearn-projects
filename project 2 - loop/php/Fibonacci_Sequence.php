<?php
$n = isset($_GET['n']) ? intval($_GET['n']) : 0;

$a = 0;
$b = 1;

echo "The Fibonacci sequence is:\n";

for ($i = 0; $i < $n; $i++) {
    echo $a . " ";
    $temp = $b;
    $b = $a + $b;
    $a = $temp;
}
echo "\n";
?>