"""
32). Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
"""

from functools import reduce



k = list(map(int, input('Введите последовательность чисел, через пробел: ').split()))
print(k)
result = []

for el in k:
    if el not in result:
        result.append(el)
# result.sort()
print(result)