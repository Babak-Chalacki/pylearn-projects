num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 < num2:
    smaller = num1
else:
    smaller = num2

gcd = 1 
for i in range(1, smaller + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i 
lcm = (num1 * num2) // gcd

print(f"The Least Common Multiple (LCM) of {num1} and {num2} is: {lcm}")