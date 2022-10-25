a = 1
divisible = 0
rez = 0
while divisible != 2**500500:
    divisible = 0
    a = a + 1
    for b in range(1,a+1):
        if a % b == 0:
            divisible = divisible + 1
    print(a)
rez = a % 500500507
print("")
print(f"divisibles {divisible}")
print(f"Modulo {rez}")