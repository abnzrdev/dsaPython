a,b = map(int, input("").split())
if a == b:
    min = a
else: 
    min = (int(a > b) * b + int(a < b) * a)
factorial = 1
while min > 0:
    factorial *= min
    min -= 1
print(factorial)