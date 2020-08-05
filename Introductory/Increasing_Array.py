# Problem name: Increasing Array
# Description: You are given an array of n integers.
# You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
# On each turn, you may increase the value of any element by one. What is the minimum number of turns required?
# Strategy:check from index 1 , whether it is greater than or equal to its previous element, if not, then find the difference and append it to ta list, find the sum of that list

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




