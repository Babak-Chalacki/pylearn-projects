
<?php

class Date {
    private $year;
    private $month;
    private $day;

    public function __construct($year, $month, $day) {
        $this->year = $year;
        $this->month = $month;
        $this->day = $day;
    }

    public function special_day() {
    }

    public function free_days() {
    }
}

?>