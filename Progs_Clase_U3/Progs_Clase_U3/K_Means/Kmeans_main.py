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

K = 3

import random as rnd   ##actulización
index = []

n = rnd.randrange(0, len(instancia))
index.append(n)

temp = 2
while(temp>0):
    n = rnd.randrange(0, len(instancia))
    if not n in index:
        index.append(n)
        temp -= 1

print("indice" + str(index))


centroides = []
centroides.append(instancia[index[0]].copy())
centroides.append(instancia[index[1]].copy())
centroides.append(instancia[index[2]].copy())

print("\nCENTROIDES:")
centroides[0][1] = "---"
print(centroides)


for iteracion in range(10):
    print("Iteración " + str(iteracion))
    ###############################

    grupos = [[], [], []]

    print("\nGRUPOS:")
    for kgrupo in grupos:
        print(kgrupo)
        print("\n")

    #####################################################################################
    ##checar a que grupo pertenece cada registro
    ##print("\n asiganción:")

    from MetricasSimilitud import Metricas

    for registro in instancia:
        indexasignado = -1
        distanciaMin = 10000000
        for index, centroide in  enumerate(centroides):
            distancia = Metricas.Euclidiana(centroide[0], registro[0])
            if distancia < distanciaMin:
                distanciaMin = distancia
                indexasignado = index
        grupos[indexasignado].append(registro)

    print("\nGRUPOS LLENOS:")
    for kgrupo in grupos:
        for reg  in kgrupo:
            print(reg)
        print("\n")

    #########################################################################################

    cantCaracteristicas = len(centroides[0][0])  # centroides[0] = centroide 1
                                            #centroides[0][0] = el vector de caracteristicas del centroide 1
    print("cant Caracteristicas: " +  str(cantCaracteristicas))

    for index, centroide in  enumerate(centroides):
        m = [] #una posicion por cada caracteristica

        for i in range(cantCaracteristicas):
            suma = 0
            for reg in grupos[index]:
                #print(reg)
                suma += reg[0][i]

            m.append(suma/len(grupos[0]))

        print(m)
        print("\n")

        #actualizar centroides
        centroides[index][0] = m
        centroides[index][1] = "---"

    print("Centroides Nuevos: ")
    print(centroides)

    print("\n#####################################################################################\n\n")