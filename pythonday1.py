tuple_=("python","java")
for s in range(len(tuple_)):
 print(tuple_[s].upper())
 
 a=1
 b=2
 c=a+b
 print(c)
 
 list1  = [1, "hi", "dc", 20000,"salma","hari,'a'"]    
#Checking type of given list  
print(type(list1)) 
#Printing the list1  
print (list1) 
# List slicing  # 3 and above
print (list1[3:])  
print(list1[:3])
print (list1[0:3])   
print (list1 + list1)  
print (list1 * 3)  
print("------------------------------")
a,b=b,a#swapping a&b value
print (a,b)
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
print("-----------------------------------------------------------")
def sam(*kids):
 print("The youngest child is ",kids[2])
sam("Emil","Tobias","Linus")
class sam:
 count=0
 def __init__(self):
  sam.count=sam.count+1
  print(sam.count)

 def cityname(*city):
  print("second City name is ",city[4])
s1=sam()
s2=sam()
s3=sam()
s1.cityname("chennai","cbe","madurai","ooty","kodaikanal","keralam","goa")  
print("------------------------------------------------------------------")