import time
start_time = time.time()

massive = [int(x[:-1]) for x in list(open("17(37357).txt"))]

divisors = [[],[],[],[],[],[],[]]
eights = []

mx = 0
count = 0


for x in massive:
    if x%8 == 0:
        eights.append(x)
    else:
        divisors[x%8-1].append(x)

for i in range(4):
    for x in divisors[i]:
        for y in divisors[6-i]:
            if (c := x + y) % 8 == 0:
                mx = max(mx, c)
                count += 1

for x in range(len(eights)-1):
    for y in range(x+1,len(eights)):
        if (c:= x+y)%8 == 0:
            mx = max(mx, x + y)
            count += 1

print(count, mx)
print("--- %s seconds ---" % (time.time() - start_time))