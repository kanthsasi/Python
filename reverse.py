text="python"[::-1]
print(text)
print("-------------")
def my_function(x):
 return x[::-1]
mytxt=my_function("sasikanth")
print(mytxt)
print("-------------")
my_num=[1,2,3,4,5,6][::-1]
print(my_num)
print("--------------")
my_numbers=[1,2,3,4,5]
my_numbers.reverse()
print(my_numbers,end=" ")
print(type(my_numbers))

my_numbers=[1,2,3,4,5]
for number in reversed(my_numbers):
 print(number)


text=[1234,5][::-1]
print(text)

def reversestring(rs):
 return rs[::-1]
my_string=reversestring("sasikanth")
print(my_string)