class person:
 def __init__(self,name,age):
  self._name=name
  self._age=age
 def _display(self):
  print(self._name,self._age)
class student(person):
 def __init__(self,name,age,rollnumber):
  super().__init__(name,age)
  self._rollnumber=rollnumber
 def display(self):
  self._display()
  print(self._rollnumber)
s=student("sasi",21,1)
s.display()
s=person("Dinesh",20)
s._display()