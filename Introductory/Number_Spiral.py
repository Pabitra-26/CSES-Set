# Problem name: Number Spiral
# Description: A number spiral is an infinite grid whose upper-left square has number 1. Here are the first five layers of the spiral:
#arr=[[1,2,9,10,25],[4,3,8,11,24],[5,6,7,12,23],[16,15,14,13,22],[17,18,19,20,21]]
# Your task is to find out the number in row y and column x.
# Strategy: observe the given matrix and write the code



num=int(input())
for i in range(num):
    x,y=input().split()
    x=int(x)
    y=int(y)
    if(y>x):
        if(y%2!=0):
            result= (y*y)-x+1
        else:
            result = ((y-1) * (y-1)) +x
    else:
        if(x%2!=0):
            result=((x-1)*(x-1))+y
        else:
            result = (x * x) -y+1
    print(result)


