print("1.converting an integer into_decimals")
import decimal
integer=10
print(decimal.Decimal(integer))
print(type(decimal.Decimal(integer)))
print("--------------------------------------")

print("2.converting an string of integer into decimal")
import decimal
string="12345"
print(decimal.Decimal(string))
print(type(decimal.Decimal(integer)))
print("----------------------------------------")

print("3.reversing a string using an extended slicing technique")
string="PYTHON PROGRAMMING"
print(string[::-1])
print("-----------------------------------------")

print("4.counting vowels in a given word")
vowel=["a","e","i","o","u"]
word="sasikanth"
count=0
for character in word:
 if character in vowel:
  count+=1
print(count)
print("------------------------------------------")

print("5.counting consonants in a given word")
vowel=["a","e","i","o","u"]
word="abcdefghijklmnopqrstuvwxyz"
count=0
for character in word:
 if character not in vowel:
  count+=1
print(count)
print("------------------------------------------")

print("6.counting the number of occurances of a character in a string")
word="python programing"
character="p"
count=0
for letter in word:
 if letter == character:
  count+=1
print(count)
print("--------------------------------------------")

print("7.writing fibonacci series")
a,b=1,2
max_count=10
count=0
while count<max_count:
 print(a,end=",")
 a,b=b,a+b
 count+=1
print("----------------------------------------------")

print("8.finding the maximum numbers in a list")
numberList=[15,85,35,89,125,2]
maxnum=numberList[0]
for num in numberList:
 if maxnum<num:
  maxnum=num
print(maxnum)
print("------------------------------------------------")

print("9.finding the minimum number in a list")
numberList=[15,85,35,89,125,2]
minnum=numberList[0]
for num in numberList:
 if minnum>num:
  minnum=num
print(minnum)
print("------------------------------------------------")

print("10.finding the middle element in a list")
numlist=[1,2,3,4,5]
midelement=int((len(numlist)/2))
print(numlist[midelement])
print("------------------------------------------------")

print("11.converting list into a string")
list=["p","y","t","h","o","n"]
string="".join(list)
print(string)
print(type(string))
print("------------------------------------------------")

print("12.counting white space in string")
string= "P r ogramm in g "
print(string.count(" "))
print("------------------------------------------------")

print("13.adding two list elemens together")
list1=[1,2,3]
list2=[4,5,6]
res_list=[]
for i in range(0,len(list1)):
 res_list.append(list1[i]+list2[i])
print(res_list)
print("-----------------------------------------------")

