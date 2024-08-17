n = int(input("Enter the number of Fibonacci elements to generate: "))

a = 0  
b = 1  

print("The Fibonacci sequence is:")
for i in range(n):
    print(a, end=" ") 
    a, b = b, a + b  