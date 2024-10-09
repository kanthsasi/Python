num=100
factorial=1
original_num=num
while num>0:
 factorial*=num
 num-=1
print(f"the factorial of{original_num}:",factorial)
print()
total=0
num=1
while num<=2:
 total+=num
 num+=1
print("the sum of 1to100 is:",total)
print()
a,b=0,1
max_count=10
count=0
while count<=max_count:
 print(a,end=(' '))
 a,b=b,a+b
 count+=1
print()
while True:
 age_str=input("enter your age:")
 if age_str.isdigit():
  age=int(age_str)
  print("your age is:",age)
  break
else:
 print("invaild meassage-please enter vaild meassage")