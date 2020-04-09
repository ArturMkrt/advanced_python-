number= int(input())
sum_1 = 0
while number!=0:
    if number % 2 == 1:
        sum_1+=1
    number//=2
print(sum_1)