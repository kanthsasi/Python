class hello:
 def __init__(self,name,age):
  self._name=name
  self.age=age
 def show(self):
  print(self._name,self.age)
class hai(hello):
 def dis(self):
  print(self._name,self.age)
h=hai("kutta",1);
h.dis()