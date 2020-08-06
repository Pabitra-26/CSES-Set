# Problem name: Two Knights
# Description: Your task is to count for k=1,2,…,n the number of ways two knights can be placed on a k×k chessboard so that they do not attack each other.
# Strategy: take a small part of the chess board and analyse, all the possibilities, total number of ways will be (n^2)(n^2-1), from that subtract the possibilities

num=int(input())
for n in range(1,num+1):
    print(((n*n)*(n*n-1))//2-(4*(n-1)*(n-2)))
