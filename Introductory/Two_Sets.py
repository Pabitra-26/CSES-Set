# Problem name: Two Sets
# Description:Your task is to divide the numbers 1,2,…,n into two sets of equal sum.
# Strategy: first find the sum of n numbers, if its divisible by 2, only then solution exists, crest two sets and keep on adding numbers from 1,2,...n, while checking their sum.

num=int(input())
n=(num*(num+1))//2
if(n%2!=0):
    print("NO")
else:
    a=set()
    b=set()
    s=0
    s1=0
    for i in range(num,0,-1):
        if(s1>s):
            s+=i
            b.add(i)
        else:
            s1+=i
            a.add(i)
    print("YES")
    print(len(a))
    print(*a)
    print(len(b))
    print(*b)


