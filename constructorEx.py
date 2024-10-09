class student:
 def __init__(self,id,name,dept,course,yop,age):
  print(id,name,dept,course,yop,age)
 def studentInfo(self,id,course,duration,modeOfClass):
  print(id,course,duration,modeOfClass) 
#objname=classname()
s=student(1,"sanju",'cse','python',2024,22)
s1=student(2,"sasi","it","java",2021,23)
s2=student(3,"manoj","ece","dot net",2023,21)
s.studentInfo(1,"java",4,"offline")
s.studentInfo(2,"python","python","online")  