import numpy as np
import random

symbols = ['R', 'B', 'Y', 'G']

random_string = ''.join(random.choices(symbols, k=100))

print(random_string)

