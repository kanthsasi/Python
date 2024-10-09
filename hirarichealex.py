class sasi:
 def add(self,a,b):
  print(a+b)
class sanju(sasi):
 def sub(self,a,b):
  print(a-b)
class manoj(sasi):
 def mul(self,a,b):
  print(a*b)
class sabu(sasi):
 def div(self,a,b):
  print(a/b)

sa=sanju()
sa.add(202,202)
sa.sub(20,10)
sab=sabu()
sab.add(1,1)
sab.div(5,10)
sa.add(202,202)