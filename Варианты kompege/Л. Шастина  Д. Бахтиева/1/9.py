file = open("9.csv").readlines()
file[0] = sorted(list(map(int, file[0][3:-1].split(";"))))
for x in range(1, len(file)):
    file[x] = file[x][:-1]
    file[x] = sorted(list(map(int, file[x].split(";"))))

count = 0


for x in file:
    k = 0
    flag = False
    if (x[-1]+x[-2])*2 > 3*(x[0]+x[1]+x[2]):
        for i in x:
            if str(i)[-1] == "5":
                k += 1
                if k >= 2:
                    flag = True
        if flag:
            count += 1
print(count)