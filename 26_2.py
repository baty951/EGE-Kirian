from math import ceil

f = open("26.txt")
massive = []
for x in f:
    x = x.split()
    x = list(map(int, x))
    massive.append(x)
massive = sorted(massive)
queue = [info[1] for info in massive]

def isalife(number : int) -> bool:
    return queue[number] > 0 

def war(number_p : int, number_en : int):
    global queue
    if isalife(number_p) and isalife(number_en):
        if (pl := queue[number_p]) > (en := queue[number_en]):
            queue[number_en] = 0
            queue[number_p] = ceil((queue[number_p])*2/3)
        elif pl == en:
            queue[number_en] = 0
            queue[number_p] = 0
        else:
            queue[number_en] = ceil((queue[number_en])*2/3)
            queue[number_p] = 0

        

for i in range(len(queue)):
    info = massive[i]
    if info[1] == 0:
        continue
    if isalife(info[2]-1):
        queue[info[2]-1] += info[1]
    for x in range(3,6):
        war(info[0]-1, info[x]-1)

print(max(queue), queue.count(0))