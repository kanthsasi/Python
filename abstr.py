from abc import ABC
class sample(ABC):
 def studentDetails(self,id,name,course,ph):
  pass
 def staffDetails(self,id,name,experience):
  pass 

class sasi(sample): 
 def studentDetails(self,id,name,course,ph):
  print(id,name,course,ph)
 def staffDetails(self,id,name,experience):
  print(id,name,experience)
 
s=sasi()
s.staffDetails(1,"salma",5)
s.studentDetails(101,"sanju","python",7896541236)