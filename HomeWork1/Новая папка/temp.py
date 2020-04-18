def bit_concat(lst):
    lst = ['{:08b}'.format(x) for x in lst]
    m = 6
    y = 8
    s = ''
    for n in range(len(lst)):
        print(n)
        s = lst[n][m:y] + s
        m-=2
        y-=2
    return int(s,2)
print(bit_concat([3,12]))
