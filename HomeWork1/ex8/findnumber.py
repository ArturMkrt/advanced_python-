sequence = [int(x) for x in input("Enter a sequence ").split()]
length = len(sequence)+1
print(sequence," ->",(length*(length+1))//2-sum(sequence))

