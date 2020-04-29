def bisect_position(lst, num):
    m = 0
    n = len(lst) - 1
    while m <= n:
        k = (n + m) // 2
        if lst[k] < num:
            m = k + 1
        elif lst[k] > num:
            n = k - 1
        else:
            return k
    return m

def all_sums(num):
    return [(i,num-i) for i in range(1,num//2+1)]

from collections import defaultdict 
def duplicate_characters(str):
    s=set ()
    d = defaultdict(int)
    for j in str:
        if j == ' ':
            continue
        if not d [j]:
            d[j]+=1
        else:
            s.add(j)
    return s

def compare_lists(lst1,lst2):
    d_1 = {}
    d_2 = {}
    if len(lst1) != len(lst2):
        return False
    for x in lst1:
        if x in d_1:
            d_1[x]+=1
        else:
            d_1[x]=1
    for y in lst2:
        if y in d_2:
            d_2[y]+=1
        else:
            d_2[y]=1
    for z in d_1:
        if z not in d_2 or d_1[z] != d_2[z]:
            return False
    return True

def heapq(lst,num):
    lst.append(num)
    pos = len(lst)-1
    while pos > 0:
        pr_pos = (pos -1) // 2 
        p_r = lst[pr_pos] 
        if num < p_r:
            lst[pos] = p_r
            pos = pr_pos
            continue
        break
    lst[pos] = num
    return lst

def sort_list(arr,order='ascending'):
    if order=='descending':
        op = lambda x,y:x > y
    else:
        op = lambda x,y:x < y
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        sort_list(L,order)
        sort_list(R,order)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if op(L[i],R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr