# Problem name: Missing number
# Description: You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.
# Strategy: find the sum of numbers from 1 to n and the keep subtracting the array values one by one from it, when one value remains, i.e the missing number


num=int(input())
li=list(map(int,input().split()))
lis=list(range(1,num+1))
lis=sum(lis)
for i in li:
    lis-=i
print(lis)
