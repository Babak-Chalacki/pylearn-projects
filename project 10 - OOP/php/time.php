<?php

class Time{

private $second;
private $minute;
private $houre; 

public function __construct($second,$minute,$houre){
    
    $this->second = $second;
    $this->minute = $minute;
    $this->houre = $houre;
}

public function alarm(){}
public function displayTime(){}

}

?>