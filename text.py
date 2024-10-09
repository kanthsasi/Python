#1.fibnaciss
a,b=1,2
max_count=10
count=0
while count<=max_count:
 print(a,end=" ")
 a,b=b,a+b
 count+=1
 
print("-------------------------------------------------")

#2.factorial
factorial=1
num=5
temp_value=num
while num>0:
 factorial*=num
 num-=1
print(f"the factorial of {temp_value} is:",factorial)
 
print("------------------------------------------------")

#3.odd or even
num=int(input("enter the number:"))
while num%2==0:
 print(f"the given {num} is even")
 break
else:
 print(f"the given {num} is odd") 

print("------------------------------------------------------")

#4.armsstrong number
def armsstrong_number(num):
 digits=str(num)
 power=len(digits)
 total=sum(int(digit) ** power for digit in digits)
 return total==num
num=int(input("enter number:"))
if armsstrong_number(num):
 print(f"{num} is armsstrong number.")
else:
 print(f"{num} is a armsstrong number.")
 
print("-------------------------------------------------------------")

#5.triangle
def shapes(height):
 for i in range(1,height+1):
  print("*" *i)
input_=int(input("enter height:"))
shapes(input_)

print("-------------------------------------")

def shapes(height):
 for i in range(height,0,-1):
  print("*" *i)
input_=int(input("enter height:"))
shapes(input_)

print("---------------------------------------")

def shapes(height):
 for i in range(1,height+1):
  print(" " *(height-i),"*" *i)
input_=int(input("enter height:"))
shapes(input_)

print("----------------------------------------")

def shapes(height):
 for i in range(height,0,-1):
  print(" " *(height-i),"*" *i)
input_=int(input("enter height:"))
shapes(input_)

print("-------------------------------------------")

#6.sum of 1to10
total=0
num=1
while num<=10:
 total+=num
 num+=1
print("the sum of 1to10 is:",total)