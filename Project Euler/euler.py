a = 1
div_by = 10 # a is divisible by every number upto div_by
divisible = False
list = []
while divisible != True:
    for b in range(1,21):
        if a % b == 0:
            list.append(b)
            if len(list) == div_by:
                print(a)
                print(list)
                divisible = True
        else:
            list.clear()
            break

    a = a + 1