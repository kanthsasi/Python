class admin:
 def __init__(self,id,name,yop,age):
  self.id=id
  self.name=name
  self.yop=yop
  self.age=age
  
 def display(self):
  print(self.id,self.name,self.yop,self.age)
s0=admin(1,"sasi",2024,22)
s0.display()
s1=admin(2,"sanjiv",2023,23)
s1.display()
s2=admin(3,"manoj",2024,22)
s2.display()
 