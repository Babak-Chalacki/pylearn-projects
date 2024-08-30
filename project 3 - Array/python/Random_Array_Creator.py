import random

myArrays = []
num_random_numbers = 10

while len(myArrays) < num_random_numbers:
    random_number = random.randint(1, 100)
    
    if random_number in myArrays:
        print(f"{random_number} already exists in the array.")
    else:
        myArrays.append(random_number)
        print(f"Added {random_number} to the array.")

print("Final array of random numbers:", myArrays)
