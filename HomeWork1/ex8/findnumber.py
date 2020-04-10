def find(lst):
    x = len(lst)+1
    return (x*(x+1))//2 - sum(lst)
print(find([1,2,3,4,5]))