def num(x,y):
    if max(x,y) // min(x,y) == 0 or x==y:
        return y
    if x>y:
        return num(x-y,y)
    else:
        return num(y-x,x)
print(num(16,24))