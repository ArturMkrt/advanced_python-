def listcomp(lst):
    return [lst[x] for x in range(len(lst)) if lst[x] not in lst[x+1:]]
print(listcomp([[],[]]))