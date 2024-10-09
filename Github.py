#1.Coverting an integer into decimal.
import decimal
integer=10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))
print("----------------------------------------------")
#2.Converting an string of integer into decimal.
import decimal
string="12345"
print(decimal.Decimal(string))
print(type(decimal.Decimal(string)))
print("----------------------------------------------")
#3.Reversing a string using an extended slicing technique.
string="Python Prigramming"
print(string[::-1])
print("----------------------------------------------")
#4.Counting vowels in a given word.
vowel=["a","e","i","o","u"]
word="Python Programming"
count=0
for character in word:
 if character in vowel:
  count=count+1
print(count)
print("----------------------------------------------")
#5.Counting consonants in a given word.
vowel=["a","e","i","o","u"]
word="PythonProgramming"
count=0
for character in word:
 if character not in vowel:
  count=count+1
print(count)
print("----------------------------------------------")
#6.Counting the number of occurances of a character in a string.
word="Python"
character="P"
count=0
for letter in word:
 if letter in character:
  count=count+1
print(count)
print("----------------------------------------------")
#7.Writing fibonacci series.
a,b=0,1
max_count=10
count=0
while count<=max_count:
 print(a)#print(a,end=" ")
 a,b=b,a+b
 count=count+1;
print("----------------------------------------------")
#8.finding maximum number in a list.
numberList=[15,85,35,89,1]
maxNum=numberList[0]
for num in numberList:
 if maxNum<num:
  maxNum=num
print(maxNum)
print("----------------------------------------------")
#9.Finding minmum number ina a list.
numberList=[1,2,3,4,5]
minNum=numberList[0]
for num in numberList:
 if minNum>num:
  minNum=num
print(minNum)
print("----------------------------------------------")
#10.Finding the middle element in a list.
numberList=[1,2,3,4,5,6]
midElement=int((len(numberList)/2))
print(numberList[midElement])
print("----------------------------------------------")
#11.Converting a list into a atring.
lst=["p","y","t","h","o","n"]
string="".join(lst)
print(string)
print(type(string)) 
print("----------------------------------------------")
#12.Adding two list elemens together.
lst1=[1,2,3]
lst2=[4,5,6]
res_lst=[]
for i in range(0,len(lst1)):
 res_lst.append(lst1[i]+lst2[i])
print(res_lst)
print("----------------------------------------------")
#13.Comparing two strings for anagram.
str1="listen"
str2="silent"
str1=list(str1.upper())
str2=list(str2.upper())
str1.sort(),str2.sort()

if(str1==str2):
 print("True")
else:
 print("False")
print("----------------------------------------------")
#14.Checking for palindrome using extended slicing technique.
def is_palindrome(s):
 return s==s[::-1]
string="nun"
print(f"{string} is a palinfrome:{is_palindrome(string)}")
print("----------------------------------------------")
#15.Counting the whitespaces in a string.
string="Pro g ra mm ing"
print( string.count(" "))
print("----------------------------------------------")
#16.Counting digits,letters and spaces in a string.
import re
name="python is 1"
digitcount=re.sub("[^0-9]","",name)
lettercount=re.sub("[^a-zA-Z]","",name)
spacescount=re.findall("[ \n]",name)
print(len(lettercount))
print(len(digitcount))
print(name.count(" "))
print(len(spacescount))
print("----------------------------------------------")
#17.Counting special characters in a string.
import re
specialchar="0!@#$%^&*()"
sprchar=(re.sub("[/w]+","",specialchar))
print(len(sprchar))
print("----------------------------------------------")
#18.Removing all whitespaces in a string.
import re
string=" c o d e"
remove=re.compile(r"\s+")
spaces=re.sub(remove,"",string)
print(spaces)
print("----------------------------------------------")
#19.Building pyramid in python.
floors=5
h=2*floors-1
for i in range(1,2*floors,2):
 print("{:^{}}".format("*" *i,h))
print("----------------------------------------------")
#20.Shuffle the list.
from random import shuffle
lst=["python","is","easy"]
shuffle(lst)
print(lst)
shuffle(lst)
print(lst)
print("----------------------------------------------")
#21.Length of  a string without using in-build function.
string="Welcome"
count=0
for i in string:
 count+=1
print(count)
print("----------------------------------------------")
#22.Write a python program to count the frequency of 
#each element in a list.
def count_frequency(numbers):
 frequency={}
 for num in numbers:
  if num in frequency:
   frequency [num]+=1
 else:
  frequency[num]=1
 return frequency
nums=[6,2,3,2,1,3,2,4,6]
frequency_count=count_frequency(nums)
print(frequency_count)
print("----------------------------------------------")
#23.Write a program to find the common elements between two list.
def find_common_elements(list_a,list_b):
 common_elements=[]
 for item in list_a:
  if item in list_b:
   common_elements.append(item)
 return common_elements
list_a=[1,2,3,4,5]
list_b=[4,5,6,7,8]
common=find_common_elements(list_a,list_b)
print(common)
print("----------------------------------------------")
#24.Write a program to sort a list of elements.
num=[9,8,7,6,5,4,3,2,1]
num.sort()
print(num)
res=num[-2]
print(res)
print("----------------------------------------------")
#25.Write a program to find second largest number in a list.
data=[1,2,3,4,5,6,7,8]
def find_secound_largest(list_1):
 first_max=max(list_1[0],list_1[1])
 second_max=min(list_1[0],list_1[1])
 for i in range(2,len(list_1)):
  if list_1[i]>first_max:
   second_max=first_max
   first_max=list_1[i]
  elif list_1[i]>second_max and first_max!=list_1[i]:
   second_max=list_1[i]
 return second_max
result=find_secound_largest(data)
print("Second largest number is:",result)
print("----------------------------------------------")
#26.Remove the duplicate elements in a list.
nums=[1,1,2,2,3,3,4,4,5,5,6]
def remove_duplicate(numbers):
 unique_num=[]
 for num in numbers:
  if num not in unique_num:
   unique_num.append(num)
 return unique_num
result=remove_duplicate(nums)
print(result)
print("----------------------------------------------")
#27.Write a program to find the sum of natural numbers.
#N=1,2,3,4,5,6,7,8,......
limit=int(input("Enter the number:"))
sum=0
for i in range(1,limit+1):
 sum+=i
print("The sum of natural numbers up to",limit,"is:",sum)
print("----------------------------------------------")

