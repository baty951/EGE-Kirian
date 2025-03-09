def f(a, x, y) -> bool:
    return bool((x <= 19) or (y < 2*x + a - 50) or (y > 17))

for a in range(10**3):
    if all(f(a, x, y) == True for x in range(10**3) for y in range(10**3)):
        print(a)
        break