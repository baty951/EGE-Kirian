m = []
for n in range(10**4):
    x = bin(n)[2:]
    if (c := sum(list(map(int, list(x))))) % 3 == 0:
        x = x + bin(c % 5)[2:]
    else:
        x = "1" + x + "10"
    r = int(x, 2)
    if r > 89:
        m.append(r)
print(min(m))
#ответ 91