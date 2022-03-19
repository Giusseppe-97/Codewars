def blind_number(n):
    m = 3**(n)
    a = "0"*n
    lis = [a]
    cont=0
    for i in range(n+1):
        print('{num:01d}'.format(num=i))
        for j in range(n+1):
            z = '{num:02d}'.format(num=j)
            cont +=1
    for i in range(1,3):
        for j in range(n):
            r=a[j]+str(i)
            lis.append(str(r))
    

    print(lis)       

    return(cont)

    

print(blind_number(3))