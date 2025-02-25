from sys import setrecursionlimit
setrecursionlimit(10**9)

def f(n):
    if n > 400:
        return n**n
    else:
        return n + 6 + f(n+12)
print(f(72)-f(108))