#4466
f = open("9.csv").readlines()
f[0] = f[0][3:]
for i in range(len(f)):
    f[i] = f[i][:-1]
    f[i] = f[i].split(";")

count = 0
t = False
sr = int()

for i in range(len(f)):
    t = False
    sr = (f[i][0]+f[i][-1])/2
    for x in range(len(f[i])):
        if f[i][x] == sr:
            t = True
    if t:
        count += 1

print(count)