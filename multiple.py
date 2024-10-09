class sasi:
 def add(self,a,b):
  print(a+b)
class sanju:
 def sub(self,a,b):
  print(a-b)
class manoj(sasi,sanju):
 def mul(self,a,b):
  print(a*b)
m=manoj()
m.add(1,1)
m.sub(2,1)