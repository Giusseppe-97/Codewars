# def isPP(n):
#     import math
#     sr = math.sqrt(n)
#     cr = n ** (1/3)
#     if n%cr==0:
#         return [int(cr),3]
#     if n%sr==0:
#         return [sr, 2] 
def isPP(n):
    for i in range(2,round(n/2)):
        sr = round(n ** (1/i),ndigits=5)
        if n%sr==0:
            return [int(sr), i]
        

