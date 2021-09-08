def rgb(r, g, b):

    colors = [r,g,b]
    cols = ["","",""]
    for i in range(len(colors)):
        
        if colors[i]//16 == 10:
            cols[i] = "A"
        elif colors[i]//16 == 11:
            cols[i] = "B"
        elif colors[i]//16 == 12:
            cols[i] = "C"
        elif colors[i]//16 == 13:
            cols[i] = "D"
        elif colors[i]//16 == 14:
            cols[i] = "E"
        elif colors[i]//16 == 15:
            cols[i] = "F"
        else:
            cols[i] = str(colors[i]//16) 

        if colors[i]%16 == 10:
            cols[i] = cols[i] + "A"
        elif colors[i]%16 == 11:
            cols[i] = cols[i] + "B"
        elif colors[i]%16 == 12:
            cols[i] = cols[i] + "C"
        elif colors[i]%16 == 13:
            cols[i] =  cols[i] + "D"
        elif colors[i]%16 == 14:
            cols[i] = cols[i] + "E"
        elif colors[i]%16 == 15:
            cols[i] = cols[i] + "F"
        else: 
            cols[i] = cols[i]  + str(colors[i]%16 )

        if colors[i]<0:
            cols[i] = str(0)+str(0)
        elif colors[i]>255:
            cols[i] = "F" + "F"

    return cols[0] + cols[1] + cols[2]

def rgb_best(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
