import random
list = []
highest = 0
high_text = ""
for _ in range(1000):
    list.append(random.randint(0,9))
print(list)
for a in range(0, 997):
    num = list[a] * list[a+1] *list[a+2] *list[a+3]
    if num > highest:
        high_text = f"{list[a]} * {list[a+1]} * {list[a+2]} * {list[a+3]}"
        highest = num
print(f"{high_text} = {highest}")