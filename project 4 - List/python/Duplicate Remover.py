user_input = input("Enter a list of elements separated by commas: ")
original_list = user_input.split(",")

unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print("Original List:", original_list)
print("List with Duplicates Removed:", unique_list)