length=int(input())
arr=[]
for i in range(length):
    x,y=map(int,input().split())
    arr.append((x,y))
# print(arr)
arr.sort()
day=0
prize=0
for i in range(length):
    day+=arr[i][0]
    dead=arr[i][1]
    prize+=dead-day
print(prize)
