for A in range(100):
    c = 0
    for x in range(1,1000):
        if ((x % 2 == 0) <= (x % 3 != 0)) or (x + A >= 80):
            c += 1
        if c == 1000:
            print(A)
            break