myArrays = []
while True:
    user_char = input("enter your some word")
    if user_char in myArrays:
        print(f"{user_char} is already exist")
        print("enter other words")
    else:
        myArrays.append(user_char)
    print(myArrays)

        