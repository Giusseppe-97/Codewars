def solution(string):
    var = ""
    for i in range(len(string), 0, -1):
        var = var + string[i-1]

        
    return var 

print(solution("hola"))