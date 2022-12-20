num=int(input())
arrival=[0]*num
leave=[0]*num
for i in range(num):
    arrival[i],leave[i]=map(int,input().split())
arrival.sort()
leave.sort()
count=0
x=0
y=0
maximum=0
lenx=len(arrival) 
leny=len(leave)
total=sorted(arrival+leave)
for i in range(2*num):
    if x<lenx and arrival[x]==total[i]:
        x+=1
        count+=1
    elif y<leny and leave[y]==total[i]:
        y+=1
        count-=1
    maximum=max(maximum,count)
