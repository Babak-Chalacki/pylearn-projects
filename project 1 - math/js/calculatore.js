
        let a = Number(prompt("Enter your number"));
        let op = prompt("Enter your symbol: - + / * sin tan sqrt cot cos factorial:");
    
        if (op === "-" || op === "+" || op === "/" || op === "*") {
            let b = Number(prompt("Enter your second number"));
            if (op === "-") {
                alert(a - b);
            } else if (op === "+") {
                alert(a + b);
            } else if (op === "/") {
                if (b !== 0) {
                    alert(a / b);
                } else {
                    alert("Error: Division by zero is not allowed.");
                }
            } else if (op === "*") {
                alert(a * b);
            }
        } else {
            if (op === "sin") {
                alert(Math.sin(a));
            } else if (op === "cos") {
                alert(Math.cos(a));
            } else if (op === "tan") {
                alert(Math.tan(a));
            } else if (op === "cot") {
                if (Math.tan(a) !== 0) {
                    alert(1 / Math.tan(a));
                } else {
                    alert("Error: Cotangent is not defined for this angle.");
                }
            } else if (op === "sqrt") {
                if (a >= 0) {
                    alert(Math.sqrt(a));
                } else {
                    alert("Error: Square root of negative number is not a real number.");
                }
            } else if (op === "factorial") {
                let fact = 1;
                for (let i = 1; i <= a; i++) {
                    fact *= i;
                }
                alert(fact);
            }
        }
