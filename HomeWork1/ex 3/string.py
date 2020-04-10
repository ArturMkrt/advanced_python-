def sym(str):
    for s in range(len(str)//2):
        if str[s] != str[len(str)-1]:
            return False
    return True
print(sym("abc"))
