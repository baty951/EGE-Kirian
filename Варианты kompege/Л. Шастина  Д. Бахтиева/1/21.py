def f(x, k):
    if (k == 2 or k == 4) and x >= 54:
        return 1
    elif (k == 2 or k == 4) and x < 54:
        return 0
    elif (k == 1 or k == 3) and x >= 54:
        return 0
    else:
        if k % 2 != 0:
            return f(x + 2, k + 1) and f(x * 2, k + 1)
        else:
            return f(x + 2, k + 1) or f(x * 2, k + 1)

def f1(n, k):
    if k==2 and x >= 54:
        return 1
    elif k == 2 and x < 54:
        return 0
    elif k < 2 and x >= 54:
        return 0
    else:

for x in range(1,54):
    if f(x, 0):
        print(x)