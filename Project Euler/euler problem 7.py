def find_prime(num):
    list = []
    for c in range(1, num * num):
        if len(list) == num+1:
            print(list[num])
            break
        else:
            k = 0
            for a in range(1, c + 1):
                if c % a == 0:
                    k += 1
            if k < 3:
                list.append(c)


find_prime(10001)