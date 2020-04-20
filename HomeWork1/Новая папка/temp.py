"""def int_to_ipv4(num):
    chunks = ['{:032b}'.format(num)[i:i+8] for i in range(0,32,8)]
    return  ''.join()
print(int_to_ipv4(167772210))"""
map(lambda i:int(i,2),['100','100'])