  
        "use strict";  
        let choice = prompt("Enter 'd' for degree to radians or 'r' for radians to degree").toLowerCase();  
        
        if (choice === "d") {  
            let degreeInput = Number(prompt('Enter your degree'));  
            let radian = degreeInput * (Math.PI / 180);  
            alert("The result in radians is: " + radian);  
        }   
        else if (choice === "r") {  
            let radianInput = Number(prompt('Enter your radians'));   
            let degree = radianInput * (180 / Math.PI);  
            alert("The result in degrees is: " + degree);  
        }   
        else {  
            alert("Invalid input");  
        }  
   