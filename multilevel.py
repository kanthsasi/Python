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
m.add(20,30)
m.mul(20,30)
m.sub(20,30)