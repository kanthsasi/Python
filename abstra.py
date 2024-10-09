from abc import ABC
class subject(ABC):
 def studentdata(self,id,name,course,ph):
  pass
 def staffdetails(self,id,name,experiance,ph):
  pass
 
class sasi(subject):
 def studentdetails(self,id,name,course,ph):
  print(id,name,course,ph)
 def staffdetails(self,id,name,experiance,ph):
  print(id,name,experiance,ph)
sasi=sasi()
sasi.studentdetails(1,"sanjiv","python",123456)
sasi.studentdetails(2,"manoj","python",123456789)
sasi.staffdetails(1,"sindhu",4,1234567)
