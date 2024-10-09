class sasi:
 def add(self,a,b):
  print(a+b)
class sanju(sasi):
 def sub(self,a,b):
  print(a-b)
class manoj(sasi):
 def mul(self,a,b):
  print(a*b)
 

m=manoj()
m.add(100,200)
m.mul(3,4) 
sa=sanju()
sa.sub(8,2)
sa.add(5,5)
  