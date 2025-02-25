from itertools import product

alphabet = "бенрстья"
count = 0
for x in product(alphabet, repeat=5):
    count += 1
    if x[0] == "р" and x.count("ь") == 0:
        print(count, x)