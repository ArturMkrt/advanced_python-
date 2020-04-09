def rem(array, element):
    a = array[:]
    while True:
        try:
            a.remove(element)
        except:
            break
    return a
print(rem([],0))