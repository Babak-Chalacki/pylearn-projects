def f(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d

def f_prime(x, a, b, c):
    return 3 * a * x**2 + 2 * b * x + c

def newton_raphson(a, b, c, d, initial_guess=0.0, tolerance=1e-7, max_iterations=1000):
    x = initial_guess
    for _ in range(max_iterations):
        fx = f(x, a, b, c, d)
        fpx = f_prime(x, a, b, c)
        if abs(fx) < tolerance:
            return x
        if fpx == 0:
            break
        x -= fx / fpx
    return None

a = int(input("enter number a"))
b = int(input("enter number b"))
c = int(input("enter number c"))
d = int(input("enter number d"))


root1 = newton_raphson(a, b, c, d)
print("one", root1)

root2 = newton_raphson(a, b, c, d, initial_guess=-5)
print("two", root2)

root3 = newton_raphson(a, b, c, d, initial_guess=5)
print("three", root3)
