def custom_order(str1, str2):
    return "".join(sorted(str1, key=str2.index))


print(custom_order("abc", "befca"))
print(custom_order("abaabbccabbed", "bedac"))