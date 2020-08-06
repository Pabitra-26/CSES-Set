# Problem name: Trailing zeros
# #Description:
# Strategy: add the quotients after repeatedly dividing the number by 5. 10=5*2, so it's important to know the number of 5's


n=int(input())
s=0
while(n):
    n//=5
    s+=n
print(s)