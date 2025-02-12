def f(n, ss):
    numberinneedss = ""
    while n != 0:
        numberinneedss += str(n % ss)
        n = n//ss
    return numberinneedss[::-1]

def f1(n: str, l: list):
    max_common = 0
    max_common_number = 0
    if n.count("5") == n.count("7"):
        return n+n[-1]
    else:
        for x in range(9):
            #smax = [max(smax[0], n.count(x)), l if n.count(x) > smax[0] else smax[-1]]
                number_count = n.count(str(x))
                if max_common < number_count:
                    max_common = number_count
                    max_common_number = x
                if max_common == number_count and x > max_common_number:
                    max_common = number_count
                    max_common_number = x
        return n + str(max_common_number)
        #return n+x

for n in range(1,10000):
    n_d = f(n, 9)
    n_s = set(n_d)
    n_l = list(sorted(list(n_d)))[::-1]
    for x in range(5):
        i = f1(n_d, n_l)
    n_sh = hex(int(i, 9))[2:]
    if "bac" in n_sh:
        print(n_sh, n)