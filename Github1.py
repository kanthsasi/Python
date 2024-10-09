#28.Write a program to find armstrong number using python.
def armstrong_num(num):
 digits=str(num)
 power=len(digits)
 total=sum(int(digit)**power for digit in digits)
 return total==num
number=int(input("Enter the number:"))
if armstrong_num(number):
 print(f"{number} is a armstrong number")
else:
 print(f"{number} is not a armstrong number")
print("----------------------------------------------")
#28.Write a python program to find armstrong number in a interval.
lower=int(input("Enter the lower limit of the interval:"))
upper=int(input("Enter the upper limit of the interval:"))

for num in range(lower,upper+1):
 power=len(str(num))
 temp_num=num
 sum=0
 while temp_num>0:
  digit=temp_num%10
  sum+=digit**power
  temp_num//=10
 if num==sum:
  print(num)
print("----------------------------------------------")
#29.Write a program for fibonacci series.
a , b = 0 , 1
max_count=10
count=0
while count<=max_count:
 print(a,end=" ")
 a,b=b,a+b
 count+=1
print("----------------------------------------------")
#30.write a table using python.
num=int(input("Enter the number:"))
for i in range(1,10):
 print(f"{num}x{i}={num*i}")
print("----------------------------------------------")
#31.Write a program to find factorial.
factorial=1
num=int(input("Enter the number:"))
original_num=num
while num>0:
 factorial*=num
 num-=1
print(f"{original_num} factorial is:",factorial)
print("----------------------------------------------")
#32.Write a program to check it's prime number or not.
num=int(input("Enter the number:"))
if (num%2==0):
 print(f"{num} is a prime number")
else:
 print(f"{num} is not a prime number")
print("----------------------------------------------")
#33.Write a program to find leap year or not.
def leap_year(year):
 return((year%4==0 and year%100!=0)or(year%400==0))
year=int(input("Enter the year:"))
print(f"{year} is leap year:{leap_year(year)}")
print("----------------------------------------------")
#34.Write a program to check if a number is prime or odd.
num=int(input("Enter the number:"))
if num%2==0:
 print("It,s a prime number")
else:
 print("It,s a odd number")
print("----------------------------------------------")
#35.Write a python program to check if a number is positive,negative or zero.
num=float(input("Enter the number:"))
if num>0:
 print("It is a positive number")
elif num==0:
 print("Zero")
else:
 print("It is a negative number")
print("----------------------------------------------")
#36.Write a program to swap two variables without temp variables.
a=5 
b=10
a,b=b,a
print("After swapping:")
print("a=",a)
print("b=",b)
print("----------------------------------------------")