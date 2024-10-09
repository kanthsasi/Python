def is_armstrong_number(num):
 digits = str(num)
 power = len(digits)
 total = sum(int(digit) ** power for digit in digits)
 return total == num

number = int(input("Enter a number: "))
if is_armstrong_number(number):
 print(f"{number} is an Armstrong number.")
else:
 print(f"{number} is not an Armstrong number.")