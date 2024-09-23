def print_multiplication_table(n, m):
    for i in range(1, n + 1):
        row = ""
        for j in range(1, m + 1):
            row += f"{i * j:4}"
        print(row)


n = int(input("row => "))
m = int(input("col => ")) 
print_multiplication_table(n, m)