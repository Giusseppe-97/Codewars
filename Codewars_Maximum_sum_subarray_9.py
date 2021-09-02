# The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
def max_sequence(arr):
    new = []
    alt = []
    if len(arr)>0:
        for i in range(len(arr)):
            if arr[i]>=0:
                new.append(arr[i])
            elif arr[i]==-1 and arr[i+1]>0:
                new.append(arr[i])
            else:
                alt =new
                new = []
            
    if sum(alt)>sum(new):
        return sum(alt)
    else:
        return sum(new)

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))