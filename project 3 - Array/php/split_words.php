<?php
if (isset($_GET['sentence'])) {
    $sentence = $_GET['sentence'];
    $words = explode(" ", $sentence);
    $word_count = count($words);
    echo "The sentence has $word_count words.";
}
?>

<form method="get">
    <input type="text" name="sentence" required>
    <input type="submit" value="Count Words">
</form>