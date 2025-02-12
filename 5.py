def summ(x):
    return sum(map(int, list(x)))

for n in range(100):
    x = bin(n)[2:]
    if summ(x) % 2 == 0:
        x = x + "11"
    else:
        x = x + "01"
    if (r := int(x, 2)) > 61:
        print(r)