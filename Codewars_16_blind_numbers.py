def blind_number(n):
    m = 3**(n)
    a = "0"*n
    lis = [a]
    for i in range(n):
        # print('{num:01d}'.format(num=i))
        for j in range(n):
            print('{num:02d}'.format(num=j))

    # for i in range(1,3):
    #     for j in range(n):
    #         r=a[j]
    #         lis.append(str(r))
    

    # print(lis)

print(blind_number(3))