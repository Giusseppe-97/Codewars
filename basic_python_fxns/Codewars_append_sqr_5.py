def square_digits(num):
    num = str(num)
    list = ""
    for i in range(len(num)):
        number = num[i]
        numi = int(number)*int(number)
        list=list + str(numi)
    return int(list)

