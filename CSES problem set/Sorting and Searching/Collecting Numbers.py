length=int(input())
arr=list(map(int,input().split()))
locations=[0]*length
for i in range(length):
    locations[arr[i]-1]=i
# print(locations)
count=1
for i in range(length-1):
    if locations[i]<locations[i+1]:
        pass
    else:
        # print(i)
        count+=1
print(count