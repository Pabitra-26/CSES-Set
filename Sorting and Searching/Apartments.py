# Problem name: Apartments
# Description: There are n applicants and m free apartments
# Your task is to distribute the apartments so that as many applicants as possible will get an apartment.
# Each applicant has a desired apartment size, and they will accept any apartment whose size is close enough to the desired size.
# Strategy: use a single loop to reduce time complexity, and sort the two lists first



li=list(map(int,input().split()))
people=li[0]
apartments=li[1]
k=li[2]
lis_people=list(map(int,input().split()))
lis_apt=list(map(int,input().split()))
lis_people.sort()
lis_apt.sort()
count=0
i,j=0,0
while(i<people and j<apartments):
    if(lis_people[i]+k<lis_apt[j]):
        i+=1
    elif(lis_people[i]-k>lis_apt[j]):
        j+=1
    else:
        i+=1
        j+=1
        count+=1
print(count)
