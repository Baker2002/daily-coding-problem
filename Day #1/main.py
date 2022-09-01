import random

list = []
for a in range(1,5):
    list.append(random.randint(4,20))

k = random.randint(16,40)
print(f"{list}\n{k}")

for b in range(0,len(list)-1):
    r = k - list[b]
    if list.count(r) == 1:
        index = list.index(r)
        tacanBroj = list[index]
        print(f"{list[b]} + {tacanBroj} = {k}")
        break