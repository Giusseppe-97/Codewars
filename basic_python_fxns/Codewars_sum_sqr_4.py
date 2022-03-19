def square_sum(numbers):
    suma = 0
    for i in range(len(numbers)):
        suma = suma + numbers[i]*numbers[i]
    return suma

print(square_sum([1,2]))