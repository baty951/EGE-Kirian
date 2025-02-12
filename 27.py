f = open('27_A.csv', "r").readlines()
f[0] = f[0][3:]
for i in range(0, len(f)):
    f[i] = f[i].replace(",", ".")
    f[i] = list(map(float ,f[i].split(";")))
    f[i][1] = str(f[i][1]).replace("\n", "")
    f[i][1] = float(f[i][1])
d = 99999999999999999
best = 0
o = 0

for i in f:
    for w in f:
        o += (((w[0]-i[0])**2)+((w[1]-i[1])**2))**0.5
    if o < d:
        d = o
        best = i
    o = 0
print(best)