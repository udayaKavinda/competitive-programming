n,m,k=map(int,input().split())
applicants=sorted(list(map(int,input().split())))
house=sorted(list(map(int,input().split())))
# print(applicants)
# print(house)
temp=0
count=0
for i in range(n):
    for j in range(temp,m):
        if(applicants[i]-house[j]>k):
            temp=j+1
        elif(applicants[i]-house[j]<-k):
            break
        else:
            temp=j+1
            count+=1
            break
print(count)