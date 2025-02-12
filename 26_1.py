f = open("26.txt")
massive = []
for x in f:
    x = x.split()
    x = list(map(int, x))
    massive.append(x)
massive = sorted(massive)

def war(strong : int, number: int, enemies_number : list, enemies_strong : list) -> list:
    x = {}
    for i in range(3):
        if strong > 0:
            if strong > enemies_strong[0]:
                strong = ((strong-1)//3*2+1)
                x.
                #x.extend([{number:strong},{enemies_number[0]:0}])
                del(enemies_number[0])
                del(enemies_strong[0])
            elif strong == enemies_strong[0]:
                #x.extend([{number:0},{enemies_number[0]:0}])
                break
            else:
                enemies_strong[0] = (enemies_strong[0]-1)//3*2+1
                #x.extend([{number:0},{enemies_number[0]:enemies_strong[0]}])
                break
    return x