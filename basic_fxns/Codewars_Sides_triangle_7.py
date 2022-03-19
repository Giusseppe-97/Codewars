# Implement a method that accepts 3 integer values a, b, c. 
# The method should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    if a>=c+b or c>=a+b or b>=a+c:
        return False
    else:
        return True

def is_triangle_clever(a, b, c):
    return 2 * max(a, b, c) < a + b + c

         
    