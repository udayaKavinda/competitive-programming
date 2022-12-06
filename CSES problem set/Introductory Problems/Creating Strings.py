count=0
mem=[]
def rec(num,arr,step,s):
    global count
    if step==len(num):
        mem.append(s)
        count+=1
        return
    for i in range(len(num)):
        if(arr[i]==-1 and(i==0 or( num[i-1]!=num[i]) or arr[i-1]==0)):
            arr[i]=0
            rec(num,arr,step+1,s+num[i])
            arr[i]=-1
 
num=input()
num=sorted(num)
arr=[-1]*len(num)
rec(num,arr,0,"")
print(count)
print("\n".join(mem))
