def triangle(height):
 for i in range(1,height+1):
  print(" "*(height-i),'*'*i)
  

userinput=int(input("enter height="))
triangle(userinput)  