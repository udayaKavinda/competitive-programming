length=int(input())
arr=list(map(int,input().split()))
if length!=1:
    j=1
    count=0
    sett=set(arr[0:1])
    # print(sett)
    for i in range(length):
        if(i>0):
            sett.discard(arr[i-1])
 
        while(j<length):    
            if arr[j] not in sett:
                sett.add(arr[j])
                count=max(count,len(sett))
                j+=1
            else:
                break
        # print(i,j,sett)
    print(count)
else:
    print(1)