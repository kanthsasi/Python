class hello:
 def _init_(self,name,age):
  self._name=name
  self._age=age
 
 def show(self):
  print(self._name,self._age)

class hai(hello):
 def __init__(self,name,age):
  self._name=name
  self._age=age
 def display(self):
  print(self._name,self._age)

class manoj(hello):
 def __init__(self,name,age):
  super().__init__(name,age)
 def _display(self):
  self.show()
m=manoj("salma",22);
m._display()
