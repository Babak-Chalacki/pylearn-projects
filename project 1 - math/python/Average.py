name = input("enter your name:")
family = input("enter your family:")
num1 = float(input("enter your grade1"))
num2 = float(input("enter your grade2"))
num3 = float(input("enter your grade3"))
result = (num1 + num2 + num3) / 3
if result >=16:
    print(f"{name} {family} your graye = A")
elif result >=10 and result<=15:
    print(f"{name} {family} your graye = B")
else:
    print(f"{name} {family} your graye = C")