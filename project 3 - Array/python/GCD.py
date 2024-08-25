num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = 1  
if num1 < num2:
    smaller = num1
else:
    smaller = num2

for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i  
print(f"The greatest common divisor of {num1} and {num2} is: {gcd}")