number= int(input())
sum = 0
while number!=0:
    if number % 2 == 1:
        sum+=1
    number//=2
print(sum)