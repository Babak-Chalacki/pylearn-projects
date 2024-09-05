number = int(input("input: "))

if number < 1:
    print("output: no") 
else:
    factorial = 1
    i = 1

    while factorial < number:
        i += 1
        factorial *= i

    if factorial == number:
        print("output: yes") 
    else:
        print("output: no")  