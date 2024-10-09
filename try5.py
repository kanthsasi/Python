def triangle(height):
 for i in range(1,height+1):
  print("*" *i)
user_input=int(input("enter height:"))
triangle(user_input)
print("----------------------------------")
def triangle(height):
 for i in range(height,0,-1):
  print("*" *i)
user_input=int(input("enter height:"))
triangle(user_input)
print("------------------------------------")
def triangle(height):
 for i in range(1,height+1):
  print(" " *(height-i),"*" *i)
user_input=int(input("enter height:"))
triangle(user_input)
print("---------------------------------------")
def triangle(height):
 for i in range(height,0,-1):
  print(" " *(height-i),"*" *i)
user_input=int(input("enter height:"))
triangle(user_input)
print("----------------------------------------")
def is_armsstrong_number(num):
 digits=str(num)
 power=len(digits)
 total=sum(int(digit) ** power for digit in digits)
 return total==num
num=int(input("Enter number:"))
if is_armsstrong_number(num):
 print(f"{num} is a armsstrong number.")
else:
 print(f"{num} is not a armsstrong number.")
print("-----------------------------------------------")
# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.

num = int(input("Enter a number: "))
if (num % 2) == 0:
   print(f"{num} is Even")
else:n
   print(f"{num} is Odd")


