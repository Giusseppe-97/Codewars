# Implement a method that accepts 3 integer values a, b, c. 
# The method should return true if a triangle can be built with the sides of given length and false in any other case.

# (In this case, all triangles must have surface greater than 0 to be accepted).

def is_triangle(a, b, c):
    var = 0
    try:
        if a<=0 or b<=0 or c<=0:
            return bool(0)

    except:
        var = 0
        if a>=b:
            if a>=c:
                if a<c+b:
                    var =+1
            elif c>=b:
                if c<a+b:
                    var =+1
        elif b>=c:
            if b<a+c:
                    var =+1
        else:
            var=1
        return bool(var)

    

print(is_triangle(0, 2, 3))

         
    