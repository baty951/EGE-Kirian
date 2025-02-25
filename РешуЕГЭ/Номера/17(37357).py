import time
start_time = time.time()

massive = [int(x[:-1]) for x in list(open("17(37357).txt"))]

divisors = [[],[],[],[],[],[],[],[]]

mx = 0
count = 0

for x in massive:
    divisors[x%8].append(x)

for i in range(1,4):
    for x in divisors[i]:
        for y in divisors[8-i]:
            if (c := x + y)&8 == 0:
                mx = max(mx, c)
                count += 1

for x in range(len(divisors[4])-1):
    for y in range(x+1, len(divisors[4])):
        if (c := x+y)&8 == 0:
            mx = max(mx, c)
            count += 1

for x in range(len(divisors[0])-1):
    for y in range(x+1, len(divisors[0])):
        if (c := x+y)&8 == 0:
            mx = max(mx, c)
            count += 1

print(count, mx)
print("--- %s seconds ---" % (time.time() - start_time))