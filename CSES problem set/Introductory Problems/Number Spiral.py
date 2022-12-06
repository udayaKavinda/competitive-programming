num=int(input())
while(num):
    num=num-1
    x,y=map(int,input().split())
    # print(max(x,y)**2-max(x,y)+1)
    # print(min(x,y)//2)
    if (x>y and x%2==1) or (y>x and y%2==1):
        print(max(x,y)**2-max(x,y)+1+y-x)
    elif (x>y and x%2==0) or (y>x and y%2==0):
        print(max(x,y)**2-max(x,y)+1+x-y)
    else:
        print(max(x,y)**2-max(x,y)+1+x-y)