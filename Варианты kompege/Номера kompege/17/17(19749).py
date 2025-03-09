massive = [int(x[:-1]) for x in list(open("17(19749).txt"))]
mx = max(massive)%7
mn = min(massive)%3
count = 0
ans = 0

for x in range(1, len(massive)-1):
    s = (massive[x-1],massive[x],massive[x+1])
    k3 = 0
    k7 = 0
    for i in s:
        if i%3 == mn:
            k3 += 1
        if i%7 == mx:
            k7 += 1
    if k3 == 1 and k7 > 1:
        ans = max(ans, sum(s))
        count += 1
print(count, ans)