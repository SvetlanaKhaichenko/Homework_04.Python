"""
Вычислить число π c заданной точностью d
Пример:
при d = 0.001,π = 3.141 10^(-1)≤d≤10^(-10)

"""
# from math import acos

# def printValueOfPi():
#     pi = round ( 2 * acos( 0.0 ), 10 )
#     return print(pi)
import math
pi_num = str(math.pi)
d_polz = input('Задайте точность вывода числа Pi: d = ')
d = len(d_polz)
print(float(pi_num[:d]))

