def f(x, k):
    if x >= 2200 and k == 2:
        return 1
    if x >= 2200 and k != 2:
        return 0
    if x < 2200 and k < 2:
        return 0
    else:
        return f(x + 2, k + 1) or f(x + 3, k + 1) or f(x * 2, k + 1)
    
for x in range(2200):
    if f(x, 0):
        print(x)