
import math

def recibiendo_paquetes(paquetes):
    cienes = 0
    veinticincos = 0
    dieces = 0
    unos = 0
    if math.floor(paquetes/100)>0:
        cienes = math.floor(paquetes/100)
        paquetes = paquetes - cienes*100
        
    if math.floor(paquetes/25)>0:
        veinticincos = math.floor(paquetes/25)
        paquetes = paquetes - veinticincos*25
        
    if math.floor(paquetes/10)>0:
        dieces = math.floor(paquetes/10)
        paquetes = paquetes - dieces*10
        
    unos = paquetes
    
    return [cienes, veinticincos, dieces, unos]

print(recibiendo_paquetes())
        

         
        

