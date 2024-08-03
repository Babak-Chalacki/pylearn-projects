
side1 = float(input("enter your side1"))
side2 = float(input("enter your side2"))
side3 = float(input("enter your side3"))

result =  side1 + side2 > side3 or side3 + side2 > side1 or side1 + side3 > side2
if result :
    print("it is a triangle")
else:
    print("it is not a triangle")
