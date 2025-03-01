from itertools import product

alphabet = " 0123456789"

for x in range(10):
    for z in range(10):
        for y in product(alphabet, repeat=3):
            if (c := int("21"+str(x)+"3"+str("".join((y[0]+y[1]+y[2]).replace(" ","")))+"145"+str(z)+"5")) < 10**10:
                if c % 2025 == 0:
                    print(c, c//2025)