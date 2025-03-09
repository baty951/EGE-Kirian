file = open("9.csv")
massive = [list(map(int, i.split(";")))[0] for i in file]
file.close()
del(file)

for x in massive