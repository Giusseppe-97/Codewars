def solution(string):
    """
    This function returns a word written backwords
    """
    var = ""
    for i in range(len(string), 0, -1):
        var = var + string[i-1]

        
    return var 

print(solution("paranguaricutrimicuaro"))


def sumar(a, b): 
    return a + b

def restar(a, b): 
    return a - b

def multiplicar(a, b): 
    return a*b

def words_even_or_odd(string):
    variable = len(string)
    if variable%2 == 0:
        return "Es par"
    else: 
        return "Es impar"

print(words_even_or_odd("papaya"))

print(multiplicar(8,22))
print(restar(235635738,756583579))
print(sumar(2356345738,33464756583579))

import random

lista = ["a", "b", "c", "d"]
def aleatorio(lista):
    rd = random.randint(0,3)
    return lista[rd]
print(aleatorio(lista))