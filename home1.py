def is_paledrom(sasi):
 i=len(sasi)
 return i == i[::-1]
number="mom"
print(f"{number} is a palindrome:{is_paledrom(number)}")

