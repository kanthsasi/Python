n=int(input("Enter number:"))
sum=0
for digit in str(n):
 sum=sum+int(digit)
print("the sum of given number is:",sum)
 
total=0
num=1
while num<=10:
 total+=num
 num+=1
print("the sum of one to ten is:",total)
 
fac=1
num=5
original_num=num
while num>0:
 fac*=num
 num-=1
print(f"the factorial of{original_num} is:",fac)

a,b=0,1
max_terms=10
count=0
while count<=max_terms:
 print(a)
 a,b=b,a+b
 count+=1
 
 