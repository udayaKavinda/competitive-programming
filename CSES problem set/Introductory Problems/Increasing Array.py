num=input()
arr=list(map(int,input().split()))
mem=arr[0]
count=0
for i in range(1,int(num)):
    if(arr[i]<mem):
        # print(mem-arr[i])
        count=count+mem-arr[i]
        mem=mem
    else:
        mem=arr[i]
print(count)
