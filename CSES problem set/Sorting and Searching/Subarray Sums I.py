num,target=map(int,input().split())
arr=list(map(int,input().split()))
 
count=0
big=[0 for x in range(num+1)]
big[1]=arr[0]
for i in range(1,num):
    big[i+1]=big[i]+arr[i]
 
i=0
j=1
while(i<len(arr) and j<len(arr)+1):
    if big[j]-big[i]<target:
        j+=1
    elif big[j]-big[i]==target:
        i+=1
        count+=1
    else:
        i+=1
print(count)