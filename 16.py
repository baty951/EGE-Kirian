#5291
from sys import setrecursionlimit

setrecursionlimit(10000)

def F(n):
    if n < 3:
        return 1
    elif n > 2 and n % 2 != 0:
        return F(n-1)+n
    elif n > 2 and n % 2 == 0:
        return F(n-3)+2*n
    
print(F(2048) - F(2041))