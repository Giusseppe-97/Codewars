def persistence(n):
    m = str(n)
    length = len(m)
    con = 0
    par=0
    for i in range(length):
        if m[i]=="0":
            length = 0
            con = 1
    
    while length>1:
        w = int(m[0])
        w_2 = int(m[1])
        ans = w*w_2
        if length> 2:
            w_3 = int(m[2])
            ans = ans*w_3
        if length> 3:
            w_4 = int(m[3])
            ans = ans*w_4
        if length> 4:
            w_5 = int(m[4])
            ans = ans*w_5
        if length> 5:
            w_6 = int(m[5])
            ans = ans*w_6
        m = str(ans)
        length =len(str(ans))
        con = con+1

    return con

def persistence_best(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count

print(persistence(999))
print(persistence_best(999))


    
