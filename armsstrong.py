def arms_trong(num):
 digits=str(num)
 power=len(digits)
 total=sum(int(digit)**power for digit in digits)
 return total==num

number=int(input("Enter the number:"))
if arms_trong(number):
 print(f"{number} is a armstrong number")
else:
 print(f"{number} is a not a armstrong number")
 
 
def shapes(height):
 for i in range(1,height+1):
  print("*" *i)
userinput=int(input("Enter the height:"))
shapes(userinput)

def halftriangle(pattern):
 for i in range(pattern,0,-1):
  print(" "*(pattern-i),"*" *i)

userinput=int(input("Enter the value:"))
halftriangle(userinput)  


def palindrome(num):
 s=str(num)
 return s == s[::-1]
userinput=int(input("Enter the string:"))
print(f"{userinput} is a palindrome:{palindrome(userinput)}")

def palindrome(s):
 return s == s [::-1]
userinput=input("Enter the input:")
print(f"{userinput} is a palindrome:{palindrome(userinput)}")

def isleapyearornot(year):
 return((year%4==0 and year%100!=0)or(year%400==0))
year=2024
print(f"{year} is a leap year:{isleapyearornot(year)}")


n=3
if(n%2==0):
    print("Not Weired")
else:
    print("Weired")
