def find_prime(num):
    sum_prime = -1
    for c in range(1, num):
        k = 0
        if num > c:
            for a in range(1, c):
                if c % a == 0:
                    k += 1
                    if k == 1:
                        if c % c == 0:
                            k += 1
                    if k > 2:
                        break
            if k < 3:
                sum_prime += c
    print(sum_prime)


find_prime(50_000)



