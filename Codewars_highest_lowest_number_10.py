# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.
def high_and_low(numbers):
    list = numbers.split(" ")
    maxi = int(list[0])
    mini = int(list[0])
    for i in range(0, len(list)):
        num = int(list[i])
        if maxi<num:
            maxi = num
        elif mini>num:
            mini = num

    return str(maxi) +" "+ str(mini)

print(high_and_low("-334 650 -814 -29 591 -702 -111 -747 461 20 386 70 -206 983 270"))

def high_and_low_best(numbers): #z.
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn),min(nn))