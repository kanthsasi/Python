class sasi:
 def add(self,a,b):
  print(a+b)
class sanju(sasi):
 def sub(self,a,b):
  print(a-b)
class manoj(sanju):
 def mul(self,a,b):
  print(a*b)
 

m=manoj()

m.add(100,200)
m.sub(100,30)
m.mul(3,4) 
  
  