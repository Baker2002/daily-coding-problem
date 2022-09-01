#Given an array of integers, return a new array such that each element at index i
# of the new array is the product of all the numbers in the original array except the one at i
#
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
#Follow-up: what if you can't use division?

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