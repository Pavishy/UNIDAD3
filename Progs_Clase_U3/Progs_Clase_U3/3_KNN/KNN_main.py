def Euclidiana(A, B):
    distancia = 0
    for i in range(len(A)):
        distancia += (A[i]-B[i])**2
    distancia = distancia ** (1/2)
    distancia = round(distancia, 2)
    return distancia

###CARGAR INSTANCIA
archivo = open("Instancia.txt","r")  #ABRIR EL ARCHIVO
contenido = archivo.readlines()  #LEER EL CONTENIDO DEL ARCHIVO
print(contenido)  #VISUALIZAR EL CONTENIDO DEL ARCHIVO

#CREAR UNA LISTA EN LA QUE CADA ELEMENTO SEA UNA LINEA DEL ARCHIVO CONVERTIDA EN LISTA SEPARADA POR TABULADOR
lista = [linea.split("\t") for linea in contenido]
print("Lista de listas separadas por tabulador: ")
print(lista)

# [ [ [ 1, 80, 90 ,..., 90 ], 'Guerrero'],
#   [ [ 2, 75, 59 ,..., 90 ], 'Duelista']
# ]

#CONVIERTE LA LISTA DE LISTAS EN LA INSTANCIA NECESARIA PARA TRABAJAR CON EL KNN
instancia = [ [ list(map(int,x[:6])), x[6].replace("\n","") ] for x in lista ]
print(instancia)

##############################################################################
##SELECCIÓN / CREACIÓN DEL VECTOR A CLASIFICAR
NC = [23, 85, 84, 66, 1, 34] #NC = no clasificado
#23	85	84	66	1	34  = MAGO
##############################################################################
###DEFINIR EL VALOR DE "K"  - Un número entre 1 y el total de registros de la instancia
K = 5  #por ejmeplo el k = 5
##############################################################################

estructuraDatos = {} ##diccionario que fungira como estructura de datos para las distancias

for NoCaso, registro in enumerate(instancia):  #por cada elemento/registro de la instancia
    distancia_NC_i = Euclidiana(NC, registro[0]) #registro[0] = vector carac   -- registro[1] = clase
    #print(distancia_NC_i)
    estructuraDatos[NoCaso] = distancia_NC_i

print(estructuraDatos)


ordenado = sorted(estructuraDatos.items(), key=lambda x: x[1]) ## 0 = NoCaso   1 = Distancia
print(ordenado)


temporalK = []
for i in range(K):
    NoCaso = ordenado[i][0] ##0 = NoCaso
    registro = instancia[NoCaso]
    #print(registro)
    temporalK.append(registro[1]) ##etiqueta asociada al NoCaso

print(temporalK)

########################################################################
##ENCONTRAR LA MODA EN "TEMPORAL_K" PARA ASIGNAR ESA ETIQUETA/CLASE AL VECTOR "NC"

from statistics import mode #, multimode
etiquetasModa = mode(temporalK)
#etiquetasModa = multimode(temporalK)
print("Etiquetas Moda/Clase Asignada:", etiquetasModa)


# Tarea:
#Validación:
#
#   CrossValidation - Validación Cruzada
#   SplitValidation - Validación Segmentada  80%/20%  70%/30% 60%/40% => entrenamiento/prueba




