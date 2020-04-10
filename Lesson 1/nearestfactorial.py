def get_neares_factorial(n):
  f = 1
  i = 2
  while f <= n:
    f *= i
    i += 1
  return f

print(get_neares_factorial(10))
print(get_neares_factorial(100))