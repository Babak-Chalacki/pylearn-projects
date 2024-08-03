
let side1 = Number(prompt("enter your side1"))
let side2 = Number(prompt("enter your side2"))
let side3 = Number(prompt("enter your side3"))

result = side1 + side2 > side3 || side1 + side3 > side2 || side3 + side2 > side1;

if(result === 180){
    console.log("it is a triangle")
}else{
    console.log("it is not triangle");
}
