num=int(input())
arr=list(map(int,input().split()))
a=0
sum=-float("inf")
for i in range(num):
    a+=arr[i]
    sum=max(sum,a)
    if(a<0):
        a=0
print(sum)