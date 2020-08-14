#Problem name: Apple division
# Description:There are n apples with known weights.
# Your task is to divide the apples into two groups so that the difference between the weights of the groups is minimal.
# Strategy: Recursion



n=int(input())
li=list(map(int,input().split()))
li.sort()
s=sum(li)
def minimum(s,li):
    if(len(li)==1):
        return abs(s-2*li[0])
    else:
        m=abs(s-2*li[0])
        for i in range(1,len(li)):
            m=min(m,abs(minimum(s-2*li[i],li[:i])))
        return m
print(minimum(s,li))