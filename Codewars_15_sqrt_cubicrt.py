def isPP(n):
    import math
    sr = math.sqrt(n)
    cr = n ** (1/3)
    if n%cr==0:
        return [int(cr),3]
    if n%sr==0:
        return [sr, 2] 
def isPP(n):
    for i in range(2,n):
        sr = round(n ** (1/i),ndigits=10)
        if n%sr==0:
            return [int(sr), i]

from math import ceil, log, sqrt

def isPP_best(n):
    for b in xrange(2, int(sqrt(n)) + 1):
        e = int(round(log(n, b)))
        if b ** e == n:
            return [b, e]
    return None
