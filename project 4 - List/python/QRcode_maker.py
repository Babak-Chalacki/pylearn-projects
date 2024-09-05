import qrcode
name = input("enter your name")
number = int(input("enter your number"))
concat = f"{name} | {number}"
img = qrcode.make(concat)
img.save("user_QRcode.png")