#11258
from itertools import product

alphabet = " 0123456789"
for x in product(alphabet, repeat=3):
    for y in product(alphabet, repeat=3):
        for z in range(10):
            if int((w := str(x) + "75" + str(z) + "122" + str(y))) % 8387:
                print(w)