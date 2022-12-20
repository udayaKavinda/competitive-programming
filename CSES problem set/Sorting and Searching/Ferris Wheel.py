num,allowed=map(int,input().split())
arr=sorted(list(map(int,input().split())))
# print(arr)
temp=num-1
count=0
i=0
while(i<num):
    # print(i)
    if(i==temp):
        count+=1
        break
    if(i>temp):
        break
    if(arr[i]+arr[temp]<=allowed):
        count+=1
        temp=temp-1
    else:
        count+=1
        temp=temp-1
        i-=1
    i+=1
print(count)
