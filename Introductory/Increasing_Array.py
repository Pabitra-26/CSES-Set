# Problem name: Increasing Array
# Description: You are given an array of n integers.
# You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
# On each turn, you may increase the value of any element by one. What is the minimum number of turns required?
# Strategy:

l=int(input())
li=list(map(int,input().split()))
lis=[]
for i in range(1,l):

    if(li[i]>=li[i-1]):
        continue
    else:
        m=li[i-1]-li[i]
        lis.append(m)
        li[i]+=m
print(sum(lis))




