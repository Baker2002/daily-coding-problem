from euler13file import var

ukupno = 0
count = 0
temp = ""

for a in var:
    temp += a
    count += 1
    if count == 50:
        count = 0
        ukupno += int(temp)
        temp = ""

print(ukupno)