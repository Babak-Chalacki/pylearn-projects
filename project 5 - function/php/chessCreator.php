<?php
    if (isset($_GET['n']) && isset($_GET['m'])) {
        $row = (int)$_GET['n'];
        $col = (int)$_GET['m'];

        function print_chessboard($row, $col) {
            for ($i = 0; $i < $row; $i++) {
                $line = '';
                for ($j = 0; $j < $col; $j++) {
                    if (($i + $j) % 2 == 0) {
                        $line .= "*";
                    } else {
                        $line .= "#";
                    }
                }
                echo "<div>$line</div>";
            }
        }

        print_chessboard($row, $col);
    } else {
        echo "Failed: Please provide valid parameters.";
    }