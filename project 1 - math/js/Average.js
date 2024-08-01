
        let name = prompt("enter your name")
        let family = prompt("enter your family")
        let num1 = Number(prompt("num1"))
        let num2 = Number(prompt("num2"))
        let num3 = Number(prompt("num3"))
        let result = (num1 + num2 + num3) / 3
        if(result >= 17){
            alert(`${name} ${family} your course grade = A`)
        }
        else if(result >= 12 && result < 17){
            alert(`${name} ${family} your course grade = B`)
        }
        else{
            alert(`${name} ${family} your course grade = C`)
        }
  