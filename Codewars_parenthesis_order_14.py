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
    cont_1=0
    if string=="":
        return False
    for i in range(len(string)):
        if string[i]=="(" or string[i]==")":
            pare = pare + string[i]
    for j in range(len(pare)):
        if pare[j]=="(":
            cont_1 += 1
        else:
            cont_1 -= 1
        if cont_1 == -1 or cont_1%2!=0:
            return False
            
    return True

# def valid_parentheses(string):
#     i=0
#     while i != (len(string)):

#         if string[i] == "":
#             return True

#         elif string[i] == ")":
#             break
#         elif string[i]!= "(":
#             i += 1
#         else:
#             open_par = string.count("(")
#             close_par = string.count(")")
#             if open_par == close_par:
#                 return True
#     return False

print(valid_parentheses("  ("))
print(1%2)

# test.assert_equals(valid_parentheses("  ("),False)
# test.assert_equals(valid_parentheses(")test"),False)
# test.assert_equals(valid_parentheses(""),True)
# test.assert_equals(valid_parentheses("hi())("),False)
# test.assert_equals(valid_parentheses("hi(hi)()"),True)



