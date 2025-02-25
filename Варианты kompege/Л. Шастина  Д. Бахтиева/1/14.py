def f(n):
    joiaasdqw = ""
    while n != 0:
        joiaasdqw += str(n%4)
        n //= 4
    return joiaasdqw[::-1].zfill(1)

a = 4**644 + 4**322 + 16**35 - 64**3
print(f(a).count("3"))