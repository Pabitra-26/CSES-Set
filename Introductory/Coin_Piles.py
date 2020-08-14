# Problem name: Coin Piles
# Description: You have two coin piles containing a and b coins.
# On each move, you can either remove one coin from the left pile and two coins from the right pile, or two coins from the left pile and one coin from the right pile.
# Your task is to efficiently find out if you can empty both the piles.
# Strategy: if a nd b are two given numbers then let x=2 from a and 1 from b and y=2 from b and 1 from a(the ways).
# Form equations for a and b--> a=(2*x)+(1*y) and b=(2*y)+(1*x) , now while solving both the equations we get--> 2a-b=3x and 2b-a=3y, which means, 2a-b and 2b-a should be a multiple of 3

# Optimized code:
n=int(input())
for i in range(n):
    li=list(map(int,input().split()))
    a=li[0]
    b=li[1]
    if(((2*a)-b)%3==0 and ((2*a)-b)>=0 and ((2*b)-a)%3==0 and ((2*b)-a)>=0):
        print("YES")
    else:
        print("NO")

#Brute-Force approach:
"""n=int(input())
for i in range(n):
    li=list(map(int,input().split()))
    if(li[0]+li[1])%3!=0:
        print("NO")
    else:
        flag=0
        n=li[0]+li[1]
        while(n>0):
            if(li[0]==0 or li[1]==0):
                print("NO")
                flag=1
                break
            if(n%3==0):
                if(li[0]>li[1]):

                    li[0]-=2
                    li[1]-=1
                    n=li[0]+li[1]
                else:
                    li[0]-=1
                    li[1]-=2
                    n=li[0]+li[1]
            else:
                flag=1
                print("NO")
                break
        if(flag==0):
            print("YES")
"""

