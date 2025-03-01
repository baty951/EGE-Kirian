file = [int(x[:-1]) for x in open("26.txt")]
mass = 835*1000
massive = list()
for x in file:
    massive.append(x)
massive = list(reversed(sorted(list(map(int, massive)))))
baggage = list()

for x in massive:
    if sum(baggage)+x < mass and (x < 12001 and x > 6999):
        baggage.append(x)

print(len(baggage), baggage[-1])