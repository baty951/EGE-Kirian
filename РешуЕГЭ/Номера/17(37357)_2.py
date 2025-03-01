import time
start_time = time.time()

massive = [int(x[:-1]) for x in list(open("17(37357).txt"))]

divisors = [[],[],[],[],[],[],[],[]]

mx = 0
count = 0

for x in massive:
    divisors[x%8].append(x)

