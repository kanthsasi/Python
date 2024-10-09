def triangle(height):
 for i in range(1, height+1):
  print("*" *i)
 
userinput=int(input("enter height "))
triangle(userinput)
print("---------------------------------")
def triangle(height):
 for i in range(height,0,-1):
  print("&" *i)
userinput=int(input("enter height="))
triangle(userinput)