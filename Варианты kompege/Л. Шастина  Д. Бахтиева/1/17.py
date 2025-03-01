massive = [int(x[:-1]) for x in open("17.txt").readlines()]
count = 0
mx = 0
mn = min(massive)

for x in range(len(massive)-1):
    y = x + 1
    if (massive[x]%77 + massive[y]%77) == mn:
        count += 1
        mx = max(mx, massive[x] + massive[y])
print(count, mx)