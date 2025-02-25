print("x w y z")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (y <= x) and not(w) and z:
                    print(x, w, y, z)