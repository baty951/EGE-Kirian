for n in reversed(range(10**3)):
    nb = bin(n)[2:].zfill(3)
    if n % 5 == 0:
        nb = nb[:3] + nb
    else:
        nb += bin((n%5)*5)[2:]
    r = int(nb, 2)
    if r < 313 and n%2 != 0:
        print(n)