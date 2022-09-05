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
highest = 0
line = 0
for a in range(0, len(br)):
    d = pow(int(br[a]),int(br2[a]))
    if d > highest:
        d = highest
        line = a

print(line)