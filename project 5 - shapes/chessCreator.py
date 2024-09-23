def print_chessboard(n, m):
    for i in range(n):
        row = ""
        for j in range(m):
            if (i + j) % 2 == 0:
                row += "*"
            else:
                row += "#"
        print(row)

n = int(input("row => "))
m = int(input("col => "))  
print_chessboard(n, m)