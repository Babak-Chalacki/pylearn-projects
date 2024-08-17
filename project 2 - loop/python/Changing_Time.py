choose = input("time to seconde = 1 , seconde to time = 2")
if choose == "1":
    houre = int(input("houre"))
    minute = int(input("minute"))
    secound = int(input("secound"))

    houre *= 3600
    minute *= 60
    
    print(f"your time is : {houre + minute + secound}")
elif choose == "2":

    user_time = int(input("enter your time"))

    hours = user_time // 3600
    minute = (user_time % 3600) / 60
    secound = user_time %60
    print(f"Your time is: {hours} hours, {minute} minutes, and {secound} seconds.")
else:
    print("Invalid choice. Please enter 1 or 2.")