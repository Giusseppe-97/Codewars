def rgb(r, g, b):
    red = ""
    green = ""
    blue = ""
    red_1 = r%16  
    green_1 = g%16  
    blue_1 = b%16 

    red_16 = r//16  
    green_16 = g//16  
    blue_16 = b//16  
    if red_16<9:
        red = str(red_16) + str(red_1)
    if green_16<9:
        green = str(green_16) + str(green_1)
        red = str(red_16) + str(red_1)
    if blue_16<9:
        blue = str(blue_16) + str(blue_1)

    return red + green + blue

print(rgb(18,18,18))
