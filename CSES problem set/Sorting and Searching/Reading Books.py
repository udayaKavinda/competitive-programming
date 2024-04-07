length=int(input())
arr=sorted(list(map(int,input().split())),reverse=True)
j=length-1
fsum=arr[0]
bsum=sum(arr[1:])
if fsum>=bsum:
    print(fsum*2)
else:
    print(fsum+bsum)
