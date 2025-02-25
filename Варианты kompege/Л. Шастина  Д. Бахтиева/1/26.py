file = open("26.txt").readlines()
for x in range(len(file)):
    file[x] = file[x][:-1]
first_str = file[0].split(" ")
del(file[0])
mass = int(first_str[-1])*1000
massive = list()
for x in file:
    massive.append(x)
massive = list(reversed(sorted(list(map(int, massive)))))
baggage = list()

for x in massive:
    if sum(baggage)+x < mass and (x < 12001 and x > 6999):
        baggage.append(x)

print(len(baggage), baggage[-1])