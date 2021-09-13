# Write a function that takes a string of parentheses,
# and determines if the order of the parentheses is valid. 
# The function should return true if the string is valid, and false if it's invalid.

"""
    "()"              =>  true
    ")(()))"          =>  false
    "("               =>  false
    "(())((()())())"  =>  true
"""

def valid_parentheses(string):
    pare = ""
    cont_1 = 0
    
    for i in range(len(string)):
        if string[i]=="(" or string[i]==")":
            pare = pare + string[i]
            
    if pare.count("(") == pare.count(")"):
        for j in range(len(pare)):
            if pare[j]=="(":
                cont_1 += 1
            if pare[j]==")":
                cont_1 -= 1
            if cont_1 == -1:
                return False
        if cont_1!=0 and cont_1%2!=0:
            return False
    else:
        return False
    return True

def valid_parentheses_best(string):
    cnt = 0
    for char in string:
        if char == '(': cnt += 1
        if char == ')': cnt -= 1
        if cnt < 0: return False
    return True if cnt == 0 else False



