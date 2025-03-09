f = open("17(12926).txt")
massive = [int(x[:-1]) for x in f]
f.close()

m = [[] for x in range(10)]
for x in massive:
    m[int(str(x)[-1])].append(x)

for i in range(10):
    for x in