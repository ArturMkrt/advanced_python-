str = input('Enter a text ')
for char in ' ?.!/;:,':
    str = str.replace(char,' ')
text = str.lower().split()
dic1_1 = {}
for item in text:
    if item in dic1_1:
        dic1_1[item] += 1
    else:
        dic1_1[item] = 1
print(dic1_1)