n = int(input())
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(factorial)

def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n
print(factorial(5))