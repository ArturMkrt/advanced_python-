def is_shifted(list1, list2):
  if len(list1) == len(list2):
    str1 = "".join([str(i) for i in list1])
    str2 = "".join([str(i) for i in list2])
    return str1 in str2*2
  return False


print(is_shifted([1, 2, 3], [2, 3, 1]))
print(is_shifted([1, 3, 4, 5, 2], [5, 2, 1, 3, 4]))
print(is_shifted([1, 2, 3], [3, 2, 1]))



