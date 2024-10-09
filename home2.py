i=0
while i<5:
 i+=1
 if i%2==0:
  continue
 print(i)
 
a=9
while a ==5:
 print("a")
else:
 print("A")
 
def is_palendrom(letter):
 return letter==letter[::-1]
string="nun"
print(f"{string} is palendrom:{is_palendrom(string)}")

def is_palendrom(numbers):
 string=str(numbers)
 return string==string[::-1]
number=12345676543215
print(f"{number} is palendrom : {is_palendrom(number)} ")

x=[1,2,3,4]
print(x[1:])