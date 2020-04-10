def second_max(l):
    m = l[0]#max
    m2 = None#second_max
    for i in l[1:]:
        if i > m:
            m2 = m
            m = i
        elif (m2 is None or i > m2) and i < m:
            m2 = i
    if m2 is not None:
        return m2
    return 0.5


print(second_max([1, 5, 6, 4, 2]))
print(second_max([1, 5, 5]))
print(second_max([5, 5, 5]))