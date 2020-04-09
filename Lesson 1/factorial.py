def factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
print(factorial(5))

def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n
print(factorial(5))