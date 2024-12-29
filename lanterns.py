import numpy as np
import random

symbols = ['R', 'B', 'Y', 'G']

random_string = ''.join(random.choices(symbols, k=100))

print("Случайная последовательность цветов:", random_string, sep=' ')

lis_lis = []

lis = []

def find_symbols(n, lis, lis_lis):
    if n in lis:
        lis.clear()
    else:
        lis.append(n)
        if len(lis) == 4:
            lis_lis.append(lis[:])
            lis.clear()
         

for i in random_string:
    find_symbols(i, lis, lis_lis)

print("Наборы последовательностей из 4 цветов:", lis_lis, sep=' ')
