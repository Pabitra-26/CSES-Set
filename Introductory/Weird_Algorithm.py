# Problem name: Weird Algorithm
# Description: Consider an algorithm that takes as input a positive integer n.
# If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one.
# The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
# 3→10→5→16→8→4→2→1
# Strategy: Use a while loop for constraint, so, that when it becomes it stops and use if-else


num=int(input())
while(num!=1):
    print(num,end=" ")
    if(num%2==0):
        num//=2

    else:
        num*=3
        num+=1
print(1)
