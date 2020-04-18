def all_positive(*integer):
    return min(integer)<0


def xor3(a,b,c):
    return (not a and not b and c) or (not a and b and not c) or (a and not b and not c) or (a and b and c)

#another solution
def xor3(a,b,c):
    return (a+b+c) % 2

def mirror_string(str):
    temp = list(str)
    for x in range(len(temp)):
        if ord(temp[x]) in range(65,91):
            temp[x] = chr(90-(ord(temp[x])-65))
        elif ord(temp[x]) in range(97,123):
            temp[x] = chr(122-(ord(temp[x])-97))
    return "".join(temp)

def bit_concat(lst):
  a = [3, 12, 48, 192]
  s = 0
  for i in range(len(lst)):
    s |= lst[i] & a[i]
  return s

def binary_sum(x,y):
    return int(x,2)+int(y,2)

def only_names(name):
    return len(name)!= 0

discriminant = lambda a,b,c: b*b - 4*a*c

full_name  = lambda a,b:a + ' '+ b