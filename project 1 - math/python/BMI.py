weight = float(input("enter your weight (kg): "))  
height = float(input("enter your height (m): "))  
result = weight / height ** 2  

if result < 18.5:  
    print("underweight")  
elif 18.5 <= result < 25:  
    print("normal weight")  
elif 25 <= result < 30:  
    print("overweight")  
elif 30 <= result < 35:  
    print("obese")  
elif 35 <= result < 40:  
    print("extra obese")  
else:  
    print("severely obese")