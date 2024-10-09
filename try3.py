for i in range(5):
 print(i)
print("--------------")
for char in "hello":
 print(char)
print("--------------")
numbers = [5, 2, 9, 1, 5]
for number in sorted(numbers):
 print(number)
print("-------------------------")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
 print(f"Color {index + 1}: {color}")
print("------------------------------")
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
 print(f"{name} is {age} years old")
print("--------------------------------")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
 if number == 3:
  continue  # Skip number 3
 if number == 8:
  break  # Exit the loop when reaching number 8
 print(number)
print("-------------------------------------")
numbers = [11, 22, 33, 44, 55]
for number in numbers:
 if number % 2 == 0:
  print(f"{number} is even")
 else:
  print(f"{number} is odd")
print("---------------------------------------")
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
 print(f"{key}: {value}")






