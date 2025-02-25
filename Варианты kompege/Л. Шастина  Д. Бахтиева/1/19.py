def f(x, k):
    if k == 2 and x >= 54:
        return 1
    if k == 2 and x < 54:
        return 0
    if k == 1 and x >= 54:
        return 0
    else:
        if k % 2 == 0:
            return f(x + 2, k + 1) and f(x * 2, k + 1)
        else:
            return f(x + 2, k + 1) or f(x * 2, k + 1)

for x in range(1,54):
    if f(x, 0):
        print(x)