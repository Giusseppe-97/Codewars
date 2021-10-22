def opposite(number):
    num =str(number)
    if num[0]=="-":
        ans = str(number).replace("-","")
    else:
        ans = "-" + str(number)

    return ans

def opposite_best(number):
    return -number