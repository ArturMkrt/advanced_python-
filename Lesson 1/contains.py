def contains(list1, list2):
    diff = len(list1) - len(list2)
    if diff >= 0:
        for i in range(diff):
            if list1[i:i + len(list2)] == list2:
                return True
    return False


def is_shifted(list1, list2):
    return len(list1) == len(list2) and contains(list2 * 2, list1)


print(is_shifted([1, 2, 3], [2, 3, 1]))
print(is_shifted([1, 3, 4, 5, 2], [5, 2, 1, 3, 4]))
print(is_shifted([1, 2, 3], [3, 2, 1]))



