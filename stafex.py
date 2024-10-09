class staff:
 def __init__(self,id,name,dept,course,yoe):
  self.id=id
  self.name=name
  self.dept=dept
  self.course=course
  self.yoe=yoe
 
  
 def display(self):
  print(self.id,self.name,self.dept,self.course,self.yoe) 
#objname=classname()
s=staff(1,"sanju",'cse','python',2024)
s.display()
s1=staff(2,"sasi","it","java",2021)
s1.display()
s2=staff(3,"manoj","ece","dot net",2023)
s2.display()
 