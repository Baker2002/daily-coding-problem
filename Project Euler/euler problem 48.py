rez = 0
c = 0
for a in range(1,1001):
    print(a,c)
    c = a ** a
    rez = rez + c
print(rez)
