total=0
num=1
while num<=5:
 total+=num
 num+=1
print("the sum of 1to5 is:",total)

print("-------------------------------")

def is_palindrome(m):
 return m == m[::-1]
string = "madam"
print(f"'{string}' is a palindrome: {is_palindrome(string)}")

print("--------------------------------------")

def is_palindrome(n):
 s=str(n)
 return s == s[::-1]
number=123456
print(f"{number} is a palindrome:{is_palindrome(number)}")

print("----------------------------------------")

def is_a_leapyear(year):
 return(year %4 == 0 and year %100 != 0)or(year %400 == 0)
year=2018
print(f"{year} is a leap year:{is_a_leapyear(year)}")
