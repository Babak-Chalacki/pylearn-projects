<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pascal's Triangle</title>
    <style>
        body {
            background-color: gray;
            color: white;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        .triangle {
            margin: 20px auto;
            display: inline-block;
        }
    </style>
</head>
<body>
    <form method="get">
        <label for="rows">Enter the number of rows:</label>
        <input type="number" id="rows" name="rows" min="1" required>
        <input type="submit" value="Generate">
    </form>

    <?php
    if (isset($_GET['rows'])) {
        $n = (int)$_GET['rows'];
        print_pascal_triangle($n);
    }

    function print_pascal_triangle($n) {
        $pascal_triangle = [[1]];

        for ($i = 1; $i < $n; $i++) {
            $row = [1];
            for ($j = 1; $j < $i; $j++) {
                $row[] = $pascal_triangle[$i - 1][$j - 1] + $pascal_triangle[$i - 1][$j];
            }
            $row[] = 1;
            $pascal_triangle[] = $row;
        }

        foreach ($pascal_triangle as $row) {
            echo str_repeat("&nbsp;", ($n - count($row)) * 2);
            foreach ($row as $num) {
                echo sprintf("%3d", $num) . "&nbsp;";
            }
            echo "<br>";
        }
    }
    ?>
</body>
</html>