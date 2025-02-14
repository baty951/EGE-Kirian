def f(n):
    joiaasdqw = ""
    while n != 0:
        joiaasdqw += str(n%3)
        n //= 3
    return joiaasdqw[::-1].zfill(1)

for n in range(9, 10**4):
    x = f(n)
    if n % 3 == 0:
        x = x + x[-2:]
    else:
        x = x + f(sum(list(map(int, list(x)))))
    r = int(x, 3)
    if r > 220 and r % 2 == 0:
        print(r)
        break
        #ответ 222