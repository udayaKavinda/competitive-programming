num=int(input())
arr=list(range(1,num+1))
if sum(arr)%2!=0:
    print("NO")
else:
    if len(arr)>3:
        arr1=[]
        arr2=[]
        count=0
        for i in reversed(arr):
            if(count==0):
                arr1.append(i)
            if(count==1):
                arr2.append(i)
            if(count==2):
                arr2.append(i)
            if(count==3):
                arr1.append(i)
                count=-1
            count=count+1
        print("YES")
        print(len(arr1))
        print(" ".join(list(map(str,arr1))))
        print(len(arr2))
        print(" ".join(list(map(str,arr2))))
    else:
        print("YES")
        print(1)
        print(3)
        print(2)
        print(2,1)
 
 
 
 
