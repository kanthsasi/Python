total=0
sum=1
while sum<=10:
 total+=sum
 sum+=1
print(total)

import re
string="C  O  D  E"
spaces=(re.compile(r"\s+"))
result=(re.sub(spaces, "",string))
print(result)
print(string.count(" "))

factorial=1
num=5
org_num=num
while num>0:
 factorial*=num
 num-=1
print(factorial)

def func(x, y=10):
 return x*y
print(func(5))
print(func(5,3))

x=[10,20,30]
y=x
y[0]=100
print(x)