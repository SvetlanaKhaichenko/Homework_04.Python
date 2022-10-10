''' 33). Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k и приравняйте его к нулю.
Пример:
k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
2*x*2 + 4*x + 5 = 0
или
2*x^2 + 4*x + 5 = 0 '''

# from functools import reduce
from random import randint
k = int(input('Задайте натуральную степень k = '))
k += 1
lst = [el for el in range(2, k)]
lst = lst[::-1]
x = 'x'
indexes = {"0": "\u2070",
           "1": "\u00B9",
           "2": "\u00B2",
           "3": "\u00B3",
           "4": "\u2074",
           "5": "\u2075",
           "6": "\u2076",
           "7": "\u2077",
           "8": "\u2078",
           "9": "\u2079",
           "-": "\u207B"
           }
degrees = []
for el in lst:
    if el < 10:
        el = str(el)
        degrees.append(x + indexes[el])
    elif el > 9:
        s = str(el)
        q = ''
        for i in s:
            q += indexes[i] or ''
        degrees.append(x+q)
degrees.append(x)

rand_value = []
for i in range(len(degrees) + 1):
    rand_value.append(randint(0, 101))

sum_x = []
for i in range(len(degrees)):
    if not rand_value[i] == 0:
        if rand_value[i] == 1:
            sum_x.append(degrees[i])
        else:
            sum_x.append(str(rand_value[i]) + degrees[i])   
if not rand_value[-1] == 0:
    sum_x.append(rand_value[-1])
result = ''
s = ' + '
ex = ' = 0'

for j in range(len(sum_x)):
    if not j == len(sum_x)-1:
        result += str(sum_x[j]) + s
    else:
        result += str(sum_x[-1]) + ex
print(result)
with open('file.txt', "r+", encoding='utf-8') as resfile:
    resfile.write(result)
