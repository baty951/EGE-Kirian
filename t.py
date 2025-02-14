from sys import setrecursionlimit
setrecursionlimit(10**9)

def f(n):
    if n <= 5:
        return n
    else:
        return n*f(n-4)*f(n-2)
print((f(32768) - 9 * f(32766))/f(32764))