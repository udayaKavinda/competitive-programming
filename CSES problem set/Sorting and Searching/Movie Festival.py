num=int(input())
arr=[]
for i in range(num):
    arr.append(tuple(map(int,input().split())))
arr=sorted(arr,key=lambda x :x[1])
last_end=arr[0][1]
count=1
for i in range(1,num):
    if last_end<=arr[i][0]:
        count+=1
        last_end=arr[i][1]
print(count)
