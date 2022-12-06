num=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
for i in range(1,num):
    if(arr[i-1]!=i):
        print(i)
        break
else:
    print(num)
 
 
 
