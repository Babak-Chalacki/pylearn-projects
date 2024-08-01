import math

a = float(input("inter your number"))
op = input("inter your symbol: - + / * sin tan sqrt cot cos factorial")
b = None

if op in ["-","+","/","*"]:
    b = float(input("inter your number"))

if op == "+":
   result = a+b

elif op == "-":
   result = a-b

elif op == "/":
   result = a/b

elif op == "*" :
  result = a*b
else:
 if op == "sin":
    result = math.sin(a)
 elif op == "tan":
    result = math.tan(a)
 elif op == "cos":
    result = math.cos(a)
 elif op == "sqrt":
    result = math.sqrt(a)
 elif op == "cot":
    result  = math.cot(a)
 elif op == "factorial":
    result = math.factorial(a)

print(result)


