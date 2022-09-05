file = open("G:\p099_base_exp.txt", 'r')
list = file.read()

br = []
br2 = []
load = ""
c = 0

for a in range(0,len(list)):
    #print(list[a])
    print(list[a])
    if list[a].isnumeric():
        load = load + list[a]
    if list[a] == ",":
        if c == 0:
            br.append(load)
            c += 1
        else:
            br2.append(load)
            c = 0
        load = ""
    if list[a].isspace():
        if c == 0:
            br.append(load)
            c += 1
        else:
            br2.append(load)
            c = 0
        load = ""
br.sort()
br2.sort()

max_left = int(br[0])
max_right = int(br2[0])
print(f"{max_left} ** {max_right}")

print(pow(max_left,max_right))