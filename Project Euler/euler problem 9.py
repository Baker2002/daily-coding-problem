a = 2
b = 2
c = 8



left_s = (a * a) + (b * b)
right_s = (c * c)

pythagorean = (f"{left_s} = {right_s}")




for prvi in range(1,1001):
    a = prvi
    a2 = a*a
    for drugi in range(1,1001):
        b = drugi
        b2 = b*b
        for treci in range(1,1001):
            c = treci
            c2 = c*c
            if a2 + b2 == c2:
                #print(f" {a2} + {b2} = {c2}")
                if a + b + c == 1000:
                    print(f"{a} + {b} + {c} = 1000 EEEEEEEEEEEEEEEEEEEEEEEE")
                    print(f"{a} * {b} * {c} = {a*b*c} ")




