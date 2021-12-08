def Euclidiana(A, B):
    distancia = 0
    for i in range(len(A)):
        distancia += (A[i]-B[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia


def Mode(list):
    rep = 0
    mode = []
    for i in list:
        temp = list.count(i)
        if temp > rep:
            rep = temp

    for i in list:
        temp = list.count(i)
        if temp == rep and i not in mode:
            mode.append(i)

    if len(mode) != len(list):
        return mode
    else:
        return -1


###CARGAR INSTANCIA DE ENTRENAMIENTO

archivo = open("wine_entrenamiento.csv","r")
#archivo = open("iris_entrenamiento.csv","r")

contenido = archivo.readlines()
#print(contenido)

lista = [linea.split(",") for linea in contenido]
#print(lista)

instancia = [ [ list(map(float,x[:13])), x[13] ] for x in lista ] #wine
#instancia = [ [ list(map(float,x[:4])), x[4] ] for x in lista ] #iris
print("Instancia de entrenamiento:")
print(instancia)
print(len(instancia))

##############################################################################
###CARGAR INSTANCIA DE PRUEBA

archivo = open("wine_prueba.csv","r")
#archivo = open("iris_prueba.csv","r")

contenido = archivo.readlines()
#print(contenido)

lista = [linea.split(",") for linea in contenido]
##print(lista)

prueba = [ [ list(map(float,x[:13])), x[13] ] for x in lista ] #wine
#prueba = [ [ list(map(float,x[:4])), x[4] ] for x in lista ] #iris
print("Instancia de prueba:")
print(prueba)
print(len(prueba))

##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia (entrenamiento)
K = 10
##############################################################################

contAciertos = 0

for registroNC in prueba:
    print("Clasificación del registro: ")
    print(registroNC)

    NC = registroNC[0] #vector de caracteristicas del registro actual de prueba

    estructuraDatos = {}

    for NoCaso, i in enumerate(instancia):
        distancia_NC_i = Euclidiana(NC, i[0])
        #print(distancia_NC_i)
        estructuraDatos[NoCaso] = distancia_NC_i

    #print(estructuraDatos)  # La distancia de los registros con el registroNC

    ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1]) #ordena los registros
    #de menor a mayor de acuerdo con la distancia con el registroNC
    #print(ordenado)

    temporalK = []
    for i in range(K):
        NoCaso = ordenado[i][0]
        #print(etiqueta)
        registro = instancia[NoCaso]
        #print(registro)
        temporalK.append(registro[1]) #obtencion de la etiqueta

    print("Clases de los vectores más cercanos a el registro NC:")
    print(temporalK)  #los primeros K vectores
    print("\n\n")

    moda = Mode(temporalK)
    respKnn = moda[0]

    print("Clase asignada por el 3_KNN: "  + str(respKnn))
    print("Clase Real: " + registroNC[1])

    if str(respKnn) == registroNC[1]:
        contAciertos += 1

print("Total de aciertos: " + str(contAciertos))
print("Total de pruebas: " + str(len(prueba)))
print("Rendimiento: " + str(contAciertos/len(prueba)*100))

#Practica:

#Realizar la aplicación de KNN para el calculo del rendimiento de la técnica utilizando IRIS
#   Consideraciones:
#           *Usar statistics para el calculo de la moda
#           *Añadir el código necesario para realizar la busqueda del valor de k que de mejores resultados
#           *Reportar que valor de k es el mejor y que rendimiento genera
#           *OPCIONAL: PROBAR OTRAS METRICAS DE SIMILITUD

