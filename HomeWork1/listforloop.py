list_1 = [1,2,3,1]
new_list = []
for x in list_1:
    if x not in new_list:
        new_list.append(x)
print(new_list)
