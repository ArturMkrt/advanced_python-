def implication3(a,b,c):
    return not a or not b or c

def last_digit(n):
    return int((((n*(n+1)*(2*n+1))/6) % 10))

def quick_or (lst):
    return max(sorted(lst,reverse=True)) > 0

def is_polyndrome(st):
    odd=0
    myset=set(st)
    for i in myset: 
        n=st.count(i)
        if n%2!=0:
            odd+=1
    return odd<=1

def recursive_or(lst):
    return lst[0] or (len(lst)> 1 and recursive_or(lst[1:]))
