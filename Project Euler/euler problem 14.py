def is_even(number):
    return  number / 2

def is_odd(number):
    return 3 * number + 1


def solver(a):
    count = 1
    while a != 1:
        if a % 2 == 0:
            a = is_even(a)
            count = count + 1
        else:
            a = is_odd(a)
            count = count + 1
        #print(a)
    return count

highest = 0
num = 0

for b in range(1, 1_000_000):
    highest2 = solver(b)
    if highest2 > highest:
        highest = highest2
        num = b

print(highest, num)