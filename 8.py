from itertools import product

alphabet = "БЕНРСТЬЯ"
count = 0

for x in product(alphabet, repeat=5):
    count += 1
    if x[0] == "Р" and x.count("Ь")==0:
        print(count, x)