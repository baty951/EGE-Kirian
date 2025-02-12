f = open("26.txt")
massive = []
for x in f:
    x = x.split()
    x = list(map(int, x))
    massive.append(x)
massive = sorted(massive)
a = [massive[i][1] for i in range(len(massive))]
print(max(a))