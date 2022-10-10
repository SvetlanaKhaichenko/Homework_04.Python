"""
31). Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
"""

import math


def factorization(numbers):
    result = []
    list_prime = []
    for i in range (97, 1, -1):                     #Список простых чисел [3,97] включая 2, следующие за ними являются составными.
        if ((math.factorial(i-1))+1) % i == 0:
            list_prime.append(i)
            list_prime.sort()
    if numbers%2 ==0:
        while numbers %2 == 0:
            result.append(2)
            numbers = numbers/2
    for i in list_prime:
        while numbers%i == 0:
            result.append(i)
            numbers = numbers/i
    result.append(round(numbers))    
    return result

value = int(input('Введите число для проверки: '))
print(factorization(value))


