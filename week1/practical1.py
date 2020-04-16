def implication3(a,b,c):
    return not a or not b or c

def last_digit(n):
    return int((((n*(n+1)*(2*n+1))/6) % 10))

def expr_value(expr):
    return round(eval(expr),2)