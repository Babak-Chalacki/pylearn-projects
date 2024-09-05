user_input = input("Enter a list of elements separated by commas: ")
my_list = user_input.split(",")
reversed_list = my_list[::-1]

print("Original List:", my_list)
print("Reversed List:", reversed_list)