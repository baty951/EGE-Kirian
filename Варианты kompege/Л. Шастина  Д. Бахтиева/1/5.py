rm = []
for n in range(10**4):
    x = bin(n)[2:]
    if x.count("1") % 2 == 0:
        x += "11"
    else:
        x += "01"
    r = int(x, 2)
    if r > 61:
        rm.append(r)
print(min(rm))