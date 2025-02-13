def f(n):
    joiaasdqw = ""
    while n != 0:
        joiaasdqw += str(n%3)
        n //= 3
    return joiaasdqw[::-1].zfill(1)

