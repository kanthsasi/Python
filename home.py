def shapes(height):
 for i in range(1,height+1):
  print("*" *i)
input_=int(input("enter height:"))
shapes(input_)

def arms_num(num):
 digit=str(num)
 power=len(digit)
 total=sum(int(digit) ** power for digit in digit)
 return total==num
num=int(input("ENTER THE NUMBER:"))
if arms_num(num):
 print(f"the given {num} is arms_num.")
else:
 print(f"the given {num} is not a arms_num.")

def shapes(height):
 for i in range(height,0,-1):
  print(" " *(height-i),"+" *i)
num=int(input("ENTER THE NUM:"))
shapes(num)

def is_paledrom(sasi):
 s=str(sasi)
 return s == s[::-1]
number=12344321
print(f"{number} is a palindrome:{is_paledrom(number)}")

names=["sasi","sanjiv","manoj"]
for index,name in enumerate(names):
 print(f"name {index+1} is: {name}")
 
n=int(input("enter the number:"))
square=n*n
print("square is:",square)

for i in range(1,10):
 for j in range(1,10):
  print(f"{i} * {j}={i * j}")
 
i=1
num=int(input("enter the number:"))
while i<=20:
 print(f"{num} * {i} = {num * i}")
 i=i+1