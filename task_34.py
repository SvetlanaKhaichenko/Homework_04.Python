"""
34). Даны два файла, в каждом из которых находится запись многочлена, приравненного к нулю. Задача - сформировать файл, содержащий сумму многочленов (суммируем подобные слагаемые).
Пример:
1 Файл : 2*x2 + 4*x + 5 = 0
2 Файл : 4*x2 + 7*x + 9 = 0
3 Файл: (содержит результат) 6*x2 + 11*x + 14 = 0
Пример:
1 Файл : 2*x3 + 4*x2 + 5*x + 1 = 0
2 Файл : 4*x2 + 7*x + 9 = 0
3 Файл: (содержит результат) 2*x3 + 8*x2 + 12
"""


def addpoly(p1, p2):
    i = 0
    j = 0
    c = []
    if len(p1) == 0:
        # if p1 empty
        return p2
    if len(p2) == 0:
        # if p2 is empty
        return p1
    while i < len(p1) and j < len(p2):
        if p1[i][1] == p2[j][1]:
            su = int(p1[i][0])+int(p2[j][0])
            if su != 0:
                c.append((str(su), p1[i][1]))
                i = i+1
                j = j+1
        elif p1[i][1] > p2[j][1]:
            c.append((p1[i]))
            i = i+1
        elif p1[i][1] < p2[j][1]:
            c.append((p2[j]))
            j = j+1
    if p1[i:] != []:
        for k in p1[i:]:
            c.append(k)
    if p2[j:] != []:
        for k in p2[j:]:
            c.append(k)

    return c


with open('file_1.txt', "r") as resfile:
    equation_1 = resfile.read()
with open('file_2.txt', "r") as resfile:
    equation_2 = resfile.read()

eq_1 = equation_1.replace(' ', '')
eq_1 = eq_1.replace('=0', '')
eq_1 = eq_1.split('+')

eq_2 = equation_2.replace(' ', '')
eq_2 = eq_2.replace('=0', '')
eq_2 = eq_2.split('+')

res_eq = []
for i in eq_1:
    if '*x' in i:
        a, c = i.split('*x')
        res_eq.append((a, c))
    else:
        res_eq.append((i, 0))
res_eq_2 = []
for i in eq_2:
    if '*x' in i:
        a, c = i.split('*x')
        res_eq_2.append((a, c))
    else:
        res_eq_2.append((i, 0))

result = addpoly(res_eq, res_eq_2)
add_result = ''
j = 0
c = 1
for i in range(len(result)):
    add_result += result[i][j]
    p = '*x^' + str(result[i][c]) + ' + '
    add_result += p
    if result[i][c] == 0:
        add_result += str(result[i][j])

add_result += ' = 0'

with open('result.txt', "w+") as rs:
    rs.write(add_result)
print(add_result)
