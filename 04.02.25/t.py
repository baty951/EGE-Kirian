def NToR(num):
    num_nine = ToNine(num)

    for _ in range(5):
        fife_count = num_nine.count('5')
        seven_count = num_nine.count('7')

        if fife_count == seven_count:
            num_nine = num_nine + str(int(num_nine) % 10)
        else:
            num_nine = num_nine + str(MaxCommonNumber(num_nine))
    
    result = hex(int(num_nine, 9))
    return result

def ToNine(num):
    num_nine = ''

    while num != 0:
        res_prom = str(num % 9)
        num = num // 9
        num_nine = res_prom + num_nine
    return num_nine

def MaxCommonNumber(num_nine):
    max_common = 0
    max_common_number = 0
    for number in range(0, 9):
        number_count = num_nine.count(str(number))
        if max_common < number_count:
            max_common = number_count
            max_common_number = number
        if max_common == number_count and number > max_common_number:
            max_common = number_count
            max_common_number = number
    return max_common_number
            
for num in reversed(range(1,10000)):
    result = NToR(num)
    
    if 'bac' in result:
        print(num)
        break