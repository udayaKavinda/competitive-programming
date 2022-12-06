def rec(arr,step,left,right):
    if(step==len(arr)):
        return abs(left-right)
    
    a=rec(arr,step+1,left+arr[step],right)
    b=rec(arr,step+1,left,right+arr[step])
    return min(a,b)
 
 
 
num=int(input())
arr=list(map(int,input().split()))
print(rec(arr,0,0,0))