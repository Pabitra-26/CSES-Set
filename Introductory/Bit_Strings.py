num=int(input())
num=2**num
if(num<(((10)**9)+7)):
    print(num)
else:
    print(num%(((10)**9)+7))