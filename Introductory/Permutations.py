# Problem name: Permutations
# Description: A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.
# Given n, construct a beautiful permutation if such a permutation exists.
# Strategy: use if-else concept



num=int(input())
if(num==1):
    print(1)
elif(num==3 or num==2):
    print("NO SOLUTION")

else:
    li=list(range(1,num+1))
    if(num%2==0):
        for i in range(1, num, 2):
            print(li[i], end=" ")
        for i in range(0, num, 2):
            print(li[i], end=" ")
    else:
        for i in range(0, num, 2):
            print(li[i], end=" ")
        for i in range(1, num, 2):
            print(li[i], end=" ")


