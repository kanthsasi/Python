class sasi:
 def __init__(self,id,name,course):
  self.id=id
  self.name=name
  self.course=course
  
 def display(self):
  print("Values:",self.id,self.name,self.course)

s=sasi(1,"sasi","java,python")
s.display()

def definition(a,b,c):
 d=a+b+c
 print(d)
definition(1,2,3)

class student:
 def __init__(self,id,name):
  print(id,name)
s=student(1,"sasikanth")

name="sasikanth"
for i in name:
 if(i=="a"):
  print("if blocks",end=(" "))
 else:
  print(i,end=(" "))