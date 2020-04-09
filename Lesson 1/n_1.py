def int_l(lst):
    a = True
    for item in lst:
        if len(str(item)) == len(set(str(item))):
            a = False
            return item
    if a:
        return -1
print(int_l([101, 110, 11, 111]))