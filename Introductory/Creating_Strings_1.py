#Problem name: Creating Strings 1
# Description: Given a string, your task is to generate all different strings that can be created using its characters.
# Strategy: use permutations method from itertools module



from itertools import permutations
string=input()
ls=sorted(list(set(permutations(string))))
li=[]
print(len(ls))
for i in ls:
    print("".join(i))
