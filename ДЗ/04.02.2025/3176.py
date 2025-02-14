def f(n):
    joiaasdqw = ""
    while n != 0:
        joiaasdqw += str(n%9)
        n //= 9
    return joiaasdqw[::-1].zfill(1)

def f1(n : str):
    m = []
    m.extend([n.count("8"), n.count("7"), n.count("6"), n.count("5"), n.count("4"),
              n.count("3"), n.count("2"), n.count("1"), n.count("0")])
    i = m.index(max(m))
    i = 8 - i
    return str(i)
for n in reversed(range(10**4)):
    x = f(n)
    for pqe in range(5):
        if x.count("5") == x.count("7"):
            x += x[-1]
        else:
            x += f1(x)
    r = hex(int(x, 9))[2:]
    if "bac" in r:
        print(n, r)
        break
        #ответ 9918