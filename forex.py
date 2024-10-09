a,b = 0, 1
max_terms = 10
count = 0

while count < max_terms:
 print(a, end=' ')
 a, b = b, a + b
 count += 1
