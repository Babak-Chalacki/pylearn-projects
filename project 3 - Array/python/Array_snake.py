while True:
    try:
        user_num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")


    for i in range(user_num):
        print("*#" , end="")
