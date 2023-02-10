# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
d = input('Write d:')
lenght = d.split(".")[1]
lenght = len(lenght)
print(lenght)
print(round(math.pi ,lenght))