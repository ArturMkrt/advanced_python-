def a(word):
    vowels = "aeiou"
    string = list(word)
    i = 0
    j = len(word)-1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)
print(a("america"))