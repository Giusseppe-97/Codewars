def high_and_low(numbers):
    n= numbers.replace(" ","")
    maxi = 0
    mini = 0
    for i in range(len(n)):
        a = int(n)
        if n[i]>maxi:
            maxi == a[i]
        if n[i]<mini:
            mini == a[i]
    return maxi, " ", mini

print(high_and_low("1 2 3 4 5 6"))