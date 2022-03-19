# write a function which returns the sum of following series upto nth term(parameter).
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
# You need to round the answer to 2 decimal places and return it as String.

# If the given value is 0 then it should return 0.00

# You will only be given Natural Numbers as arguments.

def series_sum(n):
    return "{:.2f}".format(sum([(1/(3*i+1)) for i in range(n)]))

#This time, mine was the best possible solution