a = 2
for b in range(1,1000):
    a = a * 2
b = 0


print(a)
while a != 0:
    b = b + (a % 10)
    a = a // 10

print(b)
