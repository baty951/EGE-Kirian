from itertools import product

alphabet = "люстра"
consonants = "лстр"
count = 0

for i in product(alphabet, repeat=5):
    if i.count("ю") < 3 and not(i[-1] in consonants):
        count += 1
print(count)