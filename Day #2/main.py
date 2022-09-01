import random

list = []
list2 = []
for a in range(0,5):
    list.append(random.randint(1,10))
print(list)
listBackup = list
for a in range(0,len(list)):
    r = listBackup[a]
    listBackup.pop(a)
    sum2 = listBackup[0] * listBackup[1] * listBackup[2] * listBackup[3]
    list2.append(sum2)
    listBackup.insert(a, r)
print(list2)