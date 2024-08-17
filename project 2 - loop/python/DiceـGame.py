import random

while True:
    cumpoter = random.randint(1,6)
    print(f"cumpoter number = {cumpoter}")

    if cumpoter == 6:
        print("you win")
    else:
        print("you loose")
        break