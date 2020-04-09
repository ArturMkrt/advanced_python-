def rem(array,element):
    return [i for i in array if i!=element]
print(rem([[1,2,3],3,4,5,[1,2,3]],[1,2,3]))