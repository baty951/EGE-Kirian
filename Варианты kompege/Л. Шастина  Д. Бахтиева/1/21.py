from sys import setrecursionlimit

setrecursionlimit(10**9)

def f(x : int, k : int) -> bool:
    if x > 53 and (k == 2 or k == 4):
        return True
    elif x > 53 and (k == 1 or k == 3):
        return False
    elif x < 53 and k == 4:
        return False
    else:
        if k%2 == 0:
            return f(x + 2, k + 1) and f(x * 2, k + 1)
        else:
            return f(x + 2, k + 1) or f(x * 2, k + 1)
    
def f1(x : int, k : int) -> bool:
    if x > 53 and k == 2:
        return True
    elif x > 53 and k == 1:
        return False
    elif x < 53 and k == 2:
        return False
    else:
        if k%2 == 0:
            return f(x + 2, k + 1) or f(x * 2, k + 1)
        else:
            return f(x + 2, k + 1) or f(x * 2, k + 1)

for x in range(1,54):
    if f(x, 0) and f1(x, 0):
        print(x)
        print("================")