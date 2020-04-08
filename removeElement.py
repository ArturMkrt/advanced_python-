list_1 = [1,2,3,4]
remove = [int(x) for x in input("remove element ").split()]
if len(remove) == 1:
    while remove[0] in list_1:
        list_1.remove(remove[0])
else:
    while remove in list_1:
        list_1.remove(remove)
print(list_1)