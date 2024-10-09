print("14.comparing two strings for anagrams")
str1="listen"
str2="silent"

str1=list(str1.upper())
str2=list(str2.upper())
str1.sort(),str2.sort() 

if (str1==str2):
 print("TRUE")
else:
 print("False")
print("--------------------------------------")

print("15.palindrome")
str1="kayak"
if (str1[::-1]):
 print("true")
else:
 print("false")
print("--------------------------------------")

print("16.counting digit,letters,and spaces in a string")
#importing regular experessions
import re
name="Python is 1"
digitcount=(re.sub("[^0-9]", "",name))
letterscount=(re.sub("[^a-zA-Z]", "",name))
spacescount=(re.findall("[ \n]",name))
print(len(digitcount))
print(len(letterscount))
print(len(spacescount))
print("--------------------------------------")

print("17.counting the special characters in string")
import re
spstr="!@#$%^&*()"
count=(re.sub("[ \n]+", "",spstr))
print(len(count))
print("----------------------------------------")

print("18.removing all whitespaces in a string")
import re
string="C O D E"
spaces=(re.compile(r"\s+"))
result=(re.sub(spaces, "",string))
print(result)
print("--------------------------------------")

print("19.randomizing the items of a list in python")
from random import shuffle
list=["python","is","easy"]
shuffle(list)
print(list)

def shapes(height):
 for i in range(1,height+1):
  print ("*" *i)#(" " *(height-i),"*" *i)
input_=int(input("enter the number:"))
shapes(input_)

def shapes(height):
 for i in range(height,0,-1):
  print(" " *(height-i),"$" *i)
input_=int(input("enter the number:"))
shapes(input_)