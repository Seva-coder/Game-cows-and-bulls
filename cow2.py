import random
import copy

def FindByk(main, curr):
    sovpad = 0
    m1 = str(main)
    m2 = str(curr)

    for n in range(0, len(m2)):
        if m1[n] == m2[n]:
            sovpad += 1
    return sovpad

def FindCow(main, curr):
    sovpad = 0
    mainStr = str(main)
    currStr = str(curr)
    for n in range(0, len(currStr)):
        if mainStr.find(currStr[n]) != -1 and mainStr.find(currStr[n]) != n:
            sovpad += 1
    return sovpad

total2 = []
total =[]
for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                if a != b and a != c and a != d and b != c and b != d and c != d:
                    total.append(a * 1000 + b * 100 + c * 10 + d)

iterac = 0
number = random.randint(0, len(total) - 1)
selected = total[number]
print("Итерация 0 ", selected)
byk = int(input("Быков "))
cow = int(input("Коров "))

while byk != 4:
    iterac += 1
    print("Итерация №", iterac)
    total2.clear()
    total2 = copy.copy(total)
    for i in total2:
        if (FindByk(selected, i) != byk) or (FindCow(selected, i) != cow):
            total.remove(i)
    print("В списке осталось ", len(total), " чисел")
    if len(total) == 1:
        print("Загаданное число ", total, "!")
        break
    number = random.randint(0, len(total) - 1)
    selected = total[number]
    print(selected)
    byk = int(input("Быков "))
    cow = int(input("Коров "))


print("всё")
