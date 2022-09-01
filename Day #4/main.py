import random

list = []
for a in range(0,8):
    list.append(random.randint(-5,5))
print(list)

done = False
a = 1
while done != True:
    if list.count(a) == 0:
        print(a)
        done = True
    else:
        a = a + 1