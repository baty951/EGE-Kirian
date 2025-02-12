q = open("26.txt")
m=[]
for x in (q):
    x=x.split()
    x=list(map(int, x))
    m.append(x)
m = sorted(m)
deaths = []
l = 0

def f(m,x):
    global deaths
    for i in range(3):
        if m[x[3]-1][0] not in deaths:
            if x[1] > (c := m[x[3]-1][1]):
                deaths.append(m[x[3]-1][0])
                m[x[3]-1][1] = 0
                x[1] = (x[1]-1)//3*2+1
                del(x[3])
            elif x[1] == c:
                deaths.extend([x[0], m[x[3]-1][0]])
                m[x[3]-1][1] = 0
                x[1] = 0
                break
            else:
                deaths.append(x[0])
                x[1] = 0
                c = (c-1)//3*2+1
                break
    return m

            

for x in m:
    if x[0] not in deaths:
        if x[2] not in deaths:
            m[x[2]-1][1] += x[1]
        m = f(m,x)
print(len(deaths))
for i in m:
    l += i[1]
print(l)