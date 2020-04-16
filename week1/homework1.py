def all_positive(*integer):
    return min(integer)<0


def xor3(a,b,c):
    return (not a and not b and c) or (not a and b and not c) or (a and not b and not c) or (a and b and c)