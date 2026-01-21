num = int(input(""))
max = 1
result = {}
for i in range(num):
    tmp = int(input(""))
    if tmp > max:
        max = tmp
    result[tmp] += 1

print(max, result[max], end=" ")
