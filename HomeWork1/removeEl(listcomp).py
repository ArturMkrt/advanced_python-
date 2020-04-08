list_1 = [[1,2],[1,2,3],[1,2]]
remove = [int(x) for x in input('remove').split()]
if len(remove) == 1:
    answer = [x for x in list_1 if remove[0] != x]
else:
    answer = [x for x in list_1 if remove != x]
print(answer)