file = open("27_A1.csv")
massive_a = [list(map(float, x.replace(",", ".").split(";"))) for x in file.readlines()]
file.close()
file = open("27_A2.csv")
massive_b = [list(map(float, x.replace(",", ".").split(";"))) for x in file.readlines()]
file.close()


def f(massive):
    mn = [9**10, []]
    for i in range(len(massive)):
        p = 0
        for m in range(len(massive)):
            p += ((massive[m][0] - massive[i][0])**2+(massive[m][1] - massive[i][1])**2)**0.5
        if p < mn[0]:
            mn = [p, massive[i]]
    return mn

a = f(massive_a)
b = f(massive_b)
print(a[1], b[1])
print(int((a[1][0]+b[1][0])/2*100), int((a[1][1]+b[1][1])/2*100))