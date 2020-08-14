# Problem name: Distinct Numbers
# Description: You are given a list of n integers, and your task is to calculate the number of distinct values in the list.
# Strategy; convert the given list to a set and then print its length


n=int(input())
li=list(map(int,input().split()))
li=list(set(li))
print(len(li))