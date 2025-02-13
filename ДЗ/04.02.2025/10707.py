def f(n):
    joiaasdqw = ""
    while n != 0:
        joiaasdqw += str(n%6)
        n //= 6
    return joiaasdqw[::-1].zfill(1)


for n in range(10**4):
    x = f(n)
    if n % 3 == 0:
        x = x + x[0:2]
    else:
        x = x + f(n%3*10)
    r = int(x, 6)
    if r > 680:
        print(r)
        break #ответ 694