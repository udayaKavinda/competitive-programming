num=int(input())
for i in range(num):
    x,y=map(int,input().split())
    # if x==2 and y==1
    if (2*min(x,y)>=max(x,y)) and (2*x-y)%3==0 and (2*y-x)%3==0:
        print("YES")
    else:
        print("NO")
