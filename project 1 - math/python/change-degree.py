import math
choose = input("degree = d and radians = r")

if choose == "d":
    prompt = float(input("enter your degree"))
    result =   prompt * (math.pi / 180)
    print(f"your radians = {result}")
elif choose == "r":
    prompt = float(input("enter your radians"))
    result = prompt * (180 / math.pi)
    print(f"your degree = {result}")  
else:
    print("invalid input")

