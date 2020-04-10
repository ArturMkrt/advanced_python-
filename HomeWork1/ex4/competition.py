def dig(num):
    return sum(int(digit) for digit in str(num))
print(dig(123))