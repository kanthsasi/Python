i=1
count=0
while i<=10:
 
 count+=1
 i+=1
print(count)


floor=5
h=2*floor-1
for i in range(1,2*floor,2):
 print("{:^{}}".format("*" *i,h))

data=[1,2,3,67,99]
def fsl(num):
 fln=max(num[0],num[1])
 sln=min(num[0],num[1])
 for i in range(2,len(num)):
  if num[i]>fln:
   sln=fln
   fln=num[i]
  elif num[i]>sln and fln!=num[i]:
   sln=num[i]
 return sln
res=fsl(data)
print(res)