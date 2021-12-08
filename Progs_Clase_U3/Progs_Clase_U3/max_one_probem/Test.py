padre1 = [1, 2, 3, 4]

padre2 = [5, 6, 7, 8]

import random as rnd

punto_de_cruza = int(rnd.random()*4)
print("Punto de Cruza : " + str(punto_de_cruza))

hijo1 = padre1[0:punto_de_cruza] + padre2[punto_de_cruza:]
hijo2 = padre1[punto_de_cruza:]  + padre2[0:punto_de_cruza]

print(hijo1)
print(hijo2)


