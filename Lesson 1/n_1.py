def int_l(lst):
    for item in lst:
        if len(str(item)) == len(set(str(item))):
            a = False
            return item
    return -1
print(int_l([101, 110, 11, 111]))