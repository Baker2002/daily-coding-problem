def square(num):
    c = 0
    for a in range(1,num+1):
        c = c +(a * a)
    return c
def square_sum(num):
    c = 0
    for a in range(1, num + 1):
        c = c + a
    return c * c

a = 100

result = square_sum(a) - square(a)
print(result)