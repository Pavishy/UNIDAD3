def Euclidiana(A, B):
    distancia = 0
    for i in range(len(A)):
        distancia += (A[i]-B[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia

###################################################################################################

###CARGAR INSTANCIA
archivo = open("Instancia.txt","r")
contenido = archivo.readlines()
print(contenido)

lista = [linea.split("\t") for linea in contenido]
print(lista)

# [ [ [ 1, 80, 90 ,..., 90 ], 'Guerrero'],
#   [ [ 2, 75, 59 ,..., 90 ], 'Duelista']
# ]

instancia = [ [ list(map(int,x[:6])), x[6] ] for x in lista ]
print(instancia)

###################################################################################################

K = 3 #grupos a generar

import random as rnd   ##actualización
index = []

n = rnd.randrange(0, len(instancia))
index.append(n)

temp = K-1
while(temp>0):
    n = rnd.randrange(0, len(instancia))
    if not n in index:
        index.append(n)
        temp -= 1

print("indice" + str(index))

###################################################################################################
##CENTROIDES INICIALES

centroides = []
#centroides.append(instancia[index[0]].copy())
#centroides.append(instancia[index[1]].copy())
#centroides.append(instancia[index[2]].copy())

for i in index:
    centroides.append(instancia[i].copy())

print("\nCENTROIDES:")
#centroides[0][1] = "---"
for i in centroides:
    i[1] = "---"
print(centroides)

###################################################################################################

for iteracion in range(10): #repetir a partir del paso 4 un total de 10 veces
    print("Iteración " + str(iteracion))
    ###############################

    #grupos = [[], [], []]
    grupos = []
    for i in range(K):
        grupos.append([])

    print("\nGRUPOS:")
    for kgrupo in grupos:
        print(kgrupo)
        print("\n")

###################################################################################################

    ##checar a que grupo pertenece cada registro
    ##print("\n asiganción:")

    for registro in instancia:
        indexasignado = -1
        distanciaMin = 10000000
        for index, centroide in  enumerate(centroides):
            distancia = Euclidiana(centroide[0], registro[0])
            if distancia < distanciaMin:
                distanciaMin = distancia
                indexasignado = index
        grupos[indexasignado].append(registro)

###################################################################################################

    print("\nGRUPOS LLENOS:")
    for kgrupo in grupos:
        for reg  in kgrupo:
            print(reg)
        print("\n")

###################################################################################################

    cantCaracteristicas = len(centroides[0][0])
                                     # centroides[0] = centroide 1
                                     # centroides[0][0] = el vector de caracteristicas del centroide 1
    print("cant Caracteristicas: " +  str(cantCaracteristicas))

    for index, centroide in  enumerate(centroides):
        m = [] #una posicion por cada caracteristica

        for i in range(cantCaracteristicas):
            suma = 0
            for reg in grupos[index]:
                #print(reg)
                suma += reg[0][i]

            m.append(suma/len(grupos[index]))

        print(m)
        print("\n")

        #actualizar centroides
        centroides[index][0] = m
        centroides[index][1] = "---"

    print("Centroides Nuevos: ")
    print(centroides)

    print("\n#####################################################################################\n\n")

#Programa: Realizar la aplicación de Kmeans en Excel y en Programa Python con la instancia "Iris" completa