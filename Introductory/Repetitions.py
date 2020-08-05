# Problem name: Repetitions
# Description: You are given a DNA sequence: a string consisting of characters A, C, G, and T.
# Your task is to find the longest repetition in the sequence.
# This is a maximum-length substring containing only one type of character
# Strategy: check adjacent elements, if thery are same, increment count value, else append the previous count to a list and reset count to 1


s=input()
s=list(s)
li=[]
n=0
count=1
while(n<len(s)-1):
    if(s[n]==s[n+1]):
        count+=1
        n+=1
    else:
        li.append(count)
        count=1
        n+=1
li.append(count)

if(li==[]):
    print(count)
else:
    print(max(li))
