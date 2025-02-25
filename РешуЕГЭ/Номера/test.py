import time
start_time = time.time()
count = m = 0
f = open('17(37357).txt')
l = [int(i) for i in f]
for i in range(len(l) - 1):
    for j in range(i + 1, len(l)):
        if (l[i] + l[j]) % 8 == 0:
            count += 1
            m = max(m, l[i] + l[j])
print(count, m)
print("--- %s seconds ---" % (time.time() - start_time))