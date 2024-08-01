 
let weight = parseFloat(prompt("Enter your weight (kg):"));  
let height = parseFloat(prompt("Enter your height (m):"));  

 
let bmi = weight / (height ** 2);  

 
if (bmi < 18.5) {  
    console.log("Underweight");  
} else if (bmi >= 18.5 && bmi < 25) {  
    console.log("Normal weight");  
} else if (bmi >= 25 && bmi < 30) {  
    console.log("Overweight");  
} else if (bmi >= 30 && bmi < 35) {  
    console.log("Obese");  
} else if (bmi >= 35 && bmi < 40) {  
    console.log("Extra obese");  
} else {  
    console.log("Severely obese");  
}
