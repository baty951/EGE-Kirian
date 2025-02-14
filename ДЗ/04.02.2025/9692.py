def f(n):
    return bin(sum(list(map(int, list(n)))))[2:]

for n in range(10**5):
    x = bin(n)[2:]
    if n % 2 == 0:
        x = f(x) + x + ("0" if list(x).count("1") % 2 == 0 else "1")
    else:
        x = x + "0" + f(x)
    r = int(x, 2)
    if r < 256:
        print(f"n : {n}, r : {r}")
        #ответ 28