num=int(input())
count=0
count2=0
num1=num
while(num1>=5):
    num1=num1//5
    count2=count2+1
 
# for i in range(1,num+1):
#     for j in range(1,count2+1):
#         if(i%(5**j)==0):
#             count=count+1
for j in range(1,count2+1):
    count=count+num//(5**j)
 
print(count)