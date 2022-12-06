num=input()
a=None
count=0
mem=0
for i in range(len(num)):
    count=count+1
    if num[i]!=a:
        a=num[i]
        count=1
    mem=max(count,mem)
    
 
print(mem)
