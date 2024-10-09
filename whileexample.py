num=2
while(num<=20):
 print(num,end=",")
 num=num+2
print("------------------------------------------------------")
num=1
while(num<=20):
 print(num)
 num=num+2
print("------------------------------------------------------")
total = 0
num = 1
while num <= 10:
 total += num
 num += 1
 print("The sum of numbers from 1 to 10 is:", total)
print("---------------------------------------------------")
count = 5
while count > 0:
 print(count,end=",")
 count -= 1
 print("liftoff",end=",")
print("-----------------------------------------------")
num=1
print("numbers""  ""tsquares")
while(num<=10):
 print(num,"       ",num**2)
 num=num+1
print("-------------------------------------------------")
num=10
while(num<=300):
 print(num,end=",")
 num=num+10
 print("increse 10")
print("--------------------------------------------------")
while True:
 age_str = input("Enter your age: ")
# Check if the input can be converted to an integer
 if age_str.isdigit():
  age = int(age_str)
  print("Your age is:", age)
  break  # Exit the loop if valid input is received
else:
  print("Invalid input. Please enter a valid age.")
print("---------------------------------------------------")
password = input("Enter a password (at least 8 characters long): ")
while len(password) < 8:
 print("Password is too short. Please enter at least 8 characters.")
 password = input("Enter a password (at least 8 characters long): ")
print("Password set successfully!")
print("------------------------------------------------------")



