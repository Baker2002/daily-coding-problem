import random

list = []
list2 = []

for a in range(0,5):
    list.append(random.randint(1,10))
print(list)

for a in range(0,len(list)):
    r = list[a]
    list.pop(a)
    sum2 = list[0] * list[1] * list[2] * list[3]
    list2.append(sum2)
    list.insert(a, r)
print(list2)