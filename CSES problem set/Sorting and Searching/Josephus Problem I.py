num=int(input())
arr=[x for x in range(1,num+1)]
 
while(len(arr)!=1):
    if len(arr)%2==0:
        print(*([arr[x] for x in range(len(arr)) if x%2==1]),end=" ")
        arr=[arr[x] for x in range(len(arr)) if x%2==0]
    else:
        print(*([arr[x] for x in range(len(arr)) if x%2==1]),end=" ")
        arr=[arr[x] for x in range(len(arr)) if x%2==0]
        a=arr.pop()
        arr.insert(0,a)
    # print(arr)
    
print(*arr)